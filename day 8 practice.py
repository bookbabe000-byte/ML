#wap to people who r above 18 can vote and above 80 cant vote and clg stds r not alloed go in the rallly
'''
age=int(input("enter the age of people:"))
if(age>=18):
          print("can vote")
          print("not allowed to move on the rally of partiies.")
else:
    print("can't vote\nnot allowed move on rally ")
   '''

##WAP TO CHECK IF A NUMBER IS ODD OR EVEN
'''
num=int(input("enter the number:"))
if(num%2!=0):
    print("number is odd:")
elif(num%2==0):
    print("number is even:")
    '''

#wap to find the graetest of 3 numbers

'''
num1=int(input("enter the number"))

num2=int(input("enter the number"))

num3=int(input("enter the number"))
if(num1>num2 and num1>3):
    print("num1 is is greater:",num1 )
elif(num2>num1 and num2>num3):
    print("num2 is greater",num2) 
else:
    print("num3is greater",num3)       
'''

#wap to check if a number is a multiple of 7 or not
'''
x=int(input("enter the number"))
if(x%7==0):
    print("number is multiple of 7")
else:
    print("number is not multiple of 7")    
    '''

#listing
'''
student=["dhiraj sah","biratnagar",9705946375,"arniko +2",12]
print(student)
print(len(student))
print(type(student))
'''
'''
student=["dhiraj sah","biratnagar",9705946375,"arniko +2",12]
print(student[3])
student[3]=9827876618
print(student)
'''
'''
list=[1,2,3,4]
# list.append(5)
print(list.sort())
# print(list.sort(reverse=True))
print(list)
''' 


#tuple
''''
tup=()
print(tup)
print(type(tup))
'''

'''
tup=(1,2,3,4,5)
print(tup)
print(type(tup))
print(tup[1:5])
'''
'''
tup=(1,2,3,4,5)

print(tup.index(3))
print(tup.count(3))
'''

#wap to ask the names of 3 movies and store them in list

'''
movies=[]
movies.append(input("enter the 1st movie name:"))
movies.append(input("enter the 2nd movie name:"))
movies.append(input("enter the 3rd movie name:"))
print(movies)
'''

#wap to check if a list contains a palindrome of elements 
'''
# num_list = [1,2,3,2,1]
num_list2=[1,2,3,4]

copy_num_list=num_list2.copy()
copy_num_list.reverse()

if(copy_num_list==num_list2):
    print("palindrome")
else:
    print("not palindrome")
'''


# WAP to count the number of students with the “A” grade in the following tuple.

# Store the above values in a list & sort them from “A” to “D”
# .

# [”C”
# ,
# “D”
# ,
# “A”
# ,
# “A”
# ,
# “B”
# ,
# “B”
# ,
# “A”]

'''

grade=['C','D','A','B','B','A']
print(grade.count('A'))
grade.sort()
print(grade)
'''

