# Lötabend Weihnachten 2024 - Build Instructions

Willkommen zu unserem Lötabend für Weihnachten 2024! In dieser Anleitung werden wir 
gemeinsam ein PCB mit einem ESP32, LEDs und einem Button zusammenlöten. Es ist eine 
großartige Gelegenheit, mehr über Elektronik und Löten zu lernen, während wir ein 
festliches Projekt erstellen, das auch als Weihnachtsbaum fungiert.

---

## Benötigte Komponenten

Stellen Sie sicher, dass Sie alle folgenden Komponenten zur Hand haben, bevor Sie 
mit dem Löten beginnen:

- 1 x PCB (Weihnachtsbaum-Design)
- 11 x LEDs
- 1 x ESP32 (mit Stiftleisten)
- 1 x Button
- Diverse Lötmaterialien (Lötkolben, Lötzinn, Drahtschneider)
- USB-C Kabel

![Bild: Benötigte Komponenten](/documentation/images/Komponente.png)

---

## Schritt-für-Schritt Anleitung

### 1. Schritt: Vorbereitung der Platine

Beginnen Sie mit der Vorbereitung der Platine. Stellen Sie sicher, dass Sie die
Komponenten entsprechend den Markierungen auf der Platine platzieren.

![Bild: Vorbereitung der Platine](/documentation/images/PCP.png)

---

### 2. Schritt: Löten des Buttons

Setzen Sie den Button an der vorgesehenen Stelle ein und löten Sie ihn fest.

<div style="display: flex; justify-content: space-around;">
  <img src="/documentation/images/Button_vorne.png" alt="Button vorne" width="200"/>
  <img src="/documentation/images/Button_hinten.png" alt="Button hinten" width="200"/>
  <img src="/documentation/images/Button_Platz.png" alt="Button Lötplatz" width="200"/>
  <img src="/documentation/images/Button_platziert.png" alt="Button richtig platziert" width="200"/>
</div>

---

### 3. Schritt: Platzierung der LEDs

Schneiden Sie die Beine der LEDs direkt nach dem dicken Abschnitt ab, wie im Bild gezeigt.
Verwenden Sie einen Seitenschneider, um die Beine auf die richtige Länge zu kürzen, damit
die LED gut auf der Platine sitzt.

<div style="display: flex; justify-content: space-around;">
  <img src="/documentation/images/LEDs.png" alt="LED Schritt 1" width="200"/>
  <img src="/documentation/images/Seitenschneider.png" alt="Seitenschneider" width="200"/>
  <img src="/documentation/images/LED_Beine.png" alt="LED_Beine" width="200"/>
  <img src="/documentation/images/LED_Beine_Schneiden.png" alt="LED Beine Schneiden" width="200"/>
</div>

Setzen Sie die LEDs an den vorgesehenen Stellen ein und beachten Sie dabei, dass die
flache Seite jedes LEDs auf die flache Seite der Platine platziert wird, wie im Bild gezeigt.

<div style="display: flex; justify-content: space-around;">
  <img src="/documentation/images/LED_richtig_Platziert.png" alt="LED richtig platziert" width="200"/>
  <img src="/documentation/images/LED_falsch_Platziert.png" alt="LED falsch platziert" width="200"/>
</div>

und löten Sie sie fest.

---

### 4. Schritt: Stiftleisten (Pins) auf dem ESP32 löten

Setzen Sie den ESP32 an den entsprechenden Stellen der Platine ein.

<div style="display: flex; justify-content: space-around;">
  <img src="/documentation/images/ESP_mit_Stiftleisten.png" alt="ESP_mit_Stiftleisten" width="200"/>
  <img src="/documentation/images/ESP_auf_dem_Baum.png" alt="ESP auf dem Baum" width="200"/>
</div>

Löten Sie zuerst die Pins des ESP32.
Legen Sie den ESP32 dann beiseite und löten Sie den schwarzen Pin-Halter auf der Platine.

![Bild: Vorbereitung ESP32](/documentation/images/ESP_mit_Stiftleisten.png)

---

### 5. Schritt: Fertig montierte Platine

Nachdem Sie alle Komponenten erfolgreich gelötet haben, sollte Ihre Platine wie folgt aussehen.

![Bild: Fertig montierte Platine](/documentation/images/Baum_fertig.png)

---

## Glückwunsch!

Jetzt hast du das kleine Projekt erfolgreich abgeschlossen! Du kannst die Reihenfolge, in der die Lichter blinken, ändern, indem du einmal auf den Button klickst. Wenn du den Button lange drückst, kannst du die Lichter ein- und ausschalten.

Zusätzlich hat dein Weihnachtsbaum jetzt einen Access Point, mit dem du dich verbinden kannst. Über dein Handy kannst du die Lichter steuern und die Einstellungen ändern.