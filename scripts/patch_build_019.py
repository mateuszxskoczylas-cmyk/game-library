from pathlib import Path

path = Path('index.html')
s = path.read_text(encoding='utf-8')

if 'BUILD_018' not in s:
    raise SystemExit('Expected BUILD_018')

def rep(old, new):
    global s
    if old not in s:
        raise SystemExit('Missing fragment: ' + old[:120])
    s = s.replace(old, new, 1)

rep('.hero-layout{display:flex;align-items:flex-start;justify-content:space-between;gap:20px}.hero-card{background:rgba(255,255,255,.92);border:2px solid var(--ink);padding:18px;max-width:880px;flex:1;box-shadow:6px 6px 0 var(--purple)}.tga-window{width:255px;flex:0 0 255px;', '.hero-layout{display:flex;align-items:stretch;justify-content:space-between;gap:12px}.hero-card{background:rgba(255,255,255,.92);border:2px solid var(--ink);padding:14px;max-width:760px;flex:1 1 520px;box-shadow:5px 5px 0 var(--purple)}.hero-side{display:grid;grid-template-columns:repeat(2,205px);gap:10px;align-items:stretch}.tga-window,.next-window{width:205px;min-height:132px;')
rep('.tga-titlebar{display:flex;align-items:center;gap:6px;padding:4px 6px;background:linear-gradient(90deg,#0d7dad,var(--sky));color:#fff;font:700 10px "Courier New",monospace}', '.tga-titlebar,.next-titlebar{display:flex;align-items:center;gap:6px;padding:4px 6px;background:linear-gradient(90deg,#0d7dad,var(--sky));color:#fff;font:700 9px "Courier New",monospace}.next-titlebar{background:linear-gradient(90deg,var(--purple),var(--pink))}')
rep('.tga-titlebar .app-icon{flex:0 0 17px}.tga-body{padding:10px 10px 11px;text-align:center;background:#ececec;border-top:1px solid #fff}', '.tga-titlebar .app-icon,.next-titlebar .app-icon{flex:0 0 17px}.tga-body,.next-body{padding:8px 9px 9px;text-align:center;background:#ececec;border-top:1px solid #fff}.next-body{display:flex;min-height:101px;flex-direction:column;justify-content:center}.next-game{font:900 13px Georgia,"Times New Roman",serif;line-height:1.05;color:#111}.next-date{margin-top:6px;font:700 10px "Courier New",monospace;color:var(--purple)}.next-days{display:inline-block;align-self:center;margin-top:7px;padding:3px 6px;background:var(--yellow);border:1px solid #111;font:900 9px "Courier New",monospace}')
rep('.tga-logo{display:block;width:88px;height:68px;object-fit:contain;margin:0 auto 7px}', '.tga-logo{display:block;width:68px;height:48px;object-fit:contain;margin:0 auto 5px}')
rep('.tga-date{margin:3px 0 2px;font:900 20px Georgia,"Times New Roman",serif;color:#111}', '.tga-date{margin:3px 0 2px;font:900 17px Georgia,"Times New Roman",serif;color:#111}')
rep('.released-ribbon{position:absolute;', '.new-ribbon{position:absolute;top:8px;left:-31px;width:112px;z-index:5;transform:rotate(-37deg);background:var(--pink);color:#fff;border-top:2px solid #ffb9dd;border-bottom:2px solid #75003f;box-shadow:0 2px 0 #111;text-align:center;padding:4px 0;font:900 9px "Courier New",monospace;letter-spacing:.12em}.released-ribbon{position:absolute;')
rep('.node{font:8px "Courier New",monospace;color:#666}', '.source-badge{font:900 7px "Courier New",monospace;padding:3px 4px;border:1px solid #111;background:#d8d8d8;color:#111}.source-badge.steam{background:#b9d7ef}.source-badge.ps{background:#c6b7ff}.source-badge.www{background:#baf2df}.node{font:8px "Courier New",monospace;color:#666}')
rep('@media(max-width:900px){.hero-layout{flex-wrap:wrap}.tga-window{width:min(100%,320px);flex-basis:320px;margin-left:auto}}', '@media(max-width:1100px){.hero-layout{flex-wrap:wrap}.hero-card{max-width:none;flex-basis:100%}.hero-side{width:100%;grid-template-columns:repeat(2,minmax(0,1fr))}.tga-window,.next-window{width:auto}}@media(max-width:700px){.hero-side{grid-template-columns:repeat(2,minmax(0,1fr))}}@media(max-width:460px){.hero-side{grid-template-columns:1fr}}')

