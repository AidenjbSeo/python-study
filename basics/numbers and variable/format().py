# format()

'''
Format is a function that we input some variable into a string and get an output
'''
F = "{}" .format(10)
print(F)
print(type(F))

S = "{} {}" .format(10, 30)
print(S)
print(type(S))

print(F, S)

# We can utilize input() here
PP = input("Type your income: ")
format_a = "{} bucks". format(PP)
print(format_a)
format_b = "In 10 years later your income will be {}, after 20 is {}, and after 30 is going to be {}". format("double", "triple", "forth")
print(format_b)

#IndexError
#IF we have more number of {} than the variable, then it will cause an IndexError

TT = "{} {}". format(1, 2, 3)
print(TT)

"""
FF = "{} {} {}". format(1, 2)
print(FF)
"""

# More functions of the format()
# various types of integer prints

#Integer
output_a = "{:d}". format(13)

# print in the specific field
output_b = "{:10d}". format(123) # spaced 10 times
output_c = "{:5d}". format(123) # spaced 5 times

# Fill "0" in the empty spot
output_d = "{:010d}". format(123) # Positive number
output_e = "{:015d}". format(-123) # Negative number

print(output_a)
print(output_b)
print(output_c)
print(output_d)
print(output_e)

# Print with signs +, -
output_f = "{:+d}". format(10) # printed with + sign
output_h = "{:+d}". format(-10) # printed with - sign
output_i = "{: d}". format(52) # postivie number, empty space for sign's location
output_j = "{: d}". format(-52) # negative number, empty space for sign's location

print(output_f)
print(output_h)
print(output_i)
print(output_j)

#Combination
output_k = "{:+5d}". format(20) # 5 space shifted with + sign
output_l = "{:+5d}". format(-20) # 5 space shifted with - sign
output_m = "{:=+5d}". format(20) # sign does not shift
output_n = "{:=+5d}". format(-20)
output_o = "{:+05d}". format(20) # fill 0's in the empty spot
output_p = "{:+05d}". format(-20)

print(output_k)
print(output_l)
print(output_m)
print(output_n)
print(output_o)
print(output_p)

#Important: combination does matter
"""
output_aa = "{:=0+5d}". format(10)
print(output_aa)
"""

# float "{:f}"
output_qq = "{:f}". format(52.345)
output_ww = "{:15f}".format(52.345) # 15 spaced
output_ee = "{:+15f}". format(52.345) # 15 spaced with +
output_rr = "{:+015f}". format(52.345) # fill 0 in the empty spot

print(output_qq)
print(output_ww)
print(output_ee)
print(output_rr)

# Specify decimal point "{:.#f}"
output_yy = "{:15.3f}". format(52.345)
output_uu = "{:15.2f}". format(52.345)
output_ii = "{:15.1f}". format(52.345)
output_oo = "{:.1f}". format(52.345)

print(output_yy)
print(output_uu)
print(output_ii)
print(output_oo)

# reduce the meaningless decimal points "{:g}"
output_pp = 15.0
output_ppp = "{:g}". format(output_pp)
print(output_pp)
print(output_ppp)

# but "{:g}" can't reduce all the decimal points like
output_aaa = 15.1231231
output_sss = "{:g}". format(output_aaa)
print(output_sss)
# we can apply (it might round the decimal point)
output_aaaa = 15.1231231
output_ssss = "{:.0f}". format(output_aaaa)
print(output_ssss)

# Capital case and lower case
# upper(), lower()

qw = "Hello World"
print(qw.upper())
print(qw.lower())

# remove the empty spaces between the string
#strip() -> able to remove the spaces on the left and right
#lstrip() -> able to remove the spaces on the left side
#rstrip() -> able to remove the spaces on the right side

input_as = """

Hello?
This is Aiden.

            """
print(input_as.strip())


# Determine the composition of the string
# isOO()
'''
isalnum(): check if a string consists only of letters or numbers
isalpha(): check if a string is an alphabet
isidentifier(): check if the string is a valid identifier
isdecimal(): check if the string is an integer
isdigit(): check if the string can be identified as a number
isspace(): check if the string is empty
islower(): check if the string is the only lowercase string
isupper(): check if the string is the only upper case string
'''
print("Aiden100" .isalnum()) # True
print("10" .isdigit()) # True
print("10.2" .isdecimal()) # False

# find the specific string
# find(), rfind()

out_a = "HelloHello". find("H") #from the left
print(out_a)
out_b = "HelloHello". rfind("H") # from the right
print(out_b)

# Searching the string, in

print("Hello" in "Hello World") #True
print("Hello" in "hello world") # False (Capital case does matter)
print("Bye" in "Hello World") # False (Not exist)

# Split the string
# split()

sp = "10 20 30 40 50".split(" ")
spp = "10 20 30 40 50".split("0")
# 공백을 기준으로
print(sp)
print(spp)

#f string
# f string provides the simple version of the format()
asd = "{}". format(10)
print(asd)
asde = f'{10}'
print(asde)

# We can also
f"3 + 4 = {3 + 4}"

f""" 1 + 2 = {1 + 2}
2 + 3 = {2 + 3}
3 + 4 = {3 + 4}
"""

# format() VS f string
# prefer format() when the string is too long
# prefer format() when the input variables are too many
