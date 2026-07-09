# if statement
'''
if statement is a system that executes a block of code only
When a specified condition evaluates to
'''

if True:
  print("It's True!")
  print("Wow it is True!")

if False:
  print("It's False...")

# now we can determine whether a number whether they are a positive or a negative number

number = int(input("Type any integer: "))

if number > 0:
  print("It's a postivie number!")

if number < 0:
  print("It's a negative number!")

if number == 0:
  print("It's zero")

# We can also determine whether a number is an odd or an even number

num = int(input("Type any integer: "))

if num % 2 == 1:
  print("It's an odd number!")

else:
  print("It's an even number!")

# And there is another way to do it
numm = input("Type the integer: ")

# take out the last character
last_char = numm[-1]
last_num = int(last_char)
# check even number
if last_num == 0 \
  or last_num == 2 \
  or last_num == 4 \
  or last_num == 6 \
  or last_num == 8:
  print("It's an even number!")
#check odd number
if last_num == 1 \
  or last_num == 3 \
  or last_num == 5 \
  or last_num == 7 \
  or last_num == 9:
  print("It's an odd number!")

# We can utilize the date & time

# import date and time
import datetime

# find the current date and time
now = datetime.datetime.now()

# now print
print("{} {} {} {} {} {}". format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
))

# Now we are going to determine now is daytime or not
import datetime

now1 = datetime.datetime.now()

if now1.hour < 12:
  print("It's {} so it's a daytime!". format(now1.hour))

if now1.hour >= 12:
  print("It's {} so it's not a daytime!". format(now1.hour))

# We can also determine the season!
import datetime

now2 = datetime.datetime.now()
# if we want to change 6 -> June
# use strftime()
'''
strftime("%B") -> June
strftime("%b") -> Jun
strftime("%m") -> 06
'''

monthname = now2.strftime("%B")

if 3 <= now2.month <= 5:
  print("It's {} so it's a spring season!". format(monthname))

if 6<= now2.month <= 8:
  print("It's {} so it's a summer season!". format(monthname))

if 9 <= now2.month <= 11:
  print("It's {} so it's a Fall season!". format(monthname))

if now2.month == 12 or 1 <= now2.month <= 2:
  print("It's {} so it's a winter season!". format(monthname))


