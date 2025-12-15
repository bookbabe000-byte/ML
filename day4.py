
'''
password=input("enter your password")
min_len=8
default_password="12345678"


is_longer=len(password)>min_len
is_not_default=(password !=default_password)

print(f"the entered password is longer?:",(is_longer))
print(f"the entered password isnot longer?:"(is_not_default))
'''
'''
password=input("enter your password")
min_len=8
max_len=20
default_password="12345678"

is_longer=len(password)>min_len
is_not_default=len(password !=default_password)
is_shorter_than_max=len<max_len

print(f"the entered password is longer",{is_longer})
print(f"the entered password is default",{ default_password})
print(f"the entered password isnot longer: ")
'''

#logical operator
'''
a=True
b=False
print(f"True and True:,{a and a}")
print(f"True and False:,{a and b}")
print(f"False and True:,{b and a}")
print(f"False and False:,{b and b}")
'''
#find which one is greater
'''
a=34
b=44
c=56
is_a_max=(a>b)and(a>c)
is_b_max=(b>a)and(b>c)
is_c_max=(c>a)and(c>b)

print(f"is a maximum?:{is_a_max}")
print(f"is b maximum?:{is_b_max}")
print(f"is c maximum?:{is_c_max}")
'''
'''
a=[1,2,3]
b=[1,2,3]
print(a is b)
print(a==b)
'''
'''
li1=[3,4,7]
print(9 in li1)
'''
'''
name=input("enter your name:")

print("a" in name)
'''