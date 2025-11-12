# Binary encoding exercise template
# GPIOZERO guide: https://raspberrytips.com/gpio-zero-guide-raspberry-pi/
from gpiozero import LEDBoard
from signal import pause
from time import sleep

# Setup the board
# Pins: https://raspberrytips.com/wp-content/uploads/2024/12/pinout_bcm_board-1.jpg
leds = LEDBoard(1, 12, 16, 20, 21)

# Turn on LED if HIGH or blink if LOW
def act(led,state):
    led.on() if state else led.blink(0.1)

# Indicate the start of a transmission
def start(leds):
    for i in range(2):
        for led in leds:
            led.on()
            sleep(0.1)
            led.off()
        for led in reversed(leds):
            led.on()
            sleep(0.1)
            led.off()       

# Apply a bit pattern to a set of LEDS
def apply_pattern(leds,pattern):
    for i,p in enumerate(pattern):
        act(leds[i],p)

# Indicate the end of a transmission
def stop(leds):
    for led in leds:
        led.blink(0.1,0.1,10)

# Main loop
while True:
    # Wait for user to send a message
    response = input("Send a message? (y/N)> ")
    if not(response.strip() == "y" or response.strip() == "Y"):
        continue

    # Enter the message
    message = input("Enter your message> ")

    # Confirm
    response = input(f"Is this your message: '{message}'? (y/N)> ")
    if not(response.strip() == "y" or response.strip() == "Y"):
        continue
    response = ""

    print("")
    print("="*50)
    print("= T R A N S M I S S I O N")
    print("="*50)

    # Wait to send a START signal
    while response != "y" and response != "Y":
        response = input("Send START? (y/N)> ")
    start(leds)
    response = ""

    print("")

    # Transmit the nibbles
    for w in message:
        # Convert the character to an ASCII number
        value = ord(w)
        # Get the upper and lower parts 
        upper = (value >> 4) & 0xF
        lower = value & 0xF

        # Wait to send the high part
        while response != "y" and response != "Y":
          response = input(f"Send high part of '{w}' ({format(upper, '04b')})? (y/N)> ")
        pattern = [1] + [int(d) for d in format(upper, '04b')]
        print(f"PATTERN SENT: {pattern}")
        apply_pattern(leds,pattern)
        response = "" 

        # Wait top send the low part
        while response != "y" and response != "Y":
          response = input(f"Send low part of '{w}' ({format(lower, '04b')})? (y/N)> ")
        pattern = [0] + [int(d) for d in format(lower, '04b')]
        print(f"PATTERN SENT: {pattern}")
        apply_pattern(leds,pattern)
        response = ""

        print("")

    # Wait to send a STOP signal
    while response != "y" and response != "Y":
        response = input("Send STOP? (y/N)> ")
    stop(leds)
    response = ""

    print("="*50)
    print("= E N D")
    print("="*50)
    print("")


