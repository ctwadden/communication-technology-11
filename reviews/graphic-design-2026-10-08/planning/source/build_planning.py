"""Reproducible original planning illustrations and source-based review guide.
Native Photoshop captures stay distinct from authored teaching diagrams.
"""
from pathlib import Path
import sys, json, shutil, textwrap, hashlib
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).resolve().parent
OUT=ROOT/'student/planning'
IMG=OUT/'img'; IMG.mkdir(parents=True,exist_ok=True)
FONTS=ROOT/'student/labs/fonts'
INK='#193443'; TEAL='#056068'; ORANGE='#b85a36'; PAPER='#fbfaf6'
def font(n,b=False):return ImageFont.truetype(str(FONTS/('DejaVuSans-Bold.ttf' if b else 'DejaVuSans.ttf')),n)
def panel(size=(1080,1350)):
    im=Image.new('RGB',size,PAPER);return im,ImageDraw.Draw(im)
def text(d,xy,t,n=32,b=False,c=INK,width=48,spacing=12):
    lines=[]
    for s in t.split('\n'):lines+=textwrap.wrap(s,width=width) or ['']
    d.multiline_text(xy,'\n'.join(lines),font=font(n,b),fill=c,spacing=spacing)
def save(im,name):im.save(IMG/name,optimize=True)
def box(d,rect,fill=None,outline=INK,w=3):d.rounded_rectangle(rect,12,fill=fill,outline=outline,width=w)

from build_reference import build_reference
build_reference()

# Mood board is deliberately a constructed example, not a fictitious real campaign.
im,d=panel();text(d,(55,42),'NORTHCOAST / QUIET MOMENT',36,True,width=40)
text(d,(55,100),'MOOD BOARD · constructed practice example',21,c=TEAL,width=60)
box(d,(55,170,625,655),fill='#ece0c9',outline=None)
d.ellipse((170,460,505,580),fill='#b8ab91');d.rounded_rectangle((215,320,430,515),25,fill=PAPER,outline=INK,width=6)
d.arc((390,342,495,470),270,90,fill=INK,width=14)
for x in [260,315,370]:d.arc((x,226,x+26,315),60,285,fill=ORANGE,width=5)
text(d,(83,192),'IMAGE DIRECTION',22,True,c=TEAL);text(d,(83,590),'Calm space · one clear focal object',22,width=38)
text(d,(674,177),'PALETTE ROLES',26,True)
for y,col,label in [(234,'#f4ead5','Cream / background'),(340,INK,'Ink / readable words'),(446,ORANGE,'Terracotta / accent')]:
    box(d,(674,y,745,y+65),fill=col,outline=None);text(d,(765,y+10),label,20,width=18)
text(d,(674,563),'Small accent,\nclear contrast',23,b=True,width=19)
box(d,(55,704,1025,1012),fill='#e4eeea',outline=None)
text(d,(83,730),'TYPE + TONE',24,True,c=TEAL)
text(d,(83,790),'Find your quiet moment',40,True,width=34)
text(d,(83,855),'Simple sans serif / clear information',26,width=47)
text(d,(83,915),'Calm · warm · uncluttered',25,width=48)
text(d,(55,1062),'WHY THESE REFERENCES?',28,True)
text(d,(55,1120),'One focal object and generous space support a calm tone. Dark words carry the message; the warm accent marks the action.',25,width=57)
text(d,(55,1288),'Original illustration + DejaVu Sans. Not a Photoshop screenshot.',18,width=82)
save(im,'mood-board-model.png')

for variant in ['A','B']:
    im,d=panel();text(d,(55,35),f'SKETCH {variant} / SAME BRIEF',32,True)
    text(d,(55,93),'1080 × 1350 · layout hypothesis, not finished ad',21,c=TEAL,width=70)
    if variant=='A':
        box(d,(70,170,1010,350));text(d,(110,210),'HEADLINE FIRST',47,True,width=30)
        box(d,(160,420,920,935),fill='#ece0c9');d.line((170,430,910,925),fill='#9d8d74',width=3);d.line((910,430,170,925),fill='#9d8d74',width=3)
        text(d,(290,642),'FOCAL IMAGE',40,True,width=24)
        box(d,(70,1020,720,1130));text(d,(105,1045),'SUPPORTING DETAIL',28,width=30)
        box(d,(70,1170,580,1270),fill=ORANGE,outline=None);text(d,(108,1190),'NEXT ACTION',32,True,c='white',width=30)
    else:
        box(d,(70,170,1010,770),fill='#ece0c9');d.line((80,180,1000,760),fill='#9d8d74',width=3);d.line((1000,180,80,760),fill='#9d8d74',width=3)
        text(d,(215,437),'IMAGE FIRST',46,True,width=25)
        box(d,(70,830,1010,990));text(d,(110,870),'HEADLINE SECOND',44,True,width=30)
        box(d,(70,1040,1010,1130));text(d,(105,1060),'SUPPORTING DETAIL',28,width=40)
        box(d,(500,1170,1010,1270),fill=ORANGE,outline=None);text(d,(540,1190),'NEXT ACTION',32,True,c='white',width=28)
    save(im,f'sketch-{variant.lower()}-model.png')

