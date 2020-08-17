#File Handling
#How to acess a file
#Step 1- Create a file to be access
#Step 2- Access the file
'''
open('E:\\upmanyu\\Python\\myname.txt','r')
print(r.read())


r=open('E:/upmanyu/Python/myname.txt','w')
r.write('I am a python programmer \n I like to write python code')
r.close()
print('File written succesfully')

'''


#copy a file data
#open old file
oldfile=open('E:\\upmanyu\\Python\\myname.txt','r')
newfile=open('E:\\upmanyu\\Python\\hello.txt','w')
newfile.write(oldfile.read())
newfile.close()
print('Data copied')
