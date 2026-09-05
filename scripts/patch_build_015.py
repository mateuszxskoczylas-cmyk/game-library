from pathlib import Path

path = Path("index.html")
s = path.read_text(encoding="utf-8")

if "BUILD_014" not in s:
    raise SystemExit("Expected BUILD_014")


def rep(old: str, new: str) -> None:
    global s
    if old not in s:
        raise SystemExit(f"Missing expected fragment: {old[:120]!r}")
    s = s.replace(old, new, 1)


rep(
    '.poster.cut-corners{clip-path:polygon(12px 0,calc(100% - 12px) 0,100% 12px,100% calc(100% - 12px),calc(100% - 12px) 100%,12px 100%,0 calc(100% - 12px),0 12px)}.fallback{',
    '.poster.cut-corners{clip-path:polygon(12px 0,calc(100% - 12px) 0,100% 12px,100% calc(100% - 12px),calc(100% - 12px) 100%,12px 100%,0 calc(100% - 12px),0 12px)}.game-card.released .poster,.game-card.released .fallback{filter:grayscale(1) contrast(.88)}.released-ribbon{position:absolute;top:17px;right:-42px;width:154px;z-index:4;transform:rotate(36deg);background:var(--yellow);color:var(--purple);border-top:2px solid #fff;border-bottom:2px solid #5b5300;box-shadow:0 2px 0 #111;text-align:center;padding:5px 0;font:900 10px "Courier New",monospace;letter-spacing:.12em;text-shadow:1px 1px 0 #fff}.game-card.released .badge{background:#d8d8d8;color:#555}.fallback{'
)

rep(
    '.dialup-box{background:#efefef;border:2px inset #999;padding:14px;font:12px "Courier New",monospace}.progress-shell{',
    '.dialup-box{background:#efefef;border:2px inset #999;padding:14px;font:12px "Courier New",monospace}.dialup-row{display:flex;align-items:center;gap:12px}.dialup-icon{width:50px;height:50px;background:var(--sky);border:2px outset #fff;display:grid;place-items:center;font-size:24px}.progress-shell{'
)

rep(
    '.cancelled-mode .game-title{text-decoration:line-through}.context-menu{',
    '.cancelled-mode .game-title{text-decoration:line-through}.cancelled-mode .release-window{filter:grayscale(.8)}.build-hold{cursor:default}.context-menu{'
)

rep(
    '<p>Jedna strona. Cztery okna premier. Nadchodzące gry, studia i planowane daty w kolorowym interfejsie rodem z końcówki lat 90.</p>',
    '<p>Strona zaprojektowana po to, żeby udowodnić, że gry jednak wychodzą — i czasem jest ich naprawdę sporo.</p>'
)

rep(
    '<span id="buildText">BUILD_014</span>',
    '<span id="buildText" class="build-hold">BUILD_015</span>'
)

rep(
    '<div class="context-menu" id="contextMenu"><button id="ctxPizza">sprzedaj mi te pizze</button><div class="context-sep"></div><button id="ctxCancel">Anuluj</button></div>',
    '<div class="context-menu" id="contextMenu"><button data-context="open">Otwórz</button><button data-context="copy">Kopiuj nazwę</button><div class="context-sep"></div><button data-context="pizza">sprzedaj mi te pizze</button></div>'
)

rep(
    '{title:"Halloween: The Game",studio:"IllFonic",date:"08.09.2026",sortDate:"2026-09-08",status:"POTWIERDZONE",image:"https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/3219630/3e4a35d27eabd7691d8af4f5b94d38cae3bcce8d/library_capsule.jpg"}]},',
    '{title:"Halloween: The Game",studio:"IllFonic",date:"08.09.2026",sortDate:"2026-09-08",status:"POTWIERDZONE",image:"https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/3219630/3e4a35d27eabd7691d8af4f5b94d38cae3bcce8d/library_capsule.jpg"},\n{title:"Onimusha: Way of the Sword",studio:"CAPCOM",date:"03.09.2026",sortDate:"2026-09-03",status:"POTWIERDZONE",steamAppId:"2638890"}]},'
)

