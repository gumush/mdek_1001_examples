# Examples for MDEK 1001 Devkit 
These codes written in Python3.6 and runs on Raspberry Pi Zero W 
First try these codes please do not forget to enable serial communication over raspi-config
These codes simplifies to connec unit over serial and send UART commands.

Example Usage 
```
# read anchors list
read_msg("la")
# read unit modes
read_msg("nmg")
# read accelerometer values
read_msg("av")
