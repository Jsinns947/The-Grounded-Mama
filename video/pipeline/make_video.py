# -*- coding: utf-8 -*-
"""The Grounded Mama — faceless video assembler.
script.json -> stock images + AI voiceover + burned captions + music -> 9:16 MP4.

Usage:
  python make_video.py --script ../scripts/01.json --voice sapi
  python make_video.py --script ../scripts/01.json --voice elevenlabs   (needs ELEVENLABS_KEY)
  python make_video.py --script ../scripts/01.json --voice piper         (needs piper + model)

Asset sourcing per beat (in priority order):
  beat["img_url"]              -> download directly (Unsplash etc.)
  beat["query"] + PEXELS_KEY   -> Pexels photo/video search   (run on your machine)
  beat["query"] + PIXABAY_KEY  -> Pixabay search
Keys via env: PEXELS_KEY, PIXABAY_KEY, ELEVENLABS_KEY (never commit them).
"""
import os, sys, json, wave, shutil, argparse, subprocess, urllib.request

VIDEO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # .../video
FONT_SRC  = os.environ.get("CAPTION_FONT", r"C:/Users/Athanase-Chrisbert J/_fonts/DMSans-Bold.ttf")
FFMPEG    = os.environ.get("FFMPEG", "ffmpeg")
W, H, FPS = 1080, 1920, 30

def run(cmd, cwd=None):
    r = subprocess.run(cmd, cwd=cwd, stdout=subprocess.PIPE,
                       stderr=subprocess.STDOUT, text=True)
    if r.returncode != 0:
        sys.stderr.write((r.stdout or "")[-2500:])
        raise SystemExit("CMD FAILED: " + " ".join(str(c) for c in cmd[:4]) + " ...")

# ---------- assets ----------
def fetch_url(url, dest):
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        return
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as r, open(dest, "wb") as f:
        shutil.copyfileobj(r, f)

def get_image(beat, dest):
    if beat.get("img_url"):
        fetch_url(beat["img_url"], dest); return
    q = beat.get("query")
    if q and os.environ.get("PEXELS_KEY"):
        import urllib.parse
        u = "https://api.pexels.com/v1/search?per_page=1&orientation=portrait&query=" + urllib.parse.quote(q)
        req = urllib.request.Request(u, headers={"Authorization": os.environ["PEXELS_KEY"]})
        d = json.load(urllib.request.urlopen(req, timeout=30))
        fetch_url(d["photos"][0]["src"]["large2x"], dest); return
    if q and os.environ.get("PIXABAY_KEY"):
        import urllib.parse
        u = ("https://pixabay.com/api/?key=%s&image_type=photo&orientation=vertical&per_page=3&q=%s"
             % (os.environ["PIXABAY_KEY"], urllib.parse.quote(q)))
        d = json.load(urllib.request.urlopen(u, timeout=30))
        fetch_url(d["hits"][0]["largeImageURL"], dest); return
    raise SystemExit("Beat has no img_url and no stock key for query: %r" % q)

