from pathlib import Path
import re

path = Path('index.html')
s = path.read_text(encoding='utf-8')

old_menu_css = '.menubar{padding:5px 8px;background:#d4d4d4;border-bottom:1px solid #777;font-size:12px}.menubar button{border:0;background:transparent;padding:0;margin-right:18px;text-decoration:underline;text-underline-offset:2px;cursor:pointer;color:#111}'
new_menu_css = '.menubar{padding:4px 8px;background:linear-gradient(#eeeeee,#cfcfe0);border-bottom:1px solid #777;font-size:12px;position:relative;z-index:80}.menubar button{border:0;background:transparent;padding:2px 3px;margin-right:18px;text-decoration:underline;text-underline-offset:2px;cursor:pointer;color:#111}.menu-drop{display:inline-block;position:relative;margin-right:18px}.menu-label{display:inline-block;padding:2px 3px;text-decoration:underline;text-underline-offset:2px;cursor:default;color:#111}.menu-drop:hover .menu-label{background:#7451c7;color:#fff;text-decoration:none}.menu-panel{display:none;position:absolute;left:-3px;top:20px;min-width:178px;padding:4px;background:linear-gradient(135deg,#f8f5ff,#d9eaff 62%,#f4d8ff);border-top:2px solid #fff;border-left:2px solid #fff;border-right:2px solid #56506c;border-bottom:2px solid #56506c;box-shadow:4px 4px 0 rgba(75,42,130,.28);z-index:200}.menu-drop:hover .menu-panel{display:block}.menu-entry{padding:5px 22px 5px 8px;white-space:nowrap;color:#26213a;font:11px "Tahoma","MS Sans Serif",sans-serif;pointer-events:none}.menu-entry:before{content:"◇";display:inline-block;width:16px;color:#a400d8}.menu-sep{height:1px;background:#8d86a0;border-bottom:1px solid #fff;margin:3px 2px}'
assert old_menu_css in s
s = s.replace(old_menu_css, new_menu_css, 1)

pattern = re.compile(r'\.desktop-icons\{[^}]*\}\.desktop-mode \.desktop-icons\{[^}]*\}\.desktop-mode #mainWindow \.menubar,\.desktop-mode #mainWindow \.toolbar,\.desktop-mode #mainWindow \.address-row,\.desktop-mode #mainWindow \.page\{[^}]*\}\.desktop-shortcut\{[^}]*\}\.desktop-glyph\{[^}]*\}\.desktop-glyph\.computer:before\{[^}]*\}\.desktop-glyph\.computer:after\{[^}]*\}\.desktop-glyph\.trash:before\{[^}]*\}\.desktop-glyph\.trash:after\{[^}]*\}')
new_desktop_css = '.desktop-icons{display:none;position:fixed;left:28px;top:74px;z-index:40;grid-template-columns:92px;gap:24px}.desktop-mode .desktop-icons{display:grid}.desktop-mode #mainWindow .menubar,.desktop-mode #mainWindow .toolbar,.desktop-mode #mainWindow .address-row,.desktop-mode #mainWindow .page{display:none}.desktop-shortcut{width:92px;text-align:center;color:#fff;font:700 10px/1.15 "Tahoma","MS Sans Serif",Arial,sans-serif;text-shadow:1px 1px 0 #4b2a82,0 0 4px #7a41ce;letter-spacing:.02em;user-select:none;pointer-events:none}.desktop-glyph{width:58px;height:58px;margin:0 auto 7px;position:relative;filter:drop-shadow(3px 3px 0 rgba(75,42,130,.5))}.desktop-glyph.computer:before{content:"";position:absolute;left:5px;top:7px;width:48px;height:38px;background:linear-gradient(145deg,#d7eeff 0 20%,#70d7f3 21% 52%,#9d78ef 53% 100%);border:2px solid #4d2a83;clip-path:polygon(9% 0,100% 0,100% 82%,82% 82%,82% 100%,21% 100%,21% 82%,0 82%,0 18%);box-shadow:inset 2px 2px 0 #fff,inset -2px -2px 0 #6845a5}.desktop-glyph.computer:after{content:"☺";position:absolute;left:15px;top:13px;width:29px;height:22px;display:grid;place-items:center;background:linear-gradient(#fff98f,#ffd53d);color:#6b2fb1;border:2px solid #432268;font:900 16px Arial,sans-serif;box-shadow:inset 1px 1px 0 #fff}.desktop-glyph.trash:before{content:"";position:absolute;left:14px;top:17px;width:31px;height:34px;background:linear-gradient(135deg,rgba(255,255,255,.95),#a8e8ff 45%,#c890ff);border:2px solid #56337e;clip-path:polygon(6% 0,94% 0,84% 100%,16% 100%);box-shadow:inset 4px 0 0 rgba(255,255,255,.6),inset -4px 0 0 rgba(112,66,169,.28)}.desktop-glyph.trash:after{content:"✦";position:absolute;left:9px;top:8px;width:41px;height:11px;background:linear-gradient(90deg,#ff8bd4,#d5a3ff,#8edcff);color:#fff;border:2px solid #56337e;display:grid;place-items:center;font:900 9px Arial,sans-serif;box-shadow:inset 1px 1px 0 #fff}'
s, n = pattern.subn(new_desktop_css, s, count=1)
assert n == 1

