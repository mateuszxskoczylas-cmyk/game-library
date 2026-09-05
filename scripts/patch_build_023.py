from pathlib import Path

path = Path('index.html')
s = path.read_text(encoding='utf-8')

# Night mode readability + desktop anchoring + clickable view menu actions + help diagnostics.
s = s.replace(
    '.night-mode .desktop-shortcut{color:#f7f6ff;text-shadow:1px 1px 0 #12152d,0 0 5px #b65cff}.party-mode',
    '.night-mode .desktop-shortcut{color:#f7f6ff;text-shadow:1px 1px 0 #12152d,0 0 5px #b65cff}.night-mode .badge{background:#fff07a;color:#2c174d;border-color:#f4f0ff}.night-mode .badge.unannounced{background:#ff9fd5;color:#2b0b28}.night-mode .released-ribbon{background:#fff07a;color:#3d2266}.night-mode .new-ribbon{background:#d72a92;color:#fff}.night-mode .modal-body,.night-mode .modal-body pre,.night-mode .photo-caption,.night-mode .screen-warning,.night-mode .loading-box,.night-mode .dialup-box{color:#17122b}.menu-entry.menu-action{pointer-events:auto;cursor:pointer}.menu-entry.menu-action:hover{background:#7451c7;color:#fff}.help-secret{margin-top:14px;background:#d8d8e6;border-top:2px solid #707080;border-left:2px solid #707080;border-right:2px solid #fff;border-bottom:2px solid #fff;padding:6px 8px}.help-secret summary{cursor:pointer;font:700 11px "Courier New",monospace;color:#4b2a82}.help-secret div{margin-top:7px;background:#fff;padding:8px;border:1px solid #999;font:11px/1.4 "Courier New",monospace;color:#222}.party-mode'
)

s = s.replace(
    '.desktop-icons{display:none;position:fixed;left:28px;top:74px;z-index:40;grid-template-columns:92px;gap:24px}',
    '.desktop-icons{display:none;position:absolute;left:28px;top:74px;z-index:40;grid-template-columns:92px;gap:24px}'
)

old_menu = '<div class="menubar"><div class="menu-drop"><span class="menu-label">Plik</span><div class="menu-panel"><div class="menu-entry">Nowy</div><div class="menu-entry">Otwórz...</div><div class="menu-entry">Właściwości</div><div class="menu-sep"></div><div class="menu-entry">Zakończ</div></div></div><div class="menu-drop"><span class="menu-label">Edycja</span><div class="menu-panel"><div class="menu-entry">Cofnij</div><div class="menu-sep"></div><div class="menu-entry">Kopiuj</div><div class="menu-entry">Znajdź...</div></div></div><button data-menu="view">Widok</button><div class="menu-drop"><span class="menu-label">Ulubione</span><div class="menu-panel"><div class="menu-entry">Premiery 2026</div><div class="menu-entry">Premiery 2027</div><div class="menu-entry">Premiery 2028</div><div class="menu-entry">Dalej</div></div></div><button data-menu="help" id="helpBtn">Pomoc</button></div>'
new_menu = '<div class="menubar"><div class="menu-drop"><span class="menu-label">Plik</span><div class="menu-panel"><div class="menu-entry">Nowy</div><div class="menu-entry">Otwórz...</div><div class="menu-entry">Właściwości</div><div class="menu-sep"></div><div class="menu-entry">Zakończ</div></div></div><div class="menu-drop"><span class="menu-label">Edycja</span><div class="menu-panel"><div class="menu-entry">Cofnij</div><div class="menu-sep"></div><div class="menu-entry">Kopiuj</div><div class="menu-entry">Znajdź...</div></div></div><div class="menu-drop" id="viewMenu"><span class="menu-label">Widok</span><div class="menu-panel"><div class="menu-entry menu-action" id="themeToggle">Przełącz na tryb nocny</div><div class="menu-entry menu-action" id="colorToggle">Zmień kolor strony</div></div></div><div class="menu-drop"><span class="menu-label">Ulubione</span><div class="menu-panel"><div class="menu-entry">Najbliższa premiera</div><div class="menu-entry">The Game Awards</div><div class="menu-entry">Najbardziej oczekiwane</div><div class="menu-entry">W produkcji</div></div></div><button data-menu="help" id="helpBtn">Pomoc</button></div>'
assert old_menu in s
s = s.replace(old_menu, new_menu, 1)

# Rename DALEJ section/tab.
s = s.replace('<a href="#beyond">DALEJ</a>', '<a href="#beyond">W PRODUKCJI</a>', 1)
s = s.replace('{id:"beyond",label:"DALEJ",note:"NIEZAPOWIEDZIANE / BRAK DATY // SORTOWANIE: STUDIO → TYTUŁ",games:[', '{id:"beyond",label:"W PRODUKCJI",note:"PROJEKTY W PRODUKCJI / BEZ DATY PREMIERY // SORTOWANIE: STUDIO → TYTUŁ",games:[', 1)

