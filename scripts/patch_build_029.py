from pathlib import Path

path = Path('index.html')
s = path.read_text(encoding='utf-8')

s = s.replace('BUILD_028', 'BUILD_029')
s = s.replace('Wersja 0.28.', 'Wersja 0.29.')
s = s.replace('OBECNE OKNO PREMIER // SORTOWANIE: NAJBLIŻSZE → PÓŹNIEJSZE', 'OBECNE OKNO PREMIER // NADCHODZĄCE: NAJBLIŻSZE → PÓŹNIEJSZE // WYDANE NA KOŃCU')

old = '''function section(block,index){const games=[...block.games].sort((a,b)=>block.id==="beyond"?((a.studio||"").localeCompare(b.studio||"","pl",{sensitivity:"base"})||(a.title||"").localeCompare(b.title||"","pl",{sensitivity:"base"})):(a.sortDate||"").localeCompare(b.sortDate||""));return `<section class="window release-window" id="${block.id}"><div class="titlebar release-titlebar"><div class="title-left"><span class="app-icon">${String(index+1).padStart(2,"0")}</span><span>${esc(block.label)} // PREMIERY <span class="section-count">[${games.length}]</span></span></div></div><div class="release-inner"><p class="section-note">&gt; ${esc(block.note)}</p><div class="rail">${games.map(card).join("")}</div></div></section>`}'''
new = '''function section(block,index){const games=[...block.games].sort((a,b)=>{if(block.id==="beyond")return (a.studio||"").localeCompare(b.studio||"","pl",{sensitivity:"base"})||(a.title||"").localeCompare(b.title||"","pl",{sensitivity:"base"});const aReleased=isReleased(a),bReleased=isReleased(b);if(aReleased!==bReleased)return aReleased?1:-1;return (a.sortDate||"").localeCompare(b.sortDate||"")});return `<section class="window release-window" id="${block.id}"><div class="titlebar release-titlebar"><div class="title-left"><span class="app-icon">${String(index+1).padStart(2,"0")}</span><span>${esc(block.label)} // PREMIERY <span class="section-count">[${games.length}]</span></span></div></div><div class="release-inner"><p class="section-note">&gt; ${esc(block.note)}</p><div class="rail">${games.map(card).join("")}</div></div></section>`}'''
if old not in s:
    raise SystemExit('section sorter pattern not found')
s = s.replace(old, new, 1)

path.write_text(s, encoding='utf-8')
