# list =[12,"hello",45]

# try:
#   print(list[3])
# except IndexError:
#   print("index is out of range")

'''

list1=["123","45",'34','hello','python','100']


converted_list=[]
for element in list1:
        try:
          converted_list.append(int(element))
        except ValueError:
             converted_list.append("invalid")
print(converted_list)
'''

'''

def calculate_score():
    phy=float(input("enter the marks of physics:"))
    chemi=float(input("enter the marks of chemistry:"))
    maths=float(input("enter the marks of maths:"))

    percent=(phy+chemi+maths) / 3
    return phy,chemi,maths,percent

def calculate_grade(percent):
if percent >=90:
    return"A"
def calculate_grade(percent):
elif percent >=70:
    return "B"
def calculate_grade(percent):
elif percent >=50:
   return"c"

def calculate_grade(percent):
elif percent>=40:
   return"D"
else:
   return "fail"
'''