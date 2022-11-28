def make_change(coin_vals, change):
    """coin_vals is a list of positive ints and coin_vals[0] = 1, change is a positive int > 0.
    return the minimum number of coins needed to have a set of coins the values of which sum to change.
    Coins may be used more than once. For example, make_change([1, 5, 8], 11) should return 3."""

    def combination(coin_vals, change):
        if change > 0:
            for coin in sorted(coin_vals, reverse=True):
                if change - coin >= 0:
                    return [coin] + combination(coin_vals, change - coin)
        if change == 0:
            return []

    def combinations(coin_vals, change):
        if coin_vals == [1]:
            return [1] * change
        else:
            return combination(coin_vals, change) + combinations(sorted(coin_vals, reverse=True)[:-1], change)

    result = combinations(coin_vals, change)
    return min(result, key=len)















# 1. Write a Python program to calculate the sum of a list of numbers

def sum1(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] + sum1(list[1:])


# Write a Python program to get the sum of a non-negative integer. Go to the editor
# Test Data:
# sumDigits(345) -> 12
# sumDigits(45) -> 9

def digitsum(number):
    if len(str(number)) == 1:
        return number
    else:
        return int(str(number)[0]) + digitsum(int(str(number)[1:]))



# 11. Write a Python program to find  the greatest common divisor (gcd) of two integers.
# example: GCD(16, 12) returns 4

def GCD(a,b, c=None):
    if c == None:
        c = b
    if a < b: a, b = b, a
    if a % c == 0 and b % c == 0:
        return print(f"The GCD is {c}")
    else:
        GCD(a, b, c-1)






# Write a recursive function that accepts an integer argument and returns the factorial.

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)



# Write a recursive function that accepts two numbers as its argument and returns its power

def power(a,b):
    if b == 0:
        return 0
    elif b == 1:
        return a
    else:
        return a * power(a, b-1)




# Write a recursive function that accepts a decimal integer and display its binary equivalent

def binary(n):
    if n==0: return
    binary(n // 2)
    print(n % 2,end="")