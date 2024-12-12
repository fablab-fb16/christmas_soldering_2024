# Weihnachtslöten 2024 - Anleitung

Willkommen zum Löten für Weihnachten 2024! 🎄 In dieser Anleitung werden wir gemeinsam ein Tannenbaum-PCB mit einem ESP32, LEDs und einem Button zusammenlöten. Es ist eine großartige Gelegenheit, mehr über Elektronik und Löten zu lernen, während wir ein festliches Projekt erstellen, das auch als Weihnachtsbaum fungiert. ✨

---

## Benötigte Komponenten

Stell sicher, dass du alle folgenden Komponenten zur Hand hast, bevor du mit dem Löten beginnst. 😊

- 1x PCB (Weihnachtsbaum-Design)
- 11x LED
- 1x ESP32 (mit 2x Stiftleiste, einreihig)
- 1x Button
- 2x Stiftleiste 2x8 Pins
- USB-C Kabel

An zusätzlichem Werkzeug brauchst du:
- Lötmaterialien: Lötkolben, Lötzinn
- kleinen Seitenschneider

![Bild: Benötigte Komponenten](/documentation/images/Komponente.png)

---

## Schritt-für-Schritt Anleitung

### 0. Schritt: Vorbereitung der Platine

Mache dich mit der Platine vertraut.

Die Komponenten werden entsprechend den weißen Markierungen auf der Platine platzierst. 🛠️

Festgelötet wird jedes Bauteil dann auf der jeweils gegenüberliegenden Seite der Platine.

Wir führen dich nun Schritt für Schritt durch jedes Bauteil.

![Bild: Vorbereitung der Platine](/documentation/images/PCP.png)

---

### 1. Schritt: Löten des Buttons

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

### 2. Schritt: Platzierung der LEDs

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

### 3. Schritt: Stiftleisten (Pins) auf dem ESP32 löten

Löte dann die **2x8 Pin Header** zuerst fest auf die Platine, wie im Bild gezeigt.

![Bild: 2x8PinHead](/documentation/images/2x8PinHead.png)

---

### 4. Schritt: ESP32 in die Pin Header stecken

Stecke jetzt die Pins des ESP32 in die 2x8 Pin Header und löte sie fest. 🖤

Achte darauf, dass die **kurzen Beine** der Pin Header am ESP32 sind und die **langen Beine** nach unten zeigen. 🔩

<div style="display: flex; justify-content: space-around;">
  <img src="/documentation/images/ESP_mit_Stiftleisten.png" alt="ESP_mit_Stiftleisten" width="200"/>
  <img src="/documentation/images/ESP_auf_dem_Baum.png" alt="ESP auf dem Baum" width="200"/>
  <img src="/documentation/images/ESP_PINS.gif" alt="ESP Pins GIF" width="200"/>
</div>

---

### 5. Schritt: Fertig montierte Platine

Nachdem du alle Komponenten erfolgreich gelötet hast, sollte deine Platine wie folgt aussehen:

![Bild: Fertig montierte Platine](/documentation/images/Baum_fertig.png)

---

### 6. Schritt: WLED Software flashen

<!-- > [!IMPORTANT]
> Dieser Schritt ist nur nötig, wenn du beim Weihnachtslöten bist oder dir den Bausatz selbst zusammengestellt hast. Wenn du einen vorkonfektionierten Bausatz erhalten hast, ist dein ESP schon mit der Software geflasht und du kannst diesen Schritt überspringen. -->

Gehe nun zum Flashen der Software zur **"Flash-Station"**, dort wird die WLED Software auf den Mikrocontroller gespielt. Ohne die Software, leuchten die LEDs nur blau... Sehr blau.

---

### 7. Schritt: Inbetriebnahme & Kurzanleitung

Stecke das USB-C Kabel an den ESP und in ein USB-Netzeil oder eine USB-Powerbank zur Stromversorgung (5V, min. 1A). Der Baum sollte kurz blau leuchten und dann orange.

Du kannst die Reihenfolge und Farben, in denen die Lichter blinken, ändern, indem du kurz auf den Button klickst. Wenn du den Button lange drückst, kannst du die Lichter ein- und ausschalten. 💡

Zusätzlich hat dein Weihnachtsbaum einen WLAN Access Point, mit dem du dich verbinden kannst. Die Zugangsdaten hast du beim flashen auf einem Zettel bekommen.
- Verbinde dein Smartphone mit dem WLAN des Baumes. (WLAN Name z.B. `WLED-AP-c352c7`)
- Entweder dein Smartphone zeigt nach dem Verbinden von selbst eine Meldung an, auf die du klicken musst um zu den Licht-Einstellungen zu kommen
- Falls dein Smartphone dies nicht tut, besuche `4.3.2.1` in deinem Internet Browser.

Über dein Handy kannst du nun die Lichter steuern und die Einstellungen ändern. 📱✨

---

## Glückwunsch! 🎉

Jetzt hast du das kleine Projekt erfolgreich abgeschlossen!

Falls du mehr mit dem Baum und WLED machen möchtest, hier ein paar Inspirationen:
- Synchronisiere das Blinken mehrere Bäume über WLAN (WLED UDP Sync) [DE](https://wled-faq.github.io/#tab5faq4) / [EN](https://kno.wled.ge/interfaces/udp-notifier/)
- anderes Standard-Blinkmuster / Farben beim Anstecken des Baumes einstellen (Preset mit ID erstellen, Preset ID in den `LED Preferences` bei `Apply Preset on Boot` hinterlegen)
- LEDs zu Musik blinken lassen ("audioreactive", braucht zusätzliches Mikrofon) [DE](https://wled-faq.github.io/#tab5faq4) / [EN](https://kno.wled.ge/advanced/audio-reactive/)
- In Smart Home (Home Assistant) einbinden [EN](https://kno.wled.ge/advanced/home-automation/)
- ... (google for more)

---
