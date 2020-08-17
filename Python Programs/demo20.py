#classes in python
'''
def student(name,age):
    return(name,age)

s1= student('Bipul',30)
s2=student('Rahul',27)

print(s1)
print(s2)
'''

class Student:
    count=0
    def __init__(self,name,age):
        self.n=name
        self.a=age
        Student.count=Student.count+1
    def displaycount():
        print("Count:",Student.count)

    def displayStudent(self):
        print("Name:",self.n,"age:",self.a)

    def displaydata(self):
        print(self.n,"is of age:",self.a)
#Instances of class

s1=Student("Pavan",27)
s2=Student("John",28)
s3=Student("james",32)
s1.displayStudent()
s2.displayStudent()
s3.displayStudent()
s1.displaydata()
s2.displaydata()
s3.displaydata()

Student.displaycount()

#getattr()
#hashattr()
#setattr()
#delattr()
print(getattr(s1,'a'))
print(hasattr(s1,'n'))
setattr(s1,'a',45)
delattr(s1,'a')
s1.a=35
s1.n='Bipul'
s1.displayStudent()






    
        
        
