from microbit import *
import music

# frequency image pairs
# standard guitar tuning
open_string_notes = [
    [ 82,   Image("99999:90000:99990:90000:99999")], # E
    [ 110,  Image("09990:90009:90009:99999:90009")], # A
    [ 147,  Image("99990:90009:90009:90009:99990")], # D
    [ 196,  Image("09999:90000:90999:90009:09990")], # G
    [ 247,  Image("99990:90009:99990:90009:99990")], # B
    [ 330,  Image("09990:90009:99990:90000:09990")]  # E
]

note_count = len(open_string_notes)
current_note = 0

while True:
   # show image instead of letter?
    display.show(open_string_notes[current_note][1])

    # select a string
    if button_a.was_pressed():
        current_note += 1
        if current_note >= note_count:
            current_note = 0
    # play that note
    elif button_b.was_pressed():
        music.pitch(open_string_notes[current_note][0])
        sleep(1000)
        music.stop()
