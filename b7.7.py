file=open("abc.txt","r")
s=0
for line in file:
    s=s+1
print("so dong cua file la: ",s)
file.close()
