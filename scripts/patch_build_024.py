from pathlib import Path

path = Path('index.html')
s = path.read_text(encoding='utf-8')

# --- BUILD 024: stable menus, desktop explorer windows and taskbar ---

# Keep dropdowns attached to labels and allow click-pinned menus.
s = s.replace('.menu-panel{display:none;position:absolute;left:-3px;top:20px;', '.menu-panel{display:none;position:absolute;left:-3px;top:100%;')
s = s.replace('.menu-drop:hover .menu-panel{display:block}', '.menu-drop:hover .menu-panel,.menu-drop.open .menu-panel{display:block}')
s = s.replace('.desktop-shortcut{width:92px;text-align:center;', '.desktop-shortcut{width:92px;text-align:center;cursor:default;pointer-events:auto;')

# Add desktop/taskbar/explorer styling before animations.
needle = '@keyframes shake{'
extra_css = r'''
body.desktop-mode{overflow:hidden;min-height:100vh}.desktop-taskbar{display:none;position:fixed;left:0;right:0;bottom:0;height:38px;z-index:1200;align-items:center;gap:5px;padding:3px 5px;background:linear-gradient(#dedee8,#bfc1d2);border-top:2px solid #fff;box-shadow:0 -1px 0 #666;font:11px Tahoma,"MS Sans Serif",Arial,sans-serif}.desktop-mode .desktop-taskbar{display:flex}.task-start{height:30px;padding:2px 11px 2px 6px;display:flex;align-items:center;gap:5px;font-weight:700;background:linear-gradient(90deg,#8fe6cf,#d8fb7c);border-top:2px solid #fff;border-left:2px solid #fff;border-right:2px solid #555;border-bottom:2px solid #555}.task-start-badge{width:18px;height:18px;display:grid;place-items:center;background:#6b46b8;color:#fff;border:1px solid #34245f;font-weight:900}.task-app{height:30px;min-width:190px;max-width:320px;padding:4px 10px;text-align:left;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;background:#d1d1d9;border-top:2px solid #666;border-left:2px solid #666;border-right:2px solid #fff;border-bottom:2px solid #fff}.task-spacer{flex:1}.task-tray{height:30px;display:flex;align-items:center;gap:8px;padding:3px 8px;background:#c8cad8;border-top:2px solid #777;border-left:2px solid #777;border-right:2px solid #fff;border-bottom:2px solid #fff;white-space:nowrap}.tray-net{font-weight:700;color:#164d75}.tray-clock{text-align:right;line-height:1.05}.desktop-app{display:none;position:fixed;z-index:1000;width:min(540px,calc(100vw - 36px));height:350px;background:#cfcfd5;box-shadow:8px 8px 0 rgba(45,28,85,.34)}.desktop-mode .desktop-app.open{display:block}.desktop-app.computer-window{left:150px;top:92px}.desktop-app.trash-window{left:225px;top:138px;width:min(470px,calc(100vw - 36px));height:310px}.desktop-app .titlebar{cursor:default}.desktop-app-toolbar{display:flex;gap:14px;padding:5px 8px;background:#dedee3;border-bottom:1px solid #777;font:11px Tahoma,"MS Sans Serif",sans-serif}.desktop-app-address{display:flex;align-items:center;gap:6px;padding:5px 7px;background:#d5d5da;border-bottom:1px solid #777;font:11px Tahoma,"MS Sans Serif",sans-serif}.desktop-app-address b{font-weight:400}.desktop-app-path{flex:1;min-height:23px;padding:3px 7px;background:#fff;border-top:2px solid #666;border-left:2px solid #666;border-right:2px solid #fff;border-bottom:2px solid #fff;font:11px "Courier New",monospace;color:#111}.desktop-app-body{height:236px;margin:6px;background:#fff;border-top:2px solid #777;border-left:2px solid #777;border-right:2px solid #fff;border-bottom:2px solid #fff;color:#111;overflow:auto}.computer-window .desktop-app-body{display:grid;grid-template-columns:repeat(2,minmax(150px,1fr));gap:8px;padding:13px}.explorer-item{display:flex;align-items:center;gap:9px;min-height:58px;padding:6px;border:1px solid transparent;font:11px Tahoma,"MS Sans Serif",sans-serif}.explorer-item:hover{border:1px dotted #777;background:#edf4ff}.explorer-icon{width:42px;height:42px;display:grid;place-items:center;font-size:25px;background:linear-gradient(135deg,#fcf68b,#80ddf1 56%,#c48cff);border:2px outset #eee;color:#4b2a82}.explorer-item small{display:block;margin-top:3px;color:#666}.empty-trash{height:100%;display:grid;place-items:center;text-align:center;color:#666;font:12px "Courier New",monospace}.desktop-app-status{height:24px;margin:0 6px 6px;padding:4px 7px;background:#d3d3da;border-top:2px solid #777;border-left:2px solid #777;border-right:2px solid #fff;border-bottom:2px solid #fff;font:10px "Courier New",monospace;color:#222}.night-mode .desktop-taskbar{background:linear-gradient(#323956,#20263c);border-top-color:#737b9e;color:#f1f3ff}.night-mode .task-start{background:linear-gradient(90deg,#1d806e,#516f34);color:#fff;border-top-color:#7488a7;border-left-color:#7488a7;border-right-color:#080a18;border-bottom-color:#080a18}.night-mode .task-app,.night-mode .task-tray{background:#242b45;color:#edf0ff;border-top-color:#0a0d20;border-left-color:#0a0d20;border-right-color:#68718e;border-bottom-color:#68718e}.night-mode .tray-net{color:#85ddff}.night-mode .desktop-app{background:#2a3048}.night-mode .desktop-app-toolbar,.night-mode .desktop-app-address{background:#343b58;color:#eef1ff}.night-mode .desktop-app-body{background:#11172e;color:#eef1ff;border-top-color:#090c1c;border-left-color:#090c1c;border-right-color:#69718e;border-bottom-color:#69718e}.night-mode .desktop-app-path{background:#0d1328;color:#c8efff}.night-mode .explorer-item small{color:#aab2cf}.night-mode .explorer-item:hover{background:#202b50}.night-mode .empty-trash{color:#c1c7dd}.night-mode .desktop-app-status{background:#252b43;color:#edf0ff;border-top-color:#090c1c;border-left-color:#090c1c;border-right-color:#69718e;border-bottom-color:#69718e}
'''
assert needle in s
s = s.replace(needle, extra_css + needle, 1)

