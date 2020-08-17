#Dicrionary dataa type
#store multiple vlues in a single variable
#it will the values against a key

d={'name':'Bipul','age':30,'email':'bipul@gmail.com'}

#add a new value into dic
d['college']='IITD'
#update a existing valu
d['name']='Upmanyu'

#delete an information from a dictionary
del d['age']

print(d['name'])

print(d['email'])
d1={0:[2,3,4,5],1:'hello'}
print(d1)
d1.update(d)
print(d1)


print(d.keys())
print(d.values())
print(d)
print(len(d))


#to clear all value of dictionary
d1.clear()
print(d1)



