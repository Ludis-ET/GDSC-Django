def greet(name):
    return f"hey {name}"

def add_nums(a,b):
    return a+b

def args(*args):
    return args

def average(*args):
    sum = 0
    counter = 0
    for a in args:
        sum += a
        counter += 1
    return sum/counter


add = lambda a,b:a+b
square = lambda a:a**2
even = lambda a: True if a%2 == 0 else False 


def filter_list(l,con):
    return [i for i in l if con(i)]


def map_list(l):
    return [i*2 for i in l]

lis = [1,2,3,4,5,6,7,8]


# print(filter_list(lis,lambda x:x%2==0))
# print(map_list(lis))


try:
    a = int(input("1st num: "))
    b = int(input("2st num: "))

    print(a+b)
except:
    if type(a) is not int or type(b) is not int:
        print("must be integer")


try:
    a = int(input("1st num: "))
    b = int(input("2st num: "))

    print(a/b)
except:
    if b == 0:
        print("can't divide with 0")