#args and kargs
'''
def my_fn(*args):
    print(*args)
    print(f"my first argument:{args[0]}")
    print(f"my first argument:{args[1]}")
    print(f"my first argument:{args[4]}")

my_fn(12,34,67,"hello","dhiraj")
'''

'''
def add_num(*args):
    sum=0
    for i in args:
        sum =sum+i
    print(sum)
add_num()
add_num(34,34)
add_num(34,34,56,67)
add_num(34,56,78,98,99,23,12,34)
add_num('')
'''

#kwargs
'''
def my_fn(**kwargs):
    for key ,value in kwargs.items():
     print(f"{key}:{value}")

my_fn(name="dhiraj",standard="12",address="brt")
'''
'''
def my_fn(*args,**kwargs):
    print(args)
    print(kwargs)

my_fn("dhiraj sah",city="biratnagar",state="koshi")
'''
'''

def my_fn(*args,**kwargs):
    for i in args:
        print(i)
    print()
    for key, value in kwargs.items():
        print(f"{key}:{value}")

my_fn("dhiraj sah",city="biratnagar",state="koshi")
'''
