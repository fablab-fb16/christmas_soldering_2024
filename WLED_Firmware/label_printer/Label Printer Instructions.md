# Idea
Use Label printer to print labels with WLED SSID + password for every ESP after flashing. It must be callable from flashing bash script.

# Solution
Write python script with Inputs:
- SSID (WLED Wifi Name)
- Wifi PW

The script then
- Creates temporary image of appropriate size with the input text for printing
- Uses [brother_ql_next](https://github.com/LunarEclipse363/brother_ql_next) to print label on Brother QL Label Printer

Tested on Linux (Ubuntu/Mint).

# How to use
- install python3 & pip
- install required packages
    - brother_ql `pip install --upgrade brother_ql_next`
- connect printer via USB **and turn it on**
- run printer discovery `brother_ql discover` should give some usb id output
- some vaules in the script are hardcoded to printer model QL-800, 62mm wide paper. If you use other, please adjust in `print_label.py` file. For infos on parameters, image sizes etc, see [brother_ql_next Docs](https://github.com/LunarEclipse363/brother_ql_next)
- run a test print: `python3 print_label.py -test`

## Issue Resolution
If you run into permission issues (access denied), follow [this guide](https://github.com/pklaus/brother_ql/issues/97)

## Misc brother_ql Commands from development

`brother_ql -b pyusb -m QL-800 -p usb://0x04f9:0x209b print -l 62 --red WLED_Firmware/label_printer/test_label.png`

`brother_ql -b pyusb -m QL-800 -p usb://0x04f9:0x209b status`
