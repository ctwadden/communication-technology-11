# Trilingual lesson assets

Published 5 October 2026. The two existing root lesson filenames retain their original space and `(1)` suffix so student links do not change.

- `brand-base.html` and `art-base.html`: unchanged original English lessons, retaining sources, diagrams, IDs, slide order and pause points.
- `*-fr-1.json`, `*-fr-2.json`, `*-es-1.json`, `*-es-2.json`: reviewed translation data in original slide order. `i` is the zero-based slide index; `T/S/C/N` are title/subtitle/caption/narration; `X` contains ordered diagram labels; `A/Q/L` contain task, quiz and link-label translations. Original quiz answer indexes and link destinations come from the base lesson.
- `loader.js`: loads only same-site lesson assets, localizes the existing player and selects a matching browser voice. No paid API, remote AI translation, login, roster or assessment service is added. Only the last slide and chosen language are saved locally; answers are not stored or submitted.

Use the root `Trilingual_Lessons.html` page for all language links. Original brand artwork, source publication titles and linked videos are not redrawn or dubbed.

For future edits, update the base lesson and all matching language data together. The loader checks slide order and diagram-label counts before activating the multilingual controls.
