# WLED Firmware 💻

** English Version below **

## Verwendung des InstallScriptChristmasSoldering.sh
### Für Anwender / Teilnehmer am Weihnachtslöten
1. ESP einstecken
2. Bei der Aufforderung: "Press Enter to flash ESP:" --> Enter-Taste drücken
3. Warte bis die Ausgabe: " Bitte notieren " gefolgt von deiner individuellen WLAN SSID und deinem Passwort erscheint. Es sollte außerdem automatisch ein Label mit den Informationen ausgedruckt werden. Falls nicht, notiere dir bitte die WLAN SSID und das Passwort.
Keine Sorge, wenn die Ausgabe verschwunden ist. Du kannst einfach nach oben scrollen, um deine WLAN SSID zu sehen.

Siehe unten: "Eigene Firmware erstellen", wenn du die Firmware zu Hause neu installieren möchtest.

### Für Entwickler / Organisatoren
#### Voraussetzungen
Plattform: Linux (Ubuntu, Debian)
Tools: 
1. Python 3
	- Installation: `sudo apt install python3`
2. esptool
	- Installation mit: `sudo pip install esptool` (evtl. muss die Option --break-system-packages mit angegeben werden)
3. brother_ql
   	- Installation mit: `sudo pip install --upgrade brother_ql_next` (evtl. muss die Option --break-system-packages mit angegeben werden)

#### Verwendung
1. Stelle sicher, dass alle Voraussetzungen erfüllt sind
2. Kopiere das Skript und alle benötigten Binaries (bootloader.bin, partitions.bin, boot_app0.bin, firmware.bin) in ein beliebiges Verzeichnis.
3. Wechsel in das Verzeichnis (cd /Pfad/zum/Verzeichnis) und mach das Skript ausführbar: sudo chmod +x ./InstallScriptChristmasSoldering.sh
4. Starte das Skript mit root-Rechten: sudo ./InstallScriptChristmasSoldering.sh
5. Optional den Port des ESP angeben.

## Erstellung eigener Firmware
1. Möglichkeit über die Standardinstallation (empfohlen)
Für die Standard-Installation der WLED-Firmware gehe auf die Webseite: https://install.wled.me/ (in Microsoft Edge, Chrome oder einem anderen Chomium-basierten Browser) und folge den Installationsanweisungen.
2. Möglichkeit über Online-Konfigurator
Es gibt einen Online Konfigurator, der von der Community zur Verfügung gestellt wird und mit dem man seine eigene WLED Firmware zusammenstellen kann. Dieser ist hier zu finden: https://wled-compile.github.io/. Hier kann man verschiedene Optionen an- und ausschalten und von der Community bereitgestellte Pakete installieren. Der Konfigurator verfügt auch über ein Installationstool, welches aus einem Browser (Microsoft Edge, Chrome oder einem anderen Chomium basierten Browser) heraus gestartet werden kann. (Alternativ siehe Möglichkeit 3)
3. Möglichkeit über fertige Binarys (wird für das Weihnachtslöten 2024 verwendet)
Wenn du eine fertig kompilierte Binärdatei hast (z.B. über den Online Konfigurator oder wenn du deine eigene Binärdatei aus dem Quellcode gebaut hast), kannst du diese mit Hilfe des esptool auf deinem ESP installieren. Folge dazu folgender Anleitung https://kno.wled.ge/basics/install-binary/ oder verwende unser InstallScriptChristmasSoldering.sh. Hier musst du den Pfad zu deinem Binary und den Port des ESP angeben. Fertige Binaries findest du in diesem Ordner des Repositorys.

---------------------------------------------------------------------------
** English Version **

## Use of InstallScriptChristmasSoldering.sh
### For users / participants in Christmas soldering
1. Plug in the ESP
2. At the prompt: ‘Press Enter to flash ESP:’ --> press the Enter button
3. Wait until the message: ‘Bitte notieren’ appears followed by your individual WLAN SSID and your password. A label with the information should also be printed out automatically. If not, please make a note of the WLAN SSID and password.
Don't worry if the output has disappeared. You can simply scroll up to see your WLAN SSID.

See below: ‘Creating your own firmware’ if you want to reinstall the firmware at home.

### For developers / organisers
#### Requirements
Platform: Linux (Ubuntu, Debian)
Tools: 
1. python 3
	- Installation: `sudo apt install python3`
2. esptool
	- Installation with: `sudo pip install esptool` (you may need to specify the --break-system-packages option)
3. brother_ql
   	- Installation with: `sudo pip install --upgrade brother_ql_next` (you may need to specify the --break-system-packages option)

#### Usage
1. make sure that all requirements are met
2. copy the script and all required binaries (bootloader.bin, partitions.bin, boot_app0.bin, firmware.bin) to any directory.
3. Change to the directory (cd /path/to/directory) and make the script executable: sudo chmod +x ./InstallScriptChristmasSoldering.sh
4. start the script with root rights: sudo ./InstallScriptChristmasSoldering.sh
5. optionally enter the port of the ESP. 

## Creating your own firmware
1. option via the standard installation (recommended)
For the standard installation of the WLED firmware, go to the website: https://install.wled.me/ (in Microsoft Edge, Chrome or another Chomium-based browser) and follow the installation instructions.
2. option via online configurator
There is an online configurator provided by the community that you can use to create your own WLED firmware. This can be found here: https://wled-compile.github.io/. Here you can switch various options on and off and install packages provided by the community. The configurator also has an installation tool that can be started from a browser (Microsoft Edge, Chrome or another Chomium-based browser). (Alternatively, see option 3)
3. option via ready-made binaries (will be used for Christmas soldering 2024)
If you have a fully compiled binary file (e.g. via the online configurator or if you have built your own binary file from the source code), you can install it on your ESP using the esptool. To do this, follow the instructions at https://kno.wled.ge/basics/install-binary/ or use our InstallScriptChristmasSoldering.sh. Here you must enter the path to your binary and the port of the ESP.
