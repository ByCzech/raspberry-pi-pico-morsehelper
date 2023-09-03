from machine import Pin
from time import sleep

morse_table = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    " ": "|"
}

morse_lit_length = {
    ".": 0.0625,
    "-": 0.1875,
    "|": 0.0625
}

def char2morse(msg):
    morse = ""
    for char in msg.upper():
        if char in morse_table:
            morse += morse_table.get(char, "")
            morse += "|"

    return morse

def morse_blink(msg, morse_led=Pin("LED", Pin.OUT), verbose=False):
    morse_led.off()
    sleep(.5)
    
    morse_chars = ""
    for char in msg.upper():
        if char not in morse_table:
            break

        morse_chars += morse_table.get(char, "")
        morse_chars += "|"

        if verbose:
            print(char, end="")

        for morse_char in morse_chars:
            morse_led.on()
            sleep(morse_lit_length.get(morse_char, 0.3333))
            morse_led.off()
            sleep(morse_lit_length.get(".", 0.3333))

        morse_chars = ""
    
    if verbose:
        print()

    return


if __name__ == "__main__":
    #print(char2morse("Hello World"))
    morse_blink("Hello World", verbose=True)
