"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def checkPrime(number):
    for i in range(2, (number//2) + 1):
        if number % i == 0:
            return False
    
    return True

def primes(number_of_primes):

    if number_of_primes < 1:
        raise ValueError("Sorry, zero and below is not allowed.")

    list = []
    currentNumber = 2
    
    while len(list) < number_of_primes:
        if checkPrime(currentNumber) == True:
            list.append(currentNumber)
        currentNumber += 1

    return list
