"""Generate small, self-contained SVG profile artwork using Python's standard library."""
from html import escape
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets"
PALETTES = {
    "dark": dict(bg="#0c1513", panel="#13221d", ink="#e2efe8", muted="#a0b8aa", line="#2a3e33", accent="#37c69b"),
    "light": dict(bg="#fcfdfc", panel="#f2f6f3", ink="#14261f", muted="#53665b", line="#dae5dc", accent="#178262"),
}
CSS = """
text{font-family:'Segoe UI',Arial,sans-serif} .muted{fill:var(--muted)}
.signal{animation:wave 7s ease-in-out infinite;transform-box:fill-box;transform-origin:center}
.pulse{animation:pulse 6s ease-in-out infinite;transform-box:fill-box;transform-origin:center}
.packet{stroke-dasharray:30 300;animation:travel 7s linear infinite}
.trace{animation:trace 7s ease-in-out infinite;transform-box:fill-box;transform-origin:left}
.orbit{animation:orbit 18s linear infinite;transform-origin:1050px 195px}
.check{animation:check 7s ease-in-out infinite}
@keyframes wave{0%,100%{transform:scaleY(.5);opacity:.35}50%{transform:scaleY(1);opacity:.9}}
@keyframes pulse{0%,100%{transform:scale(.85);opacity:.45}50%{transform:scale(1.15);opacity:1}}
@keyframes travel{to{stroke-dashoffset:-660}}
@keyframes trace{0%,100%{transform:scaleX(.55)}50%{transform:scaleX(1)}}
@keyframes orbit{to{transform:rotate(360deg)}}
@keyframes check{0%,100%{opacity:.4}40%{opacity:1}}
@media(prefers-reduced-motion:reduce){*{animation:none!important}}
"""

def svg(theme, name, height, content, title):
    p = PALETTES[theme]
    variables = ";".join(f"--{k}:{v}" for k, v in p.items())
    text = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{height}" viewBox="0 0 1200 {height}" role="img" aria-labelledby="title" style="{variables}">
<title id="title">{escape(title)}</title>
<style>{CSS}</style>
<defs><radialGradient id="glow"><stop stop-color="{p['accent']}" stop-opacity=".16"/><stop offset="1" stop-color="{p['bg']}" stop-opacity="0"/></radialGradient></defs>
<rect width="1200" height="{height}" rx="22" fill="{p['bg']}"/>
{content}
</svg>'''
    ET.fromstring(text)
    (OUT / f"{name}-{theme}.svg").write_text(text + "\n", encoding="utf-8")

def hero(theme):
    p = PALETTES[theme]
    bars = []
    for i in range(30):
        h = [34, 75, 116, 55, 148, 92, 64][i % 7]
        bars.append(f'<rect class="signal" x="{890 + i * 8}" y="{200 - h/2}" width="3" height="{h}" rx="1.5" fill="{p["accent"]}" style="animation-delay:-{i*.23:.2f}s"/>')
    content = f'''
<ellipse cx="1000" cy="160" rx="330" ry="270" fill="url(#glow)"/>
<circle class="pulse" cx="51" cy="54" r="6" fill="{p['accent']}"/>
<text x="72" y="62" fill="{p['muted']}" font-size="24" letter-spacing="4">AKSHAT MISHRA</text>
<text x="44" y="168" fill="{p['ink']}" font-size="76" font-weight="600" letter-spacing="-4">Building apps.</text>
<text x="44" y="255" fill="{p['ink']}" font-size="76" font-weight="600" letter-spacing="-4">Improving open source.</text>
<text x="47" y="323" fill="{p['muted']}" font-size="28">Python · TypeScript · SQL</text>
<text x="47" y="371" fill="{p['muted']}" font-size="24">Build with purpose. Follow the evidence. Keep improving.</text>
{''.join(bars)}
<path d="M46 410 H1154" stroke="{p['line']}" fill="none"/>
<path class="packet" d="M46 410 H1154" stroke="{p['accent']}" stroke-width="2" fill="none"/>
'''
    svg(theme, "signal-hero", 440, content, "Akshat Mishra — Building apps. Improving open source. Python, TypeScript and SQL.")

def trail(theme):
    p = PALETTES[theme]
    content = f'<path d="M150 74 H1050" stroke="{p["line"]}" stroke-width="2" fill="none"/><path class="packet" d="M150 74 H1050" stroke="{p["accent"]}" stroke-width="3" fill="none"/>'
    for i, (x, label) in enumerate([(150, "BUILD"), (600, "TEST"), (1050, "CONTRIBUTE")]):
        content += f'<circle cx="{x}" cy="74" r="18" fill="{p["bg"]}" stroke="{p["line"]}" stroke-width="2"/><circle class="pulse" cx="{x}" cy="74" r="7" fill="{p["accent"]}" style="animation-delay:-{i*2}s"/><text x="{x}" y="130" text-anchor="middle" font-size="26" letter-spacing="3" fill="{p["muted"]}">{label}</text>'
    svg(theme, "build-trail", 162, content, "Build → Test → Contribute")

def workbench(theme):
    p = PALETTES[theme]
    c = ""
    for x, label, sub in [(24, "IncidentLab", "TRACE THE FAILURE"), (418, "RepoLens", "FOLLOW THE CHANGE"), (812, "SkillCheck", "CHECK THE RESULT")]:
        c += f'<rect x="{x}" y="16" width="364" height="255" rx="16" fill="{p["panel"]}"/><text x="{x+24}" y="63" font-size="31" font-weight="600" fill="{p["ink"]}">{label}</text><text x="{x+24}" y="98" font-size="17" letter-spacing="2" fill="{p["muted"]}">{sub}</text>'
    for i, (y, w) in enumerate([(140, 280), (178, 210), (216, 125)]):
        c += f'<rect class="trace" x="48" y="{y}" width="{w}" height="13" rx="4" fill="{p["accent"]}" opacity=".7" style="animation-delay:-{i*2}s"/>'
    c += f'<path d="M478 182 H718" stroke="{p["line"]}" stroke-width="2" fill="none"/><path class="packet" d="M478 182 H718" stroke="{p["accent"]}" stroke-width="3" fill="none"/>'
    for i, x in enumerate([480, 590, 700]):
        c += f'<circle cx="{x}" cy="182" r="23" fill="{p["bg"]}" stroke="{p["line"]}" stroke-width="2"/><circle class="pulse" cx="{x}" cy="182" r="8" fill="{p["accent"]}" style="animation-delay:-{i*2}s"/>'
    for i in range(3):
        x = 850 + i * 100
        c += f'<rect x="{x}" y="149" width="68" height="68" rx="15" fill="{p["bg"]}"/><path class="check" d="M{x+18} 182 l10 10 23 -25" stroke="{p["accent"]}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" fill="none" style="animation-delay:-{i*2}s"/>'
    svg(theme, "workbench", 288, c, "Three recent builds: IncidentLab traces services, RepoLens follows code dependencies, and SkillCheck evaluates coding checks. Illustrative graphics, not application screenshots.")

if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    for theme in PALETTES:
        hero(theme)
        trail(theme)
        workbench(theme)
    print(f"Generated {len(list(OUT.glob('*.svg')))} SVG assets.")
