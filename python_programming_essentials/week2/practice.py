# 1. write a miles to feet function (1 mile = 5280 feet)

def miles_to_feet(miles):
    return miles * 5280


# 2. write a function 'total_seconds' that takes in three params: hours, minutes, seconds
# and returns the total number of seconds for each param added together

def total_seconds(hours, minutes, seconds):
    return(hours * 60 + minutes) * 60 + seconds


# 3. write a function 'rectangle_perimeter' that takes two params: width and height
# and returns the perimeter of the rectangle in inches

def rectangle_perimeter(width, height):
    return(width * 2 + height * 2)


# 4.Compute the circumference of a circle, given the length of its radius.

from math import pi

def circle_circumfrence(radius):
    return(2 * pi * radius)

"""
 Challenge question
write a function that generates 5 random numbers between 1 and 59
then generate a powerball number between 1 and 35
then output some result
"""
from random import randrange

def powerball():
    # initialize the numbers
    num0 = randrange(1,60)
    num1 = randrange(1,60)
    num2 = randrange(1,60)
    num3 = randrange(1,60)
    num4 = randrange(1,60)
    jackpot = randrange(1, 36)
    
    # convert to array
    nums = [num0,num1,num2,num3,num4]
    
    # check if there is a winner (made for fun)
    for num in nums:
        if jackpot == num:
            return(f"Today's numbers are {nums} and the powerball number was {jackpot} - YOU WON!!!!")
        else:
            return(f"Today's numbers are {nums} and the powerball number was {jackpot} - good try nerd")
