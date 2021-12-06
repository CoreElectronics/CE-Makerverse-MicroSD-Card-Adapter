""" mount_card.py
SD - Pico:
VCC - 3V3
GND - GND
CS - GP13
CLK - GP14
MISO - GP12
MOSI - GP15
"""
from machine import SPI, Pin
import sdcard_rp2, uos

sd = sdcard_rp2.SDCard(SPI(1,sck=Pin(14), mosi=Pin(15), miso=Pin(12)), Pin(13))

print(sd.sectors)

buf = bytearray(512)

sd.readblocks(1024,buf)
print(buf)