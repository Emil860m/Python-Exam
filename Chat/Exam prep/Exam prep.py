"""Built-in data structures"""

my_list = ["Hej", "Farvel"]
my_set = {"Hej", "Farvel"}
my_dict = {"hej": "farvel"}
my_tuple = ("hej", "Farvel")
print(type(my_list))
print(type(my_set))
print(type(my_dict))
print(type(my_tuple))
"""Classes and protocols"""


class A():
    def __init__(self):
        self.a = 42

    def __str__(self):
        return "This object has the number: " + str(self.a)


a = A()
print(a)

import random

"""List comprehension"""
# Hvad, hvor mange, hvornår == value, for loop, conditional statement

my_list = [random.randrange(1, 100) for i in range(10)]

print(my_list)

# dict comprehension:
my_dict = {i: i * i for i in range(1, 10)}

# Set comprehension:
my_set = {i for i in range(1, 10)}

# tuple comprehension:
my_tuple = tuple((i for i in range(1, 10)))

"""Generator"""

my_gen = (random.randrange(1, 100) for i in range(10_000_000))

print(next(my_gen))


# for i in range(10):
#     print(next(my_gen))

# Can also be made as a method:

def gen():
    for i in range(1, 10_000_000):
        yield i * i


new_gen = gen()

print(next(new_gen))

"""Decorators"""


# something that looks like nested functions ie. functions inside functions

# this is a closure:
def outer_func(msg):
    def inner_func():
        print(msg)

    return inner_func


my_func = outer_func("Hello")
my_func()


# this is a decorator

def dec_func(original_func):
    def wrapper_func():
        print("Wrapper func ran: {}".format(original_func.__name__))
        original_func()
        print("The function is now done running: {}".format(original_func.__name__))

    return wrapper_func


# simple func for show
def display():
    print("Display function ran")


display()
dec_display = dec_func(display)
dec_display()


# Another way to do it

@dec_func
def display2():
    print("Display2 function ran")


display2()


# This is used fx. as a logging function, or as a timer to count how long the function is running for


# If you need positional arguments in a decorated function you need to do this:

def dec_func2(og_func):
    def wrapper_func(*args, **kwargs):
        print("Wrapper ran on: {}".format(og_func.__name__))
        og_func(*args, **kwargs)

    return wrapper_func


@dec_func2
def display_info(name, age):
    print("This has the info: name: {} age: {}".format(name, age))


display_info("John", 25)


# You can also use decorator classes:

class dec_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print("Class call ran on: {}".format(self.original_function.__name__))
        self.original_function(*args, **kwargs)


@dec_class
def display_info2(name, age):
    print("This has the info: name: {} age: {}".format(name, age))


display_info2("John", 30)

"""Context manager"""
# Handles resources, with also handling setup and teardown of the resources for us
# Used for files, databases or logs or other things

# Example:
with open('test.txt', 'w+') as f:
    f.write('Lorem ipsum')


# Example of self-made context manager
class open_file():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        # Setup of the context manager
        self.file = open(self.filename, self.mode)
        # This is the object we work with within our context manager
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Teardown of the context manager
        self.file.close()


# When using the context manager class
# The with statement calls the __enter__ method, which in this case opens the file
# After it has run the code it calls the __exit__ method, which closes the file
with open_file("test.txt", "r") as f:
    print(f.read())

print(f.closed)

# Same thing but using a class as the context manager

from contextlib import contextmanager


@contextmanager
def context_manger(filename, mode):
    try:
        # Setup code
        f = open(filename, mode)
        yield f
    finally:
        # Teardown code
        f.close()


with context_manger("test.txt", "r") as file:
    print(file.read())

print(file.closed)


"""Duck typing and EAFP"""
# This is the concept described as:
# If i walks like a duck, and quacks like a duck, treat it as a duck
# Also EAFP: It's easier to ask forgiveness than permission
# LBYL: look before you leap is not pythonic. It's better to just try, and if it fails catch the exception

class Duck:

    def quack(self):
        print("Quack")

    def fly(self):
        print("Flap flap")

class Person:

    def quack(self):
        print("I'm quacking like a duck")

    def fly(self):
        print("I'm flapping my arms")

def quack_and_fly(thing):
    # Not Duck-typed (non-pythonic)
    if isinstance(thing, Duck):
        thing.quack()
        thing.fly()
    else:
        print("It has to be a duck")
    print()


# We do not care what type of object it is. We only care about if it can do what we want it to do
# Here we use EAFP
def quack_and_fly2(thing):
    # this is pythonic
    try:
        thing.quack()
        thing.fly()
    except AttributeError as e:
        print(e)
    print()

d = Duck()
p = Person()
a = A()

quack_and_fly(d)
quack_and_fly(p)
quack_and_fly(a)

quack_and_fly2(d)
quack_and_fly2(p)
quack_and_fly2(a)

# This is faster if you don't expect many errors, since we are not accessing anything more than once
# which we would do if we were checking if it was allowed to do
# Might also be more readable
# Lastly might create a race condition. If you check first, you might get a true back
# and then it changes before you actually access the object and it might have changed

"""Testing"""





"""Optimization"""