# Replace desktop icon block with clickable icons, two explorer windows and a classic taskbar.
old_icons = '<div class="desktop-icons" id="desktopIcons" aria-hidden="true"><div class="desktop-shortcut"><div class="desktop-glyph computer"></div><div>Mój komputer</div></div><div class="desktop-shortcut"><div class="desktop-glyph trash"></div><div>Kosz</div></div></div>'
new_icons = '''<div class="desktop-icons" id="desktopIcons" aria-hidden="true"><div class="desktop-shortcut" id="computerIcon" title="Kliknij dwukrotnie"><div class="desktop-glyph computer"></div><div>Mój komputer</div></div><div class="desktop-shortcut" id="trashIcon" title="Kliknij dwukrotnie"><div class="desktop-glyph trash"></div><div>Kosz</div></div></div>
<div class="window desktop-app computer-window" id="computerWindow"><div class="titlebar"><div class="title-left"><span class="app-icon">M</span><span>Mój komputer</span></div><div class="window-buttons"><button class="win-btn desktop-app-close" data-close-window="computerWindow">×</button></div></div><div class="desktop-app-toolbar"><span>Plik</span><span>Edycja</span><span>Widok</span><span>Pomoc</span></div><div class="desktop-app-address"><b>Adres:</b><div class="desktop-app-path">Mój komputer</div></div><div class="desktop-app-body"><div class="explorer-item"><div class="explorer-icon">▣</div><div><b>Dysk lokalny (C:)</b><small>Dysk systemowy</small></div></div><div class="explorer-item"><div class="explorer-icon">◉</div><div><b>CD-ROM (D:)</b><small>Brak nośnika</small></div></div><div class="explorer-item"><div class="explorer-icon">▤</div><div><b>Moje dokumenty</b><small>Folder systemowy</small></div></div><div class="explorer-item"><div class="explorer-icon">⚙</div><div><b>Panel sterowania</b><small>Ustawienia systemu</small></div></div></div><div class="desktop-app-status">4 obiekty</div></div>
<div class="window desktop-app trash-window" id="trashWindow"><div class="titlebar"><div class="title-left"><span class="app-icon">K</span><span>Kosz</span></div><div class="window-buttons"><button class="win-btn desktop-app-close" data-close-window="trashWindow">×</button></div></div><div class="desktop-app-toolbar"><span>Plik</span><span>Edycja</span><span>Widok</span><span>Pomoc</span></div><div class="desktop-app-address"><b>Adres:</b><div class="desktop-app-path">Kosz</div></div><div class="desktop-app-body"><div class="empty-trash"><div><div style="font-size:40px;margin-bottom:8px">♲</div>Kosz jest pusty.</div></div></div><div class="desktop-app-status">0 obiektów</div></div>
<div class="desktop-taskbar" id="desktopTaskbar"><div class="task-start"><span class="task-start-badge">G</span><span>Start</span></div><div class="task-app">Gry jednak wychodzą</div><div class="task-spacer"></div><div class="task-tray"><span class="tray-net">◉ INTERNET</span><span>🔊</span><span class="tray-clock" id="trayClock">--:--<br>--.--.----</span></div></div>'''
assert old_icons in s
s = s.replace(old_icons, new_icons, 1)

