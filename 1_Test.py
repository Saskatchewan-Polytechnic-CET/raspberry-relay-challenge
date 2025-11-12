from gpiozero import LEDBoard
from signal import pause
from time import sleep

# Chase LEDs
leds = LEDBoard(1, 12, 16, 20, 21)
while True:
    for i in range(2):
        for led in leds:
            led.on()
            sleep(0.1)
            led.off()
        for led in reversed(leds):
            led.on()
            sleep(0.1)
            led.off() 