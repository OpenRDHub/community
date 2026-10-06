import {spawnSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';

const result = spawnSync(process.env.PYTHON || 'python3',
  [fileURLToPath(new URL('./verify.py', import.meta.url)), ...process.argv.slice(2)],
  {stdio: 'inherit'});
if (result.error) console.error('Unable to start the configured Python interpreter. Check PYTHON.');
process.exit(result.status ?? 1);
