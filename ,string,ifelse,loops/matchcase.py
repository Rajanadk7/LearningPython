a=int(input('enter the value of a:'))
# a is the variable to match
match a:
    case 0:
        print(' a is zero and wont be accepted')
    case 5:
        print('a is not accepted because its 5')
    case 50:
        print(a,'a is not accepted')
    case _:
        print(a)