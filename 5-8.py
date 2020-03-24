users=[]
user=input('please enter your nick name:')
if users:
    if user == 'admin':
        print('Hello %s.Would you like to see a status report ?' % user)
    else:
        print("Hello Eric,thank you for logging in!")
else:
    print('We need to find some users!')

