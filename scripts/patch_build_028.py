from pathlib import Path

path = Path('index.html')
s = path.read_text(encoding='utf-8')
s = s.replace('BUILD_027', 'BUILD_028')
s = s.replace('Wersja 0.27.', 'Wersja 0.28.')

css = r'''
/* BUILD_028 visual patch */
body:after{content:"";position:fixed;right:7vw;top:6vh;width:88px;height:88px;border-radius:50%;background:radial-gradient(circle at 34% 30%,#fffbd0 0 12%,#ffe96a 36%,#ffc83e 68%,#f3a923 100%);box-shadow:0 0 0 8px rgba(255,234,87,.08),0 0 28px rgba(255,214,69,.48),0 0 70px rgba(255,196,50,.24);pointer-events:none;z-index:0}
.night-mode:after{background:radial-gradient(circle at 34% 30%,#fffde0 0 18%,#ecebd1 45%,#c5c6e9 72%,#9293c6 100%);box-shadow:0 0 28px rgba(220,225,255,.38),0 0 70px rgba(120,100,220,.22)}
.desktop-app>.titlebar{cursor:move;touch-action:none;user-select:none}
.desktop-app>.titlebar .win-btn{cursor:pointer}
.night-mode .desktop-app>.titlebar,.night-mode .desktop-app>.titlebar .title-left,.night-mode .desktop-app>.titlebar span{color:#fff!important;text-shadow:1px 1px 0 #161126}
.night-mode .task-app{color:#fff!important;text-shadow:1px 1px 0 #11152a}
'''
if '/* BUILD_028 visual patch */' not in s:
    s = s.replace('@keyframes shake', css + '\n@keyframes shake', 1)

path.write_text(s, encoding='utf-8')