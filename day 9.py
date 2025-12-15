

'''
def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def division(a,b):
    return a/b
def multiplication(a,b):
    return a*b
def main():
    num1, num2 = 0, 0
    take = True
    while take:
        try:
            num1=int(input("enter the first number"))
            num2=int(input("enter the second number"))
            take = False
        except ValueError:
            print("invalid value. try again")
    op=input("enter which operate to be used(+,-,*,/):")

    if op=='+':
        add=addition(num1,num2)
        print(add)
    elif op=='-':
        difference=subtraction(num1,num2)
        print(difference)
    elif op=='*':
        prod = multiplication(num1,num2)
        print(prod)
    elif op=='/':
        quotient=division(num1, num2)  
        print(quotient) 
    else:
        print("invalid operation")

main()
'''

