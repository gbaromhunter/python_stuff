def power(l1, l2):
    """l1, l2 lists of same length of numbers
    returns the sum of raising each element in l1
    to the power of the element at the same index in L2
    For example, f([1,2], [2,3]) returns 9"""
    if len(l1) != len(l2): raise ValueError("Lists have different lenght")
    return sum(map(lambda x, y: x ** y, l1, l2))


def power(l1, l2):
    """l1, l2 lists of same length of numbers
    returns the sum of raising each element in l1
    to the power of the element at the same index in L2
    For example, f([1,2], [2,3]) returns 9"""
    if len(l1) != len(l2): raise ValueError("Lists have different lenght")
    l3 = []
    for i in range(0, len(l1)):
        ans = l1[i]**l2[i]
        l3.append(ans)
    return sum(l3)


