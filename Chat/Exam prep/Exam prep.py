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
my_dict = {i: i*i for i in range(1, 10)}

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
        yield i*i

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
    print("This has the info: name: {} age: {}".format(name,age))

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
    print("This has the info: name: {} age: {}".format(name,age))

display_info2("John", 30)


"""Context manager"""
# Handles resources, with also handling setup and teardown of the resources for us


#Example:
with open('test.txt', 'w+') as f:
    f.write('Lorem ipsum')
