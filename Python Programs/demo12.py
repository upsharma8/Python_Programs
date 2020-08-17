#break and continue in a loop

i=1
while i<10:
    print(i)
    i=i+1
    if i==5:
        break
names=['Bipul','pavan','rahul','john','james']
for i in names:
    if i=='rahul':
        continue
    print(i)
    