im,d=panel((1500,650));text(d,(48,35),'SAME DIRECTION · DIFFERENT READING ORDER',34,True,width=60)
for x,v in [(50,'a'),(480,'b')]:
    pic=Image.open(IMG/f'sketch-{v}-model.png');pic.thumbnail((375,470));im.paste(pic,(x,133))
text(d,(930,148),'COMPARE A / B',30,True,width=22)
text(d,(930,217),'Keep the audience, copy, palette and size fixed. Change the hierarchy.',26,width=28)
text(d,(930,367),'Predict → ask a reader → record → revise',28,True,c=TEAL,width=26)
text(d,(48,616),'Teaching models drawn for this package. They do not depict Photoshop controls.',18,width=100)
save(im,'compare-sketches.png')
im,d=panel((1500,650));text(d,(48,35),'A PLAN MAKES YOUR CHOICES VISIBLE',36,True,width=70)
for x,label,sub in [(48,'1 / BRIEF','Audience + action'),(412,'2 / DIRECTION','Mood + references'),(776,'3 / OPTIONS','Sketch A + sketch B'),(1140,'4 / TEST','Response + revision')]:
    box(d,(x,180,x+310,480),fill='#e4eeea',outline=None);text(d,(x+24,210),label,27,True,c=TEAL,width=20);text(d,(x+24,295),sub,28,width=16)
text(d,(48,550),'Keep the first attempt. Explain the change using visible evidence.',26,width=85)
text(d,(48,613),'Original teaching diagram · not a Photoshop interface',18,width=100)
save(im,'planning-process.png')
im,d=panel((1500,650));text(d,(48,40),'MOOD BOARD / WHAT IT COMMUNICATES',35,True,width=65)
thumb=Image.open(IMG/'mood-board-model.png');thumb.thumbnail((380,475));im.paste(thumb,(50,130))
for y,t in [(153,'Image treatment: calm, simple, one focal object'),(265,'Colour roles: background, words, action'),(377,'Type roles: headline, detail, tone'),(489,'Annotations: why each choice serves this audience')]:text(d,(480,y),t,30,width=48)
save(im,'mood-explained.png')

# Genuine captures: crop only; annotate the observed controls without changing values.
capture_specs=[
 ('03-document-name.png','native-name.jpg',(1535,170,2150,350),(1580,235,2070,300),'2.1'),
 ('04-width.png','native-width.jpg',(1535,300,2150,480),(1580,360,1730,430),'2.2'),
 ('07-artboards-enabled.png','native-artboards.jpg',(1535,440,2150,620),(1875,486,1935,548),'2.4'),
 ('06-resolution-and-profile.png','native-profile.jpg',(1535,565,2150,1150),(1580,607,2120,1120),'2.5'),
 ('08-created-wrong-height.png','native-wrong-height.jpg',None,(0,1720,550,1840),'CHECK')]
caps=[]
for source,target,crop,rect,num in capture_specs:
    raw=HERE/'raw'/source
    im=Image.open(raw).convert('RGB');di=ImageDraw.Draw(im)
    di.rectangle(rect,outline='#ff870f',width=9)
    if crop:im=im.crop(crop)
    framed=Image.new('RGB',(im.width,im.height+54),'white');framed.paste(im,(0,54))
    ImageDraw.Draw(framed).text((12,10),'Action '+num+' / genuine capture',font=font(23,True),fill=INK)
    im=framed
    im.save(IMG/target,quality=92)
    caps.append({'raw':source,'derived':target,'source_sha256':hashlib.sha256(raw.read_bytes()).hexdigest(),'crop':crop,'orange_box':rect,'annotation':num,'kind':'genuine Photoshop UI capture; observed wrong height remains visible'})
im=Image.open(HERE/'raw/06-resolution-and-profile.png').convert('RGB')
im.crop((1535,300,2150,610)).save(IMG/'native-size-detail.jpg',quality=94)
ImageDraw.Draw(im).rectangle((1580,486,1730,550),outline='#ff870f',width=8)
im.crop((1535,300,2150,610)).save(IMG/'native-height-diagnosis.jpg',quality=94)
for n,box_ in [('native-size-detail.jpg',None),('native-height-diagnosis.jpg',[1580,486,1730,550])]:
 caps.append(dict(raw='06-resolution-and-profile.png',derived=n,crop=[1535,300,2150,610],orange_box=box_,kind='genuine native capture; inherited incorrect height visible'))
(HERE/'capture-manifest.json').write_text(json.dumps(caps,indent=2)+'\n')

sys.path.insert(0,str(ROOT.parent/'sprint-engine'))
from guide_engine import Guide,COACH,STUDENT_OS
from theory_deck import build_deck
from add_deck_recall import apply_recall,q

