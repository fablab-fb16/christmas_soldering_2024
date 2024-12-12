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

Ein Bild der fertig gelöteten Platine zur Orientierung findest du in [Schritt 5: Fertige Platine](#5-schritt-fertig-montierte-platine).

![Bild: Vorbereitung der Platine](/documentation/images/PCP.png)

---

### 1. Schritt: Löten des Buttons

Setze den Button an der vorgesehenen Stelle (SW1) ein. Die Markierung ist auf der Rückseite der Platine.

> [!NOTE]
> Du kannst in diesem Fall den Button auch auf der Vorderseite der Platine platzieren, wenn du möchtest. Auf der Rückseite kann das USB Kabel später vor dem Button liegen und stören. Bei diesem Bauteil kannst du selbst entscheiden, auf welche Seite du es platzierst. 😊

<!-- Nach dem Aufstecken, biege die Beinchen des Buttons etwas nach Innen um, sodass er beim Umdrehen der Platine nicht herausfallen kann.  -->
Löte den Button nun fest. 🔥

Falls du zum ersten Mal lötest und Hilfe brauchst, schau im [How to Solder Guide](/documentation/How%20to%20Solder.md) oder frag uns.

<div style="display: flex; justify-content: space-around;">
  <img src="/documentation/images/Button_vorne.png" alt="Button vorne" width="200"/>
  <img src="/documentation/images/Button_hinten.png" alt="Button hinten" width="200"/>
</div>


<div style="display: flex; justify-content: space-around;">
  <img src="/documentation/images/Button_Platz.png" alt="Button Lötplatz" width="200"/>
  <img src="/documentation/images/Button_platziert.png" alt="Button richtig platziert" width="200"/>
  <img src="/documentation/images/Button_Loetstellen.jpg" alt="Button Lötstellen" width="200"/>
</div>

---

### 2. Schritt: Platzierung der LEDs

Schneide die Beine aller 11 LEDs direkt nach dem dicken Abschnitt ab, wie im Bild gezeigt.
> [!TIP]
>Halte die Beine der LEDs gut fest, während du sie schneidest, damit sie nicht durch den Raum fliegen und dich oder andere verletzen. ⚠️

<div style="display: flex; justify-content: space-around;">
  <img src="/documentation/images/LEDs.png" alt="LED Schritt 1" width="200"/>
  <img src="/documentation/images/Seitenschneider.png" alt="Seitenschneider" width="200"/>
  <img src="/documentation/images/LED_Beine.png" alt="LED Beine" width="200"/>
  <img src="/documentation/images/LED_Beine_Schneiden.png" alt="LED Beine Schneiden" width="200"/>
</div>

Setze die erste LED an der vorgesehenen Stellen ein und achte dabei darauf, dass die flache Seite jeder LED auf die flache Seite der Markierung auf der Platine platziert wird.

> [!CAUTION]
> ❗ Achte auf die korrekte Einbaurichtung ❗

<!-- Abgeflachte Seite der Markierung auf dem Board muss mit flacher Seite der LED übereinstimmen. -->

![Bild: LED Footprint Flach](/documentation/images/LED_Footprint_Flach.jpg)

<div style="display: flex; justify-content: space-around;">
  <img src="/documentation/images/LED_richtig_Platziert.png" alt="LED richtig platziert" width="200"/>
  <img src="/documentation/images/LED_falsch_Platziert.png" alt="LED falsch platziert" width="200"/>
</div>

Dann biege die vier Beine der LED um, jeweils in die Richtung des benachbarten Löt-Pads (siehe Bilder unten), sodass sie fest auf der Platine sitzt. Zum Biegen kannst du z.B. einen kleinen Schlitz-Schraubendreher zur Hilfe nehmen.

> [!CAUTION]
> ❗ Kontrolliere nun nochmal die korrekte Einbaurichtung der LED ❗
> Flach auf flach!

Löte die umgebogenen Beine der LED nun an den Pads fest, wie auf dem Bild unten zu sehen (NICHT an den Löchern, durch die die Beinchen gesteckt sind).

Wiederhole diese Schritte für alle weiteren LEDs. 🛠️

<div style="display: flex; justify-content: space-around;">
  <img src="/documentation/images/LED_Biegung.png" alt="LED Biegung" width="200"/>
  <img src="/documentation/images/LED_Biegung_geloetet.jpg" alt="LED gelötet" width="200"/>
</div>
---

### 3. Schritt: 2x8 Pin-Header auf die Platine löten

Löte dann die beiden **2x8 Pin Header** auf die Platine, wie im Bild gezeigt.

![Bild: 2x8PinHeader](/documentation/images/2x8PinHead.png)
![Bild: 2x8PinHeader vorne](/documentation/images/2x8PinHead_Vorderseite.jpg)

---

### 4. Schritt: ESP32 in die Pin-Header stecken

Stecke jetzt den ESP32 mit seinen beiden Pin-Leisten in die inneren Reihen der 2x8 Pin-Header. Die USB-C Buchse muss zur Spitze des Baumes zeigen. 🔝

<div style="display: flex; justify-content: space-around;">
  <img src="/documentation/images/ESP_mit_Stiftleisten.png" alt="ESP_mit_Stiftleisten" width="200"/>
  <img src="/documentation/images/ESP_PINS.gif" alt="ESP Pins GIF" width="200"/>
  <img src="/documentation/images/ESP_auf_dem_Baum.png" alt="ESP auf dem Baum" width="200"/>
</div>

> [!IMPORTANT]
>Achte darauf, dass die **langen Beine** der Pin-Leisten nach unten in den Pin-Header zeigen und die **kurzen Beine** am ESP-Board sind.

![Bild: Pin-Leiste Orientierung](/documentation/images/ESP_aufstecken_1.jpg)
![Bild: ESP Aufgesteckt](/documentation/images/ESP_aufstecken_3.jpg)

Nun kannst du bequem alle 16 Pins des ESP-Boards an die Pin-Leisten löten. 🔥

Achte dabei darauf, mit dem Lötkolben keine Komponenten auf dem ESP-Board zu beschädigen. Löte dafür am besten immer mit dem Lötkolben von außen und nicht über dem ESP-Board.

<div style="display: flex; justify-content: space-around;">
  <img src="/documentation/images/ESP_Loeten_right.jpg" alt="ESP Löten richtig" width="300"/>
  <img src="/documentation/images/ESP_Loeten_wrong.jpg" alt="ESP Löten falsch" width="300"/>
</div>

> [!NOTE]
> Nach dem Löten lässt sich das ESP-Board trotzdem einfach wieder herausziehen, z.B. falls es mal getauscht werden muss (defekt) oder du es für ein anderes Projekt verwenden willst.

---

### 5. Schritt: Fertig montierte Platine

Nachdem du alle Komponenten erfolgreich gelötet hast, sollte deine Platine wie folgt aussehen:

<!-- ![Bild: Fertig montierte Platine](/documentation/images/Baum_fertig.png) -->
![Bild: Fertig montierte Platine](/documentation/images/Platine_fertig_vorne.jpg)
![Bild: Fertig montierte Platine](/documentation/images/Platine_fertig_hinten.jpg)

> [!IMPORTANT]
> Die USB-C Buchse des ESP muss nach oben zur Baumspitze zeigen. Falls nicht, ziehe den ESP ab und stecke ihn richtigherum wieder auf.

---

### 6. Schritt: Software flashen

<!-- > [!IMPORTANT]
> Dieser Schritt ist nur nötig, wenn du beim Weihnachtslöten bist oder dir den Bausatz selbst zusammengestellt hast. Wenn du einen vorkonfektionierten Bausatz erhalten hast, ist dein ESP schon mit der Software geflasht und du kannst diesen Schritt überspringen. -->

Gehe nun zum Flashen der Software zur **"Flash-Station"**, dort wird die WLED Software auf den Mikrocontroller gespielt. Ohne die Software leuchten die LEDs nur blau... sehr blau. 🔵

---

### 7. Schritt: Inbetriebnahme & Kurzanleitung

Stecke das USB-C Kabel an den ESP und in ein USB-Netzeil oder eine USB-Powerbank zur Stromversorgung (5V, min. 1A). Der Baum sollte kurz blau leuchten und dann orange.

Du kannst die Reihenfolge und Farben, in denen die Lichter blinken, ändern, indem du kurz auf den Button klickst. Wenn du den Button lange drückst, kannst du die Lichter ein- und ausschalten. 💡

Zusätzlich hat dein Weihnachtsbaum einen WLAN Access Point, mit dem du dich verbinden kannst. Die Zugangsdaten hast du beim flashen auf einem Zettel bekommen.
- Verbinde dein Smartphone mit dem WLAN des Baumes. (WLAN Name z.B. `WLED-AP-c352c7`)
- Entweder dein Smartphone zeigt nach dem Verbinden von selbst eine Meldung an, auf die du klicken musst um zu den Licht-Einstellungen zu kommen...
- Falls dein Smartphone dies nicht tut, besuche `4.3.2.1` in deinem Internet Browser.

Über dein Handy kannst du nun die Lichter steuern und die Einstellungen ändern. 📱✨

Alternativ gibt's auch eine App:

<a href='https://play.google.com/store/apps/details?id=ca.cgagnier.wlednativeandroid&utm_source=github&pcampaignid=pcampaignidMKT-Other-global-all-co-prtnr-py-PartBadge-Mar2515-1'><img alt='Get it on Google Play' src='https://play.google.com/intl/en_us/badges/static/images/badges/en_badge_web_generic.png' height='80'/></a>

<a href='https://apps.apple.com/us/app/wled-native/id6446207239'><img alt='Get it on Apple App Store' src='https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Download_on_the_App_Store_Badge.svg/320px-Download_on_the_App_Store_Badge.svg.png' height='50'/></a>

---

## Glückwunsch! 🎉

Jetzt hast du das kleine Projekt erfolgreich abgeschlossen!

Falls du mehr mit dem Baum und WLED machen möchtest, hier ein paar Inspirationen:
- Synchronisiere das Blinken mehrere Bäume über WLAN (WLED UDP Sync) [DE](https://wled-faq.github.io/#tab5faq4) / [EN](https://kno.wled.ge/interfaces/udp-notifier/)
- anderes Standard-Blinkmuster / Farben beim Anstecken des Baumes einstellen (Preset mit ID erstellen, Preset ID in den `LED Preferences` bei `Apply Preset on Boot` hinterlegen)
- LEDs zu Musik blinken lassen ("audioreactive", braucht zusätzliches Mikrofon, kann über freie Steckplätze auf den Pin-Headern direkt angeschlossen werden) [DE](https://wled-faq.github.io/#tab5faq4) / [EN](https://kno.wled.ge/advanced/audio-reactive/)
- In Smart Home (Home Assistant) einbinden [EN](https://kno.wled.ge/advanced/home-automation/)
- ... (google for more)

---
