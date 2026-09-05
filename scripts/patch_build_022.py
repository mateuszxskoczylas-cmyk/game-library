from pathlib import Path

path = Path('index.html')
s = path.read_text(encoding='utf-8')

old_desktop = '.desktop{width:min(1540px,calc(100% - 26px));margin:20px auto 50px;transition:.16s}'
new_desktop = '.desktop{width:min(1540px,calc(100% - 26px));margin:20px auto 50px;transition:.16s;position:relative;z-index:1}'
assert old_desktop in s
s = s.replace(old_desktop, new_desktop, 1)

old_party = '.party-mode{background-color:#ef5aa1}.party-mode .hero{filter:hue-rotate(70deg) saturate(1.45)}'
new_party = '''.night-mode{color:#eef1ff;background-color:#080d2a;background-image:radial-gradient(circle at 15px 18px,rgba(255,255,255,.95) 0 1px,transparent 1.5px),radial-gradient(circle at 62px 48px,rgba(181,214,255,.9) 0 1px,transparent 1.5px),radial-gradient(circle at 104px 20px,rgba(255,238,179,.9) 0 1px,transparent 1.5px),linear-gradient(160deg,#080d2a 0%,#151342 48%,#28134c 100%);background-size:120px 90px,150px 130px,190px 160px,auto}.night-mode:after{content:"";position:fixed;right:7vw;top:6vh;width:92px;height:92px;border-radius:50%;background:radial-gradient(circle at 34% 30%,#fffde0 0 18%,#ecebd1 45%,#c5c6e9 72%,#9293c6 100%);box-shadow:0 0 28px rgba(220,225,255,.38),0 0 70px rgba(120,100,220,.22);pointer-events:none;z-index:0}.night-mode .window{background:#30354d;border-top-color:#747b9a;border-left-color:#747b9a;border-right-color:#080b1c;border-bottom-color:#080b1c}.night-mode .menubar,.night-mode .toolbar,.night-mode .address-row{background:linear-gradient(#363c59,#23273d);color:#eef1ff;border-color:#11162b}.night-mode .menubar button,.night-mode .menu-label{color:#eef1ff}.night-mode .menu-panel{background:linear-gradient(135deg,#252a48,#1a2b49 62%,#39204a);border-top-color:#7f86aa;border-left-color:#7f86aa;border-right-color:#090b19;border-bottom-color:#090b19}.night-mode .menu-entry{color:#f2f1ff}.night-mode .address-box{background:#0e132b;color:#bfeeff;border-top-color:#07091a;border-left-color:#07091a;border-right-color:#626b91;border-bottom-color:#626b91}.night-mode .page{background:#10152f;border-top-color:#050716}.night-mode .hero{background:linear-gradient(135deg,#17204b 0 28%,#351449 28% 52%,#123052 52% 73%,#123d3a 73%);border-color:#8d77da;box-shadow:inset 0 0 0 4px rgba(185,200,255,.12)}.night-mode .hero-card{background:rgba(13,17,42,.94);border-color:#b6b0ff;color:#eef1ff;box-shadow:5px 5px 0 #08091c}.night-mode .hero h1{color:#fff}.night-mode .hero p{color:#d8dcf1}.night-mode .tga-window,.night-mode .next-window{background:#262c45;border-top-color:#707897;border-left-color:#707897;border-right-color:#090b19;border-bottom-color:#090b19;box-shadow:5px 5px 0 #08091c}.night-mode .tga-body,.night-mode .next-body{background:#20263f;color:#eef1ff;border-top-color:#4f5677}.night-mode .next-game,.night-mode .tga-date{color:#fff}.night-mode .release-inner{background:#181e38}.night-mode .section-note{color:#c4c9e0}.night-mode .game-card{background:#252b49;border-top-color:#6d7594;border-left-color:#6d7594;border-right-color:#080a18;border-bottom-color:#080a18;box-shadow:2px 2px 0 rgba(0,0,0,.45)}.night-mode .game-title,.night-mode .release{color:#f5f4ff}.night-mode .studio{color:#9bdcff}.night-mode .node{color:#aeb4cc}.night-mode .statusbar{background:#242a43;color:#e4e8ff;border-top-color:#0a0d20;border-left-color:#0a0d20;border-right-color:#69718f;border-bottom-color:#69718f}.night-mode .desktop-shortcut{color:#f7f6ff;text-shadow:1px 1px 0 #12152d,0 0 5px #b65cff}.party-mode{background-color:#ef5aa1}.party-mode .hero{filter:hue-rotate(70deg) saturate(1.45)}'''
assert old_party in s
s = s.replace(old_party, new_party, 1)

old_eye_css = '.eye-tool{position:relative;overflow:hidden}.eye-pyramid{position:relative;display:block;width:25px;height:21px;font:900 24px/18px Georgia,serif;color:#f0c94e;text-shadow:1px 1px 0 #4b2a82}.eye-pyramid b{position:absolute;left:8px;top:7px;font:900 8px/8px Arial,sans-serif;color:#4b2a82;text-shadow:0 0 1px #fff}'
new_eye_css = '.eye-tool{position:relative;overflow:hidden;padding:1px 4px}.eye-tool img{display:block;width:23px;height:23px;object-fit:contain;image-rendering:auto}'
assert old_eye_css in s
s = s.replace(old_eye_css, new_eye_css, 1)

old_home = '<button class="tool eye-tool" id="homeBtn" aria-label="Piramida z okiem"><span class="eye-pyramid">△<b>◉</b></span></button>'
new_home = '<button class="tool eye-tool" id="homeBtn" aria-label="Piramida z okiem" title=""><img src="https://cdn-icons-png.flaticon.com/512/1200/1200328.png" alt=""></button>'
assert old_home in s
s = s.replace(old_home, new_home, 1)

old_view = '<button data-menu="view">Widok</button>'
new_view = '<button data-menu="view" title="Tryb nocny">Widok</button>'
assert old_view in s
s = s.replace(old_view, new_view, 1)

old_handlers = '$("backBtn").onclick=()=>{codeStep("back");goYear(-1)};$("forwardBtn").onclick=()=>{codeStep("forward");goYear(1)};$("starBtn").onclick=()=>{codeStep("star");openModal("ULUBIONE",\'<h3>Ulubione zakładki</h3><p>2026 // 2027 // 2028 // DALEJ</p>\')};$("gwBtn").onclick=()=>{codeStep("gw");toast("GOTOWE")};'
new_handlers = '$("backBtn").onclick=()=>codeStep("back");$("forwardBtn").onclick=()=>codeStep("forward");$("starBtn").onclick=()=>codeStep("star");$("gwBtn").onclick=()=>codeStep("gw");$("homeBtn").onclick=()=>{};'
assert old_handlers in s
s = s.replace(old_handlers, new_handlers, 1)

old_view_handler = 'if(m==="view"){document.body.classList.toggle("party-mode");toast("ZMIENIONO WIDOK")};'
new_view_handler = 'if(m==="view"){document.body.classList.toggle("night-mode")};'
assert old_view_handler in s
s = s.replace(old_view_handler, new_view_handler, 1)

assert 'BUILD_021' in s and 'Wersja 0.21.' in s
s = s.replace('BUILD_021', 'BUILD_022', 1)
s = s.replace('Wersja 0.21.', 'Wersja 0.22.', 1)

path.write_text(s, encoding='utf-8')
