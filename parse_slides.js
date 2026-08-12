const fs = require('fs');

const d3 = fs.readFileSync('presentation/d3.html', 'utf8');

// copy everything up to S01
const s01_idx = d3.indexOf('<!-- ═══════════ S01 · TITLE ═══════════ -->');
const head = d3.substring(0, s01_idx);

// copy script tag and below
const script_idx = d3.indexOf('<script>');
const foot = d3.substring(script_idx);

fs.writeFileSync('presentation/d3-act2-base.html', head + '\n\n' + foot);
