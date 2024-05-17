# list of all odd numbers between 3 and 30
print(list(range(3,33,2)))
#  largest among the list
x=[4,8,20,90,30,1001]
print(max(x))
def display_student(name, age):
    print(name, age)

# call using original name
display_student("Emma", 26)

# assign new name
showStudent = display_student
# call using new name
showStudent("Emma", 26)