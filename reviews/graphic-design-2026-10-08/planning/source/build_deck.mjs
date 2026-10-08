import fs from 'node:fs/promises';
import path from 'node:path';
import {pathToFileURL,fileURLToPath} from 'node:url';
import {Presentation,PresentationFile,FileBlob} from '@oai/artifact-tool';
const HERE=path.dirname(fileURLToPath(import.meta.url)),root=path.resolve(HERE,'../..');
const SKILL='/Users/cdawg/.codex/plugins/cache/openai-primary-runtime/presentations/26.904.11930/skills/presentations';
process.env.RUNTIME_NODE_MODULES='/Users/cdawg/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules';
process.env.RUNTIME_NODE='/Users/cdawg/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node';
process.env.RUNTIME_PYTHON='/Users/cdawg/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3';
const {resolvePresentationFont,finalizePresentation}=await import(pathToFileURL(path.join(SKILL,'container_tools/artifact_tool_utils.mjs')));
const font=resolvePresentationFont();
const d=JSON.parse(await fs.readFile(path.join(HERE,'deck.json'),'utf8'));
const p=Presentation.create({slideSize:{width:1280,height:720}});
function txt(slide,text,x,y,w,h,size=25,bold=false,color='#193443'){
 const sh=slide.shapes.add({geometry:'textbox',position:{left:x,top:y,width:w,height:h},fill:'none',line:{fill:'none',width:0}});
 sh.text=text;sh.text.style={typeface:font,fontSize:size,bold,color,autoFit:'none'};return sh;
}
for(let i=0;i<d.slides.length;i++){
 const s=d.slides[i],slide=p.slides.add();slide.background.fill='#FBFAF6';
 txt(slide,s.title,48,32,1184,98,44,true);
 txt(slide,s.lead,48,135,1184,76,28,false,'#056068');
 const bytes=await fs.readFile(path.join(root,'student/planning',s.img));
 slide.images.add({blob:new Uint8Array(bytes),contentType:'image/png',alt:s.alt,fit:'contain',position:{left:48,top:221,width:752,height:340}});
 txt(slide,s.definition,830,220,402,164,24,true);
 txt(slide,s.example,830,390,402,168,23);
 const q=s.native_question||s.quiz?.q||s.task;
 if(q)txt(slide,'Individual check: '+q,48,570,1184,96,24,true,'#704518');
 else txt(slide,'Explain: visible feature → concept → purpose',48,584,1184,54,24,false,'#056068');
 txt(slide,'COM11 · PLAN · '+String(i+1).padStart(2,'0')+' / '+d.slides.length+' · '+s.source,48,679,1184,26,16,false);
 slide.speakerNotes.textFrame.setText(s.narration+'\n\nStudent task: '+(q||'Point to the visible feature and explain its purpose.')+'\nSource: '+s.source_url+'\nReal campaign images: copyright remains with the credited owners. Concept diagrams are labelled teaching models; practice poster is constructed. Independent assessed answers and teacher brief are separate private files.');
}
const candidate=path.join(HERE,'candidate-v5.pptx');await(await PresentationFile.exportPptx(p)).save(candidate);
const final=path.join(root,'student/downloads/COM11_GraphicDesign_Planning_2026-10-08_v5_DRAFT.pptx');
await finalizePresentation({workspaceDir:root,candidatePath:candidate,finalPath:final,pythonExecutable:process.env.RUNTIME_PYTHON,integrityValidatorPath:path.join(SKILL,'container_tools/inspect_presentation_package_integrity.py'),layoutValidatorPath:path.join(SKILL,'container_tools/inspect_presentation_layout_geometry.py'),layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-heading-fit'],requiredNativeTableOwnerSlides:[],requiredNativeChartOwnerSlides:[],fontPolicy:{basis:'design',families:[font]},verifyArtifactToolImport:true,receiptPath:path.join(HERE,'pptx-validation-v5.json')});
const finalDeck=await PresentationFile.importPptx(await FileBlob.load(final));
const rendered=path.join(HERE,'final-slides-v5');await fs.mkdir(rendered,{recursive:true});
for(let i=0;i<d.slides.length;i++){
 const blob=await finalDeck.export({slide:finalDeck.slides.getItem(i),format:'png',scale:1});
 await fs.writeFile(path.join(rendered,`slide-${String(i+1).padStart(2,'0')}.png`),new Uint8Array(await blob.arrayBuffer()));
}
console.log(`Finalized and rendered ${d.slides.length} slides. Font: ${font}`);
