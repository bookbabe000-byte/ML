


'''
class student_info:
  def _init_(self,name,roll_no,address):
    print("i am called")
    self.name=name
    self.roll_no=roll_no
    self.address=address
    print(self)
  def student_info(self):
    print(f"name:{self.name}|roll_name:{self.roll_no},|address{self.address}")
s1=student_info("student_name","007","brt")
print(s1.name,s1.roll_no,s1.address)
s1.student_info()
print(s1)
'''

#car class with properties brand ,model,whether the car is ev or diesel car with methods:start,stop,break and car info to car info to print the distributes of the car

'''
class parent:
    hair_color="golden brown"

class child(parent):
    pass
child1=child()
print(child1.hair_color)
'''

class person:
    def __init__(self,name,age):
      self.name=name
      self.age=age
    def introduce(self):
         print("i am {self.name} and and i am {self.age} year old.")
class student(person):
   def __init__(self, name, age,roll_no):
      super().__init__(name, age)     
      self.roll_no=roll_no
   def student_info(self):
     print(f"i am {self.name},i am student,my age is {self.age},my roll number is{self.roll_no}")

class Teacher(person):
   def __init__(self, name, age,subject):
      super().__init__(name, age)
      self.subject=subject

   def teach(self):
        print(f"i taech{self.subject}")      

## creating object
            

s1=student("ram",30,"007")
t1=Teacher("SUJAN",30,"maths")
s1.student_info()
s1.introduce()
t1.teach()