# ---------- voiceover ----------
def tts(beat, dest, engine):
    text = beat["vo"]
    if engine == "sapi":          # free, offline, Windows female voice (draft quality)
        ps = ("Add-Type -AssemblyName System.Speech;"
              "$s=New-Object System.Speech.Synthesis.SpeechSynthesizer;"
              "$v=$s.GetInstalledVoices()|?{$_.VoiceInfo.Gender -eq 'Female' -and $_.Enabled}|Select -First 1;"
              "if($v){$s.SelectVoice($v.VoiceInfo.Name)};$s.Rate=-2;"
              "$s.SetOutputToWaveFile('%s');$s.Speak([Console]::In.ReadToEnd());$s.Dispose()"
              % dest.replace("\\", "/"))
        subprocess.run(["powershell", "-NoProfile", "-Command", ps],
                       input=text, text=True, check=True)
    elif engine == "elevenlabs":  # warm premium voice
        key = os.environ["ELEVENLABS_KEY"]
        voice = os.environ.get("ELEVENLABS_VOICE", "XB0fDUnXU5powFXDhCwa")  # "Charlotte" warm female
        body = json.dumps({"text": text, "model_id": "eleven_multilingual_v2",
                           "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}}).encode()
        req = urllib.request.Request(
            "https://api.elevenlabs.io/v1/text-to-speech/%s" % voice, data=body,
            headers={"xi-api-key": key, "Content-Type": "application/json", "Accept": "audio/mpeg"})
        mp3 = dest[:-4] + ".mp3"
        with urllib.request.urlopen(req, timeout=60) as r, open(mp3, "wb") as f:
            shutil.copyfileobj(r, f)
        run([FFMPEG, "-y", "-i", mp3, dest])
    elif engine == "piper":       # free, offline (needs piper binary + voice model)
        model = os.environ.get("PIPER_MODEL", "en_US-amy-medium.onnx")
        subprocess.run(["piper", "--model", model, "--output_file", dest],
                       input=text, text=True, check=True)
    else:
        raise SystemExit("unknown voice engine: " + engine)

def wav_seconds(path):
    with wave.open(path, "rb") as w:
        return w.getnframes() / float(w.getframerate())

# ---------- assembly ----------
def build_clip(img, wav, caption, work, idx):
    """One beat: still -> 9:16 with Ken Burns zoom + burned caption, length = VO."""
    dur = max(wav_seconds(wav), 1.3)
    frames = int(dur * FPS) + FPS
    cap_name = "cap_%d.txt" % idx
    open(os.path.join(work, cap_name), "w", encoding="utf-8").write(caption)
    big_w, big_h = int(W * 1.4), int(H * 1.4)
    vf = (f"scale={big_w}:{big_h}:force_original_aspect_ratio=increase,"
          f"crop={big_w}:{big_h},"
          f"zoompan=z='min(zoom+0.0012,1.10)':d={frames}:s={W}x{H}:fps={FPS},"
          f"drawtext=fontfile=font.ttf:textfile={cap_name}:fontcolor=white:fontsize=80:"
          f"borderw=6:bordercolor=black@0.5:x=(w-text_w)/2:y=h*0.40")
    out = os.path.join(work, "clip_%d.mp4" % idx)
    # cwd=work so drawtext sees font.ttf / cap.txt by basename (avoids Windows path-escaping in filters)
    run([FFMPEG, "-y", "-loop", "1", "-i", os.path.abspath(img), "-i", os.path.abspath(wav),
         "-filter_complex", "[0:v]%s[v]" % vf, "-map", "[v]", "-map", "1:a",
         "-t", "%.2f" % dur, "-r", str(FPS), "-c:v", "libx264", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-ar", "44100", os.path.abspath(out)], cwd=work)
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--script", required=True)
    ap.add_argument("--voice", default="sapi", choices=["sapi", "elevenlabs", "piper"])
    ap.add_argument("--out", default=None)
    a = ap.parse_args()

    spec = json.load(open(a.script, encoding="utf-8"))
    vid = spec["id"]
    work = os.path.join(VIDEO_DIR, "out", vid)
    img_d = os.path.join(VIDEO_DIR, "assets", "img")
    vo_d  = os.path.join(VIDEO_DIR, "assets", "vo")
    for d in (work, img_d, vo_d):
        os.makedirs(d, exist_ok=True)
    shutil.copyfile(FONT_SRC, os.path.join(work, "font.ttf"))   # for drawtext

    clips = []
    for i, beat in enumerate(spec["beats"], 1):
        img = os.path.join(img_d, "%s_%d.jpg" % (vid, i))
        wav = os.path.join(vo_d,  "%s_%d.wav" % (vid, i))
        get_image(beat, img)
        if not (os.path.exists(wav) and os.path.getsize(wav) > 0):
            tts(beat, wav, a.voice)
        clips.append(build_clip(img, wav, beat["caption"], work, i))
        print("beat %d ok" % i)

    listf = os.path.join(work, "list.txt")
    open(listf, "w").write("\n".join("file '%s'" % os.path.abspath(c).replace("\\", "/") for c in clips))
    concat = os.path.join(work, "concat.mp4")
    run([FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", listf, "-c", "copy", concat])

    out = a.out or os.path.join(VIDEO_DIR, "out", "%s.mp4" % vid)
    music = spec.get("music")
    music_path = os.path.join(VIDEO_DIR, music) if music else None
    if music_path and os.path.exists(music_path):
        run([FFMPEG, "-y", "-i", concat, "-stream_loop", "-1", "-i", music_path,
             "-filter_complex",
             "[1:a]volume=0.15[m];[0:a][m]amix=inputs=2:duration=first:dropout_transition=0[a]",
             "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-shortest", out])
    else:
        shutil.copyfile(concat, out)
    print("DONE ->", out)

if __name__ == "__main__":
    main()
