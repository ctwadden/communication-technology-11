"use strict";
// Student-facing additions only. Assessed tasks and IDs live in index.html.
window.SPRINT_EXPERIENCE = {
 "studentOsUrl": "https://script.google.com/a/macros/gnspes.ca/s/AKfycby3lAqgW184t9EnOZg2XHDh6C8jYGZUBFpXeLICFZnAu0Yrkab3hcw6QFboHR7FWVTo/exec",
 "hook": {
  "lesson": "d01",
  "title": "Could you build it from this?",
  "prompt": "Imagine a dramatic, low-angle photo of a model house in moody light. Could a builder measure it from that photo?",
  "options": [
   "Yes",
   "No",
   "Only with extra photos"
  ],
  "followUp": "What would the builder need to see that a “cool” photo leaves out?"
 },
 "videos": [
  {
   "lesson": "d02",
   "title": "What cameras see that our eyes don’t",
   "channel": "TED · Bill Shribman",
   "url": "https://www.ted.com/talks/bill_shribman_what_cameras_see_that_our_eyes_don_t",
   "length": "3:05",
   "watch": "Whole talk (3:05)",
   "captions": "TED transcript and captions available",
   "questions": [
    "Which camera setting makes these images possible?",
    "What could a camera reveal about a making process that eyes miss?"
   ],
   "after": "Which setting will you change first today, and why?"
  },
  {
   "lesson": "d04",
   "title": "The magic ingredient that brings Pixar movies to life",
   "channel": "TED · Danielle Feinberg",
   "url": "https://www.ted.com/talks/danielle_feinberg_the_magic_ingredient_that_brings_pixar_movies_to_life",
   "length": "11:54",
   "watch": "Suggested 0:00–5:00; teacher to confirm the window",
   "captions": "TED transcript and captions available",
   "questions": [
    "How does light change what we notice?",
    "When does light hide information?"
   ],
   "after": "Which of your two setups will reveal the most construction detail?"
  },
  {
   "lesson": "d06",
   "title": "Macro-portraits of microscopic insects",
   "channel": "TED · Levon Biss",
   "url": "https://www.ted.com/talks/levon_biss_macro_portraits_of_microscopic_insects",
   "length": "9:52",
   "watch": "Suggested 0:00–4:00; teacher to confirm the window",
   "captions": "TED transcript and captions available",
   "questions": [
    "How does he light and photograph each small section?",
    "Why does a consistent setup matter when combining many photos?"
   ],
   "after": "Apply one idea to your making sequence."
  }
 ],
 "simulation": [
  {
   "lesson": "d02",
   "name": "Exposure Lab",
   "sourceName": "AI_STUDIO_PROMPTS.md · Exposure Lab",
   "status": "Not built yet: build it in Google AI Studio from the prompt.",
   "directions": "Use it after your camera rotation, to test a prediction.",
   "returnQuestion": "Which setting gave you the most of the object in focus, and what did it cost?"
  },
  {
   "lesson": "d04",
   "name": "Light the Object",
   "sourceName": "AI_STUDIO_PROMPTS.md · Light the Object",
   "status": "Not built yet: build it in Google AI Studio from the prompt.",
   "directions": "Use it after your two real setups.",
   "returnQuestion": "Which light position showed the most detail?"
  },
  {
   "lesson": "d05",
   "name": "Resize and Export",
   "sourceName": "AI_STUDIO_PROMPTS.md · Resize and Export",
   "status": "Not built yet: build it in Google AI Studio from the prompt.",
   "directions": "Use it after your two real exports.",
   "returnQuestion": "What did you lose at low JPG quality, and when would it matter?"
  }
 ],
 "discussion": {
  "lesson": "d08",
  "title": "Documentation or decoration?",
  "mode": "discuss",
  "respondFirst": true,
  "stimulus": {
   "label": "Post one of your own documentation photos with your response."
  },
  "prompt": "What makes a photo useful for someone who has to build the thing, and is it ever okay for documentation to be beautiful too?",
  "positions": [
   "Clarity first, always",
   "Beauty helps people care",
   "Depends on the audience"
  ],
  "reply": "Reply to one classmate: name one detail in their photo that a builder could actually measure or copy."
 },
 "choice": {
  "lesson": "d06",
  "title": "Choose what to document",
  "note": "All three assess the same skill: a clear, consistent making sequence.",
  "contexts": [
   "Building a village wall",
   "Making a sign",
   "Assembling a roof or joint"
  ],
  "prompt": "Write which task you chose and the stage you expect to be hardest to photograph."
 },
 "selfChecks": {
  "d02": [
   {
    "q": "For more of the object in focus, choose…",
    "options": [
     "f/4",
     "f/11",
     "ISO 1600"
    ],
    "answer": 1,
    "why": "A larger f-number gives deeper depth of field."
   },
   {
    "q": "A slow shutter handheld causes…",
    "options": [
     "Blur",
     "Noise",
     "Nothing"
    ],
    "answer": 0,
    "why": "Camera movement blurs; use the tripod."
   },
   {
    "q": "First thing when picking up the camera?",
    "options": [
     "Remove the cap",
     "Strap on",
     "Change the mode"
    ],
    "answer": 1,
    "why": "The strap prevents drops."
   }
  ],
  "d04": [
   {
    "q": "Which light shows every edge for documentation?",
    "options": [
     "Hard side light",
     "Soft, even light",
     "Back light"
    ],
    "answer": 1,
    "why": "Soft light reduces hiding shadows."
   },
   {
    "q": "A white card near the object…",
    "options": [
     "Blocks light",
     "Fills shadows",
     "Adds colour"
    ],
    "answer": 1,
    "why": "It reflects light into dark areas."
   }
  ],
  "d06": [
   {
    "q": "In a sequence, what should change between photos?",
    "options": [
     "Camera position",
     "Only the object",
     "Lighting"
    ],
    "answer": 1,
    "why": "Consistency makes it readable."
   },
   {
    "q": "3000 px at 300 PPI prints…",
    "options": [
     "1 in",
     "10 in",
     "30 in"
    ],
    "answer": 1,
    "why": "Pixels ÷ PPI = inches."
   }
  ],
  "d08": [
   {
    "q": "Annotations belong…",
    "options": [
     "Painted on the photo layer",
     "On separate layers",
     "In the file name"
    ],
    "answer": 1,
    "why": "The original stays unchanged."
   },
   {
    "q": "A ruler in frame gives…",
    "options": [
     "Style",
     "Scale",
     "Focus"
    ],
    "answer": 1,
    "why": "It lets people measure."
   }
  ]
 },
 "supports": {
  "start": {
   "today": "Read the route and the camera rules.",
   "glossary": [
    [
     "Documentation photo",
     "A photo that explains how something is made or measured"
    ],
    [
     "Original capture",
     "A photo you took yourself with the camera"
    ]
   ],
   "summary": "You will learn to handle the camera safely, control settings and light, export correctly, and document your village making process. Lesson 7 is your independent challenge.",
   "checklist": [
    "I know the camera rules",
    "I know lesson 7 is independent"
   ],
   "worked": {
    "title": "Worked example: documentation vs decoration",
    "text": "A mailbox photographed straight on with a ruler shows its size. The same mailbox shot low at sunset looks great but hides its shape."
   },
   "frames": [
    "A builder would need to see ___."
   ],
   "stretch": [
    "Find a product manual photo. What makes it useful?"
   ]
  },
  "d01": {
   "today": "Complete the safe routine and take a baseline.",
   "glossary": [
    [
     "Tripod plate",
     "The piece that locks the camera to the tripod"
    ],
    [
     "Baseline",
     "Your first photo, to compare later ones against"
    ]
   ],
   "summary": "Strap on, check battery and card, set up the tripod thickest legs first, lock everything, and take a level baseline photo.",
   "checklist": [
    "Routine completed and observed",
    "Baseline taken",
    "File named"
   ],
   "worked": {
    "title": "Worked example: a different object",
    "text": "A stapler on a tripod at eye level, centred, lit by the window: a clear starting point."
   },
   "frames": [
    "The step I nearly forgot was ___."
   ],
   "stretch": [
    "Time yourself setting up the tripod safely; beat it next lesson without skipping a step."
   ]
  },
  "d02": {
   "today": "Change one setting on purpose; record it.",
   "glossary": [
    [
     "Aperture",
     "Lens opening; f-number"
    ],
    [
     "Depth of field",
     "How much is sharp front to back"
    ],
    [
     "A/Av mode",
     "You choose aperture; the camera sets shutter"
    ]
   ],
   "summary": "In A/Av mode, shoot at f/4, f/8 and f/11 to see how much of the object stays sharp. Record every setting.",
   "checklist": [
    "Mode set to A/Av",
    "Three apertures shot",
    "Three compositions",
    "Settings recorded"
   ],
   "worked": {
    "title": "Worked example: a different object",
    "text": "A shoe at f/4 has a sharp toe but a blurry heel; at f/11 the whole shoe is sharp, which is better for documentation."
   },
   "frames": [
    "At f/___ the object ___ because ___."
   ],
   "stretch": [
    "Try the same comparison with the lens zoomed in versus out."
   ]
  },
  "d03": {
   "today": "Front, side and top views with a ruler.",
   "glossary": [
    [
     "Viewpoint",
     "Where the camera is"
    ],
    [
     "Straight on",
     "Camera square to the surface"
    ],
    [
     "Scale",
     "Something of known size in frame"
    ]
   ],
   "summary": "Straight-on views with a ruler let people measure; dramatic angles can distort size and shape.",
   "checklist": [
    "Front view",
    "Side view",
    "Top view",
    "Ruler visible",
    "Dramatic comparison"
   ],
   "worked": {
    "title": "Worked example: a different object",
    "text": "A mug from above shows it is round; from the side, its height against the ruler: 9 cm."
   },
   "frames": [
    "The best view for a modeller is ___ because ___."
   ],
   "stretch": [
    "Shoot the same object with the lens zoomed out close versus zoomed in far. Which distorts less?"
   ]
  },
  "d04": {
   "today": "Compare soft and hard light on one object.",
   "glossary": [
    [
     "Diffuser",
     "Material that softens light"
    ],
    [
     "Reflector",
     "White card that bounces light"
    ],
    [
     "White balance",
     "A camera setting that fixes colour cast"
    ]
   ],
   "summary": "Soft, even light shows edges for documentation; hard side light shows texture but can hide details.",
   "checklist": [
    "Soft setup",
    "Hard setup",
    "Same position",
    "Comparison"
   ],
   "worked": {
    "title": "Worked example: a different object",
    "text": "A textured brick sample: soft light shows its outline; side light shows every bump."
   },
   "frames": [
    "In setup ___ I can see ___, which is hidden in setup ___."
   ],
   "stretch": [
    "Light a shiny object without glare."
   ]
  },
  "d05": {
   "today": "Export for web and for print; explain.",
   "glossary": [
    [
     "PPI",
     "Pixels per inch when printed"
    ],
    [
     "Resample",
     "Adding or removing pixels"
    ],
    [
     "JPG / PNG",
     "Photo format / sharp-edge or transparent graphics format"
    ]
   ],
   "summary": "Web needs a modest pixel width and a small JPG. Print needs enough pixels: pixels ÷ PPI = inches.",
   "checklist": [
    "Original kept",
    "Web export",
    "Print size set",
    "Compared at 100%",
    "Reasons written"
   ],
   "worked": {
    "title": "Worked example: different numbers",
    "text": "A 2400 px wide photo prints 8 inches wide at 300 PPI (2400 ÷ 300)."
   },
   "frames": [
    "For the web I chose ___ because ___."
   ],
   "stretch": [
    "Work out the pixels needed for a 20 × 30 cm poster at 300 PPI."
   ]
  },
  "d06": {
   "today": "A consistent 5–8 stage making sequence.",
   "glossary": [
    [
     "Sequence",
     "Photos in order showing stages"
    ],
    [
     "Consistency",
     "Same position, light and framing each time"
    ]
   ],
   "summary": "Lock the tripod and light, change only the object, and photograph each visible stage.",
   "checklist": [
    "Stages planned",
    "Tripod marked",
    "All stages shot",
    "Close-up of the tricky step",
    "Captions"
   ],
   "worked": {
    "title": "Worked example: a different task",
    "text": "Making a paper cup: flat sheet, folded triangle, side folds, top folds, finished cup. Same framing each time."
   },
   "frames": [
    "Stage ___ shows ___."
   ],
   "stretch": [
    "Make the sequence understandable with no captions at all."
   ]
  },
  "d07": {
   "today": "Independent: solve the new capture problem.",
   "glossary": [
    [
     "Constraint",
     "A limit you must work within"
    ],
    [
     "Retake",
     "Shooting again after fixing a problem"
    ]
   ],
   "summary": "Solve the new situation with your own settings and light, record them, retake once, and explain why it documents well.",
   "checklist": [
    "Settings recorded",
    "Retake done",
    "Explanation",
    "Knowledge check"
   ],
   "worked": {
    "title": "No worked example today",
    "text": "This is independent evidence, so no example of the task is given. Use your success criteria."
   },
   "frames": [
    "My final photo documents well because ___, which you can see in ___."
   ],
   "stretch": [
    "Solve a second constraint card if time allows."
   ]
  },
  "d08": {
   "today": "A labelled reference sheet for a modeller.",
   "glossary": [
    [
     "Annotation",
     "A label or arrow that explains"
    ],
    [
     "Layer",
     "A separate level in the file"
    ]
   ],
   "summary": "Pick front, side, top and a detail; add dimensions and material labels on separate layers; mark edits.",
   "checklist": [
    "Photos chosen",
    "Dimensions labelled",
    "Material labelled",
    "Edits declared"
   ],
   "worked": {
    "title": "Worked example: a different sheet",
    "text": "A birdhouse: front view with height 20 cm, side view showing a 3 mm plywood edge, and a detail of the roof joint."
   },
   "frames": [
    "A modeller can find ___ here."
   ],
   "stretch": [
    "Add a simple key or legend for your labels."
   ]
  },
  "d09": {
   "today": "Defend your choices and package the handover.",
   "glossary": [
    [
     "Handover",
     "Passing work to the next stage"
    ],
    [
     "Reference brief",
     "A short note of what is provided and what is missing"
    ]
   ],
   "summary": "Explain one light and one viewpoint choice with evidence, and give the modelling sprint a tidy folder and a brief.",
   "checklist": [
    "Defence done",
    "Folder packaged",
    "Brief written",
    "Gallery post and two comments"
   ],
   "worked": {
    "title": "Worked example: a different handover",
    "text": "“Front, side and top of the library, ruler in each; height 14 cm; roof angle unknown, needs measuring.”"
   },
   "frames": [
    "I lit it with ___ so that ___."
   ],
   "stretch": [
    "Add one photo that answers the “unknown” in your brief."
   ]
  }
 }
};
