current_users=['john','victor','raul','jack','Bob']
new_users=['bob','jessi','luis','raul','sheldon']
for new_user in new_users:
    judge=False
    for current_user in current_users:
        if new_user.lower()==current_user.lower():
            judge=True
            break


    if judge==True:
        print('Sorry,%s has been used./'
              'Please pick another nick name.'%new_user)
    else:
        print("Congratulation! %s hav't been used!"%new_user)


