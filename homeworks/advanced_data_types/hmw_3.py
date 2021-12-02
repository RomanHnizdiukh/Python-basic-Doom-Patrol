import functools
# 1. Define the id of next variables:
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}
print(id(int_a))
print(id(str_b))
print(id(set_c))
print(id(lst_d))
print(id(dict_e))

# 2. Append 4 and 5 to the lst_d and define the id one more time.
lst_d.append(4)
print(lst_d)
print(id(lst_d))

lst_d.append(5)
print(lst_d)
print(id(lst_d))

# 3. Define the type of each object from step 1.
print(type(int_a))
print(type(str_b))
print(type(set_c))
print(type(lst_d))
print(type(dict_e))

# 4*. Check the type of the objects by using isinstance.
a = isinstance(int_a, int)
b = isinstance(str_b, str)
c = isinstance(set_c, set)
d = isinstance(lst_d, list)
e = isinstance(dict_e, dict)

print('Is', int_a, 'instance of list?', a)
print('Is', str_b, 'instance of string?', b)
print('Is', set_c, 'instance of set?', c)
print('Is', lst_d, 'instance of list?', d)
print('Is', dict_e, 'instance of dictionary?', e)

# String formatting: Replace the placeholders with a value: "Anna has ___ apples and ___ peaches."
# 5. With .format and curly braces {}
print("Anna has {} apples and {} peaches.".format(4, 3))

# 6. By passing index numbers into the curly braces.
print("Anna has {1} apples and {0} peaches.".format("43", "77"))

# 7. By using keyword arguments into the curly braces.
print("Anna has {ap} apples and {0} peaches.".format("498", ap="88"))

# 8*. With indicators of field size (5 chars for the first and 3 for the second)
print("Anna has {0:5} apples and {1:3} peaches.".format("34", "22"))

# 9. With f-strings and variables
apple = 45
peaches = 32
print(f"Anna has {apple} apples and {peaches} peaches.")

# 10. With % operator

apple = 56
peaches = 34
print("Anna has %d apples and %d peaches." % (apple, peaches))

# 11*. With variable substitutions by name (hint: by using dict)

apple = 21
peaches = 37
data_dict = {"ap": apple, "pch": peaches}
print("Anna has %(ap)d apples and %(pch)d peaches." % data_dict)

# Comprehensions:
# 12. Convert (1) to list comprehension
# (1)
lst = []
for num in range(10):
    if num % 2 == 1:
        lst.append(num ** 2)
    else:
        lst.append(num ** 4)
print(lst)
# list comprehension >>
list_comp = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(list_comp)

# 13. Convert (2) to regular for with if-else
# (2)
list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
print(list_comprehension)

# regular for with if-else >>
regular_lst = []
for num in range(10):
    if num % 2 == 0:
        regular_lst.append(num // 2)
    else:
        regular_lst.append(num * 10)
print(regular_lst)

# 14. Convert (3) to dict comprehension.
# (3)

d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
print(d)
# dict comprehension >>
d = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}
print(d)

# 15*. Convert (4) to dict comprehension.
# (4)
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
    else:
        d[num] = num // 0.5
print(d)
# dict comprehension>>

d = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}

print(d)

# 16. Convert (5) to regular for with if.
# (5)
dict_comprehension = {x: x ** 3 for x in range(10) if x ** 3 % 4 == 0}
print(dict_comprehension)

# dict regular>>
dict_regular = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        dict_regular[x] = x ** 3
print(dict_regular)

# 17*. Convert (6) to regular for with if-else.
# (6)
dict_comprehension = {x: x ** 3 if x ** 3 % 4 == 0 else x for x in range(10)}
print(dict_comprehension)

# regular >>
dict_comprehension = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        dict_comprehension[x] = x ** 3
    else:
        dict_comprehension[x] = x
print(dict_comprehension)


# 18. Convert (7) to lambda function
# (7)
def foo(x, y):
    if x < y:
        return x
    else:
        return y


print(foo(2, 3))

# lambda >>
foo = lambda x, y: x if x < y else y
print(foo(2, 3))

# 19*. Convert (8) to regular function

# (8)
foo = lambda x, y, z: z if y < x and x > z else y

print(foo(2, 3, 4))


# regular>>>
def foo(x, y, z):
    if y < x and x > z:
        return x
    else:
        return y


print(foo(2, 3, 4))

# 20. Sort lst_to_sort from min to max
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]

# sorted>>
print(sorted(lst_to_sort))

# 21. Sort lst_to_sort from max to min
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]

# sorted reversed >>
print(sorted(lst_to_sort, reverse=True))

# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2

lst_new = list(map(lambda x: x * 2, lst_to_sort))
print(lst_new)

# 23*. Raise each list number to the corresponding number on another list:
list_A = [2, 3, 4]
list_B = [5, 6, 7]

lst_cor_num = list(map(lambda x, y: x ** y, list_A, list_B))
print(lst_cor_num)

# 24. Use reduce and lambda to compute the numbers of a lst_to_sort.

lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
lst_to_sort_2 = functools.reduce(lambda x, y: x + y, lst_to_sort)
print(lst_to_sort_2)

# 25. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.

lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
new_lst = list(filter(lambda x: (x % 2 == 1), lst_to_sort))
print(new_lst)

# 26. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.
b = range(-10, 10)
new_lst = list(filter(lambda n: n < 0, range(-10, 10)))
print(new_lst)

# 27*. Using the filter function, find the values that are common to the two lists:

list_1 = [1, 2, 3, 5, 7, 9]
list_2 = [2, 3, 5, 6, 7, 8]
result = list(filter(lambda x: x in list_1, list_2))
print("Common values are: ", result)
