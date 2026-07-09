# dictionary and loop
# dictionary is a data type that stores data as key-value pairs
'''
# structure
dictionary = {
    key: value
}
'''

# example

student = {
    "name": "Aiden",
    "age": 23,
    "major": "Math"
}

'''
# structure

key      value
--------------
name -> Aiden
age -> 23
Major -> Math
'''

# loop the key

student = {
    "name": "Aiden",
    "age": 23,
    "major": "Math"
}

for key in student:
  print(key)
'''
name
age
major
'''

# print the value
for key in student:
  print(student[key]) # student[key] -> access value
'''
Aiden
23
Math
'''

# print with key and value (items())
student = {
    "name": "Aiden",
    "age": 23,
    "major": "Math"
}

for key, value in student.items():
  print(key, value)
  '''
  items()
  ->
  (key, value)
  (key, value)
  (key, value)
  '''

# example

scores = {
    "Math": 95,
    "English": 88,
    "Physics": 91
}

for keyy, valuee in scores.items():
  print("{} : {}".format(keyy, valuee))


