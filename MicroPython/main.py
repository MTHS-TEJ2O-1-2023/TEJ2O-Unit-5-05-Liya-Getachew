"""
Created by: Liya Getachew
Created on: Oct 2023
This module is a Micro:bit MicroPython program that creates a traffic light with Neopixels.
"""

from microbit import *
import neopixel

display.clear()
display.show(Image.HEART)

neopixelStrip = neopixel.NeoPixel(pin16, 4)

while True:
    if button_a.is_pressed():
        display.show(Image.HEART_SMALL)
        neopixelStrip[0] = (0, 225, 0)
        print(neopixelStrip[0])
        neopixelStrip.show()
        sleep(2000)
        neopixelStrip[0] = (0, 0, 0)
        neopixelStrip[1] = (225, 225, 0)
        neopixelStrip.show()
        print(neopixelStrip[1])
        sleep(2000)
        neopixelStrip[1] = (0, 0, 0)
        neopixelStrip[2] = (225, 0, 0)
        neopixelStrip.show()
        print(neopixelStrip[2])
        sleep(2000)
        neopixelStrip[2] = (0, 0, 0)
        print(neopixelStrip[2])
        neopixelStrip.show()
        display.show(Image.HEART)
