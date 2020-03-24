string1='I want a sweet love.'
string2='I want a lovely girl.'
string3=string1[:]  # 复制一份字符串
if string1==string2:
    print('The two string are the same.')
else:
    print('Warning! The two string are different.')
if string1==string3:
    print('The two string are the same.')
car='BWm'
car2='bwm'
if car.lower()==car2.lower():
    print('The two car are the same !')
num1=25
num2=16
num3=19
if num1==25:
    print('You got it!')
if num2!=16:
    print('wrong number!')
if num3>18:
    print('You are already an adult!')
if num2<18:
    print('Study is your fist assignment!')
if num1>=18 and num2<=18:
    print('DIDIDI')
if num1>18 or num2>18:
    print('One of you is an adult.')

cars = ['audi', 'bwm', 'subaru', 'toyota']
if 'bwm' in cars:
    print("I'll got it!" )
if 'BYD' not in cars:
    print("wrong guess")