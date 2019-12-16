from microbit import *

while True:

    temp_in_c = temperature()
    print(str(temp_in_c) + 'C')    
    
    sleep(500)
