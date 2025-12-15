
'''
f = open("Newfolder/exception.py", "r")

for i in f.readlines():
    print(i)

f.close()
'''


## writing something in the file
'''
f=open("new.txt","w")
f.write(f"hello, this is the first line\n")
f.write(f"hello,this is 2nd file\n")
f.write(f"hello,this is 3rd file\n")
f.close()
'''

# f=open("new.txt","r")
# # data=f.read()
# line1=f.readlines(1)
# line2=f.readlines(2)
# print(line1)
# print(line2)

# f=open("new.txt","r")
# lines=f.readlines()
# print(lines)

# with open("new.txt","r")as f:
#     content=f.read()
#     print(content)

with open("new.txt",'with') as f1:
    content=f1.read()
with open("not.txt",'w') as f2:
    f2.write(content)
  
