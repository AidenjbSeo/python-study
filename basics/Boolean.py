# Boolean
# Boolean can take only True and False
print(True)
print(False)

# So, how to make a Boolean?
# We can make a Boolean statement by using a comparison operator
'''
== means 'equal to'
!= means 'Not equal to'
< means 'smaller'
> means 'greater'
<= means 'smaller than or equal to'
>= means 'greater than or equal to'
'''

print(10 == 100)
print(10 != 100)
print(10 < 100)
print(10 > 100)
print(10 <= 100)
print(10 >= 100)

# Python also has a Boolean system in the string
# alphabet a is smaller than alphabet z since a is the 1st alphabet in the alphabet roll
print("a" == "a")
print("a" != "z")
print("a" < "z")
print("a" > "z")
print("a" <= "z")
print("a" >= "z")

# We can also compare the range by using a Boolean
x = 25
print(20 < x < 30)
y = 20
print(15 < y < 17)

# Logical Operator
'''
not -> switch the boolean (ex. True -> False)
and -> print True when both statements are true
or -> print True even if one statement is true while another one is still false
'''
print("#Logical Operator")
print(not True)
print(not False)

# Utilize the Boolean and Logical Operators
print("# Utilize the Boolean and Logical Operator")

age = int(input("Type your age: "))
under_20 = age < 20
print("under_20: ", under_20)
print("not under_20: ", not under_20)

# and operator & or operator
print("# and operator & or operator")
print(True and True)
print(True and False)
print(False and False)
print (False and True)
print("")
print(True or True)
print(True or False)
print(False or False)
print(False or True)
