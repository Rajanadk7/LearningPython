marks=[12,56,32,98,12,45,1,4]
index=0
for mark in marks:
    print(mark)
    if(index==5):
        print("rajan you passed the exam")
    index +=1
# to implement the enumerate function we dont need to write the index and we need 
# to specify the index before declearing the function
for index,mark in enumerate(marks):
    print(mark)
    if(index ==3):
        print("rajan you passed the exam")
    index+=1