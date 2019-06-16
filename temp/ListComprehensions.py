"""Comprehensions are a way to make lists or other data structures in python
This is a very simply written and easy to understand way of creating lists
It is used to make the code more maintainable
They are created by going through a loop inside the brackets when you create the list/dict/tuple/set"""



nums = [1,2,3,4,5,6,7,8,9, 10]

# for loop list comprehension, excludes the end of range
numbers = [i for i in range(8)]

values = [d for d in str(f'{100:08b}')]

binary_numbers = [str(f'{b:03b}') for b in range(8)]

#print(binary_numbers)

my_list = [letter + str(num) for letter in 'abcd' for num in range(4)]
# print(my_list)

my_dict = {number: value for number, value in zip(numbers, binary_numbers)}
print(my_dict)

nums = [1, 1 ,2, 3, 4, 5,6,7,8,9,10,2,3,4,5,6,7,8,9, 10]
my_set = {n for n in nums}
print(my_set)

my_gen = (n*n for n in numbers)
print(my_gen)
for i in my_gen:
    print(i)



