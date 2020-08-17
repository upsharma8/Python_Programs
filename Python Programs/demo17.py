r=open(r'E://upmanyu//python//myname.txt','r')
h=r.read(10)
print(h)


       
#how to check current position
pos=r.tell()
print('current positio',pos)

#how to reposition the pointer in the beginning
post=r.seek(5)
d=r.read(post)
print(d)
r.close()
