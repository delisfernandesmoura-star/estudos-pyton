const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();
for(const [f,o] of [['cover.html','cover.png'],['back.html','back.png']]){const pg=await b.newPage({viewport:{width:1600,height:2264}});
await pg.goto('file:///tmp/work/orat/'+f);await pg.evaluate(()=>document.fonts.ready);await pg.waitForTimeout(800);await pg.screenshot({path:'/tmp/work/orat/'+o});await pg.close();}
await b.close();})();
