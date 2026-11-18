#!/usr/bin/env python3
"""Little Reef v48, safe additive fix for v47 typography regression."""
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parent.parent
css_path = root / 'assets/css/reef-pages.css'
addition = root / 'assets/css/REEF_V48_ADD_TO_PAGES.css'
people_path = root / 'people.md'
head_path = root / '_includes/main/head.html'
if not css_path.is_file() or not addition.is_file():
    sys.exit('Missing reef-pages.css or v48 CSS: run this script from the repository copy.')

css = css_path.read_text(encoding='utf-8')
# Remove the over-broad v47 selector block, if present. It included all About
# descendants and overrode the original VT323 text with Silkscreen !important.
css, removed = re.subn(
    r'\n?/\* Little Reef v47 — About / People Hangul Mona12 fallback\.[\s\S]*?\}\s*'
    r'(?=\Z|/\*|body\.|@media)',
    '\n', css, count=1
)
marker = '/* Little Reef v48 — precise typography repair. */'
addition_css = addition.read_text(encoding='utf-8')
if marker not in css:
    css = css.rstrip()+'\n\n'+addition_css.rstrip()+'\n'
    css_path.write_text(css, encoding='utf-8')
    print('Added v48 font and Research spacing rules.')
else:
    if removed:
        css_path.write_text(css, encoding='utf-8')
    print('v48 CSS already installed.')

# The actual People source uses e.g. <div class="person-name">강민지 Kang, Minji</div>.
# Wrapping only Hangul runs avoids changing the English font in the SAME node.
if people_path.is_file():
    source = people_path.read_text(encoding='utf-8')
    def wrap_name(match):
        prefix, contents, suffix = match.groups()
        if 'lang="ko"' in contents:
            return match.group(0)
        updated = re.sub(r'[가-힣]+(?:\s+[가-힣]+)*',
                         lambda m:'<span lang="ko">'+m.group(0)+'</span>',contents)
        return prefix+updated+suffix
    result = re.sub(
        r'(<(?:div|h3|span)\b[^>]*class=["\'][^"\']*\bperson-name\b[^"\']*["\'][^>]*>)([^<]*)(</(?:div|h3|span)>)',
        wrap_name, source)
    if result != source:
        people_path.write_text(result, encoding='utf-8')
        print('Wrapped Korean names in People without changing English names.')
    else:
        print('People names already marked, or no mixed-language names found.')
else:
    print('people.md not found; CSS repair still applied.')

# Retain / ensure Mona12 is imported. Fonts are fetched by the browser.
if head_path.is_file():
    head = head_path.read_text(encoding='utf-8')
    url = 'https://cdn.jsdelivr.net/gh/MonadABXY/mona-font/web/mona.css'
    if url not in head:
        head_path.write_text(head.rstrip()+'\n<link rel="stylesheet" href="'+url+'">\n', encoding='utf-8')
        print('Added Mona12 font import.')
print('Done. No research.md, about.md, other tabs, or stamp files were replaced.')
