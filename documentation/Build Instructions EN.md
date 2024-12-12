# Christmas Soldering 2024 - Instructions

Welcome to Christmas Soldering 2024! 🎄 In this guide, we will solder a Christmas tree PCB with an ESP32, LEDs, and a button. This is a great opportunity to learn about electronics and soldering while creating a festive project that doubles as a Christmas tree. ✨

---

## Required Components

Make sure you have all the following components ready before starting. 😊

- 1x PCB (Christmas tree design)
- 11x LEDs
- 1x ESP32 (with 2x single-row pin headers)
- 1x Button
- 2x 2x8-pin headers
- USB-C cable  

Additional tools:  
- Soldering supplies: soldering iron, solder
- Small wire cutters  

![Image: Required Components](/documentation/images/Komponente.png)

---

## Step-by-Step Instructions

### Step 0: Preparing the PCB  

Familiarize yourself with the PCB.  

Place the components according to the white markings on the PCB. 🛠️ Solder each component on the opposite side of the PCB.  

We will guide you through each component step by step.  

Refer to [Step 5: Finished PCB](#step-5-finished-pcb) for an image of the completed board.

![Image: PCB Preparation](/documentation/images/PCP.png)

---

### Step 1: Soldering the Button  

Insert the button into the designated spot (SW1). The marking is on the back of the PCB.  

> **Note:**  
> You can place the button on the front side of the PCB if you prefer. The USB cable may get in the way if the button is placed on the back. Choose the placement that works best for you. 😊  

Solder the button in place. 🔥  

If this is your first time soldering and you need help, check the [How to Solder Guide](/documentation/How%20to%20Solder.md) or ask us.

<div style="display: flex; justify-content: space-around;">
  <img src="/documentation/images/Button_vorne.png" alt="Button front" width="200"/>
  <img src="/documentation/images/Button_hinten.png" alt="Button back" width="200"/>
</div>

<div style="display: flex; justify-content: space-around;">
  <img src="/documentation/images/Button_Platz.png" alt="Button placement" width="200"/>
  <img src="/documentation/images/Button_platziert.png" alt="Button positioned" width="200"/>
  <img src="/documentation/images/Button_Loetstellen.jpg" alt="Button soldered" width="200"/>
</div>

---

### Step 2: Placing the LEDs

Cut the legs of all 11 LEDs just after the thick section, as shown in the image.

> **Tip:**  
> Hold the LED legs firmly while cutting them to prevent them from flying across the room and causing injury. ⚠️  

<div style="display: flex; justify-content: space-around;">
  <img src="/documentation/images/LEDs.png" alt="LED Step 1" width="200"/>
  <img src="/documentation/images/Seitenschneider.png" alt="Wire Cutters" width="200"/>
  <img src="/documentation/images/LED_Beine.png" alt="LED Legs" width="200"/>
  <img src="/documentation/images/LED_Beine_Schneiden.png" alt="Cutting LED Legs" width="200"/>
</div>

Insert the first LED into its designated spot, ensuring that the flat side of the LED matches the flat side of the marking on the PCB.

> **Caution:**  
> ❗ Ensure the correct orientation of the LED ❗  

![Image: LED Footprint Flat](/documentation/images/LED_Footprint_Flach.jpg)

<div style="display: flex; justify-content: space-around;">
  <img src="/documentation/images/LED_richtig_Platziert.png" alt="LED Correctly Placed" width="200"/>
  <img src="/documentation/images/LED_falsch_Platziert.png" alt="LED Incorrectly Placed" width="200"/>
</div>

Bend the four legs of the LED toward the adjacent solder pads (as shown in the images) to secure it. You can use a small flathead screwdriver to assist with bending.

> **Caution:**  
> ❗ Double-check the LED's orientation before soldering. The flat sides must align! ❗

Solder the bent legs of the LED to the pads (do not solder at the holes where the legs are inserted). 

Repeat these steps for all remaining LEDs. 🛠️

<div style="display: flex; justify-content: space-around;">
  <img src="/documentation/images/LED_Biegung.png" alt="LED Bending" width="200"/>
  <img src="/documentation/images/LED_Biegung_geloetet.jpg" alt="LED Soldered" width="200"/>
</div>

---

### Step 3: Soldering the 2x8 Pin Headers

Solder both **2x8 Pin Headers** onto the PCB as shown in the images.

![Image: 2x8PinHeader](/documentation/images/2x8PinHead.png)
![Image: 2x8PinHeader Front](/documentation/images/2x8PinHead_Vorderseite.jpg)

---

### Step 4: Inserting the ESP32

Insert the ESP32 with its pin headers into the inner rows of the 2x8 pin headers. The USB-C port should point toward the tree's tip. 🔝

<div style="display: flex; justify-content: space-around;">
  <img src="/documentation/images/ESP_mit_Stiftleisten.png" alt="ESP with Pin Headers" width="200"/>
  <img src="/documentation/images/ESP_PINS.gif" alt="ESP Pins GIF" width="200"/>
  <img src="/documentation/images/ESP_auf_dem_Baum.png" alt="ESP on the Tree" width="200"/>
</div>

> **Important:**  
> Ensure that the **long pins** of the headers point down into the pin sockets and the **short pins** are on the ESP board.

![Image: Pin Header Orientation](/documentation/images/ESP_aufstecken_1.jpg)
![Image: ESP Inserted](/documentation/images/ESP_aufstecken_3.jpg)

Now, solder all 16 pins of the ESP board to the pin headers. 🔥  

Be careful not to damage components on the ESP board. Solder from the outside, not over the board.

<div style="display: flex; justify-content: space-around;">
  <img src="/documentation/images/ESP_Loeten_right.jpg" alt="Correct Soldering" width="300"/>
  <img src="/documentation/images/ESP_Loeten_wrong.jpg" alt="Incorrect Soldering" width="300"/>
</div>

> **Note:**  
> After soldering, the ESP board can be easily removed if needed for another project.

---

### Step 5: Finished PCB

Once all components are soldered, your PCB should look like this:

![Image: Finished PCB Front](/documentation/images/Platine_fertig_vorne.jpg)
![Image: Finished PCB Back](/documentation/images/Platine_fertig_hinten.jpg)

> **Important:**  
> Ensure the USB-C port points upward toward the tree's tip. If not, remove and reposition the ESP.

---

### Step 6: Flashing the Software

Go to the **"Flash Station"** to upload the WLED software to the microcontroller. Without the software, the LEDs will only glow blue... very blue. 🔵

---

### Step 7: Powering Up & Quick Guide

Connect the USB-C cable to the ESP and plug it into a USB power supply or USB power bank (5V, min. 1A). The tree should briefly light up blue and then orange.

You can change the sequence and colors of the blinking lights by clicking the button. Press and hold the button to turn the lights on and off. 💡

Additionally, your Christmas tree has a Wi-Fi access point that you can connect to. The login credentials were provided during flashing.

- Connect your smartphone to the tree's Wi-Fi (e.g., `WLED-AP-c352c7`).
- Your smartphone may prompt you with a notification to access the light settings.
- If not, visit `4.3.2.1` in your web browser.

Use your smartphone to control the lights and change settings. 📱✨

Alternatively, there are mobile apps available:

<a href='https://play.google.com/store/apps/details?id=ca.cgagnier.wlednativeandroid&utm_source=github&pcampaignid=pcampaignidMKT-Other-global-all-co-prtnr-py-PartBadge-Mar2515-1'><img alt='Get it on Google Play' src='https://play.google.com/intl/en_us/badges/static/images/badges/en_badge_web_generic.png' height='80'/></a>

<a href='https://apps.apple.com/us/app/wled-native/id6446207239'><img alt='Get it on Apple App Store' src='https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Download_on_the_App_Store_Badge.svg/320px-Download_on_the_App_Store_Badge.svg.png' height='50'/></a>

---

## Congratulations! 🎉

You've successfully completed the project!

If you want to do more with your tree and WLED, here are some inspirations:

- Synchronize multiple trees over Wi-Fi (WLED UDP Sync) [DE](https://wled-faq.github.io/#tab5faq4) / [EN](https://kno.wled.ge/interfaces/udp-notifier/)
- Set a different default blinking pattern or colors when powering on the tree (create a preset with an ID and set it in `LED Preferences` under `Apply Preset on Boot`)
- Make LEDs blink to music ("audioreactive" requires an additional microphone that can be connected to spare pin headers) [DE](https://wled-faq.github.io/#tab5faq4) / [EN](https://kno.wled.ge/advanced/audio-reactive/)
- Integrate with a smart home system (Home Assistant) [EN](https://kno.wled.ge/advanced/home-automation/)
- ... (Google for more)

---

