const { chromium } = require('playwright');
const fs = require('fs'); const path='/tmp/work/book/img/';
const F="/tmp/work/fonts/node_modules/@fontsource/inter/files/";
const css=`@font-face{font-family:Inter;font-weight:400;src:url(file://${F}inter-latin-400-normal.woff2)}
@font-face{font-family:Inter;font-weight:600;src:url(file://${F}inter-latin-600-normal.woff2)}
@font-face{font-family:Inter;font-weight:700;src:url(file://${F}inter-latin-700-normal.woff2)}
body{margin:0;background:transparent}`;
(async()=>{
  const b=await chromium.launch();
  for(const f of fs.readdirSync(path).filter(x=>x.startsWith('fig-')&&x.endsWith('.svg'))){
    const s=fs.readFileSync(path+f,'utf8');
    const m=s.match(/width="([\d.]+)" height="([\d.]+)"/); const w=parseFloat(m[1]),h=parseFloat(m[2]);
    const pg=await b.newPage({viewport:{width:Math.ceil(w)+2,height:Math.ceil(h)+2},deviceScaleFactor:3});
    await pg.setContent(`<html><head><style>${css}</style></head><body>${s}</body></html>`);
    await pg.evaluate(()=>document.fonts.ready); await pg.waitForTimeout(300);
    await pg.screenshot({path:path+f.replace('.svg','.png'),omitBackground:true,clip:{x:0,y:0,width:w,height:h}});
    await pg.close();
  }
  await b.close(); console.log('pngs ok');
})();
