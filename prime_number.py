import math

def is_prime(num):
    '''Check if num is prime or not.'''
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True
