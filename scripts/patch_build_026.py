from pathlib import Path

path = Path('index.html')
s = path.read_text(encoding='utf-8')

s = s.replace('BUILD_025', 'BUILD_026')
s = s.replace('Wersja 0.25.', 'Wersja 0.26.')
s = s.replace('aria-hidden="true"', 'aria-hidden="false"', 1)

integration_css = r'''
/* BUILD_026: zintegrowany pulpit + główne okno */
body{padding-bottom:40px}
.desktop{width:calc(100% - 154px);max-width:1540px;margin:20px 22px 54px 122px}
.desktop.maxed{width:calc(100% - 4px);max-width:none;margin:2px auto 40px}
.desktop-icons{display:grid;position:fixed;left:14px;top:28px;z-index:40;grid-template-columns:92px;gap:24px}
body:not(.desktop-mode) .desktop-shortcut{pointer-events:none;opacity:.72;filter:saturate(.78)}
body:not(.desktop-mode) .desktop-shortcut.selected{background:transparent}
.desktop-mode .desktop-shortcut{pointer-events:auto;opacity:1;filter:none}
.desktop-mode #mainWindow{display:none}
.desktop-taskbar{display:flex;height:34px;padding:2px 4px;opacity:.98}
.task-start,.task-app,.task-tray{height:28px}
.task-start{padding:1px 10px 1px 5px;cursor:pointer}
.task-app{cursor:pointer;min-width:180px;padding:3px 9px}
body:not(.desktop-mode) .task-app{background:#e2e2e8;border-top:2px solid #666;border-left:2px solid #666;border-right:2px solid #fff;border-bottom:2px solid #fff}
body.desktop-mode .task-app{background:#d7d7de;border-top:2px solid #fff;border-left:2px solid #fff;border-right:2px solid #666;border-bottom:2px solid #666}
.task-tray{padding:2px 7px}
.start-menu{bottom:34px}
.start-menu.open{display:flex!important}
@media(max-width:900px){
  .desktop{width:calc(100% - 10px);max-width:none;margin:5px auto 44px}
  body:not(.desktop-mode) .desktop-icons{display:none}
  .desktop-mode .desktop-icons{display:grid;left:12px;top:22px}
  .task-app{min-width:120px;max-width:190px}
}
@media(max-width:620px){
  .tray-net{display:none}.task-tray{gap:4px;padding:2px 5px}.task-app{min-width:105px;max-width:145px}.task-start{padding-right:7px}
}
'''
if integration_css.strip() not in s:
    s = s.replace('@keyframes shake', integration_css + '\n@keyframes shake', 1)

s = s.replace('.desktop.maxed{width:calc(100% - 4px);max-width:none;margin:2px auto 40px}', '.desktop.maxed{z-index:60;width:calc(100% - 4px);max-width:none;margin:2px auto 40px}', 1)

old_icon = '''function desktopIconClick(icon,windowId){if(selectedDesktopIcon===icon){openDesktopWindow(windowId);return}clearDesktopSelection();selectedDesktopIcon=icon;icon.classList.add("selected")}'''
new_icon = '''function desktopIconClick(icon,windowId){if(!document.body.classList.contains("desktop-mode"))return;if(selectedDesktopIcon===icon){openDesktopWindow(windowId);return}clearDesktopSelection();selectedDesktopIcon=icon;icon.classList.add("selected")}'''
if old_icon in s:
    s = s.replace(old_icon, new_icon, 1)
elif new_icon not in s:
    raise SystemExit('desktopIconClick pattern not found')

old_main = '''function restoreMainWindow(){document.body.classList.remove("desktop-mode");$("page").classList.remove("minimized");$("startMenu").classList.remove("open");clearDesktopSelection();document.querySelectorAll(".desktop-app.open").forEach(w=>w.classList.remove("open"))}
$("minBtn").onclick=()=>{const on=document.body.classList.toggle("desktop-mode");$("page").classList.toggle("minimized",on);$("startMenu").classList.remove("open");clearDesktopSelection();if(on)window.scrollTo({top:0,left:0,behavior:"auto"});else document.querySelectorAll(".desktop-app.open").forEach(w=>w.classList.remove("open"))};
$("taskMainApp").onclick=e=>{e.stopPropagation();restoreMainWindow()};'''
new_main = '''function setMainMinimized(on){document.body.classList.toggle("desktop-mode",on);$("page").classList.toggle("minimized",on);$("startMenu").classList.remove("open");clearDesktopSelection();if(on){window.scrollTo({top:0,left:0,behavior:"auto"})}else{document.querySelectorAll(".desktop-app.open").forEach(w=>w.classList.remove("open"))}}
function restoreMainWindow(){setMainMinimized(false)}
$("minBtn").onclick=()=>setMainMinimized(true);
$("taskMainApp").onclick=e=>{e.stopPropagation();setMainMinimized(!document.body.classList.contains("desktop-mode"))};'''
if old_main in s:
    s = s.replace(old_main, new_main, 1)
elif new_main not in s:
    raise SystemExit('main window pattern not found')

path.write_text(s, encoding='utf-8')
