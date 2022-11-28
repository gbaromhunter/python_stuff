# Write a program that examines three variables—
# x, y, and z—and prints the largest odd number among them. If none
# of them are odd, it should print the smallest value of the three.
import random
import math as m
import calendar as cal


def ex0(x, y, z):
    odd = [a for a in [x, y, z] if a % 2 != 0]
    even = [a for a in [x, y, z] if a % 2 == 0]
    if odd:
        return print(f"The largest odd number is: {max(odd)}")
    else:
        return print(f"The lowest number is: {min(even)}")


def ex1(x, y, z):
    odd = [a for a in [x, y, z] if a % 2 != 0]
    even = [a for a in [x, y, z] if a % 2 == 0]
    return print(max(odd)) if odd else print(min(even))


# the book answer
def ex2(x, y, z):
    answer = min(x, y, z)
    if x % 2 != 0:
        answer = x
    if y % 2 != 0 and y > answer:
        answer = y
    if z % 2 != 0 and z > answer:
        answer = z
    return print(answer)


# Write code that asks the user to enter their
# birthday in the form dd/mm/yyyy, and then prints a string of the
# form ‘You were born in the year yyyy.’

def bdyear():
    birthday = input(f"Insert your birthday in the form of dd/mm/yyyy")
    return print(f"You were born in the year {birthday[-4:]}")


# Replace the comment in the following code with a
# while loop


def x_many():
    num_x = int(input('How many times should I print the letter X? '))
    to_print = ''
    x = 0
    while x <= num_x:
        to_print = to_print + "X"
        x += 1
    print(to_print)


# Write a program that asks the user to input 10
# integers, and then prints the largest odd number that was entered. If
# no odd number was entered, it should print a message to that effect.


def ten_numbers():
    numbers = [int(input("Insert a number")) for n in range(10)]
    odds = [a for a in numbers if a % 2 != 0]
    if odds:
        return print(f"The highest odd number is: {max(odds)}")
    else:
        return print(f"There are no odd numbers!")


# Write a program that prints the sum of the prime
# numbers greater than 2 and less than 1000. Hint: you probably want
# to use a for loop that is a primality test nested inside a for loop that
# iterates over the odd integers between 3 and 999.


def sum_prime_numbers():
    return sum([a for a in range(3, 1000) if a % 2 != 0])


def is_prime_smallest():
    x = int(input("Insert a number greater than 2: "))
    smallest_divisor = None
    for guess in range(2, x):
        if x % guess == 0:
            smallest_divisor = guess
            break
    if smallest_divisor != None:
        print(f"The smallest divisor of {x} is {smallest_divisor}")
    else:
        print(f"{x} is a prime number")


# Change the code so that it returns
# the largest rather than the smallest divisor. Hint: if y*z = x and y is
# the smallest divisor of x, z is the largest divisor of x.


def is_prime_largest():
    x = int(input("Insert a number greater than 2: "))
    d = [a for a in range(2, x) if x % a == 0]
    if d:
        return print(f"The largest divisible is {max(d)}") if d else print(f"{x} is a prime number")


def is_prime(x):
    if not [a for a in range(2, x) if x % a == 0]:
        print(f"{x} is a prime number")
        return True
    else:
        print(f"{x} is not a prime number")
        return False


def is_prime_oneliner(x):
    return True if not [a for a in range(2, x) if x % a == 0] else False


def prime_list(n):
    return [x for x in range(3, n, 2) if not [a for a in range(2, x) if x % a == 0]]


# Write a program that asks the user to enter an
# integer and prints two integers, root and pwr, such that 1 < pwr < 6
# and root**pwr is equal to the integer entered by the user. If no such
# pair of integers exists, it should print a message to that effect.


def integer_pairs():
    x = int(input("Insert a number: "))
    for pwr in range(1, 7):
        for guess in range(2, x):
            if guess ** pwr == x:
                return print(f"The root is {guess} and the power is {pwr}")
    return print(f"There is no such number!")


