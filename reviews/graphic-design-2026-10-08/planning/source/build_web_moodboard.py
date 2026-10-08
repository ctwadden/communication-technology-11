"""Build the no-install Excalidraw lab from genuine browser action captures."""
from pathlib import Path
import sys, json, hashlib, shutil
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).resolve().parent
OUT=ROOT/'student/planning'; IMG=OUT/'img'; RAW=HERE/'web-raw'
FONT=ImageFont.truetype(str(ROOT/'student/labs/fonts/DejaVuSans-Bold.ttf'),16)
INK='#193443'
# Each box identifies the actual control/result for the adjacent instruction.
specs=[
 ('01-free-editor.jpg','web-open.jpg',(360,12,917,65),'1.1 Open the free editor. The top toolbar is available without signing up.'),
 ('02-text-tool.jpg','web-text-tool.jpg',(739,15,782,61),'1.2 Choose Text; the left panel shows Normal and the size controls.'),
 ('03-title.jpg','web-title.jpg',(63,171,144,279),'1.3 Set Normal and Large, then enter the title on the canvas.'),
 ('04-brief.jpg','web-brief.jpg',(263,142,1104,203),'1.4 Add audience, action and tone as editable text.'),
 ('05-insert-image-menu.jpg','web-image-menu.jpg',(720,77,905,109),'2.1 Alternative: More tools → Insert image. File-picker completion is not yet verified.'),
 ('06-image-pasted-too-high.jpg','web-image-wrong.jpg',(592,0,1028,280),'2.2 Observed mistake: pasted image covers the brief and extends above the canvas view.'),
 ('07-image-moved.jpg','web-image-moved.jpg',(304,210,736,580),'2.3 Drag the image below the brief. The words are visible again.'),
 ('08-image-resized.jpg','web-image-resized.jpg',(596,455,619,483),'2.4 Drag a corner handle to reduce size while keeping the cup proportions.'),
 ('09-palette-heading.jpg','web-palette-heading.jpg',(650,210,844,247),'3.1 Add the colour-role heading with Text.'),
 ('10-swatch-drawn.jpg','web-swatch.jpg',(507,18,537,58),'3.2 Choose Rectangle and drag a small swatch. Keep it selected.'),
 ('10-swatch-drawn.jpg','web-background-control.jpg',(169,171,204,204),'3.3a Background opens the fill picker; this is different from Stroke.'),
 ('11-fill-picker.jpg','web-fill-picker.jpg',(244,413,418,448),'3.3 Background opens the fill picker; use the Hex code field.'),
 ('12-cream-applied.jpg','web-cream.jpg',(246,412,420,447),'3.4 Enter f4ead5 for cream; click outside the picker to finish.'),
 ('13-text-swatch-drawn.jpg','web-ink-swatch.jpg',(653,329,711,388),'3.5 Make a second swatch for main words, then open its Background picker.'),
 ('14-ink-applied.jpg','web-ink.jpg',(653,329,711,388),'3.6 Apply 193443 for dark ink; this swatch represents the main words.'),
 ('15-accent-swatch-drawn.jpg','web-accent-swatch.jpg',(653,394,711,452),'3.7 Make a third swatch for a small accent.'),
 ('16-accent-applied.jpg','web-accent.jpg',(653,394,711,452),'3.8 Apply b85a36 for terracotta. These are worked-example values.'),
 ('17-cream-label.jpg','web-cream-label.jpg',(715,258,1112,304),'3.9 Label the cream swatch: colour name, role and hex value.'),
 ('18-ink-label.jpg','web-ink-label.jpg',(715,328,1112,369),'3.10 Label the dark swatch as main words.'),
 ('19-accent-label.jpg','web-accent-label.jpg',(715,390,1105,435),'3.11 Label the terracotta swatch as accent.'),
 ('20-type-direction.jpg','web-type-direction.jpg',(265,488,1112,528),'3.12 Describe the type direction instead of just naming a favourite font.'),
 ('21-headline-sample.jpg','web-headline.jpg',(64,239,143,277),'3.13 Set Large for a headline sample; Normal is the editor specimen, not a required Photoshop font.'),
 ('22-detail-sample.jpg','web-detail.jpg',(268,561,1100,599),'3.14 Add a smaller detail sample to show the information roles.'),
 ('23-reason.jpg','web-reason.jpg',(265,601,1140,638),'3.15 Explain the visible feature and its possible purpose for this audience.'),
 ('24-board-complete.jpg','web-credit.jpg',(266,639,1130,675),'2.5 / 3.16 Credit the reference and inspect the whole board. This is constructed practice.'),
 ('25-save-menu.jpg','web-save-menu.jpg',(19,102,241,135),'4.1 Main menu → Save to… is the editable-file route.'),
 ('26-save-to-disk.jpg','web-save-disk.jpg',(340,491,459,549),'4.2 Choose Save to file under Save to disk. Actual disk save/reopen remains unverified here.'),
 ('27-export-menu.jpg','web-export-menu.jpg',(18,135,241,168),'4.3 Main menu → Export image… opens the image review/export dialog.'),
 ('28-export-preview.jpg','web-export-preview.jpg',(1000,349,1116,388),'4.4 Preview with Background on and Scale 2×; inspect the board before exporting.'),
 ('30-copy-export.jpg','web-copy-export.jpg',(954,494,1116,545),'4.5 Copy to clipboard produced the actual PNG. The author saved its bytes through the browser clipboard API.'),
]
crops={
 'web-open.jpg':None,'web-text-tool.jpg':(0,0,900,470),'web-title.jpg':(5,75,750,315),'web-brief.jpg':(250,120,1140,220),
 'web-image-menu.jpg':(710,65,918,445),'web-image-wrong.jpg':(250,0,1060,520),'web-image-moved.jpg':(250,90,1120,610),'web-image-resized.jpg':(275,185,640,495),
 'web-palette-heading.jpg':(630,195,880,265),'web-swatch.jpg':(495,0,805,350),'web-background-control.jpg':(10,148,211,218),'web-fill-picker.jpg':(235,370,425,461),'web-cream.jpg':(235,370,425,461),
 'web-ink-swatch.jpg':(630,250,1105,465),'web-ink.jpg':(630,250,1105,465),'web-accent-swatch.jpg':(630,250,1105,465),'web-accent.jpg':(630,250,1105,465),
 'web-cream-label.jpg':(630,250,1125,465),'web-ink-label.jpg':(630,250,1125,465),'web-accent-label.jpg':(630,250,1125,465),
 'web-type-direction.jpg':(250,478,1130,540),'web-headline.jpg':(14,146,155,285),'web-detail.jpg':(250,550,1130,610),'web-reason.jpg':(250,590,1160,645),'web-credit.jpg':(250,630,1140,690),
 'web-save-menu.jpg':(14,58,250,180),'web-save-disk.jpg':(295,220,525,559),'web-export-menu.jpg':(14,58,250,180),'web-export-preview.jpg':(125,135,1155,588),'web-copy-export.jpg':(750,200,1130,565)}
