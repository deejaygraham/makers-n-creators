from microbit import *

# Wait for a button push and return the time
def wait_for_any_button():
    time = 0

    while True:
        if button_a.was_pressed() or button_b.was_pressed():
            time = running_time()
            break

        sleep(100)

    return time

def calculate_distance(speed, time):
    return speed * time

speedOfSoundMetresPerSecond = 340

lightning = Image("00990:09900:99999:00990:09000")
ear       = Image("09999:90000:90009:90000:09999")

while True:
    flashTime = 0
    thunderTime = 0

    # we're waiting for lightning
    display.show(lightning)
    flashTime = wait_for_any_button()
    # now wait for thunder
    display.show(ear)
    thunderTime = wait_for_any_button()

    timeDifference = thunderTime - flashTime
    timeDifferenceInSeconds = timeDifference / 1000

    distanceInMeters = calculate_distance(
		speedOfSoundMetresPerSecond,
		timeDifferenceInSeconds)

    display.scroll(str(distanceInMeters) + " m")
