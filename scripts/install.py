#!/usr/bin/env python3
"""Preview-first installer for reusable Claude project presets.

Usage:
    python3 scripts/install.py --preset dotnet-maui --target /path/to/app
    python3 scripts/install.py --preset dotnet-maui --target /path/to/app --apply

No network calls; no shell commands; no deletions. Existing files are not
replaced unless --apply --overwrite is explicitly supplied.
"""
from __future__ import annotations
import argparse
import hashlib
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'setups' / 'dotnet'
MAUI = ROOT / 'overlays' / 'maui-cross-platform'
ANGULAR = ROOT / 'setups' / 'angular'
IONIC = ROOT / 'overlays' / 'ionic-angular-capacitor'
EXCLUDE = {'README.md', 'MAUI_CLAUDE_APPEND.md'}

def digest(file: Path) -> str:
    return hashlib.sha256(file.read_bytes()).hexdigest()

def collect(base: Path, ignore: set[str]) -> dict[Path, Path]:
    files = {}
    for file in sorted(base.rglob('*')):
        if file.is_symlink():
            raise RuntimeError(f'Symlink not permitted in setup: {file}')
        if not file.is_file():
            continue
        relative = file.relative_to(base)
        if relative.as_posix() in ignore or file.name == '.DS_Store':
            continue
        files[relative] = file
    return files

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--preset', choices=('dotnet', 'dotnet-maui', 'angular', 'dotnet-angular', 'ionic-angular', 'dotnet-ionic-angular'), required=True)
    parser.add_argument('--target', type=Path, required=True)
    parser.add_argument('--apply', action='store_true', help='Actually copy files (default: preview)')
    parser.add_argument('--overwrite', action='store_true', help='Replace conflicting files; BACK UP FIRST')
    args = parser.parse_args()
    if args.overwrite and not args.apply:
        parser.error('--overwrite requires --apply')
    target = args.target.expanduser().resolve()
    if target == ROOT or ROOT in target.parents:
        parser.error('Target must be a separate application repository, not this setup repository')
    if not target.is_dir() and args.apply:
        parser.error('Target directory must already exist (create your app repository first)')
    if target.exists() and not target.is_dir():
        parser.error('Target must be a directory')
    merged = collect(ANGULAR, {'README.md', 'ANGULAR_CLAUDE_APPEND.md'}) if args.preset in ('angular','ionic-angular') else collect(BASE, {'README.md', 'HANDBOOK.md'})
    if args.preset in ('dotnet-angular','dotnet-ionic-angular'):
        angular = collect(ANGULAR, {'README.md', 'ANGULAR_CLAUDE_APPEND.md', 'CLAUDE.md'})
        sources_path = Path('knowledge/SOURCES.md')
        if sources_path in angular and sources_path in merged:
            angular[Path('knowledge/ANGULAR_SOURCES.md')] = angular.pop(sources_path)
        merged.update(angular)
    if args.preset == 'dotnet-maui':
        overlay = collect(MAUI, EXCLUDE)
        merged.update(overlay)  # explicit overlay wins only within preset payload
    if args.preset in ('ionic-angular', 'dotnet-ionic-angular'):
        merged.update(collect(IONIC, {'README.md', 'IONIC_CLAUDE_APPEND.md'}))
    actions: dict[str, list[Path]] = {'new': [], 'same': [], 'conflict': []}
    for rel, source in sorted(merged.items()):
        destination = target / rel
        if destination.exists() or destination.is_symlink():
            if not destination.is_file() or destination.is_symlink():
                actions['conflict'].append(rel)
            elif digest(source) == digest(destination):
                actions['same'].append(rel)
            else:
                actions['conflict'].append(rel)
        else:
            actions['new'].append(rel)
    mode = 'APPLY' if args.apply else 'PREVIEW'
    print(f'{mode}: preset={args.preset}, target={target}')
    for key, title in [('new','NEW'), ('same','UNCHANGED'), ('conflict','CONFLICT')]:
        print(f'{title} ({len(actions[key])}):')
        for rel in actions[key]:
            print(f'  {rel.as_posix()}')
    if args.apply:
        copied = 0
        for rel in [*actions['new'], *(actions['conflict'] if args.overwrite else [])]:
            source = merged[rel]
            dest = target / rel
            if dest.is_symlink():
                print(f'SKIP unsafe symlink: {rel}', file=sys.stderr)
                continue
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, dest)
            copied += 1
        print(f'COPIED {copied}. Conflicts skipped: {0 if args.overwrite else len(actions["conflict"])}.')
    else:
        print('DRY RUN ONLY. Re-run with --apply after reviewing the file plan.')
    if args.preset == 'dotnet-maui':
        print('NOTE: review overlays/maui-cross-platform/MAUI_CLAUDE_APPEND.md and merge guidance into your project CLAUDE.md.')
    if args.preset in ('dotnet-angular','dotnet-ionic-angular'):
        print('NOTE: review setups/angular/ANGULAR_CLAUDE_APPEND.md and merge guidance into your project CLAUDE.md.')
    if args.preset in ('ionic-angular','dotnet-ionic-angular'):
        print('NOTE: merge overlays/ionic-angular-capacitor/IONIC_CLAUDE_APPEND.md into project CLAUDE.md manually.')
    return 0

if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (OSError, RuntimeError) as error:
        print(f'ERROR: {error}', file=sys.stderr)
        raise SystemExit(1)
