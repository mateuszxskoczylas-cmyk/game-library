from pathlib import Path

path = Path("index.html")
s = path.read_text(encoding="utf-8")

if "BUILD_016" not in s:
    raise SystemExit("Expected BUILD_016")


def rep(old: str, new: str) -> None:
    global s
    if old not in s:
        raise SystemExit(f"Missing expected fragment: {old[:180]!r}")
    s = s.replace(old, new, 1)


rep(
    '.hero-card{background:rgba(255,255,255,.92);border:2px solid var(--ink);padding:18px;max-width:880px;box-shadow:6px 6px 0 var(--purple)}.kicker{',
    '.hero-layout{display:flex;align-items:flex-start;justify-content:space-between;gap:20px}.hero-card{background:rgba(255,255,255,.92);border:2px solid var(--ink);padding:18px;max-width:880px;flex:1;box-shadow:6px 6px 0 var(--purple)}.tga-window{width:255px;flex:0 0 255px;background:#d6d6d6;border-top:2px solid #fff;border-left:2px solid #fff;border-right:2px solid #444;border-bottom:2px solid #444;box-shadow:5px 5px 0 var(--purple)}.tga-titlebar{display:flex;align-items:center;gap:6px;padding:4px 6px;background:linear-gradient(90deg,#0d7dad,var(--sky));color:#fff;font:700 10px "Courier New",monospace}.tga-titlebar .app-icon{flex:0 0 17px}.tga-body{padding:10px 10px 11px;text-align:center;background:#ececec;border-top:1px solid #fff}.tga-logo{display:block;width:88px;height:68px;object-fit:contain;margin:0 auto 7px}.tga-kicker{font:700 9px "Courier New",monospace;color:var(--purple);letter-spacing:.06em}.tga-date{margin:3px 0 2px;font:900 20px Georgia,"Times New Roman",serif;color:#111}.tga-sub{font:700 9px "Courier New",monospace;color:var(--pink)}.kicker{'
)

rep(
    '<div class="page" id="page"><section class="hero"><div class="hero-card"><div class="kicker">// ARCHIWUM_GIER.EXE</div><h1>Nadchodzące premiery</h1><p>Strona zaprojektowana po to, żeby udowodnić, że gry jednak wychodzą — i czasem jest ich naprawdę sporo.</p></div></section>',
    '<div class="page" id="page"><section class="hero"><div class="hero-layout"><div class="hero-card"><div class="kicker">// ARCHIWUM_GIER.EXE</div><h1>Nadchodzące premiery</h1><p>Strona zaprojektowana po to, żeby udowodnić, że gry jednak wychodzą — i czasem jest ich naprawdę sporo.</p></div><aside class="tga-window" aria-label="The Game Awards"><div class="tga-titlebar"><span class="app-icon">★</span><span>THE_GAME_AWARDS.EXE</span></div><div class="tga-body"><img class="tga-logo" src="https://upload.wikimedia.org/wikipedia/commons/e/e8/The_Game_Awards_Logo_2024.svg" alt="The Game Awards"><div class="tga-kicker">GAME OF THE YEAR</div><div class="tga-date">10 GRUDNIA</div><div class="tga-sub">CEREMONIA // 2026</div></div></aside></div></section>'
)

rep(
    '<span id="buildText" class="build-hold">BUILD_016</span>',
    '<span id="buildText" class="build-hold">BUILD_017</span>'
)

rep(
    '<p>Wersja 0.16. Wszystko działa. Prawdopodobnie.</p>',
    '<p>Wersja 0.17. Wszystko działa. Prawdopodobnie.</p>'
)

rep(
    '@media(max-width:700px){.desktop{',
    '@media(max-width:900px){.hero-layout{flex-wrap:wrap}.tga-window{width:min(100%,320px);flex-basis:320px;margin-left:auto}}@media(max-width:700px){.desktop{'
)

path.write_text(s, encoding="utf-8")
print("Patched to BUILD_017")
