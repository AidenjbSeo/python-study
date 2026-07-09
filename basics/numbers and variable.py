'''
Numbers
'''
# Numbers without decimal points are called integers,
# and numbers with decimal points are called floating-point numbers.
# Integer: 0, -1, 100, 2
# Floating-point number: 0.0, 52.273, -1.2
print(273)
print(52.273)
# Numbers can be printed by simply entering them.

print(type(52))
print(type(52.273))
# int: integer
# float: floating-point number (decimal)

0.52273e2
0.52273e-2
# Integer division operator: //
print("3 / 2 =", 3 / 2)
print("3 // 2 =", 3 // 2)
# The result of using // removes the remainder.

# Expression using the remainder operator %
print("5 % 2 =",5 % 2)
# The quotient is 2, and the remainder is 1.
# This prints the remainder value.

# Exponent operator: **
print("2 ** 1 =", 2 ** 1)
print("2 ** 2 =", 2 ** 2)
print("2 ** 3 =", 2 ** 3)

# Operator precedence
'''
 Multiplication and division are
 calculated before addition and subtraction.
 '''
print(2 + 2 - 2 * 2 / 2 * 2)
print(2 - 2 + 2 / 2 * 2 + 2)

# If you want addition or subtraction to happen first,
# use parentheses ()
print((5 + 3) * 2)

# TypeError
'''
A TypeError occurs when different data types are used together.

For example:

string = "text"
number = 273

string + number

The + operator was used between a string and a number.
Since different data types were combined, an error occurred.
'''
# How to fix TypeError
print("10" + str(5))
print(int("10") + 5)

# String and operator precedence

# In this case, the output is Hibyebyebye
print("Hi" + "bye" * 3)

# In this case, the output is HiboyHiboyHiboy
print(("Hi" + "boy") * 3)

# In this case, the output is Hibyebyebye
print("Hi" + ("bye" * 3))
