# Lötabend Weihnachten 2024 - Build Instructions

Willkommen zu unserem Lötabend für Weihnachten 2024! 🎄 In dieser Anleitung werden wir gemeinsam ein PCB mit einem ESP32, LEDs und einem Button zusammenlöten. Es ist eine großartige Gelegenheit, mehr über Elektronik und Löten zu lernen, während wir ein festliches Projekt erstellen, das auch als Weihnachtsbaum fungiert. ✨

---

## Benötigte Komponenten

Stell sicher, dass du alle folgenden Komponenten zur Hand hast, bevor du mit dem Löten beginnst. 😊 Nimm die Teile aus den Boxen und zähle sie, damit du nichts vergisst!

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

Beginne mit der Vorbereitung der Platine. Stelle sicher, dass du die Komponenten entsprechend den Beschriftungen auf der Platine platzierst. 🛠️

![Bild: Vorbereitung der Platine](/documentation/images/PCP.png)

---

### 2. Schritt: Löten des Buttons

Setze den Button an der vorgesehenen Stelle (SW1) ein und löte ihn fest. 🔥 

<div style="display: flex; justify-content: space-around;">
  <img src="/documentation/images/Button_vorne.png" alt="Button vorne" width="200"/>
  <img src="/documentation/images/Button_hinten.png" alt="Button hinten" width="200"/>
</div>

Du kannst den Button auch auf der Vorderseite der Platine platzieren, wenn du möchtest. In diesem Fall ist das der bessere Platz, da das USB-Kabel nicht vor dem Button liegt. Aber du kannst selbst entscheiden, auf welche Seite du ihn platzierst. 😊

<div style="display: flex; justify-content: space-around;">
  <img src="/documentation/images/Button_Platz.png" alt="Button Lötplatz" width="200"/>
  <img src="/documentation/images/Button_platziert.png" alt="Button richtig platziert" width="200"/>
</div>

---

### 3. Schritt: Platzierung der LEDs

Schneide die Beine der LEDs direkt nach dem dicken Abschnitt ab, wie im Bild gezeigt. **Wichtig:** Halte die Beine der LEDs gut fest, während du sie schneidest, damit sie nicht durch den Raum fliegen und dich oder andere verletzen. ⚠️

<div style="display: flex; justify-content: space-around;">
  <img src="/documentation/images/LEDs.png" alt="LED Schritt 1" width="200"/>
  <img src="/documentation/images/Seitenschneider.png" alt="Seitenschneider" width="200"/>
  <img src="/documentation/images/LED_Beine.png" alt="LED Beine" width="200"/>
  <img src="/documentation/images/LED_Beine_Schneiden.png" alt="LED Beine Schneiden" width="200"/>
</div>

❗❗❗ **Setze die LEDs an den vorgesehenen Stellen ein und achte dabei darauf, dass die flache Seite jeder LED auf die flache Seite der Platine platziert wird.** ❗❗❗

<div style="display: flex; justify-content: space-around;">
  <img src="/documentation/images/LED_richtig_Platziert.png" alt="LED richtig platziert" width="200"/>
  <img src="/documentation/images/LED_falsch_Platziert.png" alt="LED falsch platziert" width="200"/>
</div>

Dann biege die Beine der LEDs um, sodass sie fest auf der Platine sitzen, und löte sie erst dann fest. 🛠️

![Bild: LED Biegung](/documentation/images/LED_Biegung.png)

---

### 4. Schritt: Stiftleisten (Pins) auf dem ESP32 löten

Löte dann die **2x8 Pin Header** zuerst fest auf die Platine, wie im Bild gezeigt.

![Bild: 2x8PinHead](/documentation/images/2x8PinHead.png)

---

### 5. Schritt: ESP32 in die Pin Header stecken

Stecke jetzt die Pins des ESP32 in die 2x8 Pin Header und löte sie fest. 🖤

Achte darauf, dass die **kurzen Beine** der Pin Header am ESP32 sind und die **langen Beine** nach unten zeigen. 🔩

<div style="display: flex; justify-content: space-around;">
  <img src="/documentation/images/ESP_mit_Stiftleisten.png" alt="ESP_mit_Stiftleisten" width="200"/>
  <img src="/documentation/images/ESP_auf_dem_Baum.png" alt="ESP auf dem Baum" width="200"/>
  <img src="/documentation/images/ESP_PINS.gif" alt="ESP Pins GIF" width="200"/>
</div>

---

### 6. Schritt: Fertig montierte Platine

Nachdem du alle Komponenten erfolgreich gelötet hast, sollte deine Platine wie folgt aussehen:

![Bild: Fertig montierte Platine](/documentation/images/Baum_fertig.png)

---

## Glückwunsch! 🎉

Jetzt hast du das kleine Projekt erfolgreich abgeschlossen! Du kannst die Reihenfolge, in der die Lichter blinken, ändern, indem du einmal auf den Button klickst. Wenn du den Button lange drückst, kannst du die Lichter ein- und ausschalten. 💡

Zusätzlich hat dein Weihnachtsbaum jetzt einen Access Point "Wifi", mit dem du dich verbinden kannst. Über dein Handy kannst du die Lichter steuern und die Einstellungen ändern. 📱✨

---