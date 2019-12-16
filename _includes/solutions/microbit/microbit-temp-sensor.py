from microbit import *

brightness = 4

while True:

    temp_in_c = temperature()

    for x in range(5):
        for y in range(5):
            temp_pixel = y * 8 + x
            pixel_intensity = brightness if int(temp_in_c) >= temp_pixel else 0
                
            display.set_pixel(x, y, pixel_intensity)

    sleep(500)