# Write a program that prints the sum of the prime
# numbers greater than 2 and less than 1000. Hint: you probably want
# to have a loop that is a primality test nested inside a loop that
# iterates over the odd integers between 3 and 999.

def prime_sum():
    return sum([x for x in range(3, 1000, 2) if not [a for a in range(2, x) if x % a == 0]])


# This is simple algorithm to find square root of x

def square(x):
    epsilon = 0.01
    step = epsilon ** 2
    num_guesses = 0
    ans = 0.0
    while abs(ans ** 2 - x) >= epsilon and ans * ans <= x:
        ans += step
        num_guesses += 1
    print(f"Number of guesses is {num_guesses}")
    if abs(ans ** 2 - x) >= epsilon:
        print(f"Failed the square root of{x}")
    else:
        print(f"{ans} is close to square root of {x}")


# This is bisection algorithm for same problem

def bise_square(x):
    x = abs(x)
    epsilon = 0.01
    num_guesses = 0
    low = 0
    high = max(1, x)
    ans = (high + low) / 2
    while abs(ans ** 2 - x) >= epsilon:
        print(f"Low is {low}, High is {high}, Answer is {ans}")
        num_guesses += 1
        if ans ** 2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
    return print(f"Square root of {x} is about {ans} and it took {num_guesses} guesses")


# What would the code in Figure 3-5 do if x = -25?


# What would have to be changed to make the code
# in Figure 3-5 work for finding an approximation to the cube root of
# both negative and positive numbers? Hint: think about changing low
# to ensure that the answer lies within the region being searched.


def bise_cube(x):
    epsilon, num_guesses, low, high = 0.01, 0, 0, max(1, abs(x))
    ans = (high + low) / 2
    while abs(ans ** 3 - abs(x)) >= epsilon:
        print(f"Low is {low}, High is {high}, Answer is {ans}")
        num_guesses += 1
        if ans ** 3 < abs(x):
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
    ans = -ans if x < 0 else ans
    return print(f"Cube root of {x} is about {ans} and it took {num_guesses} guesses")


# The Empire State Building is 102 stories high. A
# man wanted to know the highest floor from which he could drop an
# egg without the egg breaking. He proposed to drop an egg from the
# top floor. If it broke, he would go down a floor, and try it again. He
# would do this until the egg did not break. At worst, this method
# requires 102 eggs. Implement a method that at worst uses seven
# eggs.


def find_egg():
    egg = random.randint(1, 102)
    high, low, ng = 102, 1, 1
    ans = (high + low) // 2
    while ans != egg:
        if ans > egg:
            high = ans
        else:
            low = ans
        ans = (high + low) // 2
        ng += 1
    return print(f"The eggs should have broken at {egg}, we found that it breaks at {ans} with {ng} guesses")


# What is the decimal equivalent of the binary
# number 10011?


# Newton-Raphson for square root
# find x such that x**2 - k is within epsilon of 0
def square_newton(k):
    epsilon, c, guess = 0.01, 0, k / 2
    while abs(guess ** 2 - k) >= epsilon:
        print(f"Guess is {guess}")
        guess = guess - (((guess ** 2) - k) / (2 * guess))
        c += 1
    return print(f"Square root of {k} is about {guess} and it took {c} guesses")


# Add some code to the implementation of
# Newton–Raphson that keeps track of the number of iterations used
# to find the root. Use that code as part of a program that compares the
# efficiency of Newton–Raphson and bisection search. (You should
# discover that Newton–Raphson is far more efficient.)


def bise_newt_comparison(x):
    print(f"With the bisection algorithm these are the results:")
    bise_square(x)
    print(f"With the Newton algorithm these are the results:")
    square_newton(x)


# Finger exercise: Write a function is_in that accepts two strings as
# arguments and returns True if either string occurs anywhere in the
# other, and False otherwise. Hint: you might want to use the built-in
# str operator in.


def is_in(first=str, second=str):
    return True if first in second or second in first else False


# Write a function to test is_in

def test_is_in():
    # check if function works properly
    print(f"performing tests, will return True if everything's allright")
    return bool(is_in("sem", "semantica") and is_in("psycho", "psychology") and is_in("wardrobe", "ward") and not is_in(
        "hansel", "gretel"))


