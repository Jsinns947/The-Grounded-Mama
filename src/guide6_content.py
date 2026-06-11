# -*- coding: utf-8 -*-
"""The Grounded Mama — Guide 6: The Complete Emotional Intelligence Toolkit.
Structured manuscript. Block types consumed by the fpdf2 builder:
  ('h2', text) subhead | ('p', text) paragraph | ('ul', [items]) bullets
  ('callout', text) highlighted box | ('script', (say, do, follow)) script card
"""

META = dict(
    title_lines=["MY CHILD HAS BIG", "EMOTIONAL OUTBURSTS"],
    subtitle_lines=["THE COMPLETE EMOTIONAL", "INTELLIGENCE TOOLKIT"],
    byline="By The Grounded Mama",
    accent=(122, 106, 144),   # lavender #7A6A90
    tagline="Raise a child who knows what to do with what they feel.",
)

TOC = [
    "Introduction: The Supermarket Floor",
    "Chapter 1: Big Feelings Are Not a Defect",
    "Chapter 2: Why EQ Matters as Much as IQ",
    "Chapter 3: The Calm-Down Corner Blueprint",
    "Chapter 4: The Feelings Dictionary — 12 Emotions Decoded",
    "Chapter 5: EQ Conversations for Every Age (2-10)",
    "Chapter 6: Daily Family Practices That Build EQ",
    "Chapter 7: When Big Feelings Need Extra Support",
    "Bonus: The Feelings Wheel + 30-Day EQ Tracker",
]

