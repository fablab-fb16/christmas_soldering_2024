# Parts / Bill of material

You need to order these parts for one kit.

| **Part**                        | **Quantity** | **Exemplary Source**                                                | **Notes**                                   |
| ------------------------------- | ------------ | ------------------------------------------------------------------- | ------------------------------------------- |
| PCB                             | 1            | JLC PCB                                                             | See PCB order instructions below.           |
| ESP32-C3 SUPERMINI              | 1            | [Aliexpress](https://www.aliexpress.com/item/1005007663345442.html) | Should include 2x 8-pin male headers.       |
| RGB LEDs, APA106, 5mm           | 11           | [Aliexpress](https://www.aliexpress.com/item/1005006412040340.html) | Similar to WS2812, they also _should_ work. |
| Push Button 6x6mm               | 1            | [Aliexpress](https://www.aliexpress.com/item/32912263133.html)      |                                             |
| Pin Header female-male **2x8P** | 2            | [Aliexpress](https://www.aliexpress.com/item/1005001781173114.html) | optional, but highly recommended            |
| USB-C Cable                     | 1            | -                                                                   |                                             |

Cost should be under 8€ per kit, if you order parts for at least 4 kits.

# How to order your own PCB

If you want to build the kit, you need the PCB.

We ordered at JLC PCB, so you can just go to their [website](https://jlcpcb.com/), upload our production file [gerber_final_rev1-0_wl_24.zip](gerber_final_rev1-0_wl_24.zip) from this directory and order the boards in your desired quantity.

We recommend to set the option `Mark on PCB` to `Remove Mark`. Other Settings can remain on default values.

Note: If JLC contacts you after ordering because of issues with the footprint of the LEDs, just tell them:
- copper pads of similar size as the holes are fine and should be left like they are in the file
- if the holes need to be resized from 0.9mm to 0.85mm for manufacturing, they can do so.

The LED footprint is custom made for easier soldering and therefore uncommon.

To order at different manufacurers, you need to create production files form the kicad project by yourself.
