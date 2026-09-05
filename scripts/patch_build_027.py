from pathlib import Path

path = Path('index.html')
s = path.read_text(encoding='utf-8')

s = s.replace('BUILD_026', 'BUILD_027')
s = s.replace('Wersja 0.26.', 'Wersja 0.27.')

css = r'''
/* BUILD_027: ruchome okna + czytelniejszy nocny pulpit + słońce */
body:after{content:"";position:fixed;right:7vw;top:6vh;width:88px;height:88px;border-radius:50%;background:radial-gradient(circle at 34% 30%,#fffbd0 0 12%,#ffe96a 36%,#ffc83e 68%,#f3a923 100%);box-shadow:0 0 0 8px rgba(255,234,87,.08),0 0 28px rgba(255,214,69,.48),0 0 70px rgba(255,196,50,.24);pointer-events:none;z-index:0}
.night-mode:after{background:radial-gradient(circle at 34% 30%,#fffde0 0 18%,#ecebd1 45%,#c5c6e9 72%,#9293c6 100%);box-shadow:0 0 28px rgba(220,225,255,.38),0 0 70px rgba(120,100,220,.22)}
.desktop-app>.titlebar{cursor:move;touch-action:none;user-select:none}
.desktop-app>.titlebar .win-btn{cursor:pointer}
.night-mode .desktop-app>.titlebar,.night-mode .desktop-app>.titlebar .title-left{color:#fff!important;text-shadow:1px 1px 0 #161126}
.night-mode .task-app{color:#fff!important;text-shadow:1px 1px 0 #11152a}
'''
if '/* BUILD_027:' not in s:
    s = s.replace('@keyframes shake', css + '\n@keyframes shake', 1)

old = '''function openDesktopWindow(id){if(!document.body.classList.contains("desktop-mode"))return;$(id).classList.add("open")}'''
new = '''let desktopWindowZ=1000;
function bringDesktopWindowToFront(win){desktopWindowZ+=1;win.style.zIndex=desktopWindowZ}
function openDesktopWindow(id){if(!document.body.classList.contains("desktop-mode"))return;const win=$(id);win.classList.add("open");bringDesktopWindowToFront(win)}'''
if old not in s:
    raise SystemExit('openDesktopWindow pattern not found')
s = s.replace(old, new, 1)

anchor = '''document.querySelectorAll("[data-close-window]").forEach(btn=>btn.onclick=()=>$(btn.dataset.closeWindow).classList.remove("open"));'''
drag = r'''
document.querySelectorAll(".desktop-app").forEach(win=>{
  const bar=win.querySelector(":scope > .titlebar");
  if(!bar)return;
  bar.addEventListener("pointerdown",e=>{
    if(!document.body.classList.contains("desktop-mode")||e.target.closest(".win-btn"))return;
    e.preventDefault();bringDesktopWindowToFront(win);
    const rect=win.getBoundingClientRect();
    const dx=e.clientX-rect.left,dy=e.clientY-rect.top;
    try{bar.setPointerCapture(e.pointerId)}catch(_){ }
    const move=ev=>{
      const maxX=Math.max(0,window.innerWidth-win.offsetWidth);
      const maxY=Math.max(0,window.innerHeight-40-win.offsetHeight);
      const x=Math.min(maxX,Math.max(0,ev.clientX-dx));
      const y=Math.min(maxY,Math.max(0,ev.clientY-dy));
      win.style.left=x+"px";win.style.top=y+"px";
    };
    const end=()=>{bar.removeEventListener("pointermove",move);bar.removeEventListener("pointerup",end);bar.removeEventListener("pointercancel",end)};
    bar.addEventListener("pointermove",move);bar.addEventListener("pointerup",end);bar.addEventListener("pointercancel",end);
  });
  win.addEventListener("pointerdown",()=>bringDesktopWindowToFront(win));
});'''
if drag.strip() not in s:
    if anchor not in s:
        raise SystemExit('drag anchor not found')
    s = s.replace(anchor, anchor + '\n' + drag, 1)

path.write_text(s, encoding='utf-8')