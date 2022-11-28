# First function: generate a string of "Marco Spagnolo" lenght with random characters in
# Second Function: compare the string with "Marco Spagnolo" and rate the comparison
# Third function: call the two previous and show the best result

import random as r


final_line = "marco spagnolo"
chars = list("abcdefghilmnopqrstuvs ")

def string_generator():
    return "".join([r.choice(chars) for x in range(len(final_line))])

def compare_strings(s):
    return "".join(set([x for x in s if x == final_line[s.index(x)]]))

def check():
    s = string_generator()
    tries_list = []
    d = {}
    while s != final_line:
        d[s] = compare_strings(s)
        the_max = max(d.values(), key=len)
        print(f"The new combination is: {s} and the grade is: {len(d[s])}")
        print(f"The best word is: {list(d.keys())[list(d.values()).index(the_max)]}, letters in common are: {the_max}, grade: {len(the_max)} with {len(d)} combinations")
        s = string_generator()
    return f"The machine found Marco Spagnolo with {len(tries_list)} combinations!"


