# Google AI Studio build prompt — Design Decisions

Paste the text below into Google AI Studio's app builder. This is a specification for a new app, not an app that has already been built or tested. Use it after the relevant teaching, in three short visits rather than one long session.

---

Build a small, accessible browser learning app called **Design Decisions** for Nova Scotia Communication Technology 11 students learning Photoshop. It checks understanding of graphic design; it does not replace Photoshop or grade practical mastery.

Use a single-page interface with three short activities. Show one activity and one question at a time. No dashboard, avatars, points, leaderboard, badges, timer, confetti, random content, or unrestricted control panels. Each activity should take approximately 4–6 minutes, including explanation and correction. Time is an estimate to pilot.

Produce a runnable app and its editable source. Prefer ordinary HTML/CSS/JavaScript with no backend, account, API key, runtime AI call or external dependency. If the build environment requires React, keep it a small frontend and provide an offline build. Do not invent integration with Google Forms, Student OS, a roster, a gradebook or the Evidence Map.

## Learning targets

Use the existing course identity `communications-technology-11`. These are instructional targets, not new registered assessment tasks:

- 4.1: recognise design elements and explain how principles organise them.
- 4.2: use a named colour wheel to choose a palette and give colours meaningful roles.
- 4.3: choose type for a purpose and distinguish kerning, tracking and leading.
- 4.4: connect an image and words to a specific audience/message.

Do not claim that the app establishes 4.5 web-export skill or practical Photoshop competence. Those require real file evidence and teacher review.

## Interaction sequence for every activity

1. Show a one-sentence audience/message brief and a fixed visual. Explain the concept in plain language and show a short worked example on a DIFFERENT design.
2. Require a prediction before enabling the comparison: which visible feature will change, and what difference does the student expect? Offer a paper/oral-response mode so typing speed is not the construct being tested. Never use a correct choice alone as evidence of understanding.
3. Let the student make ONE deliberate change. Use two or three labelled choices with plain descriptions, not sliders or arbitrary values. Keep other variables fixed.
4. Place the before and after at identical scale, with a text alternative. Ask what changed and whether it better meets the stated brief. Ask for visible evidence.
5. Give specific feedback on the factual concept and the observed change. Invite a correction. Do not use an LLM to silently judge prose, generate grades or invent student reasoning. For open explanations, provide comparison guidance and mark teacher review as pending. Preserve the first response and correction separately.
6. Give ONE fresh, different-case check with less help. Allow either typed reasoning or a recorded note that an oral/paper response was given. End with a next target, not a completion score.

## Activity 1 — Reading order

Audience: a student glancing at a school notice on a phone. Intended message: a free repair workshop, followed by when/where and then how to join. Use a clearly labelled **constructed practice notice**, not a fake real campaign.

In the first design, headline, date and action text are all the same size. Fix text content, colour, font, position, image and spacing. Offer headline-size choices: same as details, moderately larger, extremely large. Explain the choices in words. The moderately larger treatment is the intended teaching comparison, but the extreme version must visibly wrap/crowd or reduce the space available for details: do not simulate a failure that is absent from the displayed output.

Prediction: What will a reader probably notice first, and what might become harder to read? Observation: point to the changed relative scale and the remaining date/action. Distinguish a design hypothesis from measured eye-tracking or audience behaviour. Feedback names hierarchy, emphasis and the trade-off; it never says largest is always best.

Fresh check: a different library-hours notice where the opening time needs priority. Ask which element should lead and why. Do not reveal a complete redesign recipe.

## Activity 2 — Colour roles and readability

Show a labelled traditional RYB artist's colour wheel with primary/secondary/tertiary names and an accessible text list. State that it describes teaching hue relationships; screen documents use RGB light. Avoid treating an RYB blue/orange pair as the mathematical opposite pair on an RGB/HSV wheel.

Audience/message: a calm study-space invitation. Keep the words, positions, font and text/background pair fixed. Show two predefined palettes:

- Complementary on the RYB reference: broad blue field `#174C88`, small orange accent `#EC9848`.
- Analogous on the RYB reference: broad blue field `#174C88`, blue-green accent `#247E80`, green accent `#448260`.

Offer a single choice: which palette serves this brief, and which colour should have the dominant role? Different defensible choices are possible; accept reasoned trade-offs for teacher review. Do not make complementary automatically correct or analogous automatically safe.

Then show a separate reading problem using equal-hue light and dark text/background examples. Ask why changing the hue relationship alone cannot guarantee legibility. If displaying a contrast ratio, implement the standard sRGB relative-luminance formula correctly. Explain that WCAG's text thresholds are a web-text accessibility reference, not a universal aesthetic score, and that the app does not assess the whole poster's accessibility.

Fresh check: a high-urgency notice with the same palette families. Ask whether the same dominant/accent roles still serve the new purpose. Require a feature → purpose explanation.

## Activity 3 — Typography spacing

Show a short practice notice with two lines visibly crowded vertically. Keep letterforms, font size, words and character spacing fixed. Explain three available operations:

- Kerning: space between one letter pair.
- Tracking: space across a selected character run.
- Leading: distance between text baselines.

Let the student choose ONE operation. Show the actual consequence, including plausible wrong alternatives: tracking spreads letters but leaves the baseline crowding; kerning changes only a highlighted pair; leading separates the lines. Use real CSS equivalents labelled as a browser concept model, not a fabricated Photoshop interface.

Prediction and observation must name the affected spacing. Feedback explains the observed mismatch and asks the learner to choose one change and test again. The correct control without an explanation remains incomplete evidence.

Fresh check: a different headline with one awkward `AV` pair while baseline and overall run spacing are fine. Ask which operation addresses that local problem and what it leaves unchanged. Keep the answer hidden until the first response is recorded.

## Records, access and teacher use

Keep responses locally on this device with a visible explanation and a deliberate clear/reset confirmation. Store a content version, activity name, first prediction, chosen change, observation/explanation, feedback viewed, correction, fresh-case response and next target. Do not collect names, emails, voice recordings, uploaded student files or analytics. Activity labels are local UI labels, not registered Task IDs.

Provide a plain-text/JSON download for manual teacher review. Clearly say this does not submit to Student OS or issue an evidence receipt. The teacher reviews factual explanation, visible evidence, purpose/trade-off and changed-case reasoning. Show neither a total grade nor a claim that the student has mastered the concept.

Use large readable type, high contrast, keyboard controls, descriptive labels and focus indication. Do not rely on colour alone. Offer text/paper alternatives for each visual, student-controlled read-aloud where available, no autoplay, and reduced-motion support. Keep the before/after comparison visible without animation.

Supply a teacher README and test the three normal paths, three wrong choices, correction retention, fresh-case independence, reload/download/reset, keyboard operation, narrow screen, blocked network and colour-independent labels. Inspect that each declared change is actually visible and that no unrelated variable changes. State any tests not run. Do not call the app classroom-ready until the teacher has piloted one activity with students and checked whether it clarifies the concept.

Before adding a feature, ask: what observable understanding does this reveal that the existing activity cannot? If it adds clicks without new evidence, omit it.
