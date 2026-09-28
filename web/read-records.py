"""Validate and index records. Invalid record files fail instead of disappearing."""
from pathlib import Path
from datetime import date
import json, re, sys, yaml

root = Path(sys.argv[1])
community = root / 'community' if (root / 'community').is_dir() else root
records, errors = [], []
required = {'id', 'lang', 'type', 'title', 'summary', 'date', 'updated', 'status',
            'visibility', 'publication', 'authority', 'example', 'editor', 'reviewer',
            'source', 'source_revision'}
enums = {
    'lang': {'zh', 'en'},
    'type': {'proposal', 'guide', 'reference', 'meeting', 'discussion', 'decision', 'daily'},
    'status': {'draft', 'pending-review', 'reviewed', 'superseded'},
    'visibility': {'internal', 'public', 'restricted'},
    'publication': {'pending', 'approved', 'published'},
    'authority': {'github', 'feishu'},
}
for p in sorted(community.rglob('*.md')):
    rel = p.relative_to(community)
    if rel.parts[0] in {'templates', '.github', 'web', 'node_modules'}:
        continue
    is_record = rel.parts[0] == 'records' or rel.parts[:2] == ('examples', 'records')
    try:
        text = p.read_text(encoding='utf-8')
        match = re.match(r'^---\r?\n(.*?)\r?\n---(?:\r?\n|$)', text, re.S)
        if not match:
            if is_record:
                raise ValueError('record requires YAML metadata; copy a template and fill its fields')
            continue
        meta = yaml.safe_load(match[1])
        if not isinstance(meta, dict) or 'id' not in meta:
            if is_record:
                raise ValueError('record requires an id')
            continue
        missing = required - meta.keys()
        if missing:
            raise ValueError('missing fields: ' + ', '.join(sorted(missing)))
        for key in required - {'date', 'updated', 'example'}:
            if not isinstance(meta[key], str) or not meta[key].strip():
                raise ValueError(f'{key} must be a non-empty string')
        if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9-]*', meta['id']) or meta['id'] == 'REPLACE-ME':
            raise ValueError('id must be unique and use letters, numbers or hyphens; replace REPLACE-ME')
        for key, allowed in enums.items():
            if meta[key] not in allowed:
                raise ValueError(f'{key}: expected one of {sorted(allowed)}')
        for key in ('date', 'updated'):
            meta[key] = str(meta[key])
            date.fromisoformat(meta[key])
        if not isinstance(meta['example'], bool):
            raise ValueError('example must be true or false')
        if rel.parts[:2] == ('examples', 'records') and not meta['example']:
            raise ValueError('examples/records must set example: true')
        for key in ('source_url', 'authority_url'):
            if key in meta and (not isinstance(meta[key], str) or not re.match(r'^https?://[^\s]+$', meta[key])):
                raise ValueError(f'{key} must be an http(s) URL')
        records.append(dict(meta, source_path='community/' + rel.as_posix(), body=text[match.end():].strip()))
    except (ValueError, yaml.YAMLError) as exc:
        errors.append(f'{rel}: {exc}')
seen = set()
for r in records:
    key = (r['lang'], r['id'].lower())
    if key in seen:
        errors.append(f"{r['source_path']}: duplicate id/language {key}")
    seen.add(key)
if errors:
    print('\n'.join(errors), file=sys.stderr)
    sys.exit(1)
print(json.dumps(records, ensure_ascii=False))
