#tupe-It is a form of array but immutable
#In list- add,remove,replace or insert id possible
#Tuple - No change can happen
#object hashed using hash() are irreversible,
#that means you migh loose information

t=(12,34,56,7)
#t[2]=789
'''
print(t)
print(t[2])

print(max(t))
print(min(t))
print(t*2)
print(12 in t)

t1=(4,7,7,)
t2=t+t1
print(t2)'''
#l=[2,3,4,5]
print(hash(t))
#print(hash(l))

# hash can be used only for immutable (can only be used for tuple)
# hash can't be used for list as it is mutable