# Add GTA VI PlayStation Store destination.
old_gta = '{title:"Grand Theft Auto VI",studio:"Rockstar Games",date:"19.11.2026",sortDate:"2026-11-19",status:"POTWIERDZONE",image:"https://cdn2.steamgriddb.com/grid/a55e72542860596de2ef8c0d847b6f03.png"}'
new_gta = '{title:"Grand Theft Auto VI",studio:"Rockstar Games",date:"19.11.2026",sortDate:"2026-11-19",status:"POTWIERDZONE",image:"https://cdn2.steamgriddb.com/grid/a55e72542860596de2ef8c0d847b6f03.png",storeUrl:"https://store.playstation.com/pl-pl/concept/10000730"}'
assert old_gta in s
s = s.replace(old_gta, new_gta, 1)

# Desktop icons should belong to the desktop, not follow viewport scrolling. Jump to desktop origin when minimizing.
old_min = '$("minBtn").onclick=()=>{const on=document.body.classList.toggle("desktop-mode");$("page").classList.toggle("minimized",on)};'
new_min = '$("minBtn").onclick=()=>{const on=document.body.classList.toggle("desktop-mode");$("page").classList.toggle("minimized",on);if(on)window.scrollTo({top:0,left:0,behavior:"auto"})};'
assert old_min in s
s = s.replace(old_min, new_min, 1)

# Replace old Widok behavior with two explicit dropdown actions.
old_toolbar_handlers = '$("backBtn").onclick=()=>codeStep("back");$("forwardBtn").onclick=()=>codeStep("forward");$("starBtn").onclick=()=>codeStep("star");$("gwBtn").onclick=()=>codeStep("gw");$("homeBtn").onclick=()=>{};'
new_toolbar_handlers = '$("backBtn").onclick=()=>codeStep("back");$("forwardBtn").onclick=()=>codeStep("forward");$("starBtn").onclick=()=>codeStep("star");$("gwBtn").onclick=()=>codeStep("gw");$("homeBtn").onclick=()=>{};$("themeToggle").onclick=()=>{const night=document.body.classList.toggle("night-mode");$("themeToggle").textContent=night?"Przełącz na tryb dzienny":"Przełącz na tryb nocny"};$("colorToggle").onclick=()=>{document.body.classList.toggle("party-mode");toast("ZMIENIONO KOLOR")};'
assert old_toolbar_handlers in s
s = s.replace(old_toolbar_handlers, new_toolbar_handlers, 1)

old_menu_handler = 'document.querySelectorAll("[data-menu]").forEach(btn=>btn.onclick=()=>{const m=btn.dataset.menu;if(m==="help"&&helpLongFired){helpLongFired=false;return}if(m==="view"){document.body.classList.toggle("night-mode")};if(m==="help")openModal("POMOC",\'<h3>Gry jednak wychodzą</h3><p>Wersja 0.22. Wszystko działa. Prawdopodobnie.</p>\')});'
new_menu_handler = 'document.querySelectorAll("[data-menu]").forEach(btn=>btn.onclick=()=>{const m=btn.dataset.menu;if(m==="help"&&helpLongFired){helpLongFired=false;return}if(m==="help")openModal("POMOC",\'<h3>Gry jednak wychodzą</h3><p>Ta strona zbiera najciekawsze nadchodzące gry i porządkuje je według terminu premiery. Przy każdej pozycji znajdziesz datę lub rok wydania, studio odpowiedzialne za projekt oraz — gdy jest dostępny — link do oficjalnej strony sklepu.</p><p>Na dole znajduje się sekcja <b>W PRODUKCJI</b>: gry bez ustalonej daty premiery, które zostały zapowiedziane, są rozwijane albo pojawiają się jako aktywne projekty studiów.</p><details class="help-secret"><summary>Diagnostyka systemu</summary><div>Coś chyba nie działa tak, jak powinno. W logach został ślad po zmianie podpisanej jako „Przemek”. Ktoś przeniósł informację, o której nikt nie powinien wiedzieć, w miejsce którego normalnie się nie sprawdza. Podobno dobrze ją ukrył.</div></details><p style="margin-top:10px;font-size:11px">Wersja 0.23.</p>\')});'
assert old_menu_handler in s
s = s.replace(old_menu_handler, new_menu_handler, 1)

assert 'BUILD_022' in s
s = s.replace('BUILD_022', 'BUILD_023', 1)

path.write_text(s, encoding='utf-8')

# trigger
