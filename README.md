# Communication 11 · Learning Studio

Course home: https://ctwadden.github.io/communication-technology-11/

The course home uses the same module and resource layout as Multimedia 12. Module 1 is Graphic Design & Photography, including Logo Look, Brand Foundations, the shared Photoshop foundation/bootcamp, Design Studio Explorer and Make It Matter. Further module links can be added as the course plan is confirmed. The MM12 advanced advertising sequence is not presented as required Communication 11 work.

## Existing teaching resources

- Brand Foundations unit: https://ctwadden.github.io/communication-technology-11/brand-foundations.html
- Logo Look: https://ctwadden.github.io/communication-technology-11/logo-look/
- Shared Drop Day with the COM11 course context: https://ctwadden.github.io/multimedia-12/photoshop/studio/drop-day/?course=COM11
- Assignment: https://ctwadden.github.io/communication-technology-11/assignment.html
- Student files: https://ctwadden.github.io/communication-technology-11/student-files.zip
- Teacher brief: https://ctwadden.github.io/communication-technology-11/teacher-guide.html

The original Brand Foundations homepage is preserved in `brand-foundations.html`. Its unit parts, assets, downloads, assessment pages and supporting resources remain at their existing paths. Course navigation points to the new homepage; the preserved unit also has a Unit home link.

## Rebuild the course home

Edit `factory/courses/com11.json`, then run from the repository root:

```sh
node factory/tools/make-splash.mjs --course factory/courses/com11.json --out index.html
```

Publish the catalogue, generator and generated homepage together. A card without a verified student URL displays “Online workbook coming soon”. Add the verified URL to that existing entry when the resource is published. Navigation anchors do not create or replace curriculum or evidence IDs.

The shared Coach and existing Drop Day knowledge/skill reflection are linked. This course page does not collect student data or expose the teacher assessment dashboard.
