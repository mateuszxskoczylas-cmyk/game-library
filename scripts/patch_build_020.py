from pathlib import Path

# trigger BUILD_020
path = Path('index.html')
s = path.read_text(encoding='utf-8')

s = s.replace(
    '.page{background:#f8f4d7;padding:16px;border-top:2px solid #222}.page.minimized{display:none}.hero{',
    '.page{background:#f8f4d7;padding:16px;border-top:2px solid #222}.page.minimized{display:none}.desktop-icons{display:none;position:fixed;left:28px;top:74px;z-index:40;grid-template-columns:84px;gap:22px}.desktop-mode .desktop-icons{display:grid}.desktop-mode #mainWindow .menubar,.desktop-mode #mainWindow .toolbar,.desktop-mode #mainWindow .address-row,.desktop-mode #mainWindow .page{display:none}.desktop-shortcut{width:84px;text-align:center;color:#fff;font:11px/1.15 "MS Sans Serif",Tahoma,Arial,sans-serif;text-shadow:1px 1px 0 #000;user-select:none;pointer-events:none}.desktop-glyph{width:48px;height:48px;margin:0 auto 6px;position:relative}.desktop-glyph.computer:before{content:"";position:absolute;left:5px;top:5px;width:36px;height:27px;background:#65c8e7;border-top:3px solid #fff;border-left:3px solid #fff;border-right:3px solid #4a4a4a;border-bottom:3px solid #4a4a4a;box-shadow:inset 0 0 0 3px #202060}.desktop-glyph.computer:after{content:"";position:absolute;left:15px;top:35px;width:20px;height:6px;background:#c9c9c9;border-top:2px solid #fff;border-left:2px solid #fff;border-right:2px solid #555;border-bottom:2px solid #555;box-shadow:0 5px 0 -1px #c9c9c9}.desktop-glyph.trash:before{content:"";position:absolute;left:12px;top:13px;width:25px;height:29px;background:repeating-linear-gradient(90deg,#e5e5e5 0 4px,#a9a9a9 4px 7px);border:2px solid #555;transform:skew(-2deg)}.desktop-glyph.trash:after{content:"";position:absolute;left:8px;top:8px;width:33px;height:7px;background:#d7d7d7;border-top:2px solid #fff;border-left:2px solid #fff;border-right:2px solid #555;border-bottom:2px solid #555;box-shadow:8px -5px 0 -3px #d7d7d7}.hero{'
)

old_icons_anchor = '<div class="egg-toast" id="toast"></div>'
new_icons = '<div class="desktop-icons" id="desktopIcons" aria-hidden="true"><div class="desktop-shortcut"><div class="desktop-glyph computer"></div><div>Mój komputer</div></div><div class="desktop-shortcut"><div class="desktop-glyph trash"></div><div>Kosz</div></div></div>\n<div class="egg-toast" id="toast"></div>'
assert old_icons_anchor in s
s = s.replace(old_icons_anchor, new_icons, 1)

old_invictus = '{title:"Assassin\'s Creed: Codename Invictus",studio:"Ubisoft",date:"BRAK DATY",sortDate:"9999-12-31",status:"NIEZAPOWIEDZIANE",image:"https://static.wikia.nocookie.net/assassinscreed/images/4/4f/AC_Invictus.jpg/revision/latest?cb=20230720174544&path-prefix=fr"}'
new_invictus = '{title:"Assassin\'s Creed: Codename Invictus",studio:"Ubisoft",date:"BRAK DATY",sortDate:"9999-12-31",status:"NIEZAPOWIEDZIANE",textCover:true}'
assert old_invictus in s
s = s.replace(old_invictus, new_invictus, 1)

old_hexe = '{title:"Assassin\'s Creed: Codename Hexe",studio:"Ubisoft Montreal",date:"BRAK DATY",sortDate:"9999-12-31",status:"NIEZAPOWIEDZIANE",image:"https://static.wikia.nocookie.net/assassinscreed/images/7/73/Hexe_logo.jpg/revision/latest?cb=20220911224333&path-prefix=pl"}'
new_hexe = '{title:"Assassin\'s Creed: Codename Hexe",studio:"Ubisoft Montreal",date:"BRAK DATY",sortDate:"9999-12-31",status:"NIEZAPOWIEDZIANE",textCover:true}'
assert old_hexe in s
s = s.replace(old_hexe, new_hexe, 1)

old_min = '$("minBtn").onclick=()=>$("page").classList.toggle("minimized");'
new_min = '$("minBtn").onclick=()=>{const on=document.body.classList.toggle("desktop-mode");$("page").classList.toggle("minimized",on)};'
assert old_min in s
s = s.replace(old_min, new_min, 1)

assert 'BUILD_019' in s and 'Wersja 0.19.' in s
s = s.replace('BUILD_019', 'BUILD_020', 1)
s = s.replace('Wersja 0.19.', 'Wersja 0.20.', 1)

path.write_text(s, encoding='utf-8')