# Replace menu interaction with pinned dropdowns and retain no-op decorative entries.
anchor = '$("modalClose").onclick=closeModal;$("modalBackdrop").onclick=e=>{if(e.target===$("modalBackdrop"))closeModal()};document.addEventListener("keydown",e=>{if(e.key==="Escape")closeModal()});'
menu_js = r'''
$("modalClose").onclick=closeModal;$("modalBackdrop").onclick=e=>{if(e.target===$("modalBackdrop"))closeModal()};document.addEventListener("keydown",e=>{if(e.key==="Escape")closeModal()});
document.querySelectorAll(".menu-drop").forEach(menu=>{const label=menu.querySelector(".menu-label"),panel=menu.querySelector(".menu-panel");label?.addEventListener("click",e=>{e.stopPropagation();const willOpen=!menu.classList.contains("open");document.querySelectorAll(".menu-drop.open").forEach(x=>x.classList.remove("open"));if(willOpen)menu.classList.add("open")});panel?.addEventListener("click",e=>e.stopPropagation())});document.addEventListener("click",()=>document.querySelectorAll(".menu-drop.open").forEach(x=>x.classList.remove("open")));
'''.strip()
assert anchor in s
s = s.replace(anchor, menu_js, 1)

# Make theme/color actions close the menu after use.
s = s.replace('$("themeToggle").onclick=()=>{const night=document.body.classList.toggle("night-mode");$("themeToggle").textContent=night?"Przełącz na tryb dzienny":"Przełącz na tryb nocny"};$("colorToggle").onclick=()=>{document.body.classList.toggle("party-mode");toast("ZMIENIONO KOLOR")};', '$("themeToggle").onclick=()=>{const night=document.body.classList.toggle("night-mode");$("themeToggle").textContent=night?"Przełącz na tryb dzienny":"Przełącz na tryb nocny";$("viewMenu").classList.remove("open")};$("colorToggle").onclick=()=>{document.body.classList.toggle("party-mode");$("viewMenu").classList.remove("open");toast("ZMIENIONO KOLOR")};')

# Desktop windows, classic clock and restore cleanup.
old_min = '$("minBtn").onclick=()=>{const on=document.body.classList.toggle("desktop-mode");$("page").classList.toggle("minimized",on);if(on)window.scrollTo({top:0,left:0,behavior:"auto"})};'
new_min = '$("minBtn").onclick=()=>{const on=document.body.classList.toggle("desktop-mode");$("page").classList.toggle("minimized",on);if(on)window.scrollTo({top:0,left:0,behavior:"auto"});else document.querySelectorAll(".desktop-app.open").forEach(w=>w.classList.remove("open"))};'
assert old_min in s
s = s.replace(old_min, new_min, 1)

insert_after = new_min
extra_js = r'''
function openDesktopWindow(id){if(!document.body.classList.contains("desktop-mode"))return;$(id).classList.add("open")}
$("computerIcon").ondblclick=()=>openDesktopWindow("computerWindow");$("trashIcon").ondblclick=()=>openDesktopWindow("trashWindow");document.querySelectorAll("[data-close-window]").forEach(btn=>btn.onclick=()=>$(btn.dataset.closeWindow).classList.remove("open"));
function updateTrayClock(){const d=new Date();const t=d.toLocaleTimeString("pl-PL",{hour:"2-digit",minute:"2-digit"});const date=d.toLocaleDateString("pl-PL");$("trayClock").innerHTML=`${t}<br>${date}`};updateTrayClock();setInterval(updateTrayClock,30000);
'''.strip()
s = s.replace(insert_after, insert_after + extra_js, 1)

# Build/version bump.
assert 'BUILD_023' in s
s = s.replace('BUILD_023', 'BUILD_024', 1)
s = s.replace('Wersja 0.23.', 'Wersja 0.24.', 1)

path.write_text(s, encoding='utf-8')
