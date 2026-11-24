# -*- coding: utf-8 -*-
"""Copia o texto (original, vigente, multivigente) e o indice do CGSN baixados em pasta temporaria para cgsn/."""
import os, shutil, sys
tmp, raiz = sys.argv[1], os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
n = 0
for sub in ('original', 'vigente', 'multivigente'):
    src = os.path.join(tmp, sub)
    if not os.path.isdir(src):
        continue
    dst = os.path.join(raiz, 'cgsn', sub)
    os.makedirs(dst, exist_ok=True)
    for f in os.listdir(src):
        if f.endswith('.txt'):
            shutil.copy(os.path.join(src, f), os.path.join(dst, f)); n += 1
for f in ('INDICE.csv', 'indice.json'):
    if os.path.exists(os.path.join(tmp, f)):
        shutil.copy(os.path.join(tmp, f), os.path.join(raiz, 'cgsn', f))
print('arquivos de texto do CGSN copiados:', n)
