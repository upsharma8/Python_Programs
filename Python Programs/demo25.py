f=open('E://upmanyu//Python//helloworld.txt','r+')
lines=f.read()
#print(lines.split('.'[3])
'''
for i in range(len(lines.split('.'))):
    print(i)
'''
k=open('E://upmanyu//Python//helloworld.txt','w')
for i in lines.split('.'):
    if(i!='I am a python programmer'):
        k.write(i)
k.close()