rep('<div class="page" id="page"><section class="hero"><div class="hero-layout"><div class="hero-card"><div class="kicker">// ARCHIWUM_GIER.EXE</div><h1>Nadchodzące premiery</h1><p>Strona zaprojektowana po to, żeby udowodnić, że gry jednak wychodzą — i czasem jest ich naprawdę sporo.</p></div><aside class="tga-window" aria-label="The Game Awards"><div class="tga-titlebar"><span class="app-icon">★</span><span>THE_GAME_AWARDS.EXE</span></div><div class="tga-body"><img class="tga-logo" src="https://upload.wikimedia.org/wikipedia/commons/e/e8/The_Game_Awards_Logo_2024.svg" alt="The Game Awards"><div class="tga-kicker">GAME OF THE YEAR</div><div class="tga-date">10 GRUDNIA</div></div></aside></div></section>', '<div class="page" id="page"><section class="hero"><div class="hero-layout"><div class="hero-card"><div class="kicker">// ARCHIWUM_GIER.EXE</div><h1>Nadchodzące premiery</h1><p>Strona zaprojektowana po to, żeby udowodnić, że gry jednak wychodzą — i czasem jest ich naprawdę sporo.</p></div><div class="hero-side"><aside class="next-window" aria-label="Następna premiera"><div class="next-titlebar"><span class="app-icon">→</span><span>NASTEPNA_PREMIERA.EXE</span></div><div class="next-body"><div class="next-game" id="nextGameTitle">ŁADOWANIE...</div><div class="next-date" id="nextGameDate">--.--.----</div><div class="next-days" id="nextGameDays">...</div></div></aside><aside class="tga-window" aria-label="The Game Awards"><div class="tga-titlebar"><span class="app-icon">★</span><span>THE_GAME_AWARDS.EXE</span></div><div class="tga-body"><img class="tga-logo" src="https://upload.wikimedia.org/wikipedia/commons/e/e8/The_Game_Awards_Logo_2024.svg" alt="The Game Awards"><div class="tga-kicker">GAME OF THE YEAR</div><div class="tga-date">10 GRUDNIA</div></div></aside></div></div></section>')

art = {
'Black Myth: Zhong Kui':'https://gaming-cdn.com/images/news/articles/21386/cover/1000x563/black-myth-zhong-kui-is-back-with-15-minutes-of-gameplay-cover6a86b353a58ac.jpg',
'Tomb Raider: Catalyst':'https://assetsio.gnwcdn.com/tomb-raider-catalyst-headline-trailer.jpg?width=690&quality=85&format=jpg&dpr=3&auto=webp',
'The Witcher Remake':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT0t03n0-pbJR4irWrmx_npMqsW50XwAR5HSvP-1X5VIBDWFoCvbxDEtZU&s=10',
"Marvel's Iron Man":'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTPAFmmDobYZWMh_Kgu-LlCqld_TxVPOYYN7azC0sYradF52enW4ABV1jg&s=10',
'Star Wars: Knights of the Old Republic — Remake':'https://cdaction.pl/wp-content/uploads/2025/12/kotor-1260x709.jpg',
'God of War Trilogy Remake':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSvGAAfTlKDEc4yRuQ2Qu1Gz-abQvjfsP0khkRB0FSLS6yniH6_rIcrq_9x&s=10',
"Assassin's Creed: Codename Invictus":'https://static.wikia.nocookie.net/assassinscreed/images/4/4f/AC_Invictus.jpg/revision/latest?cb=20230720174544&path-prefix=fr',
"Assassin's Creed: Codename Hexe":'https://static.wikia.nocookie.net/assassinscreed/images/7/73/Hexe_logo.jpg/revision/latest?cb=20220911224333&path-prefix=pl',
'Middle-earth — Warhorse project':'https://www.reddit.com/media?url=https%3A%2F%2Fpreview.redd.it%2Fwarhorses-new-rpg-game-map-highest-resolution-v0-p4hhtvb7ej2h1.jpeg%3Fwidth%3D640%26crop%3Dsmart%26auto%3Dwebp%26s%3D9f34d047f58b268ba54f3ba027d443cc0a4d33b3'
}
for title, url in art.items():
    old = f'{{title:"{title}",'
    pos = s.find(old)
    if pos < 0:
        raise SystemExit('Missing title: ' + title)
    end = s.find('},', pos)
    if end < 0:
        end = s.find('}\n', pos)
    frag = s[pos:end+1]
    if 'textCover:true' not in frag:
        raise SystemExit('Expected textCover for: ' + title)
    newfrag = frag.replace('textCover:true', f'image:"{url}"')
    s = s[:pos] + newfrag + s[end+1:]

