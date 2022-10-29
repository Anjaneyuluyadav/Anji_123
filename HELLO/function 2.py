# there r two types of variabes in python
# local,global
import functools

#global var : the varibales which r declared outside of the fun is called is called global var
# the var can b accesed all the functions in the file/ module

a=100 # global
def python():
    print("hello")
    print(a)
python()

def java():
    print(a)
java()

# local var :the varibales which r declared inside side of the fun is called is called local var
# the scope of the var is within the function only


# def python():
#     a=100
#     print(a)
# python()
# #
# def java():
#     b=200
#     print(b)
# java()


# gobal keyword :  to declare global var inside the fuction

# a=100 # global
# def python():
#     global a
#     a=a+10
#     print(a)  # 110
# python()
# def java():
#     global  a
#     a=a+30
#     print(a) # 140
# java()
#
# def hello():
#     a=10
#     print(a)
# hello()

# if local and global variable have same name how to access global var inside the fun
# a=1000 # global
# def hello():
#     a=10
#     print(a)
#     print("global val is :",globals()['a'])
# hello()

# recursive fun : the fun call it self is called recursive fun
# count=1
# def python():
#     global count
#     if count!=11:
#         print(count,"HELlo")
#     else:
#         return
#     count=count+1
#     return python()
# python()
# factorial of given num using recursive:

# def fact(n):
#     if n==0:
#         result =1
#     else:
#         result=n*fact(n-1)  # 4 *fact(3)
#                             # 4*3*fact(2)
#                             # 4*3*2*fact(1)
#                             # 4*3*2*1 =24
#
#     return result
# print("fact of num :",fact(2))

# for i in range(1,6):
#     print("fact of num :",fact(i))

# lamba :we can lamda fun as anonymous fun , there is name for this fun
# the main purpose of lamba fun is just for instant use
#syntax : var=lambda args:Expression


# def square(n):
#     return n*n
# print("val",square(3))

# even=lambda n: 0 if n%2==0 else 1
# for i in range(1,5):
#     out = even(i)
#     if out == 0:
#         print(i,"even")
#     else:
#         print(i,"Odd")

# def big(a,b):
#     if(a>b):
#         print(a,"is big")
#     else:
#         print(b,"is big")
# big(10,20)

# out=lambda a,b: a if a>b else b
# print("big num of ",out(20,30))

x=list(range(1,11))
out=list(map(lambda i: i*10,x))

print(out)

x=list(range(1,6))
out=functools.reduce(lambda a,b: a+b,x)
print(out)