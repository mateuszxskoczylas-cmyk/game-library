from pathlib import Path

path = Path('index.html')
s = path.read_text(encoding='utf-8')

# Version bump.
s = s.replace('BUILD_024', 'BUILD_025', 1)

# Desktop selection + Start menu styling.
marker = '.night-mode .desktop-app-status{background:#252b43;color:#edf0ff;border-top-color:#090c1c;border-left-color:#090c1c;border-right-color:#69718e;border-bottom-color:#69718e}'
assert marker in s
extra_css = '''.night-mode .desktop-app-status{background:#252b43;color:#edf0ff;border-top-color:#090c1c;border-left-color:#090c1c;border-right-color:#69718e;border-bottom-color:#69718e}.desktop-shortcut.selected{background:#000080;color:#fff;outline:1px dotted #fff;text-shadow:none}.desktop-shortcut.selected .desktop-glyph{filter:drop-shadow(3px 3px 0 rgba(0,0,0,.45)) saturate(.8)}.task-start,.task-app{cursor:pointer;user-select:none}.start-menu{display:none;position:fixed;left:5px;bottom:38px;z-index:1250;width:235px;background:#d6d6df;border-top:2px solid #fff;border-left:2px solid #fff;border-right:2px solid #454552;border-bottom:2px solid #454552;box-shadow:4px 4px 0 rgba(0,0,0,.28);font:11px Tahoma,"MS Sans Serif",Arial,sans-serif}.desktop-mode .start-menu.open{display:flex}.start-side{width:29px;display:flex;align-items:flex-end;justify-content:center;padding:7px 0;background:linear-gradient(#4b2a82,#7a52bb,#0d7dad);color:#fff;font-weight:700;letter-spacing:.08em;writing-mode:vertical-rl;transform:rotate(180deg)}.start-content{flex:1;padding:4px}.start-entry{padding:7px 8px;display:flex;align-items:center;gap:8px;color:#111}.start-entry:hover{background:#000080;color:#fff}.start-entry .mini-ico{width:22px;height:22px;display:grid;place-items:center;background:linear-gradient(135deg,#fff68a,#80ddf1 55%,#cf8cff);border:1px solid #5d467f;font-weight:900;color:#4b2a82}.start-sep{height:1px;background:#80808a;border-bottom:1px solid #fff;margin:3px 2px}.start-virus{padding:5px 7px 4px;color:#666;font:9px "Courier New",monospace;text-align:right}.night-mode .start-menu{background:#262c45;border-top-color:#707897;border-left-color:#707897;border-right-color:#090b19;border-bottom-color:#090b19;color:#eef1ff}.night-mode .start-entry{color:#eef1ff}.night-mode .start-entry:hover{background:#573b9b}.night-mode .start-virus{color:#aeb4cc}'''
s = s.replace(marker, extra_css, 1)

# Desktop taskbar gains working Start menu + restore button.
old_taskbar = '<div class="desktop-taskbar" id="desktopTaskbar"><div class="task-start"><span class="task-start-badge">G</span><span>Start</span></div><div class="task-app">Gry jednak wychodzą</div><div class="task-spacer"></div><div class="task-tray"><span class="tray-net">◉ INTERNET</span><span>🔊</span><span class="tray-clock" id="trayClock">--:--<br>--.--.----</span></div></div>'
new_taskbar = '<div class="desktop-taskbar" id="desktopTaskbar"><div class="task-start" id="startButton"><span class="task-start-badge">G</span><span>Start</span></div><div class="task-app" id="taskMainApp">Gry jednak wychodzą</div><div class="task-spacer"></div><div class="task-tray"><span class="tray-net">◉ INTERNET</span><span>🔊</span><span class="tray-clock" id="trayClock">--:--<br>--.--.----</span></div></div><div class="start-menu" id="startMenu"><div class="start-side">GRY OS 2000</div><div class="start-content"><div class="start-entry"><span class="mini-ico">▣</span><span>Programy</span></div><div class="start-entry"><span class="mini-ico">▤</span><span>Dokumenty</span></div><div class="start-entry"><span class="mini-ico">⚙</span><span>Ustawienia</span></div><div class="start-entry"><span class="mini-ico">⌕</span><span>Znajdź</span></div><div class="start-sep"></div><div class="start-entry"><span class="mini-ico">?</span><span>Pomoc</span></div><div class="start-entry"><span class="mini-ico">⏻</span><span>Zamknij system...</span></div><div class="start-virus">Przemo_virus.jpg</div></div></div>'
assert old_taskbar in s
s = s.replace(old_taskbar, new_taskbar, 1)

# Remove old visible easter-egg UI containers.
s = s.replace('<div class="egg-toast" id="toast"></div>', '', 1)
context = '<div class="context-menu" id="contextMenu"><button data-context="open">Otwórz</button><button data-context="copy">Kopiuj nazwę</button><div class="context-sep"></div><button data-context="pizza">sprzedaj mi te pizze</button></div>\n'
s = s.replace(context, '', 1)

# Remove all old easter-egg data/assets references.
start = s.index('const quotes=')
end = s.index('function esc(v)', start)
s = s[:start] + s[end:]

