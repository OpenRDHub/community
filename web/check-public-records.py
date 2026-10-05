"""Check metadata and visibility in a public repository without dumping records."""
from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
errors = []
for path in sorted((ROOT / 'web').glob('*.json')):
    try:
        json.loads(path.read_text(encoding='utf-8'))
    except json.JSONDecodeError as exc:
        errors.append(f'{path.relative_to(ROOT)}: invalid JSON at line {exc.lineno}, column {exc.colno}')

parsed = subprocess.run(
    [sys.executable, str(Path(__file__).with_name('read-records.py')), str(ROOT)],
    capture_output=True, text=True,
)
if parsed.returncode:
    print(parsed.stderr, file=sys.stderr, end='')
    sys.exit(parsed.returncode)
records = json.loads(parsed.stdout)
for record in records:
    is_fixture = record['source_path'].startswith('community/examples/records/') and record['example']
    if not is_fixture and record['visibility'] != 'public':
        errors.append(
            f"{record['source_path']}: real records must use visibility: public in this public repository; "
            'keep internal/restricted originals in the access-controlled source and submit a public summary'
        )
if errors:
    print('\n'.join(errors), file=sys.stderr)
    sys.exit(1)
print(f'Validated JSON configuration and {len(records)} record metadata entries. Public visibility check passed.')
