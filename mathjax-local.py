#!/usr/bin/env python
from pathlib import Path
import re, os, shutil

pattern = re.compile('<script.*src\s*=\s*".*MathJax\.js\?(?P<config>config=.*)".*?>', flags=re.I)

def is_legacy(text):
    m = re.search(pattern, text)
    return m

def replace_legacy(text, m):
    config = m.groupdict()['config']
    return re.sub(pattern, f'<script src="/~internet/mathjax/legacy/MathJax.js?{config}">', text)

def replace_mj(pfad):
    suff = pfad.suffix
    ziel = pfad.with_suffix(f'{suff}.ori')
    if not ziel.exists():
        shutil.copy(pfad, ziel)
    t1 = pfad.read_text()
    m = is_legacy(t1)
    if m:
        t2 = replace_legacy(t1, m)
    else:
        t2 = re.sub('<script.*src=".*mathjax.*">', 
            '<script src="/~internet/mathjax/tex-chtml.js">', t1, flags=re.I)
            # ungeprüft, weil ich kein V3-Beispiel habe
    pfad.write_text(t2)     

p = Path('.')
for root, dirs, files in os.walk(p):
    pr = Path(root)
    for f in files:
        pf = pr / f
        if pf.owner() == 'braun' and pf.suffix.lower() == '.html':
            print(pf)
            replace_mj(pf)






