# race !
for x in range(1, 10):
    for f in all_fleas:
      # 50 % chance
      if random.randint(0, 1) == 1:
          display.set_pixel(f[0], f[1], 0)
          f[0] += 1
          f[0] = min(f[0], 4)
          display.set_pixel(f[0], f[1], 9)

    sleep(500)        