# Write a function mult that accepts either one or
# two ints as arguments. If called with two arguments, the function
# prints the product of the two arguments. If called with one argument,
# it prints that argument.

def mult(a, b=None):
    return a * b if b else a


#  Using the algorithm of Figure 3-6, write a
# function that satisfies the specification

def log(x, epsilon, base=int):
    """Assumes x and epsilon int or float, base an int,
    x > 1, epsilon > 0 & power >= 1
    Returns float y such that base**y is within epsilon
    of x."""
    lower_bound = 0
    while base ** lower_bound < x:
        lower_bound += 1
    low = lower_bound - 1
    high = lower_bound + 1
    # Perfom bisection search
    ans = (high + low) / 2
    while abs(base ** ans - x) >= epsilon:
        if base ** ans < x:
            low = ans
        else:
            high = ans
    return print(f"{ans} is close to the log base {base} of {x}")


# Write a lambda expression that has two numeric
# parameters. If the second argument equals zero, it should return
# None. Otherwise it should return the value of dividing the first
# argument by the second argument. Hint: use a conditional
# expression.

lambda x, y: x / y if y != 0 else None


# Finger exercise: Use find to implement a function satisfying the
# specification
def find_last(s, sub):
    """s and sub are non-empty strings
    Returns the index of the last occurrence of sub in s.
    Returns None if sub does not occur in s"""
    return s.find(sub) if s.find(sub) != -1 else None


# Finger exercise: Write an expression that evaluates to the mean of
# a tuple of numbers. Use the function sum.

def mean(tup=tuple):
    return sum(tup) / len(tup)


# : What does the following code print?
def finger():
    L = [1, 2, 3]
    L.append(L)
    return print(L is L[-1])


def append_val(val, list_1=[]):
    if list_1: list_1 = []  # if this is omitted list won't be empty in the next calls
    list_1.append(val)
    return print(list_1)


# Finger exercise: Write a list comprehension that generates all
# non-primes between 2 and 100.

prime_100 = [x for x in range(2, 100) if all(x % y != 0 for y in range(3, x))]


def prime_list(n):
    return [x for x in range(3, n, 2) if not [a for a in range(2, x) if x % a == 0]]


# Finger exercise: Implement a function satisfying the following
# specification. Hint: it will be convenient to use lambda in the body of
# the implementation.


def power_l1_l2(l1, l2):
    """l1, l2 lists of same length of numbers
    returns the sum of raising each element in l1
    to the power of the element at the same index in L2
    For example, f([1,2], [2,3]) returns 9"""
    if len(l1) != len(l2): raise ValueError("Lists have different lenght")
    return sum(map(lambda x, y: x ** y, l1, l2))


# Finger exercise: Implement a function that meets the specification

def get_min(d=dict):
    """d a dict mapping letters to ints
    returns the value in d with the key that occurs first in the alphabet.
    E.g., if d = {x = 11, b = 12}, get_min returns 12."""
    return d[(min(d.keys()))]


# Finger exercise: The harmonic sum of an integer, n > 0, can be
# calculated using the formula . Write a recursive function
# that computes this.

def harmonic(n=int):
    return 1 / n + harmonic(n - 1) if n != 1 else n / n


def fib(n):
    """assumes  int >= 0
    returns Fibonacci of n"""
    return 1 if n == 0 or n == 1 else fib(n - 1) + fib(n - 2)


def fib_iter(n):
    f = [1, 1]
    for _ in range(n - 1): f.append(f[-1] + f[-2])
    return f


def test_fib(n):
    for i in range(n + 1):
        print(f"fib of {i} is {fib(i)}")


# When the implementation of fib in Figure 6-3 is
# used to compute fib(5), how many times does it compute the value
# of fib(2) on the way to computing fib(5)?

# 4 times

def find_thanksgiving(year):
    month = cal.monthcalendar(year, 11)
    if month[0][cal.THURSDAY] != 0:
        thanksgiving = month[3][cal.THURSDAY]
    else:
        thanksgiving = month[4][cal.THURSDAY]
    return thanksgiving