SOURCES={
 'Excalidraw':('Free MIT-licensed browser editor; observed 8 October 2026','https://github.com/excalidraw/excalidraw'),
 'Adobe-New':('Create artboard documents · checked 8 October 2026','https://helpx.adobe.com/photoshop/desktop/create-manage-layers/layout-design-tools/create-artboard-documents.html'),
 'Adobe-Add':('Add artboards · checked 8 October 2026','https://helpx.adobe.com/photoshop/desktop/create-manage-layers/layout-design-tools/add-artboards-current-document.html'),
 'Adobe-Properties':('Artboard properties · checked 8 October 2026','https://helpx.adobe.com/photoshop/desktop/create-manage-layers/layout-design-tools/artboard-properties.html'),
 'Adobe-Place':('Place files · checked 8 October 2026','https://helpx.adobe.com/photoshop/desktop/create-open-import-images/import-files/place-a-file-in-photoshop.html'),
 'Adobe-Use':('Use artboards and export · checked 8 October 2026','https://helpx.adobe.com/photoshop/desktop/create-manage-layers/get-started-layers/use-artboards-to-lay-out-designs.html'),
 'Adobe-Mood':('Design processes and mood boarding · checked 8 October 2026','https://blog.adobe.com/en/publish/2019/02/28/from-design-thinking-to-the-mood-boarding-6-commonly-used-design-processes-to-try-on-your-next-project'),
 'NS':('Nova Scotia Communications Technology 11 course source','https://curriculum.novascotia.ca/english-programs/course/communications-technology-11')}
PENDING='<p class="notice"><strong>Photoshop procedure not yet fully run.</strong> Native captures stop after creation of the first artboard with an incorrect height. Further per-action screenshots, correction, saved PSD and reopen/export proof are pending. This section needs a live teacher demonstration before student use.</p>'
g=Guide(HERE/'package','com11-ad-planning-practice-v1','Plan an ad with mood boards and artboards','Communication Technology 11','Local practice supplement; not a registered sprint')
def st(title,doc,sel,route,actions,why,check,fix,fig=None,refs='',extra='',pending=False,worked='',stretch=''):
 g.step(title,doc,sel,route,actions,fig,why,check,fix,refs=refs,summary=title+'. '+check,glossary=[('Mood board','A visual proposal for image, colour, type and tone.'),('Artboard','A named canvas inside one Photoshop document.'),('Thumbnail','A quick layout sketch showing the order and size of information.')],worked=worked,stretch=stretch,extra=(PENDING if pending else '')+extra)
g.session('A','Set a direction before you design','Lesson 1','70 minutes suggested: 5 recall, 12 concept teaching/checks, 10 brief, 25 setup/reference planning, 10 explain, 8 save/check. Teacher verifies native demonstration first.','Understand the audience; build a direction board with reasons.')
st('Name the communication problem','planning-log.txt','Approved school/community brief','Brief → audience → action → constraints',[
 'Choose one actual approved message from the four director choices in the main lab route. Verify wording, dates, location and image permission with your teacher.',
 'Write: “My audience is __. After viewing, I want them to __. They will see this at __.”',
 'Record the exact size and required information. For this digital practice use 1080 × 1350 px; change it only when the real delivery brief requires it.'
 ],'A design succeeds when the right reader can find the message and action.','Your brief names a particular audience and observable next action.','Replace “everyone” and “looks nice” with a reader, setting and action.',fig=('img:planning-process.png','Original diagram: brief → direction → options → test.'),worked='NorthCoast is a constructed practice café. A calm image and clear invitation are hypotheses, not evidence that an audience already liked them.',stretch='Explain how the reading distance could change the hierarchy.')
native_extra=''.join(f'<figure><img class="zoomable" src="img/{f}" alt="{c}" loading="lazy" tabindex="0"><figcaption>{c}</figcaption></figure>' for f,c in [('native-name.jpg','2.1 Genuine capture: document name. Height is still the inherited 2400 px; it must be changed.'),('native-width.jpg','2.2 Genuine capture: width 1080 px. This is one dimension only.'),('native-artboards.jpg','2.4 Genuine capture: Artboards checked. The incorrect height remains visible.'),('native-profile.jpg','2.5 Genuine capture: 72 PPI, RGB/8 and sRGB. These do not correct the pixel height.')])
st('Create one named artboard','New Photoshop document','No existing learner document','File → New → Artboards',[
 'Open File → New and name the document surname_AdPlanning_v01. Screenshot of the File menu is pending.',
 'Set Width 1080 Pixels. Set Height 1350 Pixels separately; confirm the displayed value. Correct-height action screenshot is pending.',
 'Check Artboards. Use RGB Color, 8 bit, White and sRGB; set Resolution 72 Pixels/Inch for this screen practice.',
 'Choose Create. Select the artboard and confirm W 1080 / H 1350 in Properties. The observed build mistakenly kept H 2400; do not copy that height.'
 ],'The artboard defines the intended output frame. Pixel dimensions, not a screen PPI label, determine this output size.','One artboard exists; Properties reports 1080 × 1350.','Select the artboard group rather than Layer 1. If height is 2400, correct its H property to 1350 before continuing; correction is not yet captured.',refs='Adobe-New · Adobe-Properties',extra=native_extra,pending=True,worked='Observed mistake: inherited H 2400 survived creation. The correct check is to read both W and H; document creation alone is not success.',stretch='Explain why changing only PPI would not repair the wrong height.')
