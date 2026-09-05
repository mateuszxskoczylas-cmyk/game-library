from pathlib import Path

path = Path("index.html")
s = path.read_text(encoding="utf-8")

if "BUILD_017" not in s:
    raise SystemExit("Expected BUILD_017")


def rep(old: str, new: str) -> None:
    global s
    if old not in s:
        raise SystemExit(f"Missing expected fragment: {old[:180]!r}")
    s = s.replace(old, new, 1)


rep('<div class="tga-sub">CEREMONIA // 2026</div>', '')

needle = '{title:"The Witcher Remake",studio:"Fool\'s Theory / CD PROJEKT RED",date:"BRAK DATY",sortDate:"9999-12-31",status:"NIEZAPOWIEDZIANE",textCover:true},'
addition = '{title:"Lollipop Chainsaw — New Game",studio:"Dragami Games / NADA HOLDINGS",date:"BRAK DATY",sortDate:"9999-12-31",status:"ZAPOWIEDZIANE",image:"https://i0.wp.com/bloody-disgusting.com/wp-content/uploads/2026/09/lollipopchainsaw.jpg?fit=900%2C580&ssl=1"},\n'
rep(needle, addition + needle)

rep('BUILD_017', 'BUILD_018')
rep('Wersja 0.17.', 'Wersja 0.18.')

path.write_text(s, encoding="utf-8")