def find_thanksgiving_canada(year):
    month = cal.monthcalendar(year, 10)
    if month[0][cal.MONDAY] != 0:
        thanksgiving = month[1][cal.MONDAY]
    else:
        thanksgiving = month[2][cal.MONDAY]
    return thanksgiving


def natale(anno=int):
    return cal.day_name[cal.weekday(anno, 12, 25)]


# Finger exercise: Write a function that meets the specification

def shopping_days(year):
    """year a number >= 1941, returns the number of days between U.S. Thanksgiving and Christmas in year"""
    return (30 - find_thanksgiving(year)) + 25


# Finger exercise: Since 1958, Canadian Thanksgiving has occurred
# on the second Monday in October. Write a function that takes a year
# (>1957) as a parameter, and returns the number of days between
# Canadian Thanksgiving and Christmas.

def shopping_days_canada(year):
    """year a number >= 1941, returns the number of days between Canadian Thanksgiving and Christmas in year"""
    return (31 - find_thanksgiving_canada(year)) + 30 + 25


# Write a program that first stores the first ten
# numbers in the Fibonnaci sequence to a file named fib_file. Each
# number should be on a separate line in the file. The program should
# then read the numbers from the file and print them.


def fibonten():
    fib_str = [str(s) + "\n" for s in fib_iter(10)]
    with open("C:/Documents and Settings/Gianluca/Documenti/python_works/python_experiments/esercizi/fibo",
              "r+") as fib_file:
        fib_file.writelines(fib_str)
        return print(fib_file.read())


# Finger exercise: Implement a function that meets the specification
# below. Use a try-except block. Hint: before starting to code, you
# might want to type something like 1 + 'a' into the shell to see what
# kind of exception is raised.

def sum_digits(s=str):
    """Assumes s is a string
    Returns the sum of the decimal digits in s
    For example, if s is 'a2b3c' it returns 5"""
    try:
        return sum([int(n) for n in s if n in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]])
    except TypeError:
        print("There is no string!")


# Finger exercise: Implement a function that satisfies the
# specification


def find_an_even(L):
    """Assumes L is a list of integers
    Returns the first even number in L
    Raises ValueError if L does not contain an even
    number"""
    even = [a for a in L if a % 2 == 0]
    if even:
        return even[0]
    else:
        raise ValueError("L does not contain an even number!")


# Finger exercise: Add a method satisfying the specification below to the Int_set class. (union method)
class Int_set(object):
    """An Int_set is a set of integers"""

    # Information about the implementation (not the abstraction):
    # Value of a set is represented by a list of ints, self._vals.
    # Each int in a set occurs in self._vals exactly once.

    def __init__(self):
        """Create an empty set of integers"""
        self._vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if e not in self._vals:
            self._vals.append(int(e))

    def member(self, e):
        """Assumes e is an integer. Returns True if e is in self, and False otherwise"""
        return e in self._vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self._vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def get_members(self):
        """Returns a list containing the elements of self. Nothing can be assumed about the order of the elements"""
        return self._vals[:]

    def __add__(self, other):
        """other is an Int_set. mutates self so that it contains exactly the elemnts in self plus the elements in other."""
        return self.get_members() + other.get_members()

    def __str__(self):
        """Returns a string representation of self"""
        if self._vals == []:
            return '{}'
        self._vals.sort()
        result = ''
        for e in self._vals:
            result = result + str(e) + ','
        return f'{{{result[:-1]}}}'


# Finger exercise: Replace the union method you added to Int_set
# by a method that allows clients of Int_set to use the + operator to
# denote set union.


# a Person

