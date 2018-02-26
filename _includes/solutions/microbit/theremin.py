from microbit import *
import music

# where am i in space?
def calculate_movement():
    scaling_factor = 20
    x = accelerometer.get_x() / scaling_factor
    y = accelerometer.get_y() / scaling_factor
    z = accelerometer.get_z() / scaling_factor
    movement = x + y + z

    return int(movement)

frequency = 440 # concert 'A'

while True:
    change = calculate_movement()
    pitch = frequency + change    
    music.pitch(pitch)
    sleep(100)
