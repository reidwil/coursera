"""
Write a program to find the 6-th Monisen number.

Classic Programming Question:
    find the n-th Monisen number.
    A number M is a Monisen number if M=2**P-1 and both M and P are prime numbers.
    For example, if P=5, M=2**P-1=31, 5 and 31 are both prime numbers, so 31 is a Monisen number.

Put the 6-th Monisen number into a single text file and submit online.
"""
import math

def is_prime(num):
    """
    checks if num is prime
    :param num: integer value
    :return: True if prime/False if not prime
    """
    
    # using the floored square root here to reduce the amount of calculations done
    for x in range(2, 1 + math.floor(math.sqrt(num))):
        if num % x == 0:
            return False
    return True

def mon_calc(p):
    """
    takes in p and returns monsier m falue
    :param p: int value
    :return:
    """
    m = 2**p-1
    return m

def run(nprime):
    """
    runs through all prime numbers until it reaches nprime then returns the result of mon_calc
    :param nprime: which n-th prime number you want to calculate monisen number for
    :return: monisen prime number for the nprime number
    """
    i = 0
    n=2
    while i < nprime:
        if is_prime(n) & is_prime(mon_calc(n)):
            i += 1
            if i == nprime:
                break
        n += 1
    return mon_calc(n)


# write it to a file
with open('output.txt', 'w') as f:
    output = str(run(6))
    f.write(output)