class Person(object):

    def __init__(self, name):
        """Assumes name a string. Create a person"""
        self._name = name
        try:
            last_blank = name.rindex(' ')
            self._last_name = name[last_blank + 1:]
        except:
            self._last_name = name
        self._birthday = None

    def get_name(self):
        """Returns self's full name"""
        return self._name

    def get_last_name(self):
        """Returns self's last name"""
        return self._last_name

    def set_birthday(self, birthdate):
        """Assumes birthdate is of type datetime.date
           Sets self's birthday to birthdate"""
        self._birthday = birthdate

    def get_age(self):
        """Returns self's current age in days"""
        if self._birthday == None:
            raise ValueError
        return (datetime.date.today() - self._birthday).days

    def __lt__(self, other):
        """Assume other a Person
           Returns True if self precedes other in alphabetical
           order, and False otherwise. Comparison is based on last
           names, but if these are the same full names are
           compared."""
        if self._last_name == other._last_name:
            return self._name < other._name
        return self._last_name < other._last_name

    def __str__(self):
        """Returns self's name"""
        return self._name


# Finger exercise: Implement a subclass of Person that meets the
# specification

class Politician(Person):
    """ A politician is a person who can belong to a
    political party"""

    def __init__(self, name, party=None):
        """name and party are strings"""
        super().__init__(name)
        self._party = party

    def get_party(self):
        """returns the party to which self belongs"""
        return self._party

    def might_agree(self, other):
        """returns True if self and other belong to the same
        party
        or at least one of then does not belong to a
        party"""
        try:
            if self._party == other._party:
                return True
            elif self._party == None or other._party == None:
                return True
            elif self._party != other._party:
                return False
            else:
                return True
        except AttributeError:
            return True


def test_politician():
    p1 = Person("Carmine Opili")
    p2 = Politician("Matteo Renzi", "PD")
    p3 = Politician("Matteo Salvini", "Lega")
    p4 = Politician("Luigi Bersani", "PD")
    p5 = Politician("Antonio Razzi")
    print("same party, Renzi and Bersani")
    print(p2.might_agree(p4))
    print("different party, Renzi and Salvini")
    print(p2.might_agree(p3))
    print("Renzi has a party, Carmine is a person without party attribute")
    print(p2.might_agree(p1))
    print("Salvini and Razzi, party with no party")
    print(p3.might_agree(p5))


class MIT_person(Person):
    _next_id_num = 0  # identification number

    def __init__(self, name):
        super().__init__(name)
        self._id_num = MIT_person._next_id_num
        MIT_person._next_id_num += 1

    def get_id_num(self):
        return self._id_num

    def __lt__(self, other):
        return self._id_num < other._id_num


class Student(MIT_person):
    def is_student(self):
        return isinstance(self, Student)


# class UG(Student):
#     def __init__(self, name, class_year):
#         super().__init__(name)
#         self._year = class_year
#
#     def get_class(self):
#         return self._year
#
#
# class Grad(Student):
#     pass
#
#
# class Transfer_student(Student):
#
#     def __init__(self, name, from_school):
#         MIT_person.__init__(self, name)
#         self._from_school = from_school
#
#     def get_old_school(self):
#         return self._from_school


class Grades(object):

    def __init__(self):
        """Create empty grade book"""
        self._students = []
        self._grades = {}
        self._is_sorted = True

    def add_student(self, student):
        """Assumes: student is of type Student
           Add student to the grade book"""
        if student in self._students:
            raise ValueError('Duplicate student')
        self._students.append(student)
        self._grades[student.get_id_num()] = []
        self._is_sorted = False

    def add_grade(self, student, grade):
        """Assumes: grade is a float
           Add grade to the list of grades for student"""
        try:
            self._grades[student.get_id_num()].append(grade)
        except:
            raise ValueError('Student not in mapping')

    def get_grades(self, student):
        """Return a list of grades for student"""
        try:
            return self._grades[student.get_id_num()][:]
        except:
            raise ValueError('Student not in mapping')

    # def get_students(self):
    #     """Return a sorted list of the students in the grade book"""
    #     if not self._is_sorted:
    #         self._students.sort()
    #         self._is_sorted = True
    #     return self._students[:]

    def get_students(self):  # new version from later in chapter
        """Return the students in the grade book one at a time
           in alphabetical order"""
        if not self._is_sorted:
            self._students.sort()
            self._is_sorted = True
        for s in self._students:
            yield s

    # Finger exercise: Add to Grades a generator that meets the
    # specification

    def get_students_above(self, grade):
        """returns one at a time the students that have a grades mean of at least grade"""
        for stud in self._students:
            mean = sum(self._grades[stud.get_id_num()]) / len(self._grades[stud.get_id_num()])
            if mean >= grade:
                yield stud


