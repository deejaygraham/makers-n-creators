
from random import *

print("Compliment Generator")
print("-" * 20)

adjectives = [ "amazing" , "above-average" , "excellent" ]
hobbies = [ "riding a bike" , "programming" , "making a cup of tea" ]

name = input("What is your name?: ")
print( "Here is your compliment" , name , ":" )

#get a random item from both lists, and add them to the compliment
print( name , "you are" , choice(adjectives) , "at" , choice(hobbies) )
print( "You're welcome!" )