# Each chapter: (title, [blocks])
CHAPTERS = [
("Introduction: The Supermarket Floor", [
 ('p', "Your child feels everything at full volume. The tears, the rage, the joy "
       "— all of it enormous, all of it right on the surface. You have watched a "
       "dropped biscuit become a genuine grief, and a trip to the park become pure, "
       "whole-body delight. You love them for it. And some days, honestly, it exhausts you."),
 ('p', "And somewhere along the way, someone called your child ‘too sensitive.’ "
       "Maybe a relative. Maybe a teacher. Maybe a stranger in a supermarket aisle "
       "watching your three-year-old sob on the floor over the wrong-coloured cup. You "
       "have heard it enough times that a quiet, awful question has started to grow: "
       "is something wrong with my child?"),
 ('p', "Let me answer that now, as a certified child development professional and a "
       "mother of three: no. Nothing is wrong with your child. A child who feels deeply "
       "is not broken — they are wired for connection, empathy, and a rich inner life. "
       "What they do not yet have is the one thing no child is born with: the skills to "
       "manage what they feel. That is not a flaw. That is the whole job of childhood."),
 ('callout', "Big feelings are not the problem to be solved. The missing skill is "
             "emotional regulation — and it can be taught. That is what this toolkit does."),
 ('p', "This is not a book about making your child feel less. It is a book about helping "
       "them understand what they feel, put words to it, and learn what to do with it. "
       "That skill — emotional intelligence — will serve them at four, at fourteen, "
       "and at forty. Let's build it together."),
]),

("Chapter 1: Big Feelings Are Not a Defect", [
 ('h2', "It's Not Drama — It's Development"),
 ('p', "When your child melts down over something that seems impossibly small, it is "
       "tempting to read it as manipulation or theatrics. It is neither. The part of the "
       "brain responsible for managing emotion — the prefrontal cortex — is one of "
       "the last regions to mature, and it is not fully developed until the mid-twenties. "
       "In a young child, it is barely online."),
 ('p', "Meanwhile, the amygdala — the brain's alarm system — is fully active from "
       "birth. So your child arrives in the world with a powerful accelerator and almost "
       "no brakes. When a big feeling hits, the alarm fires, stress hormones flood the body, "
       "and the thinking brain goes offline. In that moment your child genuinely cannot "
       "reason, negotiate, or ‘calm down’ on command. They are not giving you a hard "
       "time. They are having a hard time."),
 ('h2', "The Upstairs and Downstairs Brain"),
 ('p', "A simple way to picture it: the ‘downstairs brain’ handles survival and big "
       "emotion. The ‘upstairs brain’ handles logic, empathy, and self-control — and "
       "it is still under construction. A meltdown is the downstairs brain taking over while "
       "the staircase between them is washed out. Your job is not to argue with the downstairs "
       "brain. It is to help the storm pass, then build the staircase, one calm moment at a time."),
 ('h2', "The Sensitive Child Is Often the Perceptive One"),
 ('p', "Roughly one in five children is born more sensitive — more responsive to sound, "
       "texture, transition, and the emotions of the people around them. This is a "
       "temperament, not a disorder. Highly sensitive children often grow into unusually "
       "empathetic, observant, and creative adults. The intensity you are managing now is "
       "the early, unshaped version of a real strength."),
 ('callout', "Your calm nervous system is the most powerful tool your child has. Children "
             "co-regulate — they borrow your steadiness before they can build their own. "
             "When you stay regulated, you are not ignoring the meltdown. You are teaching."),
]),

("Chapter 2: Why EQ Matters as Much as IQ", [
 ('p', "For decades we measured children's potential almost entirely by IQ. Then the "
       "research caught up with what parents always sensed: how a child understands and "
       "manages emotion — their emotional intelligence, or EQ — predicts life outcomes "
       "at least as powerfully, and in many studies more powerfully, than raw intellect."),
 ('h2', "What the Research Actually Shows"),
 ('ul', [
   "Children who can name and regulate emotion show stronger focus, better friendships, and fewer behavioural difficulties at school.",
   "Emotional skills in early childhood predict academic achievement — a regulated brain is a brain that can learn.",
   "The capacity to delay gratification and manage frustration tracks with healthier relationships and wellbeing decades later.",
   "EQ is not fixed at birth. Unlike IQ, it is highly teachable — which means your daily influence genuinely shapes it.",
 ]),
 ('h2', "The Five Pillars of Emotional Intelligence"),
 ('p', "Everything in this toolkit builds one of five capacities, drawn from the foundational "
       "model of emotional intelligence:"),
 ('ul', [
   "Self-awareness — noticing and naming what I feel.",
   "Self-regulation — managing the feeling without being hijacked by it.",
   "Motivation — staying with something hard instead of quitting at the first frustration.",
   "Empathy — reading and caring about what others feel.",
   "Social skill — handling conflict, sharing, and repair.",
 ]),
 ('callout', "You are not raising a child who never feels angry, scared, or sad. You are "
             "raising a child who knows what those feelings are, that they are safe, and "
             "what to do when they arrive. That is the entire goal."),
]),

("Chapter 3: The Calm-Down Corner Blueprint", [
 ('p', "A calm-down corner is a small, dedicated space where your child goes to settle their "
       "nervous system — not as punishment, but as a tool. This is the single most "
       "important distinction in this chapter: a calm-down corner is the opposite of a "
       "naughty step. One says ‘go away until you behave.’ The other says ‘your big "
       "feelings are welcome, and here is a safe place to ride them out.’"),
 ('h2', "What to Include"),
 ('ul', [
   "Something soft: a cushion, beanbag, or small blanket to create a sense of safety.",
   "Something to squeeze or fidget: a stress ball, soft toy, or textured object for the hands.",
   "Something visual and calming: a glitter jar, a lava-style timer, or a poster of the Feelings Wheel (in the bonus).",
   "Something for the breath: a printed ‘breathe’ prompt, a pinwheel to blow, or a feather.",
   "Something familiar: a favourite book or two for after the storm passes.",
 ]),
 ('h2', "How to Introduce It (the part most parents skip)"),
 ('p', "Never introduce the corner during a meltdown — that frames it as a consequence. "
       "Build it together on a calm, ordinary afternoon. Let your child name it (‘the cosy "
       "corner,’ ‘the calm cave’). Let them choose what goes in it. Children protect the "
       "rules they help create, and they return to the spaces they helped build."),
 ('script', ("\"Sometimes our feelings get really big and our bodies feel out of control. "
             "This is a special place we can go to help our bodies feel calm again. It's not "
             "a place for being in trouble — it's a place for taking care of yourself.\"",
             "Sit in it together when everyone is calm. Practise the breathing. Model using it "
             "yourself: \"I'm feeling frustrated — I'm going to my calm corner for a minute.\"",
             "Over the next weeks, gently offer it during smaller upsets: \"Would your body like "
             "the calm corner right now, or shall we go together?\" Offer — never force.")),
 ('callout', "The goal is for the corner to become your child's, not yours. The day your child "
             "takes themselves there mid-storm is the day self-regulation begins."),
]),

("Chapter 4: The Feelings Dictionary — 12 Emotions Decoded", [
 ('p', "Children cannot manage a feeling they cannot name. Researchers call this ‘affect "
       "labelling’ — the simple act of putting a precise word to an emotion measurably "
       "lowers its intensity in the brain. The more specific the word, the more the nervous "
       "system settles. ‘Frustrated’ calms more than ‘bad.’"),
 ('p', "Here are twelve big emotions, what each looks like in a child, what it actually needs, "
       "and a script to help you name it for them. Over time, you hand them the words — "
       "until they reach for them on their own."),
 ('feeling', ("ANGRY", "Clenched fists, shouting, throwing, a hot red face.",
              "To feel that the anger is allowed while the behaviour has a limit.",
              "\"You are so angry right now. Anger is okay. Hitting is not. I'm here.\"")),
 ('feeling', ("FRUSTRATED", "Giving up, whining, ‘I can't!’, flinging the toy down.",
              "Acknowledgement, then a tiny piece of help — not rescue.",
              "\"This is really tricky and it's making you frustrated. Want to do the next bit together?\"")),
 ('feeling', ("SAD", "Tears, withdrawal, clinginess, a wobbly lip, low energy.",
              "Closeness and permission — not cheering up or fixing.",
              "\"You're feeling sad. It's okay to be sad. I'll sit right here with you.\"")),
 ('feeling', ("SCARED", "Freezing, hiding, clinging, refusing, sudden ‘no.’",
              "Safety first, reassurance second, never ridicule.",
              "\"That felt scary. You're safe. I've got you. We can be brave together.\"")),
 ('feeling', ("WORRIED / ANXIOUS", "‘What if’ questions, tummy aches, stalling, reassurance-seeking.",
              "To name the worry out loud so it shrinks, plus a plan.",
              "\"It sounds like your worry brain is being loud. Let's tell it what we know is true.\"")),
 ('feeling', ("JEALOUS", "‘That's not fair,’ grabbing, targeting a sibling, sulking.",
              "To feel they have not been replaced — connection, not a lecture.",
              "\"You wished that was your turn. That's a hard feeling. There's enough love for both of you.\"")),
 ('feeling', ("EMBARRASSED", "Hiding the face, anger that masks shame, refusing to try again.",
              "Privacy and a face-saving exit — never an audience.",
              "\"That felt embarrassing. It happens to everyone, even grown-ups. Let's take a breath.\"")),
 ('feeling', ("DISAPPOINTED", "Deflating, crying over a changed plan, ‘but you said…’",
              "To have the let-down acknowledged before the redirect.",
              "\"You really wanted that, and it's not happening today. That's disappointing. I get it.\"")),
 ('feeling', ("OVERWHELMED", "Shutting down, covering ears, melting at small things, too much input.",
              "Less — fewer words, lower light, a quiet exit.",
              "\"Everything feels like too much right now. Let's make it smaller. Come with me.\"")),
 ('feeling', ("EXCITED", "Bouncing, shouting, can't-sit-still, big body, sometimes tips into chaos.",
              "Help channelling the energy, not squashing the joy.",
              "\"Your body is full of excited energy! Let's give it somewhere to go — ten big jumps?\"")),
 ('feeling', ("SHY", "Hiding behind your leg, going quiet, refusing to greet, watching from afar.",
              "No pressure and no labelling them ‘shy’ to others.",
              "\"You're taking your time to feel comfortable. That's okay. I'll stay with you.\"")),
 ('feeling', ("LONELY", "‘No one likes me,’ seeking constant company, sadness after school.",
              "To feel heard and gently helped to connect.",
              "\"It hurts to feel left out. I'm so glad you told me. Let's think about this together.\"")),
]),

("Chapter 5: EQ Conversations for Every Age (2-10)", [
 ('p', "Emotional coaching looks different at three than at nine. Meet your child where their "
       "brain actually is — the words that open a toddler change very little, while an "
       "eight-year-old needs room to reason it out for themselves."),
 ('h2', "Ages 2–3: Name and Stay"),
 ('p', "Keep it tiny and concrete. One feeling word, one short sentence, your calm body close. "
       "Do not explain or reason mid-storm — they cannot process language yet. Narrate the "
       "feeling and wait it out: \"You're sad the show is finished. I'm here.\""),
 ('h2', "Ages 4–5: Name and Wonder"),
 ('p', "Now you can add gentle curiosity and simple cause-and-effect. \"You got so cross when "
       "the tower fell. Building is tricky. What could we try?\" Picture books about feelings "
       "land beautifully at this age — children meet their own emotions safely in a story."),
 ('h2', "Ages 6–7: Name and Strategise"),
 ('p', "School-age children can begin to choose their own tools. Build a shared menu of "
       "calming strategies and let them pick: \"Your worry is here again. Do you want the "
       "breathing, the calm corner, or to draw it out?\" Coach them to notice the feeling "
       "earlier, before it peaks."),
 ('h2', "Ages 8–10: Name and Reflect"),
 ('p', "Older children can reflect after the fact and build genuine self-awareness. Ask open "
       "questions, then listen more than you talk: \"What was happening in your body just "
       "before you lost it? What might help next time?\" This is where emotional intelligence "
       "becomes truly theirs."),
 ('callout', "The thread through every age is the same: connect before you correct. A child "
             "who feels understood can learn. A child who feels judged can only defend."),
]),

("Chapter 6: Daily Family Practices That Build EQ", [
 ('p', "Emotional intelligence is not built in the big dramatic moments. It is built in small, "
       "boring, repeated ones — the daily climate of your home. None of these takes extra "
       "time. They are a way of doing what you already do."),
 ('ul', [
   "Name your own feelings out loud: \"I'm feeling frustrated that we're running late — I'm going to take a breath.\" You are modelling the entire skill.",
   "Do a feelings check-in at dinner: each person names a high and a low of their day, feeling words encouraged.",
   "Read books about emotions and pause to ask, \"How do you think they feel?\"",
   "Validate before you redirect — every single time. \"You're upset, AND it's still bedtime.\"",
   "Catch and name the good ones too: \"You look really proud of that.\" Positive emotions deserve words as well.",
   "Repair after you lose your temper — because you will. \"I shouted, and that wasn't okay. I'm sorry. I'm working on my big feelings too.\"",
 ]),
 ('callout', "Repair is not a failure of good parenting — it IS good parenting. A child who "
             "watches you own a mistake and make it right learns that relationships survive "
             "rupture. That is one of the most valuable lessons you will ever teach."),
 ('h2', "The Five-Minute Connection That Prevents Half the Storms"),
 ('p', "Ten minutes of undivided, child-led attention a day — no phone, no agenda, they "
       "choose — measurably reduces attention-seeking outbursts. A full emotional cup spills "
       "less. It is the cheapest, most powerful behaviour tool there is."),
]),

("Chapter 7: When Big Feelings Need Extra Support", [
 ('p', "This toolkit is a starting point, not a diagnosis. Big feelings are normal, and "
       "intensity alone is not a red flag. But some patterns are worth a conversation with "
       "your health visitor, GP, or paediatrician — not because something is ‘wrong,’ "
       "but because every child deserves the right support."),
 ('p', "Consider reaching out if you notice:"),
 ('ul', [
   "Outbursts that are far more frequent, intense, or long-lasting than other children of the same age — and not easing over months.",
   "Aggression that regularly endangers your child or others.",
   "Emotional distress that interferes with sleep, eating, friendships, or learning.",
   "Persistent sadness, withdrawal, or anxiety that lasts for weeks.",
   "Sensory sensitivities or rigidity that significantly disrupt daily life.",
   "Your own sense — the quiet parental instinct — that something needs a closer look.",
 ]),
 ('callout', "Seeking support is not an admission that you have failed. It is the same "
             "fierce advocacy you gave your child the day they were born. Trust your gut, "
             "and ask. You are allowed to want help.")
,
 ('p', "Whatever brought you to this guide — the supermarket floor, the ‘too sensitive,’ "
       "the exhaustion of loving a child who feels everything — hold on to this: you are "
       "raising a deeply feeling human, and you are teaching them what to do with it. That is "
       "extraordinary work. Keep going, Mama."),
]),

("Bonus: The Feelings Wheel + 30-Day EQ Tracker", [
 ('p', "Print the two tools on the following pages. The Feelings Wheel gives your child the "
       "vocabulary to point to what they feel before they have the words to say it — keep it "
       "in the calm-down corner. The 30-Day EQ Tracker turns these practices into a gentle "
       "daily habit. Tick a box, not for perfection, but for showing up."),
]),
]