def test_grade():
    book = Grades()
    s1 = Student("Marco Spagnolo")
    s2 = Student("Vanni Francini")
    s3 = Student("Michele Conticello")
    book.add_student(s1)
    book.add_student(s2)
    book.add_student(s3)
    book.add_grade(s1, 9.0)
    book.add_grade(s1, 8.0)
    book.add_grade(s1, 7.0)
    book.add_grade(s2, 6.5)
    book.add_grade(s2, 6.0)
    book.add_grade(s2, 5.5)
    book.add_grade(s3, 2.5)
    book.add_grade(s3, 3.0)
    book.add_grade(s3, 1.0)
    for a in book.get_students_above(5.0): print(a)


# Finger exercise: What is the asymptotic complexity of each of the
# following functions?

def g(L, e):
    """L a list of ints, e is an int"""
    for i in range(100):
        for e1 in L:
        if e1 == e:
        return True
    return False

# 100 * 2len(L) so O(x)


def h(L, e):
    """L a list of ints, e is an int"""
    for i in range(e):
        for e1 in L:
        if e1 == e:
        return True
    return False

# O(x**2)

# Finger exercise: Why does the code use mid+1 rather than mid in
# the second recursive call?
# because otherwise the program would never stop


# Finger exercise: Modify the DFS algorithm to find a path that
# minimizes the sum of the weights. Assume that all weights are
# positive integers

def DFS(graph, start, end, path, shortest, to_print = False):
    """Assumes graph is a Digraph; start and end are nodes;
          path and shortest are lists of nodes
       Returns a shortest path from start to end in graph"""
    x = []
    path = path + [start]
    if to_print:
        print('Current DFS path:', print_path(path))
    if start == end:
        return path
    for node in graph.children_of(start):
        if node not in path: #avoid cycles
            if shortest == None or len(path) < len(shortest):
                new_path = DFS(graph, node, end, path, shortest,
                              to_print)
                if new_path != None:
                    shortest = new_path
    return shortest

def shortest_path(graph, start, end, to_print = False):
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""
    return DFS(graph, start, end, [], None, to_print)


# Use the tabular method to implement a dynamic
# programming solution that meets the specification


def make_change(coin_vals, change):
    """coin_vals is a list of positive ints and coin_vals[0] = 1
    change is a positive int,
    return the minimum number of coins needed to have a set of coins the values of which sum to change.
    Coins may be used more than once. For example, make_change([1, 5, 8], 11)
    should return 3."""
    sorted_coins = sorted(coin_vals, reverse=True)
    coin_list = []
    tot = 0
    # modules = {x : change % x for x in coin_vals if x!=1}
    while sum(coin_list) != change:
        for coin in sorted_coins:
            if coin + tot <= change:
                coin_list.append(coin)
                tot += coin
    return len(coin_list)


def minofmodule(lst, div):
    listofmodules = [div % a for a in lst]
    modules = {x : div % x for x in lst if x!=1}
    for x in lst:
        modules[x] = div % x


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




# Finger exercise:
# In a vacuum, the speed of a falling object is
# defined by the equation v = v0 + gt, where v0 is the initial velocity of
# the object, t is the number of seconds the object has been falling, and
# g is the gravitational constant, roughly 9.8 m/sec2 on the surface of
# the Earth and 3.711 m/ sec2 on Mars. A scientist measures the
# velocity of a falling object on an unknown planet. She does this by
# measuring the downward velocity of an object at different points in
# time. At time 0, the object has an unknown velocity of v0. Implement
# a function that fits a model to the time and velocity data and
# estimates g for that planet and v0 for the experiment. It should
# return its estimates for g and v0, and also r-squared for the model.



 = v0 + gt

v = 9.8