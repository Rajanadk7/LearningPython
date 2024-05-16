# Calculate the cube of all numbers from 1 to a given number
x=int(input("enter the number upto which cube to be calculated"))
i=0
for i in range(x):
    c=i*i*i
    print('the current umbers are',i,'the cube of numbers are',c)
# factorial of the given number
x=int(input("enter the number whose factorail is to be calculated"))
factorail=1
if x < 0:
    print('the factorial of the negetive number is not calculated')
elif x==0:
    print('the factorial does not exist')
else:
    for i in range(1,x+1):
        factorail=factorail*i
        print("the factorial of the given number is:",factorail)