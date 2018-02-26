from microbit import *
import music

while True:
    if pin1.is_touched() and pin2.is_touched():
        tune = ["C4:4"]
        music.play(tune)
    elif pin1.is_touched():
        tune = ["G4:4"]
        music.play(tune)
    elif pin2.is_touched():
        tune = ["A4:4"]
        music.play(tune)
    elif button_a.was_pressed():
        tune = ["F4:4"]
        music.play(tune)
    elif button_b.was_pressed():
        tune = ["E4:4"]
        music.play(tune)

    sleep(100)