old_card = '''function card(g,i){const u=g.status==="NIEZAPOWIEDZIANE"?" unannounced":"";return `<article class="game-card" data-title="${esc(g.title)}"><div class="poster-wrap">${poster(g)}</div><div class="card-body"><div class="studio">${esc(g.studio)}</div><div class="game-title">${esc(g.title)}</div><div class="release"><b>&gt;</b> ${esc(g.date)}</div><div class="badges"><span class="badge${u}">${esc(g.status)}</span><span class="node">POZYCJA_${String(i+1).padStart(2,"0")}</span></div></div></article>`}'''
new_card = '''function localDateKey(){const d=new Date();const p=n=>String(n).padStart(2,"0");return `${d.getFullYear()}-${p(d.getMonth()+1)}-${p(d.getDate())}`}
function isReleased(g){return /^\\d{4}-\\d{2}-\\d{2}$/.test(g.sortDate||"")&&g.sortDate<localDateKey()}
function card(g,i){const released=isReleased(g);const status=released?"WYDANA":g.status;const u=status==="NIEZAPOWIEDZIANE"?" unannounced":"";const ribbon=released?'<span class="released-ribbon">WYDANA</span>':"";return `<article class="game-card${released?" released":""}" data-title="${esc(g.title)}"><div class="poster-wrap">${poster(g)}${ribbon}</div><div class="card-body"><div class="studio">${esc(g.studio)}</div><div class="game-title">${esc(g.title)}</div><div class="release"><b>&gt;</b> ${esc(g.date)}</div><div class="badges"><span class="badge${u}">${esc(status)}</span><span class="node">POZYCJA_${String(i+1).padStart(2,"0")}</span></div></div></article>`}'''
rep(old_card, new_card)

start = s.find('const $=id=>document.getElementById(id);')
end = s.find('</script>', start)
if start < 0 or end < 0:
    raise SystemExit("Could not find JS tail")

