# 🎄 Christmas Soldering 2024 🎄

Home of the Christmas Soldering project for 2024.

You will find everything you need to build your own in here.

---

## 👀 Overview

**Hardware:** Custom PCB with **ESP-C3-SUPERMINI** and addressable **RGB LEDs**.
Designed by Janos Föth.

**Software:** The awesome [WLED](https://github.com/Aircoookie/WLED) for an easy start to get lights blinking. (we got a pre-configured version for you)

![PCB Front Side](/documentation/images/Overview.png)

### ✨ Features

- **Interactive**: Change light patterns using the button or via WiFi / App.
- **Extensible**: Add a microphone to make the LEDs blink to the beat of music, integrate it with your smart home or write your own custom code to control the blinking.
- **Festive**: A glowing, Christmas tree-themed project perfect for the holidays.

---

## 📚 Quick Start

Find step-by-step instructions here, if you already have the soldering-kit at hand:

- [Detaillierte Anleitung (DE)](/documentation/Build%20Instructions%20DE.md)
- [Detailed Assembly Instructions (EN)](/documentation/Build%20Instructions%20EN.md)
- For beginners in soldering: [How to Solder Guide](/documentation/How%20to%20Solder.md)


---

## 🛠 How to Build Your Own from Scratch

You can order the parts and build the blinking tree totally on your own.

1. See the [Hardware Instructions](/pcb_christmas_soldering_kit/Hardware_Instructions.md) for a list of needed parts and instructions on how to order the board (PCB).
2. When you have the ESP32 at hand, follow [Software Instructions](/WLED_Firmware/Readme.md) to get the WLED firmware flashed. We have a pre-configured version for the soldering kit that you just need to flash.
3. Solder the kit, following the [Detailed Assembly Instructions (EN)](/documentation/Build%20Instructions%20EN.md) / [Detaillierte Anleitung (DE)](/documentation/Build%20Instructions%20DE.md)
4. Enjoy the lights.

---

## 👩‍🏭 Usage at Soldering Workshops

This kit was developed for a soldering workshop and therefore to be solder-beginner-friendly.

Feel free to use it for your own soldering workshops. If you got ideas for improvement or feedback, please let us know e.g. via a github issue or email at ![email address image](/documentation/images/email.png)

For getting a large amount of ESPs flashed efficiently, we developed a flash script plus the support to print the unique SSID+PW of each ESP on small labels with Brother QL Label Printers directly after flashing. Find instructions for it [here](/WLED_Firmware/Readme.md). This way, everyone at the event knows which Wifi Access Point belongs to his Blinking Tree.
