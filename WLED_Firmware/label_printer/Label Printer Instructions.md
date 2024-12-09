# Idea
Use Label printer to print labels with WLED SSID + password for every user after flashing. It must be callable from fflashing bash script.

# Solution
Write python script with Inputs:
- SSID (WLED Wifi Name)
- Wifi Pw

The script then
- Creates image of appropriate size with the input text for printing
    - 
- Use [brother_ql_next](https://github.com/LunarEclipse363/brother_ql_next) to print label
    - 


# How to use
- install python3 & pip
- install required packages
    - brother_ql `pip install --upgrade brother_ql_next`
    - image stuff: PIL, ...
- connect printer via USB
- run printer discovery `brother_ql discover`

## Issue Resolution
If you run into permission issues (access denied), follow [this guide](https://github.com/pklaus/brother_ql/issues/97)

# Commands

brother_ql -b pyusb -m QL-800 -p usb://0x04f9:0x209b print -l 62 --red WLED_Firmware/label_printer/test_label.png

brother_ql -b pyusb -m QL-800 -p usb://0x04f9:0x209b status