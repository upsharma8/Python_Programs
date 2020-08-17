'''
r=open('E://upmanyu//python//helloworld.txt','w')
r.write('Hello everyoe')
r.close()
print('File Created')
'''
#rename or delete a file
import os
'''
#os is library to access aa directory
os.rename('E://upmanyu//python//helloworld.txt','E://upmanyu//python//welcome.txt')
print('Rename succesfully')
'''
'''
import os
#Deleting a file
os.remove('E://upmanyu//python//hello.txt')
print('removed')
'''
#print(os.listdir())


#How to create a directory

#os.mkdir("directory")
#current working directory 


print(os.getcwd())
os.rmdir('directory')
