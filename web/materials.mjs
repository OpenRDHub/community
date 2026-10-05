import fs from 'node:fs';
import path from 'node:path';
import {createHash} from 'node:crypto';

// Only this explicitly selected archive is ingested; other repository files stay opt-in.
export function collectMaterials(communityRoot) {
  const root = path.join(communityRoot, 'docs/hackathon-2026');
  const documents = [], attachments = [];
  function walk(folder) {
    for (const entry of fs.readdirSync(folder, {withFileTypes: true}).sort((a,b)=>a.name.localeCompare(b.name))) {
      const file = path.join(folder, entry.name);
      if (entry.isDirectory()) { walk(file); continue; }
      if (!entry.isFile()) continue;
      const src = 'community/' + path.relative(communityRoot, file).split(path.sep).join('/');
      if (entry.name.endsWith('.md')) {
        const md = fs.readFileSync(file, 'utf8');
        const title = md.match(/^#\s+(.+)$/m)?.[1] || entry.name;
        const route = 'material-' + createHash('sha256').update(src).digest('hex').slice(0,16) + '.html';
        documents.push({src, title, route});
      } else if (/\.(pdf|png|jpe?g|webp|gif|html)$/i.test(entry.name)) {
        attachments.push({src, file});
      }
    }
  }
  if (fs.existsSync(root)) walk(root);
  return {documents, attachments};
}

export const encodePath = value => value.split('/').map(encodeURIComponent).join('/');

export function resolveContentLink(href, src, routes, attachmentSources) {
  const value = href.replace(/&amp;/g, '&');
  const github = value.match(/^https:\/\/github\.com\/OpenRDHub\/(community|\.github)\/blob\/main\/(.*)$/);
  if (!github && /^(https?:|mailto:|#)/.test(value)) return null;
  const raw = github ? github[2] : value;
  const match = raw.match(/^([^?#]*)([?#].*)?$/);
  const filename = decodeURIComponent(match[1]);
  const suffix = match[2] || '';
  let target = github ? github[1] + '/' + filename : path.posix.normalize(path.posix.join(path.posix.dirname(src), filename));
  if (!routes[target] && routes[target.replace(/\/$/, '') + '/README.md']) target = target.replace(/\/$/, '') + '/README.md';
  if (routes[target]) return {target, suffix, github: Boolean(github)};
  if (attachmentSources.has(target)) return {asset: target, suffix};
  throw Error('Unknown local target ' + src + ' ' + href);
}
