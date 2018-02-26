from microbit import *
import radio

def convert_image_to_text(image):
    text = ""

    # append each pixel in 5 x 5 grid to line of text.
    for x in range(5):
        for y in range(5):
            text = text + str(image.get_pixel(x, y))

        # add in colon delimiters so microbit can
        # work out it's an image
        if x < 4:
            text = text + ":"

    return text

radio.on()

pic_to_send = Image("90909:09090:90909:09090:90909")

while True:
    if button_a.was_pressed():
    		pic_as_text = convert_image_to_text(pic_to_send)
		radio.send(pic_as_text)

    received_pic_as_text = radio.receive()

    if received_pic_as_text:
    		received_pic = Image(received_pic_as_text)
       	display.show(received_pic)
       	sleep(5000)
       	display.clear()
