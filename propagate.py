import re
ENGINE = '/* ============================================================\n   ENGINE'
newbio = open('unit-biochem.html').read()   # the just-edited template
bio = {'title':'Pulse — Unit 1 Biochemistry', 'sub':'Unit 1 · Biochemistry',
       'comment':'PULSE — Unit 1 (Biochemistry & Cell Biology)',
       'donebig':'Biochemistry, handled.',
       'donesub':'You worked through the energy and cell concepts ...',
       'startlbl':'Start Unit 1 &rarr;'}
def grab(pat,t):
    m=re.search(pat,t,re.S); return m.group(1) if m else None
targets={'unit-genetics.html':'unit-genetics','unit-anatomy.html':'unit-anatomy',
         'unit-biodiversity.html':'unit-biodiversity'}
for f,canon in targets.items():
    old=open(f).read()
    tmod=old[old.index('const MODULE = {'):old.index(ENGINE)]
    tl={'title':grab(r'<title>(.*?)</title>',old),
        'sub':grab(r'Pulse<span class="sub">(.*?)</span>',old),
        'comment':grab(r'(PULSE — Unit \d+ \([^)]*\))',old),
        'donebig':grab(r'<div class="big">(.*?)</div>',old),
        'donesub':grab(r'<p class="sub">(.*?)</p>',old),
        'startlbl':grab(r'(Start Unit \d+ &rarr;)',old)}
    s=newbio[:newbio.index('const MODULE = {')]+tmod+newbio[newbio.index(ENGINE):]
    for k in bio:
        if tl[k]: s=s.replace(bio[k], tl[k])
    s=s.replace("const THIS_UNIT = 'unit-biochem';", f"const THIS_UNIT = '{canon}';")
    open(f,'w').write(s)