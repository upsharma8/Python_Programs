#conditional statement
#if else
#comparison operstor
#==,>=,<=,>,<
'''
a=5
print(a)
if(a==5):
    print('hello')
else:
    print('welcome')

print(a==5)

print(a>5)
print(a<5)
print(a<=5)
print(a>=5)
print(a!=5)
'''
#Write a program for login application
#if user name and password both mathes with define credentials
#then print('welcome') else ('Try again')

uname=input('Enter name')
password=input('Enter Password')

if(uname=='upmanyu8' and password=='upmanyu9'):
    print('hello',uname)
elif(uname=='rahul' and password=='upmanyu9'):
    print('hello',uname)
    
else:
    print('try')