st('Make room for two alternatives','surname_AdPlanning_v01','First artboard group in Layers','Artboard tool → + → Layers names',[
 'Select the Artboard tool nested under Move. Select the first artboard; use a side + to add an empty artboard, then add a third.',
 'Double-click each artboard name in Layers: 01_MOOD, 02_SKETCH_A, 03_SKETCH_B.',
 'Select each group and check Properties W 1080 / H 1350. Keep identical sketch sizes for a fair comparison.'
 ],'One file keeps the visual proposal and alternative layouts available together.','Three named groups appear; sketch sizes match.','A normal + adds an empty board; Option/Alt + duplicates contents. If you duplicated accidentally, keep the board and remove only unneeded duplicate content after checking the selected group.',refs='Adobe-Add · Adobe-Properties',pending=True,stretch='Add a fourth board only if a different delivery size needs testing.')
st('Bring in your browser mood board','surname_AdPlanning_v01 + surname_MoodBoard_v01','01_MOOD','Free Excalidraw lab → PNG → File → Place Embedded',[
 'After naming the communication problem in stage 1, complete the linked free browser mood-board lab before Photoshop setup. No installation or account is needed for the Excalidraw editor. Make and explain image, colour and type choices for the brief.',
 'Keep an editable .excalidraw master, a review PNG and the credited planning log. Confirm actual files exist and the master reopens in your school browser. Browser disk-save/file-picker/reopen verification is pending; do not rely on autosave.',
 'With 01_MOOD selected in Photoshop, use File → Place Embedded for the mood-board PNG. Keep its proportions while resizing, commit with Enter/Return and check that its layer is inside 01_MOOD. This native transfer is not yet run.',
 'Keep the separate .excalidraw master for mood-board edits. The PNG is a visual reference; your Photoshop sketch boards still need editable shape and text layers. Explain a reference feature, colour role and type role tied to this audience.'
 ],'A browser mood board proposes the direction without installing another app. The PNG carries that proposal into the layout file.','The board communicates image, colour, type and tone with reasons/credits. The editable browser master is retained; the placed reference belongs to 01_MOOD.','If only a PNG exists, save the editable browser scene too. If the PNG lands on the wrong Photoshop board, inspect Layers nesting before continuing.',fig=('img:web-board-result.jpg','Genuine Excalidraw canvas capture: constructed practice board with image, labelled palette, type roles and reasons.'),refs='Excalidraw · Adobe-Place · Adobe-Mood',extra='<p><a href="web-moodboard.html">Open the linear free browser mood-board lab and action screenshots</a> · <a href="assets/COM11_MoodBoard_Worked_Example.excalidraw" download>Editable worked example</a> · <a href="assets/COM11_MoodBoard_Worked_Example.png" download>Actual worked PNG</a>.</p><p><a href="assets/reference-study-log.txt">Read the credited real-campaign study log</a>.</p><figure><img class="zoomable" src="img/reference-study.png" alt="Three actual campaign examples with visible features to study" loading="lazy" tabindex="0"><figcaption>Actual campaign study: Cossette, Ogilvy and Pentagram. Copyright remains with owners.</figcaption></figure>',pending=True,worked='The browser model proposes calm space, cream background, dark main words and a small warm accent. These are practice choices, not a required independent solution.',stretch='Explain one reference you excluded because it conflicted with the intended audience or tone.')
g.session('B','Sketch, compare and revise','Lesson 2','70 minutes suggested: 5 recall/correction, 8 teacher model, 20 two sketches, 10 fair reader test, 12 revision, 10 save/export/reopen, 5 defence.','Produce two layout ideas, collect actual feedback and defend a revision.')
st('Sketch two genuinely different layouts','surname_AdPlanning_v01','02_SKETCH_A then 03_SKETCH_B','Rectangle tool (Shape) + Type tool; optional paper sketch import',[
 'In 02_SKETCH_A, make rough boxes for headline, focal image, supporting detail and next action. Use Rectangle in Shape mode and short Type labels; keep each element editable. Exact control/action screenshots are pending.',
 'In 03_SKETCH_B, make a second composition with a different focal point or reading order. Keep the audience, required copy, palette and size fixed.',
 'Write your predicted first → second → third read beside each sketch. Stop before effects, retouching or final polish. If drawing is difficult, draw two paper thumbnails, photograph them and Place Embedded on the two sketch boards.'
 ],'Two low-cost options allow a design decision before you invest in a polished layout.','A and B differ in hierarchy or composition, rather than only a colour change.','If both sketches are the same, change the position and relative size of the primary message. Keep the actual communication problem fixed.',fig=('img:compare-sketches.png','Authored layout models: A begins with the headline; B begins with the image. Neither is a guaranteed winner.'),pending=True,stretch='Try a third layout after both alternatives pass the basic information check.')
