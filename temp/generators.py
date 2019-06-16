
"""Can be used to save memory or computing power, since none of the results are computed or saved before it's actually run
You only compute it whenever you call for the next number with either a loop or next() function
Äll that is in memory is the previous number used by the generator, to determine what should be calculated next"""

numbers = [i for i in range(6)]

def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

my_nums = square_numbers(numbers)


print(my_nums)



# recreated as generator

def square_gen(nums):
    for i in nums:
        yield i*i

gen_nums = square_gen(numbers)

for i in gen_nums:
    print(i)


print(gen_nums)