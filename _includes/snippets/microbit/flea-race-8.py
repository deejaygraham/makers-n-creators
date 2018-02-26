display.set_pixel(flea[0], flea[1], 9)

# increase the opportunities to move because
# we don't move every time...
for x in range(1, 10):
    # 50 % chance
    if random.randint(0, 1) == 1:
        display.set_pixel(turtle[0], turtle[1], 0)
        flea[0] += 1
        display.set_pixel(flea[0], flea[1], 9)

    sleep(500)        

