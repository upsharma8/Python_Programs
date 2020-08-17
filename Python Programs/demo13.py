#functions in python

#function without arguments

#function is a combined block of code which
#execute only when trrigers
#function with argument
#executes with different parameters
'''
def name(k,l):
    print('hello',k,'and',l)
    print(3+6)
    
name('bipul','john')
name('rahul','James')
name('john','abcd')
'''

#wap to createfunction to add two values passed as argukent

def name(k,l):
    
    print(k+l)
    return(k+l)
    
p=name(2,3)
print(p)



#If you have 50 lines of code to be executed 5 times
#thorugout your program
#either you can write those 50 lines for 5 timesi.e 250 lines
# or you can create a function with just 50 lines and can call
#thes for 50 instances
