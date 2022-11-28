# You are to write a function that accepts two arguments, a plain-text message and a number of letters to shift in
# the cipher. The function will return an encrypted string with all letters transformed and all punctuation and
# whitespace remaining unchanged.
from itertools import cycle

def caesar(message=str, n=int):
    message = message.lower()
    alphabet = [(chr(ord("a") + i)) for i in range(26)]
    for e in message:
        if e not in alphabet:
            raise ValueError
    uniques = sorted(list(set(message)))
    struniques = "".join(uniques)
    transl = []
    for b in uniques:
        ind = alphabet.index(b) + 1
        c = cycle(alphabet)
        for _ in range(ind + n):
            new = next(c)
        transl.append(new)
    replace = "".join(transl)
    trantab = str.maketrans(struniques, replace)
    messaget = message.translate(trantab)
    return print(messaget)

caesar("abc", 1)
caesar("xyz", 3)
caesar("mozzarella", 4)
