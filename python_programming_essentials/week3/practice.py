# 1. Write a function 'is_even' that checks if a number is even
# return true or false

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


# 2. write a function 'print_digits' that prints the digits of a two digit number

def print_digits(x):
    if 0 < x < 100:
        tens = x // 10
        ones = x % 10
        print(f"The tens digit is {tens} and the ones digit is {ones}.")
    else:
        print(f"{x} isn't between 1 and 99")
        
        
# 3. Make a piglatin thing
# Note: if a word starts with vowels, it's name + way

def pig_latin(word):
    
    first_letter = word[0]
    rest_of_word = word[1:]
    vowels = ['a','e','i','o','u']
    
    if first_letter.lower() not in vowels:
        print(f"{rest_of_word}{first_letter}ay")
    else:
        print(f"{word}way")