st('Test the reading order fairly','Both sketch boards and planning-log.txt','A and B at the same viewing size','View → compare → ask → record',[
 'Show each sketch at the same size, briefly, to a reader. Before explaining your intention ask: “What did you notice first? What is the message? What would you do next?”',
 'Record the reader’s actual words separately from your prediction. Check that all required information can be found.',
 'Choose a direction using one observed strength and one weakness. If you have no reader, mark the record “self-check”; seek an actual reader later.'
 ],'A test gives you evidence for a change. Praise alone does not locate a reading problem.','Prediction and observation are separate; your choice refers to a visible feature and actual response.','If the question led the reader toward your intended answer, repeat with neutral questions. Never invent a response.',worked='Model reasoning frame, not fabricated feedback: “If the reader notices the image but misses the action, I will strengthen the action’s placement or contrast.”',stretch='Retest at the actual intended display size.')
st('Keep the first idea and revise','surname_AdPlanning_v02','Chosen sketch duplicated as 04_REVISED','Artboard tool → Option/Alt +; Layers; Save As',[
 'Keep A and B. Duplicate the chosen board with Option/Alt + and name it 04_REVISED. Change one feature linked to the recorded problem.',
 'Retest with the same neutral questions. Record what changed and what remains uncertain.',
 'Changed brief: your teacher changes the audience or display setting. Make a brief plan with less help: identify one choice you would retain and one you would change, with reasons.'
 ],'Preserving the first idea makes your design process and learning inspectable.','Your before/after shows the targeted change; the revision is tied to evidence.','If you changed everything, you cannot identify what helped. Return to the saved version and test one purposeful change.',refs='Adobe-Use',pending=True,stretch='Explain a tradeoff introduced by the revision.')
st('Save, reopen and explain','surname_AdPlanning_v02.psd + exported boards','All planning boards','File → Save As; File → Export → Artboards To Files',[
 'Save a layered local PSD in your class project folder. Keep the planning log and permitted source assets with it. Native save/reopen proof is pending.',
 'Use File → Export → Artboards To Files for separate review images. Choose PNG and a local export folder; inspect the actual output. Exact export-dialog settings/screenshots are pending.',
 'Reopen the saved PSD: confirm named boards, editable text/shapes and image nesting. Open the exported sketches separately and check size, readable labels and absence of clipped required information.',
 'Explain the audience, one reference choice, the difference between A/B, the observed reader response and the resulting revision. Hand off through your teacher’s current Student OS task only when that task has been assigned.'
 ],'The editable source preserves decisions; exports let others review them without Photoshop.','Saved PSD reopens; expected boards and layers remain; exports match the intended dimensions.','A PNG is not a layered master. If saving only an image, return to the document and save PSD. A local note is not a confirmed evidence submission.',refs='Adobe-Use',pending=True,stretch='Defend the chosen direction under a new audience constraint without the guide.')
