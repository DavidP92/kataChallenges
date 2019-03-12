##`Write a function named sumDigits which takes a number as input and returns the sum of the absolute value of each of the number's decimal digits. For example:
##    sumDigits(10)  # Returns 1
##  sumDigits(99)  # Returns 18
##  sumDigits(-32) # Returns 5
##  Let's assume that all numbers in the input will be integer values.

def sumDigits(number):
    conversion_str = str(abs(number))
    conversion_list = list(conversion_str)
    
    placeHolderList = [int(x) for x in conversion_list]
    
    return sum(placeHolderList)
