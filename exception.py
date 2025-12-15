# s=int("1234567")
# print(s)
'''
try:
    s=int("12345")
    print(s)
    print(type(s))
except:
    print("exception occured!")
finally:
    print("code ended")
    '''

#wap to ask the two number from uer and perform division operation.
'''
try:
    num1=int(input("enter the first number"))
    num2=int(input("enter the 2nd number"))

    division =num1/num2
except ValueError:
    print("value error occured")
except ZeroDivisionError:
    print("zero division error occured")
except  TypeError:
    print("type error occured")
else:
    print(division)
finally:
    print("program ended") 
    '''