# Finger exercise: Write an expression that evaluates to the mean of
# a tuple of numbers. Use the function sum.

def mean():
    x = (3, 6, 8, 9)
    for i in x:
        y = sum(i)/len(x)
    return y