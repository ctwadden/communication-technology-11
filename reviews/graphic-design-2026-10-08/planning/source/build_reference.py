from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
ROOT=Path(__file__).resolve().parents[2]
def build_reference():
 im=Image.new('RGB',(1500,650),'#fbfaf6');d=ImageDraw.Draw(im)
 f=lambda n,b=False:ImageFont.truetype(str(ROOT/'student/labs/fonts'/('DejaVuSans-Bold.ttf' if b else 'DejaVuSans.ttf')),n)
 d.text((45,26),'STUDY A FEATURE / MAKE YOUR OWN CHOICE',font=f(34,True),fill='#193443')
 refs=[('follow-the-arches.jpg','Follow the Arches / Cossette','Simplify the focal image.\nKeep the message easy to find.'),('recycle-me.jpg','Recycle Me / Ogilvy','Study the relationship between\nimage and action text.'),('simpatico.jpg','Public Theater / Pentagram','Energetic type may conflict\nwith our proposed calm tone.')]
 for i,(file,label,note) in enumerate(refs):
  x=45+i*490;d.rounded_rectangle((x,107,x+450,465),12,fill='#e4eeea')
  p=Image.open(ROOT/'student/assets/real-campaigns'/file).convert('RGB');p.thumbnail((410,240));im.paste(p,(x+(450-p.width)//2,124+(240-p.height)//2))
  d.text((x+20,389),label,font=f(21,True),fill='#193443');d.multiline_text((x+20,492),note,font=f(24),fill='#056068',spacing=9)
 d.text((45,605),'Actual campaign images · credited teaching/criticism · rights remain with owners · not measured audience results',font=f(18),fill='#193443')
 im.save(ROOT/'student/planning/img/reference-study.png',optimize=True)
if __name__=='__main__':build_reference()
