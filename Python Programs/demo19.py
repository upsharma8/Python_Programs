'''
try:
    r=open('E://upmanyu//python//hellon.txt','r')
    print(r.read())
except FileNotFoundError:
    print('File is not there')
'''
#WAP to handle a eception in case only read access is given to a file
#And user try to write somethin into the file
try:
    w=open('E://upmanyu//python//helloworld.txt','r')
    w.write('Welome to India')
    w.close()

except IOError:
            print('Not Writable')

else:
        print(Written)
    
