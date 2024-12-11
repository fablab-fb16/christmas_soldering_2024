#!/bin/bash

# Schritt 1: Prüfen auf Root-Rechte
if [[ $EUID -ne 0 ]]; then
    echo "Fehler: Bitte als Root ausführen."
    exit 1
fi

# Einmalige Abfrage des Pfads für die Firmware
echo "Bitte die benötigten Binaries im aktuellen Verzeichnis des Skriptes ablegen! (Benötigte Binaries: bootloader.bin, partitions.bin, boot_app0.bin, firmware.bin)"

#Einmalige Abfrage des Geräte Ports
read -p "Bitte geben Sie den Port des Gerätes ein [/dev/ttyACM0]: " dev_port
dev_port=${dev_port:-/dev/ttyACM0}

while true; do
    # Schritt 1: Ausgabe leeren
    terminal_lines=$(tput lines)

    # Ausgabe nach oben schieben
    for ((i=1; i<=terminal_lines; i++)); do
        echo ""
    done

    # Welcome Bildschirm
    printf "%-45s%s\n" "****************************************" "      *"
    printf "%-45s%s\n" "*                                      *" "     ***"
    printf "%-45s%s\n" "*         Weihnachtslöten 2024         *" "     *****"
    printf "%-45s%s\n" "*                                      *" "   *******"
    printf "%-45s%s\n" "****************************************" "  *********"
    printf "%53s\n" "     ***"
    printf "%53s\n" "     ***"

    # Anleitung zum flashen printen
    echo ""
    echo "Bitte schließe deinen ESP an das USB-Kabel an. Drücke anschließend die Enter-Taste, um den ESP zu flashen."


    # Schritt 2: Abfrage an den Benutzer
    read -p "Press Enter to flash ESP: " choice
    if [[ -z "$choice" ]]; then
        # Befehl ausführen und auf Beendigung warten
        # Speicher löschen
        python3 -m esptool --port "$dev_port" erase_flash
        # Firmware flashen
        # python3 -m esptool --chip esp32c3 --port "$dev_port" --baud 460800 --before default_reset --after hard_reset write_flash -z --flash_mode dout --flash_freq 80m --flash_size 4MB 0x0 "$firmware_path"
        python3 -m esptool --port "$dev_port" --chip esp32c3 --baud 460800 --before default_reset --after hard_reset write_flash -z --flash_mode dout --flash_freq 80m --flash_size 4MB 0x0000 ./bootloader.bin 0x8000 ./partitions.bin 0xe000 ./boot_app0.bin 0x10000 ./WLED_0.14.4_ESP32-C3.bin
    else
        # Zurück zu Schritt 2
        continue
    fi

    # Schritt 3: MAC-Adresse auslesen und Rückgabe speichern
    output=$(python3 -m esptool read_mac)

    # Schritt 4: MAC-Adresse extrahieren
    mac_lines=$(echo "$output" | grep -E "MAC: ")
    mac=$(echo "$mac_lines" | tail -n 1 | awk '{print $2}')
    mac_no_colons=$(echo "$mac" | tr -d ':')
    stripped_mac=${mac_no_colons: -6}
    wlan_name="WLED-AP-$stripped_mac"

    # Schritt 5: Gestrippte MAC-Adresse ausgeben
    printf "%-45s%s\n" "****************************************"
    printf "%-45s%s\n" "*                                      *"
    printf "%-45s%s\n" "*           Bitte notieren!            *"
    printf "%-45s%s\n" "*                                      *"
    printf "%-45s%s\n" "****************************************"
    echo "Dein ESP hat die WLAN SSID: ${wlan_name}"
    echo "Das Passwort ist: wled1234"

    # Schritt 6: Label mit Label Drucker erstellen
    python3 ./label_printer/print_label.py "${wlan_name}" "wled1234" > /dev/null

    # Optional: Warten bis Nutzer aktiv Schleife neu startet
    # read -n 1 -s -r -p "Drücke eine beliebige Taste, um fortzufahren..."
done
