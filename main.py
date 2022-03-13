import pyautogui
import time

def flash_was_activated(flash_time: int):

    flash_time = int(flash_time)
    # The end of a flash should always be the dimmest light
    for i in range(flash_time):

        # Turn on light here
        print("Flashing...")
        time.sleep(1)

    # Turn off light here

    return 0

def is_white(r,g,b):

    cutoff_brightness = 250

    if r > cutoff_brightness and g > cutoff_brightness and b > cutoff_brightness:
        return 1
    return 0

def check_pixels_for_flash(img):
    """

    :param img: The image item to check
    :return: True if all of the pixels were white
    """
    # pixels_to_check = [(30, 30),
    #                    (200, 200),
    #                    (150, 150),
    #                    ]
    pixels_to_check = [(150,150)]

    for pixel in pixels_to_check:
        pixel_colors = img.getpixel(pixel)
        if not is_white(pixel_colors[0], pixel_colors[1], pixel_colors[2]):
            return 0
    print("All pixels were white...FLASH ME")
    return 1

if __name__ == "__main__":

    while True:

        img = pyautogui.screenshot(region=(0,0,300,300))
        if check_pixels_for_flash(img):
#             ACTIVATE FLASHBANG
            print("Flashed")
            time.sleep(3)

        time.sleep(0.1)
#         flash_was_activated(3)
