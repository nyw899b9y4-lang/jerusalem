#!/usr/bin/env python3
"""Baut aus index.html (Hauptquelle, Online-Fassung mit Satellitenbild) die beiden abgeleiteten Fassungen:

  aus/Jerusalem-Oben-Unten-Lesefassung.html  Download-Datei: ohne Satellitenbild, läuft ohne Internet
  aus/oben-unten-lesefassung.html             Claude-Artefakt: ohne Satellitenbild, Leaflet vom CDN
                                              (Artefakte sperren fremde Bildquellen)

Aufruf:  python3 werkzeug/baue.py          (im Repository-Ordner)
Prüft zusätzlich die Skript-Syntax mit node, falls vorhanden.
"""
import os, re, subprocess, sys, tempfile

HIER = os.path.dirname(os.path.abspath(__file__)); WURZEL = os.path.dirname(HIER)
QUELLE = os.path.join(WURZEL, 'index.html'); AUS = os.path.join(WURZEL, 'aus')

KACHELN = re.compile(r"// Satellitenbild als Bezugssystem \(Esri World Imagery\)\nL\.tileLayer\(.*?\.addTo\(map\);", re.S)
OHNE_KACHELN = "// Satellitenbild entfällt in dieser Fassung: fremde Bildquellen sind hier gesperrt."
LEAFLET_INLINE = re.compile(r"<script>\s*/\* @preserve\s*\* Leaflet 1\.9\.4.*?</script>", re.S)
LEAFLET_CDN = '<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.js"></script>'

def pruefe(html, name):
    js = re.findall(r'<script>(.*?)</script>', html, re.S)[-1]
    with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False) as f: f.write(js)
    try:
        r = subprocess.run(['node', '--check', f.name], capture_output=True, text=True)
        print(f'  {name}: Syntax', 'ok' if r.returncode == 0 else 'FEHLER\n' + r.stderr[:800])
        return r.returncode == 0
    except FileNotFoundError:
        print('  (node nicht gefunden, Syntaxprüfung übersprungen)'); return True
    finally: os.unlink(f.name)

def main():
    h = open(QUELLE, encoding='utf-8').read()
    assert KACHELN.search(h), 'Kachel-Block nicht gefunden'
    assert LEAFLET_INLINE.search(h), 'eingebettetes Leaflet nicht gefunden'
    ok = pruefe(h, 'index.html')
    os.makedirs(AUS, exist_ok=True)
    dl = KACHELN.sub(OHNE_KACHELN, h, count=1).replace('<title>Jerusalem – Oben und Unten</title>', '<title>Oben und Unten Lesefassung</title>', 1)
    open(os.path.join(AUS, 'Jerusalem-Oben-Unten-Lesefassung.html'), 'w', encoding='utf-8').write(dl)
    art = LEAFLET_INLINE.sub(lambda m: LEAFLET_CDN, dl, count=1)
    open(os.path.join(AUS, 'oben-unten-lesefassung.html'), 'w', encoding='utf-8').write(art)
    for n in ('Jerusalem-Oben-Unten-Lesefassung.html', 'oben-unten-lesefassung.html'):
        print(f'  aus/{n}: {os.path.getsize(os.path.join(AUS, n)) // 1024} KB')
    sys.exit(0 if ok else 1)

if __name__ == '__main__': main()