rep('function gameStoreUrl(g){if(g.storeUrl)return g.storeUrl;if(g.steamAppId)return `https://store.steampowered.com/app/${g.steamAppId}/`;const m=String(g.image||"").match(/\\/steam\\/apps\\/(\\d+)\\//);return m?`https://store.steampowered.com/app/${m[1]}/`:""}\nfunction card(g,i){const released=isReleased(g);const status=released?"WYDANA":g.status;const u=status==="NIEZAPOWIEDZIANE"?" unannounced":"";const ribbon=released?\'<span class="released-ribbon">WYDANA</span>\':"";const url=gameStoreUrl(g);const linkClass=url?" store-link":"";const linkData=url?` data-store-url="${esc(url)}" title="Otwórz stronę gry"`:"";return `<article class="game-card${released?" released":""}${linkClass}" data-title="${esc(g.title)}"${linkData}><div class="poster-wrap">${poster(g)}${ribbon}</div><div class="card-body"><div class="studio">${esc(g.studio)}</div><div class="game-title">${esc(g.title)}</div><div class="release"><b>&gt;</b> ${esc(g.date)}</div><div class="badges"><span class="badge${u}">${esc(status)}</span><span class="node">POZYCJA_${String(i+1).padStart(2,"0")}</span></div></div></article>`}', 'function gameStoreUrl(g){if(g.storeUrl)return g.storeUrl;if(g.steamAppId)return `https://store.steampowered.com/app/${g.steamAppId}/`;const m=String(g.image||"").match(/\\/steam\\/apps\\/(\\d+)\\//);return m?`https://store.steampowered.com/app/${m[1]}/`:""}\nfunction storeSource(g){const u=gameStoreUrl(g);if(/playstation\\.com/i.test(u))return {label:"PS",cls:"ps"};if(/steampowered\\.com/i.test(u))return {label:"STEAM",cls:"steam"};if(u)return {label:"WWW",cls:"www"};return null}\nfunction card(g,i){const released=isReleased(g);const status=released?"WYDANA":g.status;const u=status==="NIEZAPOWIEDZIANE"?" unannounced":"";const releasedRibbon=released?\'<span class="released-ribbon">WYDANA</span>\':"";const newRibbon=g.isNew?\'<span class="new-ribbon">NOWE</span>\':"";const url=gameStoreUrl(g);const src=storeSource(g);const sourceBadge=src?`<span class="source-badge ${src.cls}">${src.label}</span>`:"";const linkClass=url?" store-link":"";const linkData=url?` data-store-url="${esc(url)}" title="Otwórz stronę gry"`:"";return `<article class="game-card${released?" released":""}${linkClass}" data-title="${esc(g.title)}"${linkData}><div class="poster-wrap">${poster(g)}${newRibbon}${releasedRibbon}</div><div class="card-body"><div class="studio">${esc(g.studio)}</div><div class="game-title">${esc(g.title)}</div><div class="release"><b>&gt;</b> ${esc(g.date)}</div><div class="badges"><span class="badge${u}">${esc(status)}</span>${sourceBadge}<span class="node">POZYCJA_${String(i+1).padStart(2,"0")}</span></div></div></article>`}')

rep('document.getElementById("app").innerHTML=releaseSections.map(section).join("");\ndocument.querySelectorAll(".game-card[data-store-url]")', 'document.getElementById("app").innerHTML=releaseSections.map(section).join("");\nreleaseSections.forEach(b=>{const a=document.querySelector(`.year-tabs a[href="#${b.id}"]`);if(a)a.textContent=`${b.label} [${b.games.length}]`});\nfunction updateNextRelease(){const today=localDateKey();const games=releaseSections.flatMap(b=>b.games).filter(g=>/^\\d{4}-\\d{2}-\\d{2}$/.test(g.sortDate||"")&&g.sortDate>=today).sort((a,b)=>a.sortDate.localeCompare(b.sortDate));const g=games[0];if(!g){document.getElementById("nextGameTitle").textContent="BRAK DAT";document.getElementById("nextGameDate").textContent="TBA";document.getElementById("nextGameDays").textContent="--";return}const start=new Date(today+"T00:00:00");const target=new Date(g.sortDate+"T00:00:00");const days=Math.round((target-start)/86400000);document.getElementById("nextGameTitle").textContent=g.title;document.getElementById("nextGameDate").textContent=g.date;document.getElementById("nextGameDays").textContent=days===0?"DZISIAJ":days===1?"ZA 1 DZIEŃ":`ZA ${days} DNI`}updateNextRelease();\ndocument.querySelectorAll(".game-card[data-store-url]")')

rep('BUILD_018','BUILD_019')
rep('Wersja 0.18','Wersja 0.19')

path.write_text(s, encoding='utf-8')
