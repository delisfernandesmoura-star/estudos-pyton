const { chromium } = require('playwright'); const fs=require('fs'); const P='/tmp/work/kids/img/';
const F="/tmp/work/fonts/node_modules/@fontsource/";
const css=`@font-face{font-family:Fredoka;font-weight:600;src:url(file://${F}fredoka/files/fredoka-latin-600-normal.woff2)}
@font-face{font-family:Nunito;font-weight:600;src:url(file://${F}nunito/files/nunito-latin-600-normal.woff2)}
@font-face{font-family:Nunito;font-weight:700;src:url(file://${F}nunito/files/nunito-latin-700-normal.woff2)}body{margin:0;background:transparent}`;
(async()=>{const b=await chromium.launch();
for(const f of fs.readdirSync(P).filter(x=>x.endsWith('.svg'))){const s=fs.readFileSync(P+f,'utf8');const m=s.match(/width="([\d.]+)" height="([\d.]+)"/);const w=+m[1],h=+m[2];
const pg=await b.newPage({viewport:{width:Math.ceil(w)+2,height:Math.ceil(h)+2},deviceScaleFactor:3});await pg.setContent(`<html><head><style>${css}</style></head><body>${s}</body></html>`);
await pg.evaluate(()=>document.fonts.ready);await pg.waitForTimeout(200);await pg.screenshot({path:P+f.replace('.svg','.png'),omitBackground:true,clip:{x:0,y:0,width:w,height:h}});await pg.close();}
await b.close();console.log('ok')})();
