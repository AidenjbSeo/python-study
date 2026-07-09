# if, else, elif
# pass keyword and raise

'''
If a statement:
  print("when A statement is True")

elif B statement:
  print("when B statement is True")

elif C statement:
  print("when C statement is True")

else:
  print("None of them are True")
'''

# pass keyword
# it means "just skip the line".
# We need it when we need a code, but only for a structure.

num = int(input("type the integer"))

if num > 0:
  pass

else:
  pass

# if we leave them as a blank, it will cause an Indentation Error
# we can type 0 instead of pass. But pass is preferred since make people understand the code well

'''
Even though we typed pass, we might forget that we didn't figure it out
If the codes become more complicated.

So we use raise.

raise: it raises the error manually to remind us that we still need to figure it out.
'''

num1 = int(input("type the integer: "))

if num1 > 0:
  raise NotImplementedError

else:
  raise NotImplementedError
