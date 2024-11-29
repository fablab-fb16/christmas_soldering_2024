# WLED Firmware

** English Version below **

## Verwendung des InstallScriptChristmasSoldering.sh
# Voraussetzungen
Plattform: Linux (Ubuntu, Debian)
Tools: 
1. Python 3
	- Installation: sudo apt install python3
2. esptool
	- Installation mit: sudo pip install esptool (evtl. muss die Option --break-system-packages mit angegeben werden)

# Für Anwender / Teilnehmer am Weihnachtslöten
1. ESP einstecken
2. Bei der Aufforderung: "Flash ESP [y/n] " den Buchstaben "y" eingeben und Enter drücken
3. Warte bis die Ausgabe: " Bitte notieren " gefolgt von deiner individuellen WLAN SSID und deinem Passwort erscheint. Bitte notiere dir die WLAN SSID. Nur so kannst du später dein ESP wiederfinden und weiter konfigurieren.
Keine Sorge, wenn die Ausgabe schon verschwunden ist. Du kannst einfach nach oben scrollen, um deine WLAN SSID zu sehen.

# Für Entwickler / Organisatoren
1. Stelle sicher, dass alle Voraussetzungen erfüllt sind
2. Kopiere das Skript und die "firmware.bin" in ein beliebiges Verzeichnis.
3. Mach das Skript ausführbar: sudo chmod +x ./InstallScriptChristmasSoldering.sh
4. Starte das Skript mit root-Rechten: sudo ./InstallScriptChristmasSoldering.sh
5. Optional den Pfad zur firmware.bin inklusive Dateiname und Dateiendung sowie den Port des ESP angeben. Wenn sich die firmware.bin im aktuellen Verzeichnis befindet, kann man das wahrscheinlich überspringen.

## Erstellung eigener Firmware
1. Möglichkeit über die Standardinstallation
Für die Standard-Installation der WLED-Firmware gehe auf die Webseite: https://install.wled.me/ (in Microsoft Edge, Chrome oder einem anderen Chomium-basierten Browser) und folge den Installationsanweisungen.
2. Möglichkeit über Online-Konfigurator
Es gibt einen Online Konfigurator, der von der Community zur Verfügung gestellt wird und mit dem man seine eigene WLED Firmware zusammenstellen kann. Dieser ist hier zu finden: https://wled-compile.github.io/. Hier kann man verschiedene Optionen an- und ausschalten und von der Community bereitgestellte Pakete installieren. Der Konfigurator verfügt auch über ein Installationstool, welches aus einem Browser (Microsoft Edge, Chrome oder einem anderen Chomium basierten Browser) heraus gestartet werden kann. (Alternativ siehe Möglichkeit 3)
3. Möglichkeit über fertige Binarys (wird für das Weihnachtslöten 2024 verwendet)
Wenn du eine fertig kompilierte Binärdatei hast (z.B. über den Online Konfigurator oder wenn du deine eigene Binärdatei aus dem Quellcode gebaut hast), kannst du diese mit Hilfe des esptool auf deinem ESP installieren. Folge dazu folgender Anleitung https://kno.wled.ge/basics/install-binary/ oder verwende unser InstallScriptChristmasSoldering.sh. Hier musst du den Pfad zu deinem Binary und den Port des ESP angeben.

** English Version **

## Use of InstallScriptChristmasSoldering.sh
# Requirements
Platform: Linux (Ubuntu, Debian)
Tools: 
1. python 3
	- Installation: sudo apt install python3
2. esptool
	- Installation with: sudo pip install esptool (you may need to specify the --break-system-packages option)

# For users / participants in Christmas soldering
1. plug in the ESP
2. at the prompt: ‘Flash ESP [y/n] “ enter the letter ”y’ and press Enter
3. wait until the message: ‘ Please note ’ appears followed by your individual WLAN SSID and your password. Please make a note of the WLAN SSID. This is the only way you can find your ESP again later and continue configuring it.
Don't worry if the message has already disappeared. You can simply scroll up to see your WLAN SSID.

# For developers / organisers
1. make sure that all requirements are met
2. copy the script and the ‘firmware.bin’ to any directory.
3. make the script executable: sudo chmod +x ./InstallScriptChristmasSoldering.sh
4. start the script with root rights: sudo ./InstallScriptChristmasSoldering.sh
5. optionally enter the path to firmware.bin including file name and file extension as well as the port of the ESP. If the firmware.bin is located in the current directory, you can probably skip this.

## Creating your own firmware
1st option via the standard installation
For the standard installation of the WLED firmware, go to the website: https://install.wled.me/ (in Microsoft Edge, Chrome or another Chomium-based browser) and follow the installation instructions.
2nd option via online configurator
There is an online configurator provided by the community that you can use to create your own WLED firmware. This can be found here: https://wled-compile.github.io/. Here you can switch various options on and off and install packages provided by the community. The configurator also has an installation tool that can be started from a browser (Microsoft Edge, Chrome or another Chomium-based browser). (Alternatively, see option 3)
3rd option via ready-made binaries (will be used for Christmas soldering 2024)
If you have a fully compiled binary file (e.g. via the online configurator or if you have built your own binary file from the source code), you can install it on your ESP using the esptool. To do this, follow the instructions at https://kno.wled.ge/basics/install-binary/ or use our InstallScriptChristmasSoldering.sh. Here you must enter the path to your binary and the port of the ESP.
