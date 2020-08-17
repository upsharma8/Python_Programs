#looping in python
'''
for i in range(0,10):
    print('hello',i)
'''
engine=['google','yahoo','hello','rediff','bing']

for i in engine:
    print(i,len(i))

#Another way to do 

for i in range(len(engine)):
    print(engine[i],len(engine[i]))
    
for i in range(0,5):
    for j in range(0,i+1):
        print('*',end='')
    print('\r')
# '\r' is used for line break
#end is used for end value to give after each loop

for i in range(5):
    print(i,end='')

#homework    
j=1
or i in range(0,5):
    for k in j:
        print(end='','*')
    j=j+2 

    print('\r')

#while loop

steps=1
while(steps<10):
    print(steps)
    steps+=2
    

    

