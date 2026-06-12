# Faceless Video Pipeline (Claude Code)

Turn a script (like `scripts/01-*.md`) into a ready-to-post 9:16 video: **fetch stock → AI voiceover → burn captions → assemble with motion, transitions & music**. All scriptable, all driven by Claude Code.

## Flow
```
script.md ──► fetch_stock.py ──► tts.py ──► captions.py ──► build_video.py ──► out/01.mp4
            (Pexels/Pixabay/    (ElevenLabs   (Whisper or    (ffmpeg: Ken Burns,
             Unsplash images)    / Piper VO)    TTS marks)     crossfades, caption
                                                               burn, music duck, 9:16)
```

## Components (to be built)
- `fetch_stock.py` — pulls assets per the script's "stock search term" column. Sources: **Pexels** & **Pixabay** (free API keys) for video; **Unsplash** for images.
- `tts.py` — voiceover from the VO column. **ElevenLabs** (premium) or **Piper** (free, offline). Outputs `vo.wav` + word timings.
- `captions.py` — word-by-word SRT from the VO (Whisper, or directly from TTS word boundaries).
- `build_video.py` — ffmpeg assembly per `brand_voice.md` (1080×1920, Ken Burns on stills, 0.4s crossfades, DM Sans captions with accent highlight, music ducked to ~15%, end card).

## Keys needed (all have free tiers)
| Service | Why | Get it |
|---|---|---|
| **Pixabay** API key | free stock video + music | pixabay.com → account → API |
| **Pexels** API key | free stock video/photos | pexels.com/api |
| **ElevenLabs** key *(optional)* | warm premium voice | elevenlabs.io (or use free Piper) |

Set as env vars: `PIXABAY_KEY`, `PEXELS_KEY`, `ELEVENLABS_KEY`. Never commit them (they're gitignored).

## Two ways to run
- **A — Image-slideshow (Claude Code can build AND render this for you now):** Unsplash stills + slow zoom + VO + captions + music. Proven faceless format; works within this environment.
- **B — Full stock-video clips (run on your machine):** Pexels/Pixabay video clips. Best run on your own machine where those APIs are reachable; Claude Code provides the scripts.

## Run (once built)
```bash
python video/fetch_stock.py  --script video/scripts/01-newborn-not-manipulating.md
python video/tts.py          --script video/scripts/01-newborn-not-manipulating.md --engine elevenlabs
python video/captions.py     --vo out/01/vo.wav
python video/build_video.py  --script video/scripts/01-newborn-not-manipulating.md --out out/01.mp4
```
Output: `out/01.mp4` — ready to post to Reels / TikTok / Shorts.

> `out/` and all media/keys are gitignored — only the scripts and specs are tracked.
