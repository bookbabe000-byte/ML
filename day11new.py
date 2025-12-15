
# class student:
#     name="student_name"
#     roll_no="007"
#     section="nobel"

# s1=student()    
# s2=student()
# s3=student()        
# print(s1.name)
# print(s2.roll_no)
# print(s3.section)


class student:
  def _init_(self,name,roll_no,address):
    print("i am called")
    self.name=name
    self.roll_no=roll_no
    self.address=address
s1=student("student_name","007","brt")
print(s1.name,s1.roll_no,s1.address)
    
# s1=student()    
# s2=student()
# s3=student()        

