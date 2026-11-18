#!/usr/bin/env python3
"""v47: install Mona12 fallback on About and People, idempotently."""
from pathlib import Path

root = Path(__file__).resolve().parent.parent
head = root / '_includes/main/head.html'
css = root / 'assets/css/reef-pages.css'
addition = root / 'assets/css/ADD_TO_REEF_PAGES_MONA.css'
for path in (head, css, addition):
    if not path.is_file():
        raise SystemExit(f'Missing {path.relative_to(root)}. Apply to a Little Reef subpages repository.')
link = '<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/MonadABXY/mona-font/web/mona.css">'
t = head.read_text(encoding='utf-8')
if 'MonadABXY/mona-font/web/mona.css' not in t:
    head.write_text(t.rstrip() + '\n' + link + '\n', encoding='utf-8')
    print('Added Mona12 webfont stylesheet to head')
else:
    print('Mona12 webfont already imported')
marker = '/* Little Reef v47 — About / People Hangul Mona12 fallback.'
t = css.read_text(encoding='utf-8')
if marker not in t:
    css.write_text(t.rstrip() + '\n\n' + addition.read_text(encoding='utf-8') + '\n', encoding='utf-8')
    print('Appended About / People font rules')
else:
    print('About / People font rules already present')
