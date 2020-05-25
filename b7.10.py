file=open("aaa.txt","r")
a=file.read()
b=[x for x in a.split(' ')]
c=b[0]
for i in b:
    if i>c:
        c=i
print('chu dai nhat trong van ban la: ',c)
