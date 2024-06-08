# 1 - masala
# https://www.codewars.com/kata/5a043724ffe75fbab000009f/train/python
# Slice a middle of the list backwards

# input ==>  [4, 3, 100, 1]
# output ==> [100, 3]

def reverse_middle(lst):
    m = len(lst) // 2
    if len(lst) % 2 == 0:
        r = lst[m - 1:m + 1]
    else:
        r = lst[m - 1:m + 2]

    return r[::-1]

# print(reverse_middle([4, 3, 100, 1]))



#  2 - masala
# Sum Array with different bases
# https://www.codewars.com/kata/5a005f4fba2a14897f000086/train/python

# [["101",2], ["10",8]] --> 13
# [["ABC",16], ["11",2]] --> 2751

def sum_it_up(numbers_with_bases):
     return sum(int(n, b) for n, b in numbers_with_bases)

# print(sum_it_up([["101",2], ["10",8]]))



# 3 - masala
# Remove the minimum
# https://www.codewars.com/kata/563cf89eb4747c5fb100001b/train/python

# * Input: [1,2,3,4,5], output = [2,3,4,5]
# * Input: [5,3,2,1,4], output = [5,3,2,4]

def remove_smallest(numbers):
    if not numbers:
        return numbers
    new_numbers = numbers[:]
    new_numbers.remove(min(new_numbers))
    return new_numbers

# print(remove_smallest([1, 2, 3, 4, 5]))


# 4 - masala
# Offspring Traits
# https://www.codewars.com/kata/5b011461de4c7f8d78000052/train/python

# bear_fur(['black', 'black'])  returns 'black'
# bear_fur(['brown', 'brown'])  returns 'brown'
# bear_fur(['white', 'white'])  returns 'white'


def bear_fur(b):
    return {('black', 'black') : 'black',
             ('black', 'white') : 'grey',
             ('black', 'brown') : 'dark brown',
             ('brown', 'brown') : 'brown',
             ('brown', 'white') : 'light brown',
             ('white', 'white') : 'white'
                }.get(tuple(sorted(b)), 'unknown')

# print(bear_fur(['black', 'black']))


# 5 - masala
# Replace all items
# https://www.codewars.com/kata/57ae18c6e298a7a6d5000c7a/train/python

# input ==> [1, 2, 2] ==> obj
# find ==> 1, replace ==> 2
# output ==> [2, 2, 2]

def replace_all(obj, find, replace):
    if isinstance(obj, str):
        return obj.replace(find, replace)
    elif isinstance(obj, list):
        return [x if x != find else replace for x in obj]

# print(replace_all([2, 3, 2], 3, 2))


# 6 - masala
# New £5 notes collectors!
# https://www.codewars.com/kata/58029cc9af749f80e3001e34/train/python

# salary ==> 2000
# bills ==>[500, 160, 400]
# output ==> 188
def get_new_notes(salary, bills):
    s = sum(bills)
    r = salary - s
    if r > 0:
        return r // 5
    else:
        return 0

# print(get_new_notes(2000, [500, 160, 400]))


#  7 - masala
# The highest profit wins
# https://www.codewars.com/kata/559590633066759614000063/train/python

# [1,2,3,4,5] --> [1,5]
# [2334454,5] --> [5,2334454]
# [1]         --> [1,1]

def min_max(lst):
    result = []
    result.append(min(lst))
    result.append(max(lst))
    return result

# print(min_max([1, 2, 3, 4, 5]))


# 8 - masala
# Sum of odd numbers
# https://www.codewars.com/kata/55fd2d567d94ac3bc9000064/train/python

def row_sum_odd_numbers(n):
    return n ** 3

# print(row_sum_odd_numbers(13))

# 9 - masala
# Candy problem
# https://www.codewars.com/kata/55466644b5d240d1d70000ba/train/python


# input ==> [5,8,6,4]
# output ==> 9

def candies(lst):
    if len(lst) <= 1:
        return -1

    m = max(lst)
    t = sum(m - i for i in lst)

    return t

# print(candies([5, 4, 8, 6]))














        
    
  
