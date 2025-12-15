#function dfining
'''
def first_function():
    print("hello python programming")
first_function()
first_function()
first_function()
first_function()
first_function()
first_function()    
'''

#parameters
'''
def sec_fn(name,age):#parameters
    print(f"hello {name}!")
    print(f"your age is {age} year old")
sec_fn("dhiraj","20")    #arguments
'''
#sum of two numbers using user defind function

'''
def sum_fn(x,y):
    sum=x+y
    product=x*y
    division=x/y
    subtract=x-y
    print(sum)
    print(product)
    print(division)
    print(subtract)
sum_fn(4,64)    
'''

#rturn statment
'''
def sum_num(num1,num2):
    return (num1+num2)
# print(sum_num(45,45))

sum=sum_num(23,65)
print(sum)
'''

#parameters default
'''
def sum_fn(x=45,y=56):
    return x+y

print(sum_fn(67))    
'''

#wap to perform addition subtraction product using one return statement and svariables like sum difference product divisiontre results back to specific 

'''
def variables(n1,n2):
    sum=n1+n2
    diff=n1-n2
    product=n1*n2
    division=n1/n2
    return sum,diff,product,division
result=variables(23,23)
print(result)
'''
#create a multiple function for addition , subtraction multiplication and division and ask the uer to perform 
#which operation to be done and do th task as per userinput

#wap using multiple function to calculate the grade of the student,first function 
#to ask user about the score of the student ,2nd to check whether the user is pass or fail 
#(if score >50:pass otherwise fail)and is pass or fail, another function to
#calculate the grade of the passed student and display 