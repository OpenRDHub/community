"""Behavioral regression checks for record ingestion and repository portability."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json, os, shutil, subprocess, sys, tempfile, unittest, yaml

BASE = Path(__file__).resolve().parents[1]

class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.urls = []
    def handle_starttag(self, tag, attrs):
        self.urls += [v for k, v in attrs if k in ('href', 'src') and v]

class RecordWorkflow(unittest.TestCase):
    def test_ingest_languages_metadata_and_links(self):
        with tempfile.TemporaryDirectory() as temp:
            tmp = Path(temp); drafts = tmp/'drafts'
            if (BASE/'drafts').is_dir():
                shutil.copytree(BASE/'drafts', drafts)
            else:
                shutil.copytree(BASE.parent, drafts/'community', ignore=shutil.ignore_patterns('.git','web'))
                shutil.copytree(BASE/'organization-profile', drafts/'.github')
            records = drafts/'community/records/meetings'
            records.mkdir(parents=True, exist_ok=True)
            template = (drafts/'community/templates/meeting.md').read_text()
            _, front, body = template.split('---', 2)
            meta = yaml.safe_load(front)
            for lang in ('zh', 'en'):
                row = dict(meta, id='VERIFY-'+lang.upper(), lang=lang,
                           title='Verification '+lang, summary='Completed template '+lang,
                           authority='feishu', authority_url='https://example.org/document',
                           reviewer='Confirmed test reviewer', source='Test source',
                           source_revision='test-v2', status='reviewed')
                (records/f'only-{lang}.md').write_text('---\n'+yaml.safe_dump(row,allow_unicode=True)+'---\n'+body)
            parsed = subprocess.run([sys.executable, str(BASE/'read-records.py'), str(drafts)],capture_output=True,text=True)
            self.assertEqual(parsed.returncode,0,parsed.stderr)
            indexed=json.loads(parsed.stdout)
            self.assertEqual(sum(r['id'].startswith('VERIFY-') for r in indexed),2)
            self.assertFalse(any('/templates/' in r['source_path'] for r in indexed))
            site=tmp/'site'
            env=dict(os.environ,CONTENT_ROOT=str(drafts),SITE_OUTPUT=str(site),PYTHON=sys.executable)
            built=subprocess.run(['node',str(BASE/'build.mjs')],env=env,capture_output=True,text=True)
            self.assertEqual(built.returncode,0,built.stderr)
            zh_fallback=(site/'record-verify-en.html').read_text()
            en_fallback=(site/'en/record-verify-zh.html').read_text()
            self.assertIn('英文原文',zh_fallback)
            self.assertIn('Chinese original',en_fallback)
            self.assertIn('Confirmed test reviewer',en_fallback)
            self.assertIn('https://example.org/document',en_fallback)
            self.assertIn('Reviewed',en_fallback)
            self.assertIn('Verification en',(site/'knowledge.html').read_text())
            self.assertIn('Verification zh',(site/'en/knowledge.html').read_text())
            missing=[]
            for page in site.rglob('*.html'):
                parser=Links();parser.feed(page.read_text())
                for url in parser.urls:
                    parsed_url=urlsplit(url)
                    if parsed_url.scheme or parsed_url.netloc or not parsed_url.path:continue
                    target=page.parent/unquote(parsed_url.path)
                    if not target.exists():missing.append((str(page.relative_to(site)),url))
            self.assertEqual(missing,[])
            self.assertIn('org-board.html',(site/'index.html').read_text())
            self.assertIn('board.html',(site/'community.html').read_text())
            self.assertIn('PULL_REQUEST_TEMPLATE.md',(site/'files.html').read_text())
            for prefix in ('', 'en/'):
                self.assertIn('https://github.com/orgs/OpenRDHub/projects/1',(site/(prefix+'board.html')).read_text())
                self.assertIn('https://github.com/OpenRDHub/community/discussions/9',(site/(prefix+'discussions.html')).read_text())
                self.assertNotIn('&topic=topic',(site/(prefix+'discussions.html')).read_text())
                for n in range(1,7):
                    self.assertIn(f'https://github.com/OpenRDHub/community/issues/{n+2}',(site/(prefix+f'c0{n}.html')).read_text())
            # A malformed new record must fail before replacing the prior output.
            original=(site/'index.html').read_bytes()
            (records/'invalid.md').write_text('# No metadata\n')
            failed=subprocess.run(['node',str(BASE/'build.mjs')],env=env,capture_output=True,text=True)
            self.assertNotEqual(failed.returncode,0)
            self.assertIn('invalid.md',failed.stderr)
            self.assertEqual((site/'index.html').read_bytes(),original)
            (records/'invalid.md').unlink()
            # Required revision metadata and duplicate IDs are not silently accepted.
            file=records/'only-zh.md';valid=file.read_text()
            file.write_text(valid.replace('source_revision: test-v2\n',''))
            failed=subprocess.run([sys.executable,str(BASE/'read-records.py'),str(drafts)],capture_output=True,text=True)
            self.assertNotEqual(failed.returncode,0);self.assertIn('source_revision',failed.stderr)
            file.write_text(valid)
            (records/'duplicate.md').write_text(valid)
            failed=subprocess.run([sys.executable,str(BASE/'read-records.py'),str(drafts)],capture_output=True,text=True)
            self.assertNotEqual(failed.returncode,0);self.assertIn('duplicate',failed.stderr)

if __name__=='__main__':unittest.main(verbosity=2)
