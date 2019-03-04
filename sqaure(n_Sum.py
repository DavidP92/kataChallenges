##Complete the square sum method so that it squares each number passed into it and then sums the results together.
##For example: squareSum([1, 2, 2]) should return 9 because 1^2 + 2^2 + 2^2 = 9.

def square_sum(numbers):
    sum = 0
    for x in numbers:
        x = x**2
        sum = sum + x
    return sum
        