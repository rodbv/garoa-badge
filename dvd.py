from machine import Pin, I2C, UART
import sh1106

from utils import randint, buzz, button_clicked

sound_enabled = True
sound_button = Pin(0, Pin.IN, Pin.PULL_UP)  # GPIO0 with pull-up

# Setup UART for interrupt detection
uart = UART(0, baudrate=115200)  # UART0 is typically the USB serial port

DISPLAY_WIDTH = 128
DISPLAY_HEIGHT = 64
CHAR_WIDTH = 8

# OLED setup
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
display = sh1106.SH1106_I2C(128, 64, i2c, Pin(16), 0x3C)
display.flip()


def write_text(display, text, x_offset=0, y_offset=0):
    display.fill(0)
    display.text(text, x_offset, y_offset)
    display.show()


def check_interrupt():
    return uart.any()


def run(text="((DVD))"):
    max_x = DISPLAY_WIDTH - len(text) * CHAR_WIDTH
    max_y = DISPLAY_HEIGHT - CHAR_WIDTH

    x = randint(0, max_x)
    y = randint(0, max_y)

    x_dir = 1
    y_dir = 1

    while True:
        if check_interrupt():
            write_text(display, "TCHAU!", 60, 28)
            return

        global sound_enabled
        if button_clicked(sound_button):
            sound_enabled = not sound_enabled

        write_text(display, text, x, y)

        x += 1 * x_dir
        y += 1 * y_dir

        if x >= max_x or x <= 0:
            x_dir *= -1
            if sound_enabled:
                buzz()
        if y >= max_y or y <= 0:
            y_dir *= -1
            if sound_enabled:
                buzz()


if __name__ == "__main__":
    run()