# Replace old interactive/easter-egg tail with clean UI logic. Help diagnostic is intentionally retained as the new egg starting point.
start = s.index('const $=id=>')
end = s.index('</script>', start)
clean_js = r'''const $=id=>document.getElementById(id);
function openModal(t,h){$("modalTitle").textContent=t;$("modalBody").innerHTML=h;$("modalBackdrop").classList.add("open")}
function closeModal(){$("modalBackdrop").classList.remove("open")}
$("modalClose").onclick=closeModal;
$("modalBackdrop").onclick=e=>{if(e.target===$("modalBackdrop"))closeModal()};
document.addEventListener("keydown",e=>{if(e.key==="Escape")closeModal()});

document.querySelectorAll(".menu-drop").forEach(menu=>{const label=menu.querySelector(".menu-label"),panel=menu.querySelector(".menu-panel");label?.addEventListener("click",e=>{e.stopPropagation();const willOpen=!menu.classList.contains("open");document.querySelectorAll(".menu-drop.open").forEach(x=>x.classList.remove("open"));if(willOpen)menu.classList.add("open")});panel?.addEventListener("click",e=>e.stopPropagation())});

$("backBtn").onclick=()=>{};$("forwardBtn").onclick=()=>{};$("starBtn").onclick=()=>{};$("gwBtn").onclick=()=>{};$("homeBtn").onclick=()=>{};
$("themeToggle").onclick=()=>{const night=document.body.classList.toggle("night-mode");$("themeToggle").textContent=night?"Przełącz na tryb dzienny":"Przełącz na tryb nocny";$("viewMenu").classList.remove("open")};
$("colorToggle").onclick=()=>{document.body.classList.toggle("party-mode");$("viewMenu").classList.remove("open")};

let selectedDesktopIcon=null;
function clearDesktopSelection(){document.querySelectorAll(".desktop-shortcut.selected").forEach(x=>x.classList.remove("selected"));selectedDesktopIcon=null}
function openDesktopWindow(id){if(!document.body.classList.contains("desktop-mode"))return;$(id).classList.add("open")}
function desktopIconClick(icon,windowId){if(selectedDesktopIcon===icon){openDesktopWindow(windowId);return}clearDesktopSelection();selectedDesktopIcon=icon;icon.classList.add("selected")}
$("computerIcon").onclick=e=>{e.stopPropagation();desktopIconClick($("computerIcon"),"computerWindow")};
$("trashIcon").onclick=e=>{e.stopPropagation();desktopIconClick($("trashIcon"),"trashWindow")};
document.querySelectorAll("[data-close-window]").forEach(btn=>btn.onclick=()=>$(btn.dataset.closeWindow).classList.remove("open"));

function restoreMainWindow(){document.body.classList.remove("desktop-mode");$("page").classList.remove("minimized");$("startMenu").classList.remove("open");clearDesktopSelection();document.querySelectorAll(".desktop-app.open").forEach(w=>w.classList.remove("open"))}
$("minBtn").onclick=()=>{const on=document.body.classList.toggle("desktop-mode");$("page").classList.toggle("minimized",on);$("startMenu").classList.remove("open");clearDesktopSelection();if(on)window.scrollTo({top:0,left:0,behavior:"auto"});else document.querySelectorAll(".desktop-app.open").forEach(w=>w.classList.remove("open"))};
$("taskMainApp").onclick=e=>{e.stopPropagation();restoreMainWindow()};
$("startButton").onclick=e=>{e.stopPropagation();$("startMenu").classList.toggle("open")};
$("startMenu").onclick=e=>e.stopPropagation();

function updateTrayClock(){const d=new Date();const t=d.toLocaleTimeString("pl-PL",{hour:"2-digit",minute:"2-digit"});const date=d.toLocaleDateString("pl-PL");$("trayClock").innerHTML=`${t}<br>${date}`};updateTrayClock();setInterval(updateTrayClock,30000);
$("maxBtn").onclick=()=>$("desktop").classList.toggle("maxed");
$("closeBtn").onclick=()=>openModal("SYSTEM",'<h3>Nie można zamknąć programu.</h3><p>Trwa indeksowanie premier.</p>');

$("helpBtn").onclick=()=>openModal("POMOC",'<h3>Gry jednak wychodzą</h3><p>Ta strona zbiera najciekawsze nadchodzące gry i porządkuje je według terminu premiery. Przy każdej pozycji znajdziesz datę lub rok wydania, studio odpowiedzialne za projekt oraz — gdy jest dostępny — link do oficjalnej strony sklepu.</p><p>Na dole znajduje się sekcja <b>W PRODUKCJI</b>: gry bez ustalonej daty premiery, które zostały zapowiedziane, są rozwijane albo pojawiają się jako aktywne projekty studiów.</p><details class="help-secret"><summary>Diagnostyka systemu</summary><div>Coś chyba nie działa tak, jak powinno. W logach został ślad po zmianie podpisanej jako „Przemek”. Ktoś przeniósł informację, o której nikt nie powinien wiedzieć, w miejsce którego normalnie się nie sprawdza. Podobno dobrze ją ukrył.</div></details><p style="margin-top:10px;font-size:11px">Wersja 0.25.</p>');

document.addEventListener("click",e=>{document.querySelectorAll(".menu-drop.open").forEach(x=>x.classList.remove("open"));if(!e.target.closest("#startMenu")&&!e.target.closest("#startButton"))$("startMenu").classList.remove("open");if(document.body.classList.contains("desktop-mode")&&!e.target.closest(".desktop-shortcut")&&!e.target.closest(".desktop-app")&&!e.target.closest(".desktop-taskbar")&&!e.target.closest(".start-menu"))clearDesktopSelection()});
'''
s = s[:start] + clean_js + s[end:]

path.write_text(s, encoding='utf-8')
