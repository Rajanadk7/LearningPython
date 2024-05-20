# same as the set in a mathmatices
x={1,2,44,55,"ram","hari",44}
print(x)
# it does not print the same element twice since 44 is not printed twice
# to inatialize the each element or value of the set
for value in x:
    print(value)
# the different set operation that can be done
s1={1,2,5,6}
s2={3,6,7,8}
# to find union between to sets
print(s1.union(s2))
# to update s1 and s2
s1.update(s2)
print(s1,s2)
# to find the intersection between two sets
s1.intersection_update(s2)
print(s1)
# to find the difference between two sets
s3=s1.difference(s2)
print(s3)
#  to find superset and subset of the given sets
print(s1.issuperset(s2))
print(s2.issubset(s1))
# to remove element from the set 
s1.remove(6)
print(s1)
# discard can also be use to discard elemnet from the set
# pop method can be used to pop the random element from the element
item =s1.pop()
print(s1)
print(item)
# to check the item or element existance and print or initialize them
if 7 in s2:
    print("lucky no 7")
else:
    print("you are not lucky")