from pathlib import Path

path = Path("index.html")
s = path.read_text(encoding="utf-8")

if "BUILD_015" not in s:
    raise SystemExit("Expected BUILD_015")


def rep(old: str, new: str) -> None:
    global s
    if old not in s:
        raise SystemExit(f"Missing expected fragment: {old[:160]!r}")
    s = s.replace(old, new, 1)


rep(
    'transition:.18s}.poster-wrap{',
    'transition:.18s}.game-card.store-link{cursor:pointer}.game-card.store-link:hover{transform:translateY(-2px);box-shadow:4px 4px 0 rgba(75,42,130,.28)}.poster-wrap{'
)

rep(
    '{title:"Marvel\'s Wolverine",studio:"Insomniac Games",date:"15.09.2026",sortDate:"2026-09-15",status:"PS5",image:"https://cdn2.steamgriddb.com/grid/5a91fdd6a6ec33bf43e806a118966e8f.png"}',
    '{title:"Marvel\'s Wolverine",studio:"Insomniac Games",date:"15.09.2026",sortDate:"2026-09-15",status:"PS5",image:"https://cdn2.steamgriddb.com/grid/5a91fdd6a6ec33bf43e806a118966e8f.png",storeUrl:"https://store.playstation.com/pl-pl/product/UP9000-PPSA03671_00-MARVELSWOLVERINE"}'
)

rep(
    '{title:"Resident Evil Veronica",studio:"CAPCOM",date:"2027",sortDate:"2027-12-31",status:"ZAPOWIEDZIANE",steamAppId:"4824610",image:"https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/4824610/249c95eeaf9a26ffc90b6a55f3eda7fc72b1545c/library_capsule.jpg"}',
    '{title:"Resident Evil Veronica",studio:"CAPCOM",date:"2027",sortDate:"2027-12-31",status:"ZAPOWIEDZIANE",steamAppId:"4824610",image:"https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/4824610/249c95eeaf9a26ffc90b6a55f3eda7fc72b1545c/library_capsule.jpg",storeUrl:"https://store.steampowered.com/app/4824610/Resident_Evil_Veronica/"}'
)

old_card = '''function isReleased(g){return /^\\d{4}-\\d{2}-\\d{2}$/.test(g.sortDate||"")&&g.sortDate<localDateKey()}
function card(g,i){const released=isReleased(g);const status=released?"WYDANA":g.status;const u=status==="NIEZAPOWIEDZIANE"?" unannounced":"";const ribbon=released?'<span class="released-ribbon">WYDANA</span>':"";return `<article class="game-card${released?" released":""}" data-title="${esc(g.title)}"><div class="poster-wrap">${poster(g)}${ribbon}</div><div class="card-body"><div class="studio">${esc(g.studio)}</div><div class="game-title">${esc(g.title)}</div><div class="release"><b>&gt;</b> ${esc(g.date)}</div><div class="badges"><span class="badge${u}">${esc(status)}</span><span class="node">POZYCJA_${String(i+1).padStart(2,"0")}</span></div></div></article>`}'''
new_card = '''function isReleased(g){return /^\\d{4}-\\d{2}-\\d{2}$/.test(g.sortDate||"")&&g.sortDate<localDateKey()}
function gameStoreUrl(g){if(g.storeUrl)return g.storeUrl;if(g.steamAppId)return `https://store.steampowered.com/app/${g.steamAppId}/`;const m=String(g.image||"").match(/\\/steam\\/apps\\/(\\d+)\\//);return m?`https://store.steampowered.com/app/${m[1]}/`:""}
function card(g,i){const released=isReleased(g);const status=released?"WYDANA":g.status;const u=status==="NIEZAPOWIEDZIANE"?" unannounced":"";const ribbon=released?'<span class="released-ribbon">WYDANA</span>':"";const url=gameStoreUrl(g);const linkClass=url?" store-link":"";const linkData=url?` data-store-url="${esc(url)}" title="Otwórz stronę gry"`:"";return `<article class="game-card${released?" released":""}${linkClass}" data-title="${esc(g.title)}"${linkData}><div class="poster-wrap">${poster(g)}${ribbon}</div><div class="card-body"><div class="studio">${esc(g.studio)}</div><div class="game-title">${esc(g.title)}</div><div class="release"><b>&gt;</b> ${esc(g.date)}</div><div class="badges"><span class="badge${u}">${esc(status)}</span><span class="node">POZYCJA_${String(i+1).padStart(2,"0")}</span></div></div></article>`}'''
rep(old_card, new_card)

rep(
    'document.getElementById("app").innerHTML=releaseSections.map(section).join("");',
    'document.getElementById("app").innerHTML=releaseSections.map(section).join("");\ndocument.querySelectorAll(".game-card[data-store-url]").forEach(card=>card.addEventListener("click",()=>window.open(card.dataset.storeUrl,"_blank","noopener,noreferrer")));'
)

rep('BUILD_015', 'BUILD_016')
rep('Wersja 0.15.', 'Wersja 0.16.')

path.write_text(s, encoding="utf-8")
print("Patched BUILD_016")
