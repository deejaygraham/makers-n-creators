---

---

### Changing Colour

In While...

~~~

for event in pygame.event.get():
      if event.type == pygame.QUIT:
        done = True
      elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        is_blue = not is_blue

    screen.fill(black)

    if is_blue: box_colour = blue
    else: box_colour = orange

    pygame.draw.rect(screen, box_colour, pygame.Rect(box_left, box_top, box_width, box_height))

~~~