s = s.replace('.tool.brandmark{background:var(--teal);color:var(--purple);font-weight:900}', '.tool.brandmark{background:var(--teal);color:var(--purple);font-weight:900}.eye-tool{position:relative;overflow:hidden}.eye-pyramid{position:relative;display:block;width:25px;height:21px;font:900 24px/18px Georgia,serif;color:#f0c94e;text-shadow:1px 1px 0 #4b2a82}.eye-pyramid b{position:absolute;left:8px;top:7px;font:900 8px/8px Arial,sans-serif;color:#4b2a82;text-shadow:0 0 1px #fff}.section-count{font:700 10px "Courier New",monospace;color:var(--yellow);margin-left:6px}', 1)

s = s.replace('.source-badge{font:900 7px "Courier New",monospace;padding:3px 4px;border:1px solid #111;background:#d8d8d8;color:#111}.source-badge.steam{background:#b9d7ef}.source-badge.ps{background:#c6b7ff}.source-badge.www{background:#baf2df}', '', 1)

old_menu_html = '<div class="menubar"><button data-menu="file">Plik</button><button data-menu="edit">Edycja</button><button data-menu="view">Widok</button><button data-menu="fav">Ulubione</button><button data-menu="help" id="helpBtn">Pomoc</button></div>'
new_menu_html = '<div class="menubar"><div class="menu-drop"><span class="menu-label">Plik</span><div class="menu-panel"><div class="menu-entry">Nowy</div><div class="menu-entry">Otwórz...</div><div class="menu-entry">Właściwości</div><div class="menu-sep"></div><div class="menu-entry">Zakończ</div></div></div><div class="menu-drop"><span class="menu-label">Edycja</span><div class="menu-panel"><div class="menu-entry">Cofnij</div><div class="menu-sep"></div><div class="menu-entry">Kopiuj</div><div class="menu-entry">Znajdź...</div></div></div><button data-menu="view">Widok</button><div class="menu-drop"><span class="menu-label">Ulubione</span><div class="menu-panel"><div class="menu-entry">Premiery 2026</div><div class="menu-entry">Premiery 2027</div><div class="menu-entry">Premiery 2028</div><div class="menu-entry">Dalej</div></div></div><button data-menu="help" id="helpBtn">Pomoc</button></div>'
assert old_menu_html in s
s = s.replace(old_menu_html, new_menu_html, 1)

old_toolbar = '<div class="toolbar"><button class="tool" id="backBtn">←</button><button class="tool" id="forwardBtn">→</button><button class="tool" id="homeBtn">⌂</button><button class="tool" id="starBtn">★</button><button class="tool brandmark" id="gwBtn">GW</button></div>'
new_toolbar = '<div class="toolbar"><button class="tool" id="backBtn">←</button><button class="tool" id="forwardBtn">→</button><button class="tool eye-tool" id="homeBtn" aria-label="Piramida z okiem"><span class="eye-pyramid">△<b>◉</b></span></button><button class="tool" id="starBtn">★</button><button class="tool brandmark" id="gwBtn">GW</button></div>'
assert old_toolbar in s
s = s.replace(old_toolbar, new_toolbar, 1)

s = s.replace('http://localhost/przemo-nie-ma-racji/2026idalej', 'http://localhost/gry-jednak-wychodza/', 1)
s = s.replace('{title:"Marvel\'s Wolverine",studio:"Insomniac Games",date:"15.09.2026",sortDate:"2026-09-15",status:"PS5"', '{title:"Marvel\'s Wolverine",studio:"Insomniac Games",date:"15.09.2026",sortDate:"2026-09-15",status:"POTWIERDZONE"', 1)