apply_recall(g,{'B':('What does a mood board communicate?','How is an artboard different from a layer?','Why do two sketch options need the same brief and size?')})
credits=HERE/'credits.json';credits.write_text('{}')
g.build(eyebrow='COM11 · GRAPHIC DESIGN · PLANNING LAB',h1a='Plan the message.',h1b='Then build the ad.',lead='Use the free Excalidraw browser editor for the mood board, and Photoshop artboards to compare two layouts. Explain, test and revise your decisions.',tags=['2 proposed 70-minute classes','Free browser mood board + Photoshop','Draft: native capture incomplete'],hero_img='mood-explained.png',hero_alt='Original mood board with image, colour, type and reasons explained',hero_caption='Original teaching model. This image does not show Photoshop controls.',hero_side='<h3>Three planning outputs</h3><ol><li>Credited mood board</li><li>Two layout sketches</li><li>Test record + revision</li></ol>',brief='<section class="panel" id="brief"><h2>Start with a real message</h2><p>Insert this module before the independent design in the <a href="../lab-route.html">main lab route</a>. It is a supplement, not a calendar change. Use a teacher-approved actual school/community brief.</p><p><strong>Browser-first route:</strong> stage 1 → <a href="web-moodboard.html">free browser mood-board lab</a> → Photoshop stages 2–3 → place the PNG in stage 4. No additional software installation is required.</p>'+PENDING+'<p><a href="assets/planning-log.txt" download>Download the planning log</a> · <a href="assets/planning-models.zip" download>Download original model images</a> · <a href="theory.html">Open the narrated planning presentation</a></p></section>',industry='<section class="panel"><h2>Why a designer does this</h2><p>Discuss direction early, compare alternatives and show a client the reason for a choice. A mood board proposes a look and tone. A thumbnail proposes the arrangement. A prototype lets you test the reading experience.</p></section>',lens='<section class="panel" id="lens"><h2>Knowledge first</h2><p><strong>Mood board:</strong> references for images, colour, type and tone, with reasons. <strong>Artboard:</strong> a named canvas within a Photoshop file. <strong>Thumbnail:</strong> a rough composition. One artboard can hold a mood board; other artboards can hold sketches.</p></section>',assesses='<section class="panel" id="assesses"><h2>What your teacher reviews</h2><p>How your design serves the audience, uses graphic principles, colour and type, compares options, and improves after evidence. Your teacher reviews the design, your explanation and how you respond to a changed brief. Completing the instructions is practice.</p></section>',practical_step=6,qa=['Approved facts and audience/action recorded.','References credited and permitted; palette/type roles annotated.','A and B have distinct reading orders at equal size.','Actual test result recorded honestly.','Initial options retained; revised choice explained.','Saved layered PSD reopens; exported boards checked.'],evidence=['Who is the reader, and what action should follow?','Which reference feature influenced a choice, and why?','How do A and B differ in reading order?','What did your reader actually report? What did you revise?','What did your PSD reopen/export check show?'],frames='“I predict __ because __.” “The reader said __, so I changed __.” “Under the new brief I would change __ because __.”',sources=SOURCES,credits_file=credits,used_photos=[],footer='Draft for teacher review. Native steps beyond the initial wrong-height artboard have not yet run; independent cold run pending. Practice notes stay in this browser until you save/copy them. No Form or evidence synchronization is claimed.',evidence_title='COM11 ad planning practice reflection',evidence_file='COM11_AdPlanning_Reflection.txt',css_labels=('COM11 / DESIGN PLANNING','PLAN AN AD'))
generated=HERE/'package/student/guide.html'
page=generated.read_text().replace('<h2>Keep it short and specific.</h2>',f'<h2>Keep it short and specific.</h2><p><a href="{COACH}" target="_blank" rel="noopener">Open the shared Coach</a> · <a href="{STUDENT_OS}" target="_blank" rel="noopener">Open Student OS</a>. Use only your assigned task. No Form has been connected to this planning practice.</p>').replace('class="step"','class="step"').replace('</style>','figure img{height:auto;width:100%}.target{overflow-wrap:anywhere} .step{break-before:page} @media print{header{padding:20px}.panel{break-before:auto;break-inside:auto;margin:8pt 0;padding:6pt 0}.part{break-before:page}.step{break-inside:auto}.refs{display:none}.wcf{break-inside:avoid}header h1{font-size:34pt}header figcaption{color:#52636b!important}header .hero{display:block}.hero img{max-height:260px}.step{break-before:page}.step figure img{max-height:245px}.step figure{break-inside:avoid}.step h3{font-size:20pt}.step p,.step li{font-size:11pt}.step .target{font-size:10pt}nav,.done{display:none}textarea{display:block;height:18mm;min-height:18mm} }</style>')
(OUT/'guide.html').write_text(page)
(OUT/'index.html').write_text((HERE/'package/student/index.html').read_text())
(OUT/'assets').mkdir(exist_ok=True)
log='''COM11 AD PLANNING LOG — PRACTICE / NOT A REGISTERED SUBMISSION\nAudience:\nActual message and approved facts:\nAction the reader should take:\nDisplay setting and size:\nTone words (3):\n\nREFERENCE RECORD — repeat for each reference\nFile / image description:\nCreator / source URL:\nPermission or licence:\nVisible feature I am studying:\nReason this may serve my audience:\n\nPALETTE / TYPE ROLES\nBackground:\nMain words:\nAccent:\nHeadline type:\nDetail type:\n\nOPTIONS AND TEST\nA predicted first → second → third:\nB predicted first → second → third:\nActual reader response to A (or label self-check):\nActual reader response to B:\nChoice and one weakness:\nOne revision / reason:\nRetest response:\nChanged-brief decision:\n\nSAVE AND REVIEW\nPSD name and reopened check:\nExport names, dimensions and inspection:\nHelp used (separate from achievement):\nNext target:\n'''
(OUT/'assets/planning-log.txt').write_text(log)
import zipfile
with zipfile.ZipFile(OUT/'assets/planning-models.zip','w',zipfile.ZIP_DEFLATED) as z:
 for n in ['mood-board-model.png','sketch-a-model.png','sketch-b-model.png']:z.write(IMG/n,n)
 z.writestr('READ_ME.txt','Original constructed practice illustrations. These PNGs are examples, not layered Photoshop files or UI screenshots. Use your own approved message and permitted assets.\n')

slides=[]
def sl(title,lead,img,definition,example,notes,task=None,quiz=None,source='Original teaching model',source_url=None):
 s=dict(section='PLANNING',title=title,body=f'<p class="big">{lead}</p><p>{definition}</p><p>{example}</p>',lead=lead,img='img/'+img,alt=title+' — labelled teaching visual',definition=definition,example=example,notes=notes,narration=notes,task=task,quiz=quiz,source=source,source_url=source_url or SOURCES['Adobe-Use'][1]);slides.append(s)
