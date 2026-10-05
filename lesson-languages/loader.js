/* Learning Studio trilingual player. Translations are local lesson assets; no AI API. */
(async function(){
'use strict';
const key=document.documentElement.dataset.lesson;
if(!['brand','art'].includes(key))return;
const root=new URL('lesson-languages/',document.baseURI);
async function read(name,isJson=false){const r=await fetch(new URL(name,root),{cache:'no-cache'});if(!r.ok)throw new Error(name+': '+r.status);return isJson?r.json():r.text();}
function languagePatch(){
'use strict';
const pack=window.LESSON_LANG_DATA;delete window.LESSON_LANG_DATA;
const baseSlides=SLIDES,baseConfig=JSON.parse(JSON.stringify(CONFIG));
const clone=x=>JSON.parse(JSON.stringify(x));
let language='en';let wanted=new URL(location.href).searchParams.get('lang');
try{wanted=wanted||localStorage.getItem('learningStudioLessonLanguage');}catch(e){}
if(['en','fr','es'].includes(wanted))language=wanted;
const rows=[
['Skip to lesson','Aller à la leçon','Ir a la lección'],
['Jump to a chapter or checkpoint','Aller à un chapitre ou à une pause','Ir a un capítulo o una pausa'],
['Start guided playback','Démarrer la lecture guidée','Iniciar reproducción guiada'],
['Listen to this slide','Écouter cette diapositive','Escuchar esta diapositiva'],
['Stop listening','Arrêter l’écoute','Detener lectura'],
['Pause playback','Mettre en pause','Pausar reproducción'],
['← Previous','← Précédente','← Anterior'],['Next →','Suivante →','Siguiente →'],
['Text view','Vue texte','Vista de texto'],['Visual view','Vue visuelle','Vista visual'],
['Restart','Recommencer','Reiniciar'],['Voice','Voix','Voz'],['Speed','Vitesse','Velocidad'],
['Slower','Plus lent','Más lento'],['Normal','Normale','Normal'],['Faster','Plus rapide','Más rápido'],
['Use voice when available','Utiliser la voix disponible','Usar la voz disponible'],
['Read-aloud unavailable','Lecture à voix haute indisponible','Lectura en voz alta no disponible'],
['No matching voice available — timed captions','Aucune voix dans cette langue — sous-titres minutés','No hay voz en este idioma — subtítulos temporizados'],
['Voice, speed and playback settings','Paramètres de voix, de vitesse et de lecture','Ajustes de voz, velocidad y reproducción'],
['EXPLANATORY CAPTION','SOUS-TITRE EXPLICATIF','SUBTÍTULO EXPLICATIVO'],
['NARRATION • SENTENCE CAPTION','NARRATION • SOUS-TITRE PAR PHRASE','NARRACIÓN • SUBTÍTULO POR FRASE'],
['READING MODE • SENTENCE CAPTION','MODE LECTURE • SOUS-TITRE PAR PHRASE','MODO LECTURA • SUBTÍTULO POR FRASE'],
['PAUSE • TRY BEFORE CHECKING','PAUSE • ESSAIE AVANT DE VÉRIFIER','PAUSA • INTENTA ANTES DE COMPROBAR'],
['Your turn','À toi de jouer','Tu turno'],['Explanation','Explication','Explicación'],
['Full explanation / narration transcript','Explication complète / transcription de la narration','Explicación completa / transcripción de la narración'],
['Save the full lesson transcript','Enregistrer la transcription complète','Guardar la transcripción completa'],
['Visual labels and image descriptions','Étiquettes visuelles et descriptions des images','Etiquetas visuales y descripciones de imágenes'],
['About the examples, sources and privacy','Exemples, sources et confidentialité','Ejemplos, fuentes y privacidad'],
['Sources / example credits:','Sources et crédits des exemples :','Fuentes y créditos de los ejemplos:'],
['Show explanation after trying','Afficher l’explication après avoir essayé','Mostrar la explicación después de intentarlo'],
['Open optional Reel extension','Ouvrir le prolongement facultatif sur les Reels','Abrir la ampliación opcional sobre Reels'],
['Practice only. This player does not save, submit or grade your answers.','Entraînement seulement. Ce lecteur n’enregistre, ne transmet ni ne note tes réponses.','Solo práctica. Este reproductor no guarda, envía ni califica tus respuestas.'],
['Playback stopped. Read the slide or restart its explanation.','Lecture arrêtée. Lis la diapositive ou relance son explication.','Reproducción detenida. Lee la diapositiva o reinicia su explicación.'],
['Playback paused. Restart to hear this slide again.','Lecture en pause. Relance-la pour réécouter cette diapositive.','Reproducción en pausa. Reiníciala para escuchar esta diapositiva otra vez.'],
['Pause screen. Try the task; guided playback will stop here.','Écran de pause. Essaie la tâche; la lecture guidée s’arrête ici.','Pantalla de pausa. Intenta la tarea; la reproducción guiada se detiene aquí.'],
['Read this slide, open the full explanation, or use Listen.','Lis cette diapositive, ouvre l’explication complète ou clique sur Écouter.','Lee esta diapositiva, abre la explicación completa o pulsa Escuchar.'],
['Review the examples, then continue when you are ready.','Revois les exemples, puis continue quand tu es prêt ou prête.','Revisa los ejemplos y continúa cuando estés listo.'],
['Reading this slide. Captions follow each sentence.','Lecture de cette diapositive. Les sous-titres suivent chaque phrase.','Leyendo esta diapositiva. Los subtítulos siguen cada frase.'],
['Timed reading mode: voice unavailable or turned off. Captions follow the explanation.','Lecture minutée : voix indisponible ou désactivée. Les sous-titres suivent l’explication.','Lectura temporizada: voz no disponible o desactivada. Los subtítulos siguen la explicación.'],
['The selected voice could not play. Continuing with timed sentence captions.','La voix sélectionnée n’a pas pu démarrer. La lecture continue avec des sous-titres minutés.','La voz seleccionada no pudo reproducirse. Se continúa con subtítulos temporizados.'],
['Voice playback did not finish. Continuing with timed captions.','La lecture vocale ne s’est pas terminée. La lecture continue avec des sous-titres minutés.','La lectura en voz alta no terminó. Se continúa con subtítulos temporizados.'],
['Paused for you. Complete the task or review the examples, then use Next when ready.','Pause. Termine la tâche ou revois les exemples, puis clique sur Suivante.','En pausa. Completa la tarea o revisa los ejemplos y pulsa Siguiente.'],
['Explanation complete. Replay, reread or continue.','Explication terminée. Réécoute, relis ou continue.','Explicación terminada. Vuelve a escuchar, relee o continúa.'],
['Paused while this lesson was in another tab.','Lecture en pause pendant que cet onglet était masqué.','En pausa mientras esta pestaña estaba oculta.'],
['This source image could not load. It needs internet access and may be blocked on this network. Use the source links or the visual description in Text view; do not invent visual evidence.','Cette image n’a pas pu se charger. Elle nécessite Internet et peut être bloquée sur ce réseau. Consulte les sources ou la description en vue texte; n’invente pas de preuves visuelles.','Esta imagen no se pudo cargar. Necesita Internet y puede estar bloqueada en esta red. Consulta las fuentes o la descripción en vista de texto; no inventes evidencia visual.'],
['Guided playback stops at task screens. With voice off or unavailable, sentence captions advance on a reading timer. This is a browser lesson, not a recorded video. Keyboard: arrow keys for slides; space to start or stop playback.','La lecture guidée s’arrête aux tâches. Sans voix, les sous-titres avancent selon une minuterie de lecture. C’est une leçon dans le navigateur, pas une vidéo enregistrée. Clavier : flèches pour les diapositives; espace pour démarrer ou arrêter.','La reproducción guiada se detiene en las tareas. Sin voz, los subtítulos avanzan con un temporizador de lectura. Es una lección en el navegador, no un video grabado. Teclado: flechas para las diapositivas; espacio para iniciar o detener.']
];
const lookup=new Map();rows.forEach(row=>row.forEach(s=>lookup.set(s,row)));
const col=()=>({en:0,fr:1,es:2})[language];
const tr=s=>lookup.get(s)?.[col()]||s;
const common={fr:{'LEARNING STUDIO / BRAND DETECTIVE':'LEARNING STUDIO / DÉTECTIVE DE MARQUES','TAKEAWAY':'À RETENIR','REAL LEGO ARTWORK':'VÉRITABLE VISUEL LEGO','Needs an internet connection.':'Connexion Internet nécessaire.','Use the source link if blocked.':'Si l’image est bloquée, ouvre la source.','Source':'Source','image':'image'},es:{'LEARNING STUDIO / BRAND DETECTIVE':'LEARNING STUDIO / DETECTIVE DE MARCAS','TAKEAWAY':'IDEA CLAVE','REAL LEGO ARTWORK':'GRÁFICO REAL DE LEGO','Needs an internet connection.':'Necesita conexión a Internet.','Use the source link if blocked.':'Si está bloqueada, abre la fuente.','Source':'Fuente','image':'imagen'}};
const sectionLabels={'UNDERSTAND':['COMPRENDRE','COMPRENDER'],'SEE THE DESIGN':['OBSERVER LE DESIGN','OBSERVAR EL DISEÑO'],'BUILD EVIDENCE':['RÉUNIR DES PREUVES','REUNIR PRUEBAS'],'OPTIONAL REEL EXTENSION':['PROLONGEMENT REEL FACULTATIF','AMPLIACIÓN REEL OPCIONAL'],'OPTIONAL REEL':['REEL FACULTATIF','REEL OPCIONAL'],'REFLECT':['RÉFLÉCHIR','REFLEXIONAR'],'ELEMENTS':['ÉLÉMENTS','ELEMENTOS'],'PRINCIPLES':['PRINCIPES','PRINCIPIOS'],'GRAPHIC DESIGN':['GRAPHISME','DISEÑO GRÁFICO'],'APPLY & EXPLAIN':['APPLIQUER ET EXPLIQUER','APLICAR Y EXPLICAR'],'REVIEW':['RÉVISION','REPASO']};
const skipCommon=['','LEARNING STUDIO','LEARNING STUDIO / BRAND DETECTIVE','TAKEAWAY','REAL LEGO ARTWORK','Needs an internet connection.','Use the source link if blocked.','Source','image'];
function convert(d,s,lang){
 if(s.i!==d.number-1)throw new Error('Translation order mismatch');
 const v=clone(d);let section=d.section;
 Object.keys(sectionLabels).sort((a,b)=>b.length-a.length).forEach(k=>section=section.split(k).join(sectionLabels[k][lang==='fr'?0:1]));
 const pairs=new Map([[d.title,s.T],[d.subtitle,s.S],[d.caption,s.C],[d.section,section],...Object.entries(common[lang])]);
 const skip=new Set([...skipCommon,d.title,d.subtitle,d.caption,d.section]);
 const doc=new DOMParser().parseFromString(d.svg,'image/svg+xml');if(doc.querySelector('parsererror'))throw new Error('Diagram parse error');
 let n=0;const textNodes=[...doc.querySelectorAll('text')];
 textNodes.forEach(el=>{const old=el.textContent;let text=old;if(pairs.has(old))text=pairs.get(old);else if(!skip.has(old)&&!/^(?:[\d\s/.:–—%\-]+|[A-D])$/.test(old)&&!/^Sources?:/.test(old)){text=s.X[n++];if(typeof text!=='string')throw new Error('Incomplete diagram translation');}else if(/^Sources?:/.test(old))text=old.replace(/^Sources?:/,lang==='fr'?'Sources :':'Fuentes:');if(text!==old){el.setAttribute('data-original-text',old);el.textContent=text;}});
 if(n!==s.X.length)throw new Error('Translation label count mismatch');
 const svg=doc.documentElement;svg.setAttribute('aria-label',s.T);const title=svg.querySelector('title');if(title)title.textContent=s.T;const desc=svg.querySelector('desc');if(desc)desc.textContent=s.S+' '+s.N;
 Object.assign(v,{title:s.T,subtitle:s.S,caption:s.C,notes:s.N,section,svg:new XMLSerializer().serializeToString(svg),screenText:textNodes.map(e=>e.textContent).join('\n'),action:s.A||'',quiz:s.Q?clone(s.Q):null});
 if(v.quiz)v.quiz.answer=d.quiz.answer;
 v.links.forEach((link,i)=>{link.text=s.L[i];});return v;
}
if(pack.fr.length!==baseSlides.length||pack.es.length!==baseSlides.length)throw new Error('Incomplete language pack');
const translated={en:baseSlides,fr:baseSlides.map((d,i)=>convert(d,pack.fr[i],'fr')),es:baseSlides.map((d,i)=>convert(d,pack.es[i],'es'))};
const langLabel=document.createElement('label');langLabel.className='lesson-language';langLabel.htmlFor='lessonLanguage';langLabel.innerHTML='Language / Langue / Idioma<select id="lessonLanguage"><option value="en" lang="en">English</option><option value="fr" lang="fr">Français</option><option value="es" lang="es">Español</option></select>';document.querySelector('header').append(langLabel);
const help=document.createElement('p');help.id='lessonLanguageHelp';help.className='language-help';document.querySelector('main').prepend(help);
const style=document.createElement('style');style.textContent='header{flex-wrap:wrap}header>label{min-width:220px;flex:1}header .lesson-language{flex:0 0 240px}.language-help{background:#e5f1ec;border-left:4px solid #1d7773;padding:12px 16px;border-radius:6px;font-size:15px}.lesson-language select{width:100%}@media(max-width:780px){header .lesson-language{margin-top:12px}main{margin-bottom:250px}}';document.head.append(style);
const helpers={en:'Choose a language, then click Listen. If no matching voice is available on this device, translated captions still work.',fr:'Choisis une langue, puis clique sur Écouter. Si aucune voix correspondante n’est disponible sur cet appareil, les sous-titres traduits restent accessibles.',es:'Elige un idioma y pulsa Escuchar. Si el dispositivo no tiene una voz compatible, puedes seguir los subtítulos traducidos.'};
const privacy={en:'Only the last slide number and chosen language are saved in this browser when local storage is available. Answers are not stored, submitted or graded. Original images and source links connect to their host websites. Browser read-aloud uses available voice services; processing depends on the browser and voice provider. Do not enter names or personal information.',fr:'Seuls le numéro de la dernière diapositive et la langue choisie sont conservés dans ce navigateur lorsque le stockage local est disponible. Les réponses ne sont ni enregistrées, ni transmises, ni notées. Les images et les liens se connectent à leurs sites sources. La lecture vocale utilise les services disponibles; le traitement dépend du navigateur et du fournisseur de voix. Ne saisis aucun nom ni renseignement personnel.',es:'Solo se guardan el número de la última diapositiva y el idioma elegido en este navegador cuando el almacenamiento local está disponible. Las respuestas no se guardan, envían ni califican. Las imágenes y enlaces se conectan a sus sitios de origen. La lectura utiliza servicios de voz disponibles; el procesamiento depende del navegador y del proveedor de voz. No introduzcas nombres ni información personal.'};
const about={fr:pack.kind==='brand'?'Le logo et les visuels sont de véritables documents LEGO, attribués au groupe LEGO, à Our LEGO Agency et à Interbrand; BrickNerd reproduit les visuels d’identité et Wikimedia Commons diffuse le logo. Les intentions décrites proviennent de LEGO et d’Interbrand. Les schémas et les consignes sont des ajouts pédagogiques originaux, pas des campagnes ou spécifications officielles. Cette leçon est indépendante, sans commandite ni approbation de LEGO. Le cahier fourni comporte des questions vidéo et des consignes d’étape 5 manquantes; les exercices supplémentaires sont identifiés comme tels.':'La terminologie s’appuie sur des références de musées et de design. Les schémas, comparaisons et tâches sont des exemples pédagogiques originaux. Les affiches ne sont pas de vraies annonces scolaires. Les regroupements de vocabulaire varient selon les cours : cette introduction n’est pas une grille officielle de l’IB et ne remplace pas la carte des résultats d’apprentissage de ton enseignant. Le visuel LEGO facultatif est un document réel cité séparément, pas une campagne inventée.',es:pack.kind==='brand'?'El logo y los diseños son documentos reales de LEGO, atribuidos al Grupo LEGO, a Our LEGO Agency e Interbrand; BrickNerd reproduce los diseños de identidad y Wikimedia Commons aloja el logo. Las intenciones descritas proceden de LEGO e Interbrand. Los diagramas y consignas son aportes didácticos originales, no campañas ni especificaciones oficiales. Esta lección es independiente, sin patrocinio ni aprobación de LEGO. En el cuaderno faltan preguntas de video e instrucciones del paso 5; la práctica adicional se identifica como tal.':'La terminología se apoya en referencias de museos y diseño. Los diagramas, comparaciones y tareas son ejemplos didácticos originales. Los carteles no son anuncios escolares reales. Las agrupaciones de vocabulario varían entre cursos: esta introducción no es una rúbrica oficial del IB ni sustituye el mapa de resultados de tu docente. El diseño opcional de LEGO es un documento real acreditado por separado, no una campaña inventada.'};
let observer;let pending=false;
function ui(){
 if(observer)observer.disconnect();
 const walker=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);let node;
 while(node=walker.nextNode()){
  const parent=node.parentElement;if(!parent||parent.closest('script,style,svg,#lessonLanguage,#voice'))continue;
  const val=node.nodeValue,trim=val.trim();let next=tr(trim);
  for(const p of [['Yes — that fits the evidence. ','Oui — cela correspond aux preuves. ','Sí — eso coincide con la evidencia. '],['Not quite — compare the distinction. ','Pas tout à fait — compare la distinction. ','No exactamente — compara la diferencia. ']])for(const old of p)if(next.startsWith(old)){next=p[col()]+next.slice(old.length);break;}
  if(next!==trim)node.nodeValue=val.slice(0,val.indexOf(trim))+next+val.slice(val.indexOf(trim)+trim.length);
 }
 help.textContent=helpers[language];document.querySelector('header strong').textContent=CONFIG.title;
 document.getElementById('lessonLanguage').value=language;
 const ps=document.querySelectorAll('.source-disclosure > p');
 if(ps[0])ps[0].textContent=language==='en'?baseConfig.disclosure:about[language];
 if(ps[1])ps[1].textContent=privacy[language];
 if(ps[2])ps[2].textContent=({en:'Independent educational resource • Learning Studio • Trilingual edition • 5 October 2026.',fr:'Ressource pédagogique indépendante • Learning Studio • Édition trilingue • 5 octobre 2026.',es:'Recurso educativo independiente • Learning Studio • Edición trilingüe • 5 de octubre de 2026.'})[language];
 document.getElementById('prev').setAttribute('aria-label',tr('← Previous'));document.getElementById('next').setAttribute('aria-label',tr('Next →'));
 if(observer)observer.observe(document.body,{subtree:true,childList:true,characterData:true});
}
function fit(){
 document.querySelectorAll('#stage text[data-original-text]').forEach(el=>{el.removeAttribute('textLength');el.removeAttribute('lengthAdjust');const value=el.textContent;el.textContent=el.getAttribute('data-original-text');const old=el.getComputedTextLength();el.textContent=value;const width=el.getComputedTextLength(),x=Number(el.getAttribute('x')||0),y=Number(el.getAttribute('y')||0),anchor=el.getAttribute('text-anchor');let cap=(y<240||y>760)?1472:old*1.12;if(anchor!=='middle'&&anchor!=='end')cap=Math.min(cap,1536-x);const rects=[...document.querySelectorAll('#stage rect')].filter(r=>{const b=r.getBBox();return b.width>180&&b.width<1480&&b.height>80&&x>b.x+10&&x<b.x+b.width-10&&y>b.y&&y<b.y+b.height;});if(rects.length){rects.sort((a,b)=>a.getBBox().width-b.getBBox().width);const b=rects[0].getBBox();cap=anchor==='middle'?2*Math.min(x-b.x,b.x+b.width-x)-32:anchor==='end'?x-b.x-20:b.x+b.width-x-20;}cap=Math.max(old,cap);if(width>cap&&cap>10){el.setAttribute('textLength',cap.toFixed(2));el.setAttribute('lengthAdjust','spacingAndGlyphs');}});
}
const originalRender=render,originalStop=stop;
render=function(){originalRender();ui();requestAnimationFrame(fit);};
stop=function(message){originalStop(message);ui();};
splitSentences=function(text){if(typeof Intl.Segmenter==='function')return [...new Intl.Segmenter(language,{granularity:'sentence'}).segment(text)].map(x=>x.segment.trim()).filter(Boolean);return text.match(/[^.!?]+[.!?]+|[^.!?]+$/g)||[text];};
populateVoices=function(){
 const previous=document.getElementById('voice').selectedOptions[0]?.dataset.uri;
 try{voices=synth?synth.getVoices().filter(v=>String(v.lang).toLowerCase().replace('_','-').split('-')[0]===language):[];}catch(e){voices=[];}
 const select=document.getElementById('voice');select.innerHTML='';select.disabled=!voices.length;
 if(!voices.length){const o=document.createElement('option');o.value='';o.textContent=tr(synth?'No matching voice available — timed captions':'Read-aloud unavailable');select.append(o);return;}
 voices.forEach((v,i)=>{const o=document.createElement('option');o.value=String(i);o.dataset.uri=v.voiceURI;o.textContent=v.name+' ('+v.lang+')';select.append(o);});
 let picked=voices.findIndex(v=>v.voiceURI===previous);if(picked<0)for(const locale of ({en:['en-ca','en-us','en-gb'],fr:['fr-ca','fr-fr'],es:['es-mx','es-us','es-es']})[language]){picked=voices.findIndex(v=>v.lang.toLowerCase().replace('_','-')===locale);if(picked>=0)break;}select.value=String(picked<0?0:picked);
};
function selectLanguage(lang){
 originalStop('');language=lang;SLIDES=translated[language];CONFIG=clone(baseConfig);
 if(language!=='en'){
  CONFIG.title=SLIDES[0].title;CONFIG.chapters=CONFIG.chapters.map(c=>({...c,title:SLIDES[c.start].title}));
  document.querySelector('.notice p').textContent=language==='fr'?'Lis ou écoute, fais une pause aux tâches et utilise tes propres preuves dans le format convenu avec ton enseignant.':'Lee o escucha, detente en las tareas y utiliza tus propias pruebas en el formato acordado con tu docente.';
  document.querySelector('.online-note').textContent=language==='fr'?'Les explications et les schémas sont traduits. Les logos, les visuels originaux et les vidéos sources restent dans leur langue d’origine. Les images externes nécessitent Internet. Sur un petit écran, utilise la vue texte.':'Las explicaciones y los diagramas están traducidos. Los logos, diseños originales y videos fuente conservan su idioma original. Las imágenes externas necesitan Internet. En pantallas pequeñas, usa la vista de texto.';
 }else{document.querySelector('.notice p').innerHTML=baseConfig.intro;document.querySelector('.online-note').textContent=baseConfig.online;}
 document.querySelectorAll('#chapter option').forEach((o,i)=>o.textContent=CONFIG.chapters[i].title);
 document.documentElement.lang=({en:'en-CA',fr:'fr-CA',es:'es'})[language];
 try{localStorage.setItem('learningStudioLessonLanguage',language);}catch(e){}
 try{const u=new URL(location.href);u.searchParams.set('lang',language);history.replaceState(null,'',u);}catch(e){}
 populateVoices();render();
}
observer=new MutationObserver(()=>{if(pending)return;pending=true;queueMicrotask(()=>{pending=false;ui();});});
if(synth){synth.addEventListener('voiceschanged',populateVoices);setTimeout(populateVoices,500);}
document.getElementById('lessonLanguage').onchange=e=>selectLanguage(e.target.value);
window.addEventListener('resize',()=>requestAnimationFrame(fit));
const oldDownload=document.getElementById('transcriptDownload').onclick;
document.getElementById('transcriptDownload').onclick=()=>{const out=SLIDES.map((s,i)=>(i+1)+'. '+s.title+'\n\n'+s.notes+(s.pause?'\n\n'+s.action:'')).join('\n\n');const url=URL.createObjectURL(new Blob([CONFIG.title+'\n\n'+out],{type:'text/plain;charset=utf-8'}));const a=document.createElement('a');a.href=url;a.download=baseConfig.filename.replace('.html','_'+language+'_Transcript.txt');a.click();setTimeout(()=>URL.revokeObjectURL(url),3000);};
selectLanguage(language);
window.lessonLanguage=()=>language;
}
try{
 const [base,f1,f2,s1,s2]=await Promise.all([read(key+'-base.html'),read(key+'-fr-1.json',true),read(key+'-fr-2.json',true),read(key+'-es-1.json',true),read(key+'-es-2.json',true)]);
 const packs=JSON.stringify({kind:key,fr:[...f1,...f2],es:[...s1,...s2]}).replace(/<\//g,'<\\/');
 let source=base.replace('const CONFIG=','let CONFIG=').replace('const SLIDES=','let SLIDES=');
 source=source.replace("if(synth){populateVoices();synth.addEventListener('voiceschanged',populateVoices);setTimeout(populateVoices,500);}else populateVoices();",'/* Voices initialized by the language controller. */');
 source=source.replace('<script>','<script>window.LESSON_LANG_DATA='+packs+';\n');
 source=source.replace('</body>','<script>('+languagePatch.toString()+')();<\/script></body>');
 document.open();document.write(source);document.close();
}catch(error){console.error(error);const status=document.getElementById('loadStatus');if(status)status.textContent='The lesson could not load. Reload this page. / La leçon n’a pas pu se charger. Actualise cette page. / No se pudo cargar la lección. Recarga esta página.';}
})();
