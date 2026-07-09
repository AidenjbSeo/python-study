#for()
'''
A for loop iterates over elements of an iterable (list, string, range, etc.) one by one.
and executes code repeatedly

 for variable in iterable
 code

read it like:
for each element in the iterable,
Store it in the variable and run the code
'''

# loop through numbers with range()
for i in range(10): # 0 ~ 9
  print(i)

print("")
for i in range(1, 6): # 0 ~ 5
  print(i)

print("")
for i in range(0, 10, 2):
  print(i)


# loop through a list
fruitss = ["apple", "banana", "orange"]

for fruit in fruitss:
  print(fruit)
  '''
  apple
  banana
  orange
  '''
# loop through a string
print("")
for letter in "hello":
  print(letter)
  '''
  h
  e
  l
  l
  o
  '''

# we can also add..
print("")

for fruit in fruitss:
  print("-",fruit)
'''
- apple
- banana
- orange
'''

print("")
for i in range(5):
  print("0", i)
'''
0 0
0 1
0 2
0 3
0 4
'''

# use index with range(len())
print("")
subject = ["math", "english", "history"]

for i in range(len(subject)):
  print(i, subject[i])
  '''
  i == index
  subject[i] == element
  print(index, element)
  '''

# useful loop keywords
'''
break (stop the loop)
continue ( skip to the next iteration)
pass (do nothing)
'''
# example for break
print("")
for i in range(10):
  if i == 5:
    break

  print(i)
  '''
  0
  1
  2
  3
  4
  '''

# example for continue
print("")
for i in range(5):
  if i == 2:
    continue

  print(i)
  '''
  0
  1
  3
  4
  '''

print("")
for letter in "hello":
  if letter == "l":
    continue

  print(letter)
  '''
  h
  e
  o
  '''

# example for pass
print("")
for i in range(5):
  if i == 2:
    pass

  print(i)
  '''
  0
  1
  2
  3
  4
  '''

# nested list, nested loop
# nested list -> list inside another list
# nested loop -> loop inside another loop

list_of_list = [
    [1, 2, 3],
    [4, 5, 6, 7],
    [8, 9]
]

for items in list_of_list:
  print(items)
'''
index
0 -> [1, 2, 3]
1 -> [4, 5, 6, 7]
2 -> [8, 9]
'''

list_of_list1 = [
    [1, 2, 3],
    [4, 5, 6, 7],
    [8, 9]
]

for items in list_of_list1:
  '''
index
0 -> [1, 2, 3]
1 -> [4, 5, 6, 7]
2 -> [8, 9]
'''
  for item in items:
    '''
    items = [1, 2, 3]
    item = 1
    item = 2
    item = 3
    3 elements in the list

    items = [4, 5, 6, 7]
    item = 4
    item = 5
    item = 6
    item = 7
    4 elements in the list

    items = [8, 9]
    item = 8
    item = 9
    2 elements in the list

for item in items repeats as many times as
There are elements in the list of items

    '''
    print(items)


# Unpacking operator

numb = [1, 2, 3]
print(*numb) # 1 2 3
# without * -> [1, 2, 3]
# with * -> 1 2 3

a = [1, 2, 3, 4]
b = [*a, *a]
b
print("")
b = [1, 2, 3, 4]
c = [*b, 5]
b
print(b)
print("")
c
print(c)

aa = [1, 2, 3, 4]
aa.append(5)
print(aa) # -> aa list does change

aaa = [1, 2, 3, 4]
print(*aaa) # -> works as print(1, 2, 3, 4)
