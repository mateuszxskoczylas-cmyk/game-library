from pathlib import Path

path = Path('index.html')
s = path.read_text(encoding='utf-8')
old = '.desktop-shortcut{width:92px;text-align:center;cursor:default;pointer-events:auto;color:#fff;font:700 10px/1.15 "Tahoma","MS Sans Serif",Arial,sans-serif;text-shadow:1px 1px 0 #4b2a82,0 0 4px #7a41ce;letter-spacing:.02em;user-select:none;pointer-events:none}'
new = '.desktop-shortcut{width:92px;text-align:center;cursor:default;pointer-events:auto;color:#fff;font:700 10px/1.15 "Tahoma","MS Sans Serif",Arial,sans-serif;text-shadow:1px 1px 0 #4b2a82,0 0 4px #7a41ce;letter-spacing:.02em;user-select:none}'
assert old in s
s = s.replace(old, new, 1)
path.write_text(s, encoding='utf-8')
