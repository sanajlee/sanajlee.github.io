#!/usr/bin/env python3
"""Apply unified v43: Mona, SIDE B scrapbook with two bird photos, and Research spacing.
Run from repository root: python3 scripts/apply_little_reef_v42.py
Safe to re-run: navigation, head imports, styles and layout changes are idempotent.
"""
from pathlib import Path
import re
import shutil

root = Path(__file__).resolve().parent.parent
header = root / '_includes/main/header.html'
head = root / '_includes/main/head.html'
layout = root / '_layouts/page.html'
page_css = root / 'assets/css/reef-pages.css'
page_add = root / 'assets/css/ADD_TO_REEF_PAGES.css'
necessary = [header,head,layout,page_css,page_add,root/'non-academic.md',root/'research.md']
missing = [str(p.relative_to(root)) for p in necessary if not p.is_file()]
if missing:
    raise SystemExit('Missing required files: '+', '.join(missing)+'\nCopy ZIP contents into your existing Jekyll repo root first. If reef-pages.css is missing, apply the earlier all-tabs patch first.')

def write_change(path,new):
    old=path.read_text(encoding='utf-8')
    if new==old:
        print('Unchanged:',path.relative_to(root))
        return
    backup=path.with_name(path.name+'.before-v42.bak')
    if not backup.exists(): backup.write_text(old,encoding='utf-8')
    path.write_text(new,encoding='utf-8')
    print('Updated:',path.relative_to(root))

# Navigation: normalize existing /non-academic links (including old label) to SIDE B.
t=header.read_text(encoding='utf-8')
nav="<a href=\"{{ '/non-academic' | relative_url }}\" {% if page.url == '/non-academic' or page.url == '/non-academic/' %}class=\"is-active\"{% endif %}>SIDE B</a>"
pat=re.compile(r'(<a\b[^>]*href="\{\{\s*[\'\"]?/non-academic[\'\"]?\s*\|\s*relative_url\s*\}\}"[^>]*>)(.*?)(</a>)',re.I|re.S)
if pat.search(t):
    t=pat.sub(lambda m:m.group(1)+'SIDE B'+m.group(3),t)
else:
    mark=re.search(r'(?m)^(\s*)</nav>',t)
    if not mark:raise SystemExit('No </nav> in header; no header change made.')
    t=t[:mark.start()]+mark.group(1)+'  '+nav+'\n'+t[mark.start():]
write_change(header,t)

# Font and CSS imports.
t=head.read_text(encoding='utf-8')
links=[
 '<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/MonadABXY/mona-font/web/mona.css">',
 "<link rel=\"stylesheet\" href=\"{{ '/assets/css/reef-nonacademic.css' | relative_url }}\">",
 "<link rel=\"stylesheet\" href=\"{{ '/assets/css/reef-sideb-scrapbook.css' | relative_url }}\">",
]
for link,key in zip(links,['MonadABXY/mona-font/web/mona.css','reef-nonacademic.css','reef-sideb-scrapbook.css']):
    if key not in t:t=t.rstrip()+'\n'+link+'\n'
write_change(head,t)

# The Research page frontmatter uses research_windows:true; bypass the common enclosing window.
t=layout.read_text(encoding='utf-8')
if 'page.research_windows' not in t:
    marker='<article class="page-shell reef-os-window reef-content-window">'
    if marker not in t:
        raise SystemExit('page.html is not v25-compatible. Cannot safely insert Research layout switch.')
    i=t.index(marker)
    t=t[:i]+'{% if page.research_windows %}\n{{ content }}\n{% else %}\n'+t[i:]
    closing=t.rfind('</article>')
    if closing<0:raise SystemExit('page.html missing </article>.')
    closing+=len('</article>')
    t=t[:closing]+'\n{% endif %}'+t[closing:]
write_change(layout,t)

# Append Research-only CSS exactly once.
css=page_css.read_text(encoding='utf-8')
additional=page_add.read_text(encoding='utf-8').strip()
if '/* v40 Research-only:' not in css:
    css=css.rstrip()+'\n\n'+additional+'\n'
elif '/* v43 Research spacing:' not in css:
    suffix=additional.split('/* v43 Research spacing:',1)[1]
    css=css.rstrip()+'\n\n/* v43 Research spacing:'+suffix.rstrip()+'\n'
write_change(page_css,css)
print('v43 done: SIDE B two bird photos + Mona + Research windows/projects/spacing. No stamp or Supabase files changed.')