old_quotes = re.search(r'const quotes=\[.*?\];', s, flags=re.S)
assert old_quotes
new_quotes = 'const quotes=["sprzedaj mi ten długopis","znowu gram na ten yeahbunny deck","jakie gówno xd","tonights the night","ogien stary","pieniądz lubi cisze","czy masz rzadkie rybki?","shoty przema","wybieram mafie","polscy raperzy w srebrze i cyrkonii","galeria młynska zostaje wysadzana w 2027 roku","kupa stolec ale sztos","no oczywiscie pelen naladowany pozytywnej energii","fortnite","gry nie wychodzą","a jaka wymóweczka dziś?","ai slop","przemo jest wygenerowany komputerowo","*zaczyna dabować*","dabonyourmom69","szczupak511?","pan dyrektor podpisał nieprawdę","czy ten obiekt jest monitorowany?","sprzedaj mi te pizze"];'
s = s[:old_quotes.start()] + new_quotes + s[old_quotes.end():]

old_store_source = 'function storeSource(g){const u=gameStoreUrl(g);if(/playstation\\.com/i.test(u))return {label:"PS",cls:"ps"};if(/steampowered\\.com/i.test(u))return {label:"STEAM",cls:"steam"};if(u)return {label:"WWW",cls:"www"};return null}\n'
assert old_store_source in s
s = s.replace(old_store_source, '', 1)

card_pattern = re.compile(r'function card\(g,i\)\{.*?\}\nfunction section', re.S)
new_card = 'function card(g,i){const released=isReleased(g);const status=released?"WYDANA":g.status==="POTWIERDZONE"?"WYCHODZI":g.status;const u=status==="NIEZAPOWIEDZIANE"?" unannounced":"";const releasedRibbon=released?\'<span class="released-ribbon">WYDANA</span>\':"";const newRibbon=g.isNew?\'<span class="new-ribbon">NOWE</span>\':"";const url=gameStoreUrl(g);const linkClass=url?" store-link":"";const linkData=url?` data-store-url="${esc(url)}" title="Otwórz stronę gry"`:"";return `<article class="game-card${released?" released":""}${linkClass}" data-title="${esc(g.title)}"${linkData}><div class="poster-wrap">${poster(g)}${newRibbon}${releasedRibbon}</div><div class="card-body"><div class="studio">${esc(g.studio)}</div><div class="game-title">${esc(g.title)}</div><div class="release"><b>&gt;</b> ${esc(g.date)}</div><div class="badges"><span class="badge${u}">${esc(status)}</span><span class="node">POZYCJA_${String(i+1).padStart(2,"0")}</span></div></div></article>`}\nfunction section'
s, n = card_pattern.subn(new_card, s, count=1)
assert n == 1

section_pattern = re.compile(r'function section\(block,index\)\{.*?\}\ndocument\.getElementById\("app"\)', re.S)
new_section = 'function section(block,index){const games=[...block.games].sort((a,b)=>block.id==="beyond"?((a.studio||"").localeCompare(b.studio||"","pl",{sensitivity:"base"})||(a.title||"").localeCompare(b.title||"","pl",{sensitivity:"base"})):(a.sortDate||"").localeCompare(b.sortDate||""));return `<section class="window release-window" id="${block.id}"><div class="titlebar release-titlebar"><div class="title-left"><span class="app-icon">${String(index+1).padStart(2,"0")}</span><span>${esc(block.label)} // PREMIERY <span class="section-count">[${games.length}]</span></span></div></div><div class="release-inner"><p class="section-note">&gt; ${esc(block.note)}</p><div class="rail">${games.map(card).join("")}</div></div></section>`}\ndocument.getElementById("app")'
s, n = section_pattern.subn(new_section, s, count=1)
assert n == 1

s = re.sub(r'\nreleaseSections\.forEach\(b=>\{const a=document\.querySelector\(`\.year-tabs a\[href="#\$\{b\.id\}"\]`\);if\(a\)a\.textContent=`\$\{b\.label\} \[\$\{b\.games\.length\}\]`\}\);', '', s, count=1)

s = s.replace('$("homeBtn").onclick=()=>window.scrollTo({top:0,behavior:"smooth"});', '', 1)

menu_js_pattern = re.compile(r'document\.querySelectorAll\("\[data-menu\]"\)\.forEach\(btn=>btn\.onclick=\(\)=>\{.*?\}\);', re.S)
new_menu_js = 'document.querySelectorAll("[data-menu]").forEach(btn=>btn.onclick=()=>{const m=btn.dataset.menu;if(m==="help"&&helpLongFired){helpLongFired=false;return}if(m==="view"){document.body.classList.toggle("party-mode");toast("ZMIENIONO WIDOK")};if(m==="help")openModal("POMOC",\'<h3>Gry jednak wychodzą</h3><p>Wersja 0.21. Wszystko działa. Prawdopodobnie.</p>\')});'
s, n = menu_js_pattern.subn(new_menu_js, s, count=1)
assert n == 1

assert 'BUILD_020' in s
s = s.replace('BUILD_020', 'BUILD_021', 1)

path.write_text(s, encoding='utf-8')
