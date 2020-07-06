## Question 1
def max_of_three(a, b, c):
    numbers  = [a, b, c]
    return max(numbers) ## use the python function for simplicity

max_numbers = max_of_three(10, 10, 10)
print('maximum number: ', max_numbers)


## Question 2
def count_cases(word):
    count_upper = 0
    count_lower = 0
    for letter in word:
        if letter.isupper():
            count_upper += 1
        else:
            count_lower += 1
    return count_lower, count_upper

count_lower, count_upper = count_cases('The Quick Brown Fox Jumps Over the Lazy Dog')
print('Number of lower cases: ', count_lower)
print('Number of upper cases: ', count_upper)


## Question 5
'''import numpy  #Using number (for python versrion 3.8, one can use math.prod() by importing math)
def multiply(some_list):
    product = numpy.prod(some_list)
    return product

my_list = [3, 5, 6, 7, 10]
product = multiply(my_list)
print(product)

## Alternative to Question 5
from functools import reduce
my_list = [3, 5, 6, 7, 10]
product = reduce((lambda x, y: x * y), my_list)
print(product)


### Question 6 (set)
def commonality(list_1, list_2):
    set_list_1 = set(list_1)
    set_list_2 = set(list_2)

    if (set_list_1 & set_list_2):
        return True
    else:
        return False

print(commonality(list_1, list_2))


## Question 7
def second_largest(some_list):
    set_list = sorted(set(some_list))
    return set_list[1]

print(second_largest(my_list))
'''

## Question 8
def include_string(word):
    if len(word) < 3:
        return word
    elif word.endswith('go'):
        return word + 'ly'
    else:
        return word + 'ing'

word_1 = include_string('go')
word_2 = include_string('going')
word_3 = include_string('good')
print(word_1)
print(word_2)
print(word_3)