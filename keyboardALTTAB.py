import time
import digitalio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)

btn_pin = board.GP15
btn=digitalio.DigitalInOut(btn_pin)
btn.direction= digitalio.Direction.INPUT
btn.pull = digitalio.Pull.DOWN


while True:
    if btn.value:
        print("ALT+TAB pressed")
        keyboard.press(Keycode.ALT , Keycode.TAB)
        time.sleep(0.1)
        keyboard.release(Keycode.ALT , Keycode.TAB)
    time.sleep(0.1)