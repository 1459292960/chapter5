age=int(input('please enter your age:'))
if age<2:
    print('You are  a baby!')
elif age<4:
    print('You are toddling.')
elif age<13:
    print('You are a children.')
elif age<20:
   print('You are a teenager.')
elif age<65:
    print('You are a adult.')
else:
    print('You are the aged.')