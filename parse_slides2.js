const fs = require('fs');
const act2 = fs.readFileSync('temp/act2.html', 'utf8');

const base = fs.readFileSync('presentation/d3-act2-base.html', 'utf8');
const head = base.substring(0, base.indexOf('<div class="deck">') + 18);
const foot = base.substring(base.indexOf('</div>\n\n<script>'));

const css = `
  <!-- ACT 2 SPECIFIC CSS -->
  <style data-act="2">
    .a2-fields-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: clamp(16px, 2vw, 32px);
      margin-top: clamp(16px, 2.5vh, 32px);
      width: 100%;
    }
    .a2-half {
      display: flex;
      flex-direction: column;
      gap: clamp(8px, 1vh, 12px);
      position: relative;
    }
    .a2-half::before {
      content: '';
      position: absolute;
      top: -20px; left: -20px; right: -20px; bottom: -20px;
      background: var(--hf-glow);
      border-radius: 16px;
      z-index: -1;
      opacity: 0.5;
      filter: blur(20px);
    }
    .a2-half-head {
      margin-bottom: clamp(4px, 1vh, 12px);
      padding-bottom: 8px;
      border-bottom: 1px solid rgba(255,255,255,0.1);
    }
    .a2-hh {
      font-family: var(--font-editorial);
      font-size: clamp(24px, 2.5vw, 32px);
      color: var(--hf-c);
      margin: 0;
      line-height: 1.1;
    }
    .a2-ht {
      font-family: var(--font-mono);
      font-size: clamp(11px, 1vw, 13px);
      color: var(--text-dim);
      display: block;
      margin-top: 4px;
    }
    .a2-field-row {
      display: grid;
      grid-template-columns: auto 1fr auto;
      gap: clamp(12px, 1.5vw, 24px);
      align-items: center;
      background: rgba(13, 17, 23, 0.6);
      border: 1px solid rgba(255,255,255,0.08);
      border-radius: 8px;
      padding: clamp(12px, 1.5vh, 20px);
      transition: all 0.3s ease;
    }
    .a2-field-row:hover {
      background: rgba(13, 17, 23, 0.9);
      border-color: var(--hf-c);
      transform: translateX(4px);
    }
    .a2-f-num {
      font-family: var(--font-mono);
      font-size: clamp(18px, 2vw, 24px);
      font-weight: 700;
      color: var(--hf-c);
      opacity: 0.8;
      width: 24px;
      text-align: center;
    }
    .a2-f-body {
      display: flex;
      flex-direction: column;
      gap: 4px;
    }
    .a2-f-title {
      font-weight: 600;
      font-size: clamp(15px, 1.4vw, 18px);
      color: var(--text-main);
    }
    .a2-f-desc {
      font-size: clamp(13px, 1.1vw, 15px);
      color: var(--text-mute);
      line-height: 1.4;
    }
    .a2-f-reader {
      font-family: var(--font-mono);
      font-size: clamp(10px, 0.9vw, 12px);
      color: var(--hf-c);
      background: rgba(255,255,255,0.03);
      padding: 4px 10px;
      border-radius: 4px;
      white-space: nowrap;
    }
    .a2-graph-row {
      grid-column: 1 / -1;
      margin-top: clamp(12px, 1.5vh, 24px);
    }
  </style>
`;

const result = head.replace('</style>', '</style>\n' + css) + '\n\n' + act2 + '\n\n' + foot;
fs.writeFileSync('presentation/d3-act2.html', result);
