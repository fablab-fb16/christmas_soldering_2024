#WLED Firmware

## Benutzung des InstallScriptChristmasSoldering.sh
# Voraussetzungen
Plattform: Linux (Ubuntu, Debian)
Tools: 
1. Python 3
- Installation mit: sudo apt install python3
2. esptool
- Installation mit: sudo pip install esptool (evtl. muss die --break-system-packages Flag mit angegeben werden)

# Für Anwender / Teilnehmer am Weihnachtslöten
1. ESP anstecken
2. Bei Aufforderung: "Flash ESP [y/n] " den Buchstaben "y" eintippen und Enter drücken
3. Warten bis die Ausgabe: "Bitte notieren!" gefolgt von deiner individuellen WLAN SSID und Passwort erscheint. Bitte notiere dir die WLAN SSID. Nur damit findest du später deinen ESP und kannst ihn weiter konfigurieren.
Keine Angst, sollte die Ausgabe bereits verschwunden sein. Du kannst einfach hoch Scrollen um deine WLAN SSID zu sehen.

# Für Developer / Organisatoren
1. Stelle sicher, dass alle Voraussetzungen erfüllt sind
2. Kopiere das Skript und die "firmware.bin" in einen beliebigen Ordner
3. Mach das Skript ausführbar: sudo chmod +x ./InstallScriptChristmasSoldering.sh
4. Starte das Skript mit Root Rechten: sudo ./InstallScriptChristmasSoldering.sh
5. Optional gib den Pfad zur firmware.bin inklusive des Dateinamen und Endung, sowie den Port des ESP ein. Sollte die firmware.bin im aktuellen Verzeichnis liegen kannst du dies wahrscheinlich überspringen.

## Erstellen einer eigenen Firmware
1. Möglichkeit über Standard Installation
Rufe für die Standardmäßige Installation der WLED Firmware die Website: https://install.wled.me/ auf (in Microsoft Edge, Chrome oder einem anderen Chomium basierten Browser) und folge der Installationsanleitung.
2. Möglichkeit über Online Konfigurator
Es gibt einen von der Community bereitgestellten Online Konfigurator in dem man sich seine WLED Firmware selbst zusammen stellen kann. Diesen findest du hier: https://wled-compile.github.io/. Dabei können verschiedene Optionen ein und ausgeschaltet werden, sowie von der Commuinty bereitgestellte Packages installiert werden. Der Konfigurator verfügt auch über ein Installations Tool, welches aus einem Browser (Microsoft Edge, Chrome oder einem anderen Chomium basierten Browser) heraus gestartet werden kann. (Alternativ siehe Möglichkeit 3)
3. Möglichkeit über fertige Binarys (wird für das Weihnachtslöten 2024 verwendet)
Du kannst, wenn du eine fertig kompilierte Binary Datei hast (z.B. über den Online Konfigurator oder wenn du dir dein eigenes Binary aus dem Source Code gebaut hast) diese mithilfe des esptool auf deinem ESP installieren. Folge dazu folgender Anleitung https://kno.wled.ge/basics/install-binary/ oder verwende unser InstallScriptChristmasSoldering.sh. Hier musst du den Pfad zu deinem Binary angeben und den Port des ESP.
