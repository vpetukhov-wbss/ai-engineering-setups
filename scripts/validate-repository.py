#!/usr/bin/env python3
"""Dependency-free structural validation (does not validate runtime build or skills effectiveness)."""
from __future__ import annotations
from pathlib import Path
import json
import re
import sys
ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT/'setups'/'dotnet'
MAUI = ROOT/'overlays'/'maui-cross-platform'
ANGULAR = ROOT/'setups'/'angular'
errors=[]
for file in ('README.md','LICENSE','CONTRIBUTING.md','SECURITY.md','scripts/install.py'):
    if not (ROOT/file).is_file(): errors.append(f'Missing {file}')
for root in (BASE,MAUI,ANGULAR):
    if not root.is_dir(): errors.append(f'Missing {root.relative_to(ROOT)}'); continue
    for p in root.rglob('*'):
        if p.is_symlink(): errors.append(f'Symlink forbidden: {p}')
    claude=root/'.claude'
    for folder in ('agents','rules','skills'):
        for p in (claude/folder).rglob('*.md'):
            body=p.read_text(encoding='utf-8')
            if not re.match(r'^---\n[\s\S]*?\n---\n',body):
                errors.append(f'Invalid frontmatter: {p}')
                continue
            frontmatter=body.split('\n---\n',1)[0]
            if folder!='rules' and ('name:' not in frontmatter or 'description:' not in frontmatter):
                errors.append(f'Missing name/description: {p}')
            if folder=='skills':
                if p.name!='SKILL.md': errors.append(f'Skill filename must be SKILL.md: {p}')
                if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',p.parent.name):
                    errors.append(f'Invalid skill directory name: {p.parent}')
    for p in root.rglob('*'):
        if p.is_file() and p.suffix.lower() in ('.p12','.pfx','.mobileprovision','.jks','.keystore','.pem','.key','.env'):
            errors.append(f'Possible private credential: {p}')
settings=BASE/'.claude'/'settings.json'
if settings.is_file():
    try:
        j=json.loads(settings.read_text(encoding='utf-8'))
        if not isinstance(j.get('permissions',{}).get('deny'),list):
            errors.append('Expected permissions.deny array')
    except Exception as e: errors.append(f'Bad settings.json: {e}')
else: errors.append('Missing settings.json')
print('Core skills:',len(list((BASE/'.claude'/'skills').glob('*/SKILL.md'))))
print('MAUI skills:',len(list((MAUI/'.claude'/'skills').glob('*/SKILL.md'))))
print('MAUI agents:',len(list((MAUI/'.claude'/'agents').glob('*.md'))))
print('Angular skills:',len(list((ANGULAR/'.claude'/'skills').glob('*/SKILL.md'))))
print('Angular agents:',len(list((ANGULAR/'.claude'/'agents').glob('*.md'))))
for err in errors: print('ERROR:',err)
if errors: sys.exit(1)
print('PASS: file layout, basic metadata and sample-secret file extension checks.')
print('NOTE: no actual .NET, Xcode, Android, UI, store or Claude invocation was run.')