new_tail = r'''const $=id=>document.getElementById(id);let currentYear=0,quoteBag=[],lastQuote="",imageCache=null,lastImage="",uiCode=[],helpTimer=null,buildTimer=null,contextTitle="",helpLongFired=false;const yearIds=["y2026","y2027","y2028","beyond"];const eggAssets={dab:"assets/easter/3d7777f2-cdbc-448b-b4e3-7de67f058f24.png",sixtySeven:"assets/easter/53425a0a-5017-43ba-a576-d4e76aab068d.png"};
function toast(t){const e=$("toast");e.textContent=t;e.classList.add("show");clearTimeout(window.__toast);window.__toast=setTimeout(()=>e.classList.remove("show"),2200)}
function openModal(t,h){$("modalTitle").textContent=t;$("modalBody").innerHTML=h;$("modalBackdrop").classList.add("open")}
function closeModal(){$("modalBackdrop").classList.remove("open")}
function shuffle(a){a=[...a];for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a}
function nextQuote(){if(!quoteBag.length){quoteBag=shuffle(quotes);if(lastQuote&&quoteBag.at(-1)===lastQuote&&quoteBag.length>1)[quoteBag[0],quoteBag[quoteBag.length-1]]=[quoteBag[quoteBag.length-1],quoteBag[0]]}lastQuote=quoteBag.pop();return lastQuote}
async function loadImages(){if(imageCache)return imageCache;const r=await fetch("https://api.github.com/repos/mateuszxskoczylas-cmyk/game-library/contents/assets/easter?ref=main",{headers:{Accept:"application/vnd.github+json"}});if(!r.ok)throw new Error("HTTP "+r.status);const d=await r.json();imageCache=d.filter(x=>x.type==="file"&&/\.(png|jpe?g|gif|webp|avif)$/i.test(x.name)&&x.download_url);return imageCache}
async function randomImage(){const imgs=await loadImages();if(!imgs.length)throw new Error("brak obrazów");let img=imgs[Math.floor(Math.random()*imgs.length)];if(imgs.length>1&&img.download_url===lastImage)img=imgs[(imgs.indexOf(img)+1)%imgs.length];lastImage=img.download_url;return img.download_url}
async function surprisePhoto(title="BŁĄD_PAMIĘCI.EXE",caption=""){openModal(title,'<div class="loading-box">ODCZYTYWANIE PAMIĘCI...</div>');try{const src=await randomImage();$("modalBody").innerHTML=`<img class="photo-full" src="${esc(src)}" alt="easter egg"><div class="photo-caption">&gt; ${esc(caption||nextQuote())}</div>`}catch(e){$("modalBody").innerHTML=`<div class="loading-box">BŁĄD ODCZYTU<br>${esc(e.message)}</div>`}}
function przemoPopup(){document.body.classList.add("glitch");setTimeout(()=>document.body.classList.remove("glitch"),1100);openModal("USER_PROFILE_CORRUPTED.EXE",`<div class="przemo-stack">${przemoImages.map(x=>`<img src="${x}" alt="">`).join("")}</div><div class="photo-caption">&gt; przemo jest wygenerowany komputerowo<br>&gt; pieniądz lubi cisze<br>&gt; shoty przema</div>`)}
function openTenant(){openModal("NOTATNIK - RAPORT_SERWISOWY.TXT",`<pre>${esc(tenantText)}</pre>`)}
function monitorEgg(){surprisePhoto("MONITORING_01.CAM","czy ten obiekt jest monitorowany?")}
function galleryWarning(){document.body.classList.add("shake");setTimeout(()=>document.body.classList.remove("shake"),1100);openModal("OSTRZEŻENIE SYSTEMOWE",'<div class="screen-warning">galeria młynska zostaje wysadzana w 2027 roku</div><div class="photo-caption">&gt; pan dyrektor podpisał nieprawdę<br>&gt; nie próbuj zgrywać bohatera</div>')}
function sixtySevenEgg(){openModal("CACHE_067.EXE",`<img class="photo-full" src="${eggAssets.sixtySeven}" alt="67"><div class="photo-caption">&gt; 67<br>&gt; polscy raperzy w srebrze i cyrkonii</div>`)}
function dabEgg(){openModal("DAB.EXE",`<img class="photo-full" src="${eggAssets.dab}" alt=""><div class="photo-caption">&gt; *zaczyna dabować*<br>&gt; dabonyourmom69</div>`)}
function cancelGames(){if(document.body.classList.contains("cancelled-mode"))return;document.body.classList.add("cancelled-mode");const old=$("mainTitle").textContent;$("mainTitle").textContent="GRY NIE WYCHODZĄ";toast("a jaka wymóweczka dziś?");setTimeout(()=>{document.body.classList.remove("cancelled-mode");$("mainTitle").textContent=old;openModal("PRZYWRACANIE_SYSTEMU.EXE",'<h3>Jednak wychodzą.</h3><p>kupa stolec ale sztos</p>')},5200)}
function dialup(){openModal("POŁĄCZENIE TELEFONICZNE",'<div class="dialup-box"><div class="dialup-row"><div class="dialup-icon">☎</div><div><b>Łączenie z 067.067.067.067...</b><br><span id="dialText">Wybieranie numeru...</span></div></div><div class="progress-shell"><div class="progress-bar" id="dialProgress"></div></div><button class="classic-btn" onclick="closeModal()">Anuluj</button></div>');let p=0;const iv=setInterval(()=>{const bar=$("dialProgress"),txt=$("dialText");if(!bar||!txt){clearInterval(iv);return}p+=17;bar.style.width=Math.min(p,100)+"%";if(p>30)txt.textContent="Negocjowanie protokołu...";if(p>65)txt.textContent="Sprawdzanie nazwy użytkownika i hasła...";if(p>=100){clearInterval(iv);setTimeout(()=>surprisePhoto("POŁĄCZENIE USTANOWIONE","no oczywiscie pelen naladowany pozytywnej energii"),280)}},260)}
function goYear(d){currentYear=Math.max(0,Math.min(yearIds.length-1,currentYear+d));document.getElementById(yearIds[currentYear]).scrollIntoView({behavior:"smooth",block:"start"})}
function codeStep(x){const hidden=["star","back","forward","star","gw"];uiCode.push(x);uiCode=uiCode.slice(-hidden.length);if(hidden.every((v,i)=>uiCode[i]===v)){uiCode=[];dialup()}}
$("modalClose").onclick=closeModal;$("modalBackdrop").onclick=e=>{if(e.target===$("modalBackdrop"))closeModal()};document.addEventListener("keydown",e=>{if(e.key==="Escape")closeModal()});
$("homeBtn").onclick=()=>window.scrollTo({top:0,behavior:"smooth"});$("backBtn").onclick=()=>{codeStep("back");goYear(-1)};$("forwardBtn").onclick=()=>{codeStep("forward");goYear(1)};$("starBtn").onclick=()=>{codeStep("star");openModal("ULUBIONE",'<h3>Ulubione zakładki</h3><p>2026 // 2027 // 2028 // DALEJ</p>')};$("gwBtn").onclick=()=>{codeStep("gw");toast("GOTOWE")};
$("minBtn").onclick=()=>$("page").classList.toggle("minimized");$("maxBtn").onclick=()=>$("desktop").classList.toggle("maxed");$("closeBtn").onclick=()=>openModal("SYSTEM",'<h3>Nie można zamknąć programu.</h3><p>Trwa indeksowanie premier.</p>');
$("appIcon").ondblclick=przemoPopup;$("tab2027").addEventListener("contextmenu",e=>{e.preventDefault();galleryWarning()});
$("buildText").addEventListener("mouseenter",()=>{buildTimer=setTimeout(sixtySevenEgg,6700)});$("buildText").addEventListener("mouseleave",()=>clearTimeout(buildTimer));
$("helpBtn").addEventListener("pointerdown",()=>{helpLongFired=false;clearTimeout(helpTimer);helpTimer=setTimeout(()=>{helpLongFired=true;monitorEgg()},3200)});["pointerup","pointerleave","pointercancel"].forEach(ev=>$("helpBtn").addEventListener(ev,()=>clearTimeout(helpTimer)));
document.querySelectorAll("[data-menu]").forEach(btn=>btn.onclick=()=>{const m=btn.dataset.menu;if(m==="help"&&helpLongFired){helpLongFired=false;return}if(m==="file")openModal("PLIK",'<h3>Brak otwartych plików</h3><p>Archiwum działa w trybie tylko do odczytu.</p>');if(m==="edit")openModal("EDYCJA",'<h3>Cofnij</h3><p>Brak operacji do cofnięcia.</p>');if(m==="view"){document.body.classList.toggle("party-mode");toast("ZMIENIONO WIDOK")};if(m==="fav")openModal("ULUBIONE",'<h3>Skróty</h3><p>2026 // 2027 // 2028 // DALEJ</p>');if(m==="help")openModal("POMOC",'<h3>Gry jednak wychodzą</h3><p>Wersja 0.15. Wszystko działa. Prawdopodobnie.</p>')});
document.querySelectorAll('.game-card[data-title="Grand Theft Auto VI"]').forEach(card=>card.addEventListener("contextmenu",e=>{e.preventDefault();contextTitle=card.dataset.title;const menu=$("contextMenu");menu.style.left=Math.min(e.clientX,window.innerWidth-205)+"px";menu.style.top=Math.min(e.clientY,window.innerHeight-115)+"px";menu.classList.add("open")}));
document.addEventListener("click",e=>{if(!e.target.closest("#contextMenu"))$("contextMenu").classList.remove("open")});
$("contextMenu").addEventListener("click",e=>{const b=e.target.closest("button");if(!b)return;$("contextMenu").classList.remove("open");if(b.dataset.context==="open")toast("Otwieranie: "+contextTitle);if(b.dataset.context==="copy")navigator.clipboard?.writeText(contextTitle);if(b.dataset.context==="pizza")surprisePhoto("PIZZA.EXE","sprzedaj mi te pizze")});
let typed="";function norm(s){return s.normalize("NFD").replace(/[\u0300-\u036f]/g,"").toLowerCase().replace(/[^a-z0-9]/g,"")}
document.addEventListener("keypress",e=>{if(e.target.matches("input,textarea"))return;typed=(typed+e.key).slice(-40);const n=norm(typed);if(n.endsWith("toaleta")){typed="";openTenant()}else if(n.endsWith("gryniewychodza")){typed="";cancelGames()}else if(n.endsWith("fortnite")){typed="";document.body.classList.toggle("party-mode");dabEgg()}else if(n.endsWith("dabonyourmom69")){typed="";dabEgg()}else if(n.endsWith("szczupak511")){typed="";surprisePhoto("RZADKIE_RYBKI.EXE","czy masz rzadkie rybki?")}else if(n.endsWith("shotyprzema")){typed="";przemoPopup()}});
'''

s = s[:start] + new_tail + s[end:]
path.write_text(s, encoding="utf-8")
print("BUILD_015 patch applied")
