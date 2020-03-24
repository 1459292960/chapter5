cars=['audi','bwm','subaru','toyota']
age=15
car='BYD'
age=12
if age<4:
    price=0
elif age<18:
    price=5
else:
    price=10
available_toppings=['mushroom','olives',\
                    'green peppers','pepperoni',\
                    'pineapple','extra cheese']
req_toppings=['mushroom','french fries','extra cheese']
for req in req_toppings:
    if req in available_toppings:
        print('Adding %s.'%req)
    else:
        print("Sorry, we don't have %s."%req)