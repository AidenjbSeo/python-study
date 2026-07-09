'''
variables
'''
#It's like a name tag that saves a variable or a string
# for ex.
pi = 3.141592
print(pi)
name = "Aiden"
print(name)
#variable usage
a = 10
b = 20
print("a + b =", a + b)

#And also, we saved pi is equal to 3.141592, which is a number
# We can also do simple mathematics
print(pi + 2)
print(pi - 1)
print(pi * 2)
print(pi // 2)
print(pi / 2)

#but we can't do math with strings
#pi + "answer"
# We get,
'''
TypeError                                 Traceback (most recent call last)
/tmp/ipykernel_601/192304328.py in <cell line: 0>()
     23 #but we can't do math with strings
     24
---> 25 pi + "answer"
     26 # Now we can calculate the perimeter and the area of the circle
     27 pi = 3.14159265

TypeError: unsupported operand type(s) for +: 'float' and 'str'
'''
# But if the "answer" is defined as a variable, then it makes sense
answer = 10
print(pi + answer)
# Then answer = 10, the answer is not a string anymore, it is a variable
# Now we can calculate the perimeter and the area of the circle
pi = 3.14159265
r = 10

print("pi =", pi)
print("radius =", r)
print("Perimeter of the circle is ", 2 * pi * r)
print("Area of the circle is ", pi * r * r)

'''
In Java and C, variables must be declared with a data type before use.
Python does not require explicit type declarations.

Python is a dynamically typed language.
The type belongs to the value (object), not the variable.

x = 10         x refers to an integer object
x = "hello"      x now refers to a string object

Variables can store different data types during execution.
print(x) -> x = 10
print(type(x)) -> type of "x" which is a class 'int'
'''
# We can declare like
K = "English"
K = True
K = 7
#This flexibility can be a good factor, but it also can cause a TypeError.
#Thus, it is better to use one data type in one variable

# Compound assignment operator
'''
name of the operator
+=
-=
*=
/=
%=
**=

for example it applies like
a = 80
a += 10 is same as a = a + 10
Then it is equal to a = 80 + 10
a = 90
'''
# Then we can make
N = 100
N += 10
N += 20
N += 30
N += 40
print("N :", N)

# We can also do,
W = "안녕하세요"
W += "!"
W += "!"
print("W :", W)

# input()

Y = input("Say anything you want~ :")

print(type(Y))

string_a = input("Type the number :")
int_a = int(string_a)
print(int_a)
print(type(int_a))

string_b = input("Type the float :")
float_b = float(string_b)
print(float_b)
print(type(float_b))

print("string info :", string_a + string_b)
print("number info :", int_a + float_b)

# Also we can change the numbers into a string
output_a = str(52)
output_b = str(52.143)
print(type(output_a), output_a)
print(type(output_b), output_b)

# With this, we can make a unit converter

raw_input = input("inch to cm, type inch :")

inch = int(raw_input)
cm = inch * 2.54
print(inch, "inch is ", cm ," cm ")

'''
assignment
make a unit converter
with cm, m, mm, inch, etc
'''
