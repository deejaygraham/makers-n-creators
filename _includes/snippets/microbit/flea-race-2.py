from microbit import *

flea = [0, 0] # x, y

# start in left column.
display.set_pixel(flea[0], flea[1], 9)

for x in range(1, 4):
    # turn off current pixel
    display.set_pixel(turtle[0], turtle[1], 0)
    # move
    flea[0] += 1
    display.set_pixel(flea[0], flea[1], 9)
    # wait so we don't move too fast
    sleep(500)        
