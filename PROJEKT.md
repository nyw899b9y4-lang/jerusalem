# Jerusalem – Oben und Unten · Projektübergabe

Stand: 6. November 2026. Kartografisch-künstlerische Arbeit: Esri-Satellitenbild als „Unten“, hebräische Kalligraphie des himmlischen Jerusalem (von Gabriel) als „Oben“, mit digitalen Buchstabenebenen aus Psalm 119.

## Orte

| Was | Wo |
|---|---|
| **Hauptquelle** (Online-Fassung mit Satellitenbild) | `index.html` in diesem Repository |
| Öffentliche Seite | https://nyw899b9y4-lang.github.io/jerusalem/ (GitHub Pages, `main`, Wurzel). Browser speichern bis 10 min zwischen → zum Prüfen `?v=N` anhängen |
| Repository | https://github.com/nyw899b9y4-lang/jerusalem (Claude-GitHub-App installiert, Schreibrecht nur für dieses Repo) |
| Lesefassung (Claude-Artefakt, ohne Satellit) | https://claude.ai/artifact/V1A2G6EYPC42Xq4YKWh9Ly |
| Prüffassung (Artefakt, mit Prüfzeichen zum Verschieben) | https://claude.ai/artifact/EQJp4Xv7VLf8fkjpGtJXjy |
| Tehillim-119-Lernseite (Clipgrenzen, Wortzeiten, Datenbank `clips_adler`) | https://claude.ai/artifact/5Ffibe7sZTuuK3M3gucHxK |
| Mem-Fenster Jes 9,6 / Neh 2,13 (Codex Leningradensis) | https://claude.ai/artifact/42kMrP37yuJ6zRLiii3LkX |
| Audio: Alexander Adler, Mem-Verse 97–104 | `audio/adler_v97.mp3` … `adler_v104.mp3` (zusätzlich als data-URI in der Seite) |

## Arbeitsablauf (sparsam)

1. Repository holen: `git clone --depth 1 https://github.com/nyw899b9y4-lang/jerusalem`
2. **Nur `index.html` ändern.** Die übrigen Fassungen werden abgeleitet:
   `python3 werkzeug/baue.py` → `aus/Jerusalem-Oben-Unten-Lesefassung.html` (Download, offline) und `aus/oben-unten-lesefassung.html` (Artefakt). Das Skript prüft die JS-Syntax.
3. Testen mit Playwright/Chromium (`file://…/index.html`, Netz sperren: `page.route(/^https?:/, r => r.abort())`; Kacheln fehlen dann, alles andere läuft). iPhone: `devices['iPhone 13']`.
4. `git commit` + `git push` → Seite in ~1 min aktuell. Git-Verlauf ersetzt die früheren `_vorher`-Sicherungskopien.
5. Nur bei Bedarf: Artefakt Lesefassung mit `aus/oben-unten-lesefassung.html` neu veröffentlichen.
6. **Prüffassung und alte Vollfassung (`jerusalem-oben-unten.html`) sind eingefroren** (Stand 6.11.); nur für neue Korrekturrunden mit Prüfzeichen wieder aufnehmen.

Wünsche möglichst gesammelt schicken (mehrere Änderungen pro Runde) – das spart Durchläufe.

## Geometrie

- Kalligraphie 4538 × 6000 px; Bildmitte auf 31.7742992 N / 35.2336878 O, Drehung 3°, 1,143047 m pro Bildpixel. In 16 Kacheln (iOS).
- `bildZuGeo(x, y)` und `geoZuBild(lat, lon)` im Code.
- Goldener Kreis (Polar 782): Mitte X 2416,78 / Y 2595,40 (das Aleph, Schnitt der Achsen), r 1333,76 px, 782 Segmente.
- Lagecodes der Buchstaben: 0 Zeile unten, 1 Spalte links (90°), 2 Zeile oben (kopfüber), 3 Spalte rechts (270°).

## Ebenen (Abschnitte in index.html, Kommentar `// ---- …`)

| Ebene | Inhalt |
|---|---|
| Polar 782 | 30 Buchstaben von וישם לך שלום (Num 6,26) am Kreis; die 3 großen blauen sind offene מ (Mem-Fenster beim Berühren); Achsen schneiden im Aleph |
| Waw | Ps 119,41–48, 213 Buchstaben (`WAW_BST`), 8 Anfangs-Waw orange, Umlauflinien gelb in den Zeilenlücken |
| Resch | Ps 119,153–160, 215 Buchstaben (`RESCH_BST`), Initialen türkis |
| Chet | 8 große ח an den Strahlenden je Tor, hellgelb; unter Schwärze hebräische Tornamen (weiß, 32) |
| Mem | Ps 119,97–104, 213 Buchstaben (`MEM_BST`, `MEM_VERS`, `MEM_INITS`), innerste Spirale in zwei Windungen; Klick spielt Vers; Wortleuchten türkis (`MEM_WORT`, `MEM_WZEIT`) |
| Frequenz-Lupe | im leeren Strahlfeld NO des Quadrats, Umriss aus der Tinte (`LUPE_FELD`), Fluss innen→außen, 0–2500 Hz quer zur Mittellinie |

**Abweichungen der Kalligraphie** (weiß, Fenster mit ganzem Vers, Knopf „Gabriel check up“):
1. Waw V. 46 „ולא אבוש“ – 2. א fehlt („ולא נבוש“) – X 1833 / Y 2887
2. Mem V. 104 „ארח“ → „ארך“ – X 2066 / Y 2799
3. Mem V. 103 „אמרתך“ – ך fehlt – X 2637 / Y 2837

## Bedienung der Online-Fassung

- Start: nur Satellitenbild + „סֹבּוּ צִיּוֹן“; nur **Antippen** startet (Wischen nicht – sonst kein Ton).
- Intro: Kalligraphie 70 → 100 → aus · Schwärze (7,5 s) · חֵילוֹתֶיהָ 2 s · רוּחַ 2 s · Psalmtext, Kalligraphie 100 %. Ton: ganze Mem-Strophe ab dem Antippen.
- Menü: Kalligraphie + Regler · Buchstaben und Polar 782 · Schwärze · Ton · חֵילוֹתֶיהָ (Waw→ו, Resch→ר, Mem ab V. 98 → מַיִם) · רוּחַ (zusätzlich Waw/Resch/Chet hellblau) · Gabriel check up.
- Startzoom je Gerät: goldener Kreis füllt den Ausschnitt (MacBook 14″ ≈ 15,25, iPhone ≈ 13,75); eine halbe Stufe darunter nur Tor-Punkte (Name beim Überfahren).
- Zoomstufe beim Überfahren von +/−; Mauskoordinaten (GPS + Bild-X/Y) daneben.
- Mar Saba: vorerst ausgeblendet (Koordinaten im Code).

## Arbeitsstand außerhalb der Seite (nicht im Repo)

- Großes ם auf dem Tempelberg segmentiert (Fläche ≈ 5250 m², Innenraum ≈ 1570 m²) mit Ost-Vektor im oberen und West-Vektor im unteren Balken (geografisch, Breitengrad konstant) – noch nicht in die Seite integriert.
- Tafeln: Bauphasen der Westmauer; die 30 Schofar-Töne mit den Zeichen der Jewish Encyclopedia.

## Gewohnheiten

- Antworten auf Deutsch; Hebräisch mit Nikud, Aussprache kursiv; Übersetzungen eigene, nah am Wortlaut; Quellen nennen.
- Bevorzugter Browser am Mac: Edge; Gerät unterwegs: iPhone.
