# list
'''
list: a file that can save various information
'''
array = [212, 32, 20, "hi", True, False]
print(array)

# informations in the [] are called elements
# position in the [] is called index

fruits = ["apple", "banana", "orange", "mango"]

'''
element: "apple", "banana", "orange", "mango"
----------------------------------------------
index:      0        1         2         3
'''

fruits[0] # -> apple
fruits[1] # -> banana
fruits[2] # -> orange
fruits[1:3] # [banana, orange]

# We can also change the element in the list
list_a = [1, 2, 3, 4, 5, "hi", True]

list_a[0] = 100 # -> [100, 2, 3, 4, 5, 'hi', True]
list_a

# we can call the element from the back
list_b = [1, 2, 3, 4, 5, "hi", True]

list_b[-1] # -> True
list_b[-2] # -> 'hi'

# We can use the access operator simultaneously
list_c = [1, 2, 3, 4, 5, "Hello", True]

list_c[5]
list_c[5][0] # -> 'H'
# it finds the fifth element and  prints the 0th element from the fifth element

# we can use the list in the list
list_d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list_d[1] # -> [4, 5, 6]
list_d[1][1] # -> '5'

# IndexError in the list
# if we call the element that is not in the list, it causes an IndexError

'''
list_e = [1, 2, 3]
list_e[3]
-> IndexError
'''

# connect(+), repeat(*), len()
list_f = [1, 2, 3]
list_g = [4, 5, 6]

print("# list")
print("list_f =", list_f)
print("list_g =", list_g)
print("")
print("# list connection operator")
print("list_f + list_g = ", list_f + list_g)
print("list_f * 3 =", list_f * 3)
print("")
print("# length of the list")
print("len(list_f) =", len(list_f))


# append(), insert()
# append() -> add an element at the back
# insert() -> add an element wherever you want

print("# append()")
ff = ["apple", "banana"] # -> ["apple", "banana"]
print(ff)
ff.append("mango")
print(ff) # -> ["apple", "banana", mango]

number = []
number.append(10)
number.append(20)
print(number)

# insert()
print("insert()")
#list.insert(index, element)

number1 = ["apple", "banana"]
print(number1) # -> ["apple", "banana"]
number1.insert(1, "mango")
print(number1) # -> ["apple", "mango", "banana"]

# extend()
print("# extend()")
list_q = [1, 2, 3]
print(list_q) # -> [1, 2, 3]
list_q.extend([4, 5, 6])
print(list_q) # -> [1, 2, 3, 4, 5, 6]

# difference between extend() and list + list

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_1 + list_2
print(list_1) # -> still [1, 2, 3]
print(list_2) # -> still [4, 5, 6]

list_3 = [1, 2, 3]
list_4 = [4, 5, 6]
list_3.extend(list_4)
print(list_3) # -> [1, 2, 3, 4, 5, 6] by destructive operation
print(list_4) # -> [4, 5, 6]
# destructive operation means changing the original data to something else
'''
 tip: not using a destructive operation is better than using a destructive operation.
 since storing the original data gives us more choices.
'''

# del and pop()
#del()
list_0 = [0, 1, 2, 3, 4]

del list_0[1]
print(list_0) # list_0 = [0, 2, 3, 4]

#pop()
list_00 = [0, 1, 2, 3, 4]

list_00.pop(2)
print(list_00) # list_00 = [0, 1, 3, 4]

#pop() is able to return the removed value
item = list_00.pop(2) # [0, 1, 3, 4]

print(item) # 3
print(list_00) # list_00 = [0, 1, 4]

# if we don't assign the index, then it automatically removes the last index

list_11 = [0, 1, 2, 3, 4, 5]

kill = list_11.pop()
print(kill)
print(list_11)

# We can also assign the range
list_22 = [0, 1, 2, 3, 4, 5, 6]
del list_22[3:6]
list_22 # [0, ,1, 2, 6]

list_33 = [0, 1, 2, 3, 4, 5, 6]
list_44 = [0, 1, 2, 3, 4, 5, 6]
del list_33[:3] # [3, 4, 5, 6]
list_33
del list_44[3:] # [0, 1, 2]
list_44

#list slicing
# We assign the range and pattern to make a new list
# list = [starting_index:ending_index:pattern]

number2 = [1, 2, 3, 4, 5, 6, 7]
number2[0:5:2] # [1, 3, 5]

number3 = [1, 2, 3, 4, 5, 6, 7]
number3[::-1] #[7, 6, 5, 4, 3, 2, 1]

# remove()
# list.remove(value)

list_55 = [1, 2, 1, 2]
list_55.remove(2)
list_55 # [1, 1, 2]
'''
There are two "2" in the list, but the first "2" is deleted.
If we want to remove all "2" in the list, we can use a while loop
which we will learn later.
'''

# clear()
# delete all values in the index

list_cc = [0, 1, 2, 3]
list_cc.clear()
list_cc # []

# sort()
# sort in ascending order
# list.sort()
list_s = [57, 120, 7, 5, 6, 8, 100, 1, 95, 127, 110]
list_s.sort()
list_s # [1, 5, 6, 7, 8, 57, 95, 100, 110, 120, 127]
list_s.sort(reverse=True)
list_s # [127, 120, 110, 100, 95, 57, 8, 7, 6, 5, 1]

# in/not in
# checking whether the value is in the list or not
# value in list
list_v = [0, 2, 4, 5, 7, 10 ,12]
12 in list_v # True
4 in list_v # True
137 in list_v # False

# not in
12 not in list_v # False
4 not in list_v # False
137 not in list_v # True
