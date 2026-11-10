#!/usr/bin/env python3
"""Inline styles.css and the team photos into _src.html -> self-contained index.html."""
import os, re, base64
src = open('_src.html').read()
css = open('styles.css').read()
out = src.replace('<link rel="stylesheet" href="styles.css">', '<style>\n' + css + '\n</style>')
def inline(m):
    data = base64.b64encode(open(m.group(1), 'rb').read()).decode()
    return 'src="data:image/jpeg;base64,' + data + '"'
out = re.sub(r'src="(assets/team/[^"]+\.jpg)"', inline, out)
open('index.html','w').write(out)
print('index.html ->', os.path.getsize('index.html')//1024, 'KB')