sl('Planning starts with the reader','Audience → message → action','planning-process.png','State who will see the ad and what they should do.','The independent ad uses an actual approved school/community message.','Before choosing pictures or fonts, identify a particular reader, viewing setting and next action. Those facts guide your design choices. Planning is visible reasoning, not a requirement to decorate a page. Our worked café material is constructed practice; your independent message must be real and approved. Write your audience and intended action in one sentence.',task='Write: My audience is __. After viewing, I want them to __.')
sl('A mood board proposes a direction','Images + colour + type + tone','mood-explained.png','Curate references and explain their purpose.','A board should help someone discuss the proposed direction.','A mood board gathers a few purposeful references. It may show image treatment, a palette, typography and the tone you intend. Each reference should carry a reason tied to the brief. A board is useful when another person can tell you what the direction communicates. It is a proposal to discuss and test, not proof of an audience effect.',source='Adobe mood boarding; original model',source_url=SOURCES['Adobe-Mood'][1])
sl('An artboard is a canvas inside the file','One Photoshop document, several layouts','compare-sketches.png','Keep a PNG mood reference, option A and option B together.','Artboards contain their own layers and clip content at their edges.','A Photoshop artboard is a named canvas inside one document. The mood board describes a visual direction; an artboard is the place you can put that board or a sketch. Build the mood board in the free Excalidraw browser editor, keep its editable master, then place a PNG reference on 01_MOOD. We will keep three named boards together. A layer holds an element inside a board. Selecting the board group matters when you change its size or add content.',source='Adobe artboards; original layout models')
sl('Explain the difference','Direction and arrangement answer different questions','mood-explained.png','Mood: what should it feel like? Sketch: where does information go?','You can create both on artboards.','Check the distinction individually. A palette, image references and type samples propose a direction. Boxes for headline, image, detail and action propose an arrangement. Photoshop artboards can hold either. Calling a mood board an artboard confuses the purpose of the content with the container. After answering, explain your choice in your own words.',quiz=q('Which statement is accurate?',['A mood board is a visual direction; an artboard is a canvas.','A mood board is the final published ad.','Every layer is a separate artboard.'],0,'Purpose and container are different: an artboard can hold a mood board or a layout sketch.'))
sl('Translate a reference into a choice','Visible feature → idea → reason','reference-study.png','Study one feature; design an original response.','Record creator/source and permission.','Notice the model’s single focal object and generous empty space. Those features propose a calm tone. You can study a real advertisement’s hierarchy without copying its brand, logo or entire layout. Credit references and use original or permitted assets in your own final work. Explain exactly what the reference helped you decide; avoid saying only that it looked good.',task='Name one reference feature and explain why it might serve your reader.')
sl('Give colour and type clear roles','Background · message · accent','mood-explained.png','Annotate roles instead of listing favourites.','Keep words readable; the palette label does not prove contrast.','The model uses a cream ground, dark main words and a smaller terracotta accent. The roles explain what each colour does. A type sample should distinguish headline from supporting detail. Tie this to our colour wheel and typography lessons. A harmonious palette can still hide words, so test readability separately at the intended viewing size.')
sl('Check both artboard dimensions','1080 × 1350 px for this digital practice','native-size-detail.jpg','Use File → New, with Artboards enabled.','Genuine capture shows an incorrect inherited H 2400. Correction is pending.','This is a genuine capture from our first setup attempt. Width became 1080, but the inherited height stayed 2400. The lesson is to read both pixel dimensions before and after creation. Resolution 72 PPI and RGB colour do not repair the wrong height. The corrective native demonstration is still pending; your teacher must verify the procedure before classroom use.',source='Genuine local Photoshop capture; Adobe properties',source_url=SOURCES['Adobe-Properties'][1])
sl('Diagnose the setup mistake','Read the values, then target the cause','native-height-diagnosis.jpg','The requested frame is 1080 × 1350.','Select the artboard; inspect W and H in Properties.','Diagnose the actual mistake. A tall artboard was created because the height field did not change. The proposed repair is to select the artboard group and set its H property to 1350. That repair has not yet been captured or tested here. Changing a type layer or altering only PPI would not address this cause. Explain why your chosen repair targets the mismatch.',quiz=q('The frame is 1080 × 2400 instead of 1080 × 1350. What should you inspect?',['The selected artboard’s H property','Only the text’s tracking','Only the PPI value'],0,'The mismatch is the artboard pixel height. Confirm the board is selected, set H to 1350 and recheck.'),source='Observed local mistake; Adobe properties',source_url=SOURCES['Adobe-Properties'][1])
sl('Sketch before polishing','Compare two different reading orders','compare-sketches.png','Use boxes and short labels for the important parts.','Keep the brief, copy, palette and size fixed.','A thumbnail is a low-cost layout hypothesis. Option A may lead with a headline, while B may lead with an image. Keep the same essential information and size so the comparison is meaningful. In Photoshop use editable shape and text layers, or import paper thumbnails. Do not begin with effects or detailed retouching. The question is whether the reader finds the message and action.',task='Make A and B differ in hierarchy. Predict first → second → third for each.')
sl('Ask a reader without coaching the answer','Notice → message → action','planning-process.png','Show A and B at the same size.','Record their actual words separately from your prediction.','Ask what the reader noticed first, what the message was, and what they would do next. Avoid telling them what you intended before they respond. Record what happened, even when it disagrees with your prediction. If you have no reader, label the record self-check. A fair comparison and honest observation provide a reason for a revision; invented praise does not.')
sl('Preserve the first idea and revise','One problem → one purposeful change','compare-sketches.png','Keep A and B; duplicate the chosen direction.','Retest the change, then explain a tradeoff.','Keep the two initial sketches. Duplicate the direction you choose and change one feature connected to an observed problem. Retest with neutral questions. Explain the benefit and anything the change makes harder. If your teacher changes the audience or viewing setting, decide what you would retain and what you would change. The purpose is independent judgement, not copying the worked model.',task='Which feature would you change after feedback, and why?')
sl('Show the reasoning and the files','Direction → alternatives → evidence → revision','planning-process.png','Keep an editable PSD and review exports.','Native save/reopen and the independent cold run remain pending.','The planning submission should show a credited mood board, two different sketches, actual test notes and the reason for a revision. Retain the layered source and inspect exported boards. Our native save and reopen procedure has not yet been completed, so this remains a review draft. Tutorial completion is practice; your teacher reviews achievement through the design, explanation and response to a changed brief.',quiz=q('Which evidence best supports a revision?',['A reader response linked to a visible change','A checklist saying every tutorial step was completed','A larger file size'],0,'Explain what the reader observed, what you changed and what the retest showed. Files and completion checks alone do not establish communication quality.'))
for i,t in {3:'Choose: A direction/canvas; B final ad; C every layer. Explain.',7:'Check: A artboard height; B text tracking; C PPI only. Explain.',11:'Evidence: A reader response + visible change; B completed steps; C file size. Explain.'}.items(): slides[i]['native_question']=t
slides[4]['source']='Actual campaigns: Cossette / Ogilvy / Pentagram'
slides[4]['source_url']='https://www.cossette.com/en/blog/__temp_axdccudsbhhoymknkaqplbxaujyfvicbzotm'
slides[4]['notes']=slides[4]['narration']='These are actual campaign images from the main teaching deck. Study the simplified directional mark in Follow the Arches, the image and action relationship in Recycle Me, and the expressive typography in the Public Theater example. A feature may inspire an original decision, or conflict with your intended tone. Credit the reference and explain the connection. Do not copy the brand or assume that a visible design proves audience effects. Your final ad needs original or permitted assets.'
# Browser-tool constraint: revise existing slide positions/checks without changing their quiz order.
slides[1].update(title='Build the mood board in your browser',lead='Free Excalidraw editor · no installation or account',img='img/web-board-result.jpg',definition='Arrange an image, colour roles, type samples and reasons.',example='Keep an editable .excalidraw master and a review PNG.',source='Genuine Excalidraw canvas; original illustration',source_url='https://excalidraw.com')
slides[1]['notes']=slides[1]['narration']='Use the free editor at excalidraw.com. Its MIT-licensed source is public. No installation or account was needed for this worked board. The image is an original practice illustration. The board combines a reference, labelled colour roles, type specimens and an audience-based reason. Open the linked browser lab for action screenshots. Save an editable scene and a PNG rather than relying on shared browser storage. School access and disk-save/reopen still need verification.'
slides[5].update(img='img/web-colour-roles.jpg',source='Genuine browser palette; worked-example values',source_url='https://excalidraw.com')
slides[5]['notes']=slides[5]['narration']='In Excalidraw, Rectangle creates a swatch and Background opens its fill colour. The actual worked values are cream f4ead5, dark ink 193443 and terracotta b85a36. The labels explain background, main words and accent roles. These are practice choices, not an independent solution. Add headline and detail specimens; the browser font does not guarantee the same font exists in Photoshop. Test final readability in the intended viewing setting.'
slides[11].update(definition='Keep .excalidraw + PNG, a layered Photoshop PSD and review exports.',example='Browser disk-save/reopen and the native Photoshop workflow remain pending.')
slides[11]['notes']=slides[11]['narration']='Keep the browser mood board as an editable .excalidraw scene and a review PNG. Bring the PNG into 01_MOOD as a reference, then make two editable Photoshop layout sketches. Explain actual reader feedback and a visible revision. Canvas text, image placement, palette values and Copy PNG were observed; browser file-picker/disk-save/reopen and the native Photoshop save/reopen path remain unverified. These procedures require school-browser and independent cold-run checks before release. Your teacher evaluates the communication decisions, not completion counts.'
build_deck(OUT,'theory.html','com11-ad-planning-theory-v1','Plan an ad: mood boards and Photoshop artboards','Communication Technology 11',slides,SOURCES,'guide.html','Open the planning guide')
(HERE/'deck.json').write_text(json.dumps({'title':'COM11 — Plan an ad','slides':slides,'status':'Draft; browser disk-save/reopen, native Photoshop capture and cold run incomplete'},indent=2)+'\n')
print('Original models, annotated genuine captures, 8-stage guide and 12-slide narrated deck built.')
