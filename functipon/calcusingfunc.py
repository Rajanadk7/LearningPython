def calculator(a, b):
    addition=a+b
    subtraction=a-b
    multiplication=a*b
    division=a/b
    return addition , subtraction, multiplication, division
# splitting the input and converting each part into and integer
a,b= map(int,input("enter the numbers a and b seperated by the space:").split())
# calling calculator function and and unpacking the results
addition , subtraction, multiplication, division= calculator(a,b)
# printing each and every result seperately
print(f"Addition:", addition)
print(f"Subtraction:",subtraction)
print(f"Multiplication:",multiplication)
print(f"Division;",division)