manifest=[]
for source,target,rect,caption in specs:
 raw=RAW/source; im=Image.open(raw).convert('RGB'); d=ImageDraw.Draw(im)
 d.rectangle(rect,outline='#ff870f',width=7)
 crop=crops[target]
 if crop:im=im.crop(crop)
 n=caption.split(' ',1)[0]
 frame=Image.new('RGB',(im.width,im.height+48),'white');frame.paste(im,(0,48))
 ImageDraw.Draw(frame).text((14,9),f'Action {n}',font=FONT,fill=INK)
 frame.save(IMG/target,quality=92)
 manifest.append(dict(raw=source,derived=target,box=rect,caption=caption,crop=crop,sha256_raw=hashlib.sha256(raw.read_bytes()).hexdigest()))
# Cropped genuine canvas/result visuals for the presentation; no controls invented.
Image.open(RAW/'24-board-complete.jpg').crop((258,83,1143,681)).save(IMG/'web-board-result.jpg',quality=94)
Image.open(RAW/'24-board-complete.jpg').crop((638,210,1127,456)).save(IMG/'web-colour-roles.jpg',quality=94)
shutil.copy2(OUT/'assets/COM11_MoodBoard_Worked_Example.png',IMG/'web-board-export.png')
(HERE/'web-capture-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
sys.path.insert(0,str(ROOT.parent/'sprint-engine'))
from guide_engine import Guide,COACH,STUDENT_OS
g=Guide(HERE/'web-package','com11-web-moodboard-practice-v1','A mood board in your browser','Communication Technology 11','Local planning practice; not a registered assessment')
SOURCES={'Excalidraw':('Free browser editor; observed 8 October 2026','https://excalidraw.com'),
 'Licence':('MIT-licensed Excalidraw source and features','https://github.com/excalidraw/excalidraw'),
 'Format':('Official editable-file and clipboard schema','https://docs.excalidraw.com/docs/codebase/json-schema')}
def captures(names):
 return ''.join('<figure><img class="zoomable" src="img/'+target+'" alt="'+caption+'" loading="lazy" tabindex="0"><figcaption>'+caption+'</figcaption></figure>' for _,target,_,caption in specs if target in names)
def step(title,doc,sel,route,actions,why,check,fix,names,worked,stretch,notice=''):
 g.step(title,doc,sel,route,actions,None,why,check,fix,refs='Excalidraw · Licence · Format',summary=check,
 glossary=[('Mood board','A proposal for image, colour, type and tone, with reasons.'),('Hex code','A six-digit RGB colour value.'),('Editable file','A saved .excalidraw scene retaining separate objects; different from a flattened PNG.')],
 worked=worked,stretch=stretch,extra=notice+captures(names))
g.session('A','Build a direction, then explain it','Before Photoshop artboards','About 25 minutes of the first planning class; teacher confirms school access and saving first. Open the planning log beside the browser.','Choose and explain a visual direction without installing anything.')
step('Start with the brief and text','A new Excalidraw canvas','No existing learner drawing','excalidraw.com → Text → Normal / size',[
 'Open https://excalidraw.com in the school browser. Use the free canvas. No account, installation or Excalidraw+ subscription is needed for this lab. If school filtering blocks the address, ask your teacher to use the paper-board fallback; do not try to bypass the filter.',
 'If your previous drawing opens, save it before starting a new board. For this practice use a blank canvas. Choose Text in the top toolbar; choose Normal and Large in the left panel.',
 'Click the canvas and type NORTHCOAST / QUIET MOMENT. Press Escape to finish editing. This is a constructed café example, not a real campaign.',
 'Choose Text again; use Medium for two brief lines. Name the audience (people seeking a quiet break), action (notice a calm invitation) and tone (warm, calm, uncluttered). For your own board, replace these with your actual approved brief.'
 ],'A mood board is a proposal for a particular reader. The tool cannot decide the intended message for you.','The board names a reader, an action and three tone words; text objects remain editable.','If the board only says “looks nice,” return to the brief. If a previous drawing appears, preserve it before beginning.',
 ['web-open.jpg','web-text-tool.jpg','web-title.jpg','web-brief.jpg'],
 'The practice title names a direction. It makes no claim that an audience already liked it.','Explain how the tone would change for an urgent school notice.')
step('Add and credit a purposeful image','Current browser board + permitted reference','Image object with Selection','Permitted image → paste or More tools → Insert image',[
 'Use the supplied original cup reference for the worked example. Open the image link below; copying an image through your browser menu is the student route, but that copy-source operation has not yet been cold-run. The author run used an automated clipboard step to supply the image; your teacher must verify the student copy-image route.',
 'Return to the canvas and paste (Ctrl+V on Windows/Chromebook; Command+V on Mac). Pasting into the canvas was observed. Alternative: More tools → Insert image, then choose a permitted PNG/JPEG and place it. The file-picker alternative has not completed in this author test.',
 'Choose Selection and drag the image below the brief. Our actual first paste covered the words and extended above the visible canvas. The next capture shows the corrected placement.',
 'With the image selected, drag a corner handle to reduce it while retaining proportions. Leave space for the colour and type decisions. Inspect the cup: it should not look stretched.',
 'Use Text → Small for a credit line: original Learning Studio cup illustration, supplied for class reuse. For every real reference, record creator, source URL and permission in the planning log. Study real ads in the main presentation; use original or permitted production assets.'
 ],'One reference should communicate a direction and a reason. A pile of pictures is not an explanation.','The brief is visible, the image has sensible proportions, and its source/permission are recorded.','When the image covers words, move that object before changing the type. If distorted, undo the resize and use a corner handle.',
 ['web-image-menu.jpg','web-image-wrong.jpg','web-image-moved.jpg','web-image-resized.jpg','web-credit.jpg'],
 'The single cup and open space propose calm. It is a starting hypothesis to discuss, not audience-effect evidence.','Use a permitted reference that suggests a different tone; explain the tradeoff.',
 '<p><a href="assets/cup-reference-original.png" target="_blank">Open the original cup reference</a>. The author run used an automated clipboard step. Student copy-image and file import need classroom verification.</p>')
step('Give colour and type clear roles','Current browser board','One swatch or text object at a time','Rectangle → Background → Hex code; Text → Normal / size',[
 'Add COLOUR ROLES with Text → Medium. Choose Rectangle and drag a small swatch. Keep it selected. For the tidy worked model, choose Architect under Sloppiness and Sharp under Edges; these style settings do not establish good design.',
 'Open Background in the left panel. Enter f4ead5 in Hex code, then click outside the picker. Use Solid fill. Make a second swatch and enter 193443; make a third and enter b85a36. These cream/ink/terracotta values belong to the worked example; your independent board needs justified choices.',
 'Label each swatch with Text → Medium: Cream / background / #f4ead5; Dark ink / main words / #193443; Terracotta / accent / #b85a36. The role tells a reader what the colour will do.',
 'Add TYPE DIRECTION / simple sans serif; clear headline and detail. Use Text → Normal → Large for Find your quiet moment, then Medium for a detail sample. The editor’s specimen is not a promise that the same font is installed in Photoshop. Record the intended licensed final font separately.',
 'Add a reason tied to a visible feature and this audience. Worked reasoning: one focal object and open space suggest calm; dark words carry information. Check the whole board at a useful viewing size. Ask another person what direction they see; record their actual words, or label a self-check honestly.'
 ],'Roles connect the palette and type to the message. A palette relationship or font name alone does not prove readability.','Image, background/main-word/accent roles, two type roles and an audience-based reason can all be found.','If the swatch is empty, check Background rather than Stroke and choose Solid. If you cannot explain a reference’s purpose, remove or replace it.',
 ['web-palette-heading.jpg','web-swatch.jpg','web-background-control.jpg','web-fill-picker.jpg','web-cream.jpg','web-ink-swatch.jpg','web-ink.jpg','web-accent-swatch.jpg','web-accent.jpg','web-cream-label.jpg','web-ink-label.jpg','web-accent-label.jpg','web-type-direction.jpg','web-headline.jpg','web-detail.jpg','web-reason.jpg'],
 'Cream is a background role; dark ink carries words; a small terracotta accent can mark an action. Test the actual text contrast later in Photoshop.','Change the audience or viewing setting; retain one choice and change another, explaining both.')
step('Save a master and a review image','surname_MoodBoard_v01.excalidraw + .png','All board objects; click empty canvas before export','Main menu → Save to… / Export image…',[
 'Do not rely on browser autosave on shared school computers. Main menu → Save to… → Save to file under Save to disk. Save surname_MoodBoard_v01.excalidraw in your approved class project folder. Confirm that an actual file exists. This disk-save operation has not completed in the author’s in-app browser; teacher verification is required.',
 'Click empty canvas so export covers the board. Main menu → Export image…; inspect the preview, keep Background on and use Scale 2× for the worked model. Choose PNG and save surname_MoodBoard_v01.png. The PNG download path still needs a teacher check. Copy to clipboard produced the supplied actual PNG; its author save used automated file handling.',
 'Use Main menu → Open to reopen your .excalidraw file. Check that the image is present and text/swatches can be edited separately. This file-picker/reopen procedure remains not yet verified. A browser reload is not a file-reopen test. The supplied editable example was prepared from the editor’s actual copied objects. Author file preparation used automation.',
 'Keep both files and the planning log. In Photoshop, select 01_MOOD and use File → Place Embedded for the PNG reference; keep .excalidraw for browser edits. Photoshop placement is covered in the main planning guide and still needs native verification. The PNG reference does not preserve Photoshop text layers.',
 'Explain a reference choice, one colour role and one type role. Then make your own board for an approved real message with less help. Choose references and values yourself. Use the current assigned Student OS task only when your teacher provides it; this local lab has no connected Form or automatic score.'
 ],'The editable master preserves decisions; the PNG lets others review the direction and bring it into Photoshop.','An actual saved scene reopens with separate editable objects, and its PNG shows the whole board clearly. The school browser save/reopen check must pass before classroom release.','If only a PNG was saved, return to the canvas and save an editable .excalidraw master. If a file is absent, do not assume autosave protects it. Ask the teacher to resolve school download/storage access.',
 ['web-save-menu.jpg','web-save-disk.jpg','web-export-menu.jpg','web-export-preview.jpg','web-copy-export.jpg'],
 'Worked example files accompany this page. The PNG was produced by the actual editor; the editable example retains separate objects and its image.','After successful saving, change one direction choice, keep the first version and explain why the new brief requires it.',
 '<p class="notice"><strong>Not yet fully run:</strong> disk save, file-picker import/reopen and PNG download in a school browser. Tested: canvas creation, editable text, pasted image, moving/resizing, swatch values, type roles, copy-scene data and Copy PNG. Independent cold run is pending.</p>')
g.build(eyebrow='COM11 · NO INSTALL · BROWSER MOOD BOARD',h1a='Choose a direction.',h1b='Explain the choices.',lead='Build a mood board in the free Excalidraw browser editor, then use its image as a reference for Photoshop ad layouts.',tags=['Free editor','MIT open source','No account for this lab','Draft: school saving unverified'],hero_img='web-board-export.png',hero_alt='Actual PNG export of the worked browser mood board',hero_caption='Actual Excalidraw PNG export. Constructed practice, original illustration; this is a direction proposal, not a real advertisement.',hero_side='<h3>Three things to keep</h3><ol><li>Editable .excalidraw file</li><li>Review PNG</li><li>Credited planning log</li></ol>',brief='<section class="panel"><h2>A direction for a real message</h2><p>Use this browser lab after stage 1 of the <a href="guide.html">main planning guide</a>, before Photoshop artboard setup. It takes the mood-board portion of the first proposed planning class, not an extra software installation.</p><p><a href="https://excalidraw.com" target="_blank" rel="noopener">Open the free editor</a> · <a href="assets/COM11_MoodBoard_Worked_Example.excalidraw" download>Editable worked example</a> · <a href="assets/COM11_MoodBoard_Worked_Example.png" download>Actual worked PNG</a> · <a href="assets/planning-log.txt" download>Planning log</a></p><p>Teacher checks school-domain access, downloads and reopening first. If blocked, make the same board on paper with permitted references, swatches, type examples and annotations.</p></section>',industry='<section class="panel"><h2>Discuss the direction early</h2><p>A designer uses references to discuss tone, type and image choices with a client before polishing the final layout. Each reference needs a reason and a credit.</p></section>',lens='<section class="panel"><h2>Mood board, thumbnail, artboard</h2><p>A mood board proposes a visual direction. A thumbnail proposes the arrangement. A Photoshop artboard is a named canvas for a layout. Browser mood board → PNG reference → two Photoshop sketches → fair reader test → revision.</p></section>',assesses='<section class="panel"><h2>What your teacher reviews</h2><p>Explain how image, colour and type choices serve the actual audience. Respond to a changed brief. Completing tool steps is practice; your teacher considers product, observation and conversation.</p></section>',practical_step=4,qa=['Specific audience/action/tone named.','Permitted image with a credit and reason.','Background, main words and accent roles labelled.','Headline/detail direction explained.','Actual saved master and PNG checked; reopen verified in the school browser.'],evidence=['Which visible feature informs your direction, and why?','What does each colour do?','How are headline/detail roles different?','What did the reader actually say?','What did your file/reopen check show?'],frames='“This feature may help __ because __.” “I would change __ for the new audience because __.”',sources=SOURCES,credits_file=HERE/'credits.json',used_photos=[],footer='Review draft: source-copy/file-picker/disk-save/reopen/download and non-author cold run remain unverified. Author image/file preparation used automated clipboard and file handling. No installation, account, public share link, live Form or evidence synchronization was created.',evidence_title='COM11 browser mood-board practice reflection',evidence_file='COM11_MoodBoard_Reflection.txt',css_labels=('COM11 / MOOD BOARD','CHOOSE A DIRECTION'))
src=HERE/'web-package/student/guide.html'
page=src.read_text().replace('<h2>Keep it short and specific.</h2>',f'<h2>Keep it short and specific.</h2><p><a href="{COACH}" target="_blank" rel="noopener">Open shared Coach</a> · <a href="{STUDENT_OS}" target="_blank" rel="noopener">Open Student OS</a>. Use your assigned task; this practice has no connected Form.</p>')
page=page.replace('</style>','figure img{width:100%;height:auto} .target{overflow-wrap:anywhere} @media print{header{padding:18pt}header h1{font-size:30pt}header .hero{display:block}header .hero img{max-height:220px}.panel{break-before:auto;break-inside:auto;margin:8pt 0;padding:6pt 0}.part{break-before:page}.step{break-before:page;break-inside:auto}.step figure{break-inside:avoid}.step figure img{max-height:210px}#step-2 figure img,#step-3 figure img{max-height:180px}.step h3{font-size:20pt}.step p,.step li{font-size:11pt}.step .target{font-size:10pt}.refs,nav,.done{display:none}textarea{display:block;min-height:18mm;height:18mm}}</style>')
(OUT/'web-moodboard.html').write_text(page)
print('4-stage browser lab; 30 annotated action captures; actual worked PNG and copied editable scene.')
