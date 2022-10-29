# function : function is a group of statements in a single unit
# the main advantage of fun is code reusability
# two types of funtions
# fun starts with def keyword in python

# built in fun -> len(),max(),id(),type(),input(),print(),sorted(),input(),id() # predefined fun
#user defined -> the functions which are developed by programmer

# fun calling will be after the fun defention
# we can pass n no of args in fun
# syntx : # def fun_name(args): # args r optional  (need to use depend on req)
# any user define fun starts with keyword called def
# def python():
    #st1
    #st2
    #st3

# fun declaration , fun defenation ,fun calling  -> C ,C++,JAVA

# def python():
#     print("Python is good")
#     print("JAVA is good")
# python()

# calling fun and fun defenation contains same syntax

# fun calling should b after the fun defention

# def java():
#     print("JAVA is good")
#     print("JAVA is good")
#     print("JAVA is good")
#
# java()

# def python():
#     print("Hi")
#     print("Helo")
#     print("python")
# python()

# without args without return val
# without args with return val
# with args with return val
# with args without return val


# without args without return val
#
# def java():
#     print("java is good")
#     print("Hello java")
#     print("Hello C")
# java()

#without args with return val

def add():
    a=10
    b=200
    return a+b
# c=add()
# print(c)
#print("Result :",add())

# calling fun and fun def should be like same

#with args with return values
def mul(a,b): # a,b are called  formal args
    return a*b
# c=mul(10,20)
# print(c)
#print("Result :",mul(10,20)) # 10,20 actul args

# with args without return values

def sub(a,b): # a,b r fomal args
    print(a-b)  #10
#sub(20,10)   # actual args


# def python(): # fun defenation
#     print("Python is good lan")
#     print("Python is good lan")
#     print("Python is good lan")
#     print("Python is good lan")
# python()   # fun calling

# if u r returing some val from fun then we must store that result in another varibale

# without args without return val
# def data():
#     print("Java is ok")
#     print("python is ok")
# data()

#without args with return val
# def data():
#     print("Java is ok")
#     #return "PYTHON IS GOOD"
# #a=data() # if u r returing someval means we hav to call like this
# print(data())

# with args with return val
#formal args : the args which we r declare inside the fun defention is called formal args
#actual args : the args which we r passing from the calling function is called actual args

# def data(a,b):     # here a,b r formal
#     print(a)
#     print(b)
#     return a+b
# c=data(10,20) # if u r returing someval means we hav to call like this # here (10,20) r actual args
# print(c)

# # with args without return val
# def sravani(a,b):
#     print(a)
#     print(b)
#     print(a+b)
# sravani(10,20)

# return multible vaues from fun

def add(a,b):  # formal arg
    a=a+10   #30
    b=b+10   #40
    c=600
    d=1000
    return a+b,c+d
#a,b,c,d
# python,java=add(20,30)  # actual args
# print("i val",python)
# print("j val",java)
#print("x val",x)
#print("y val",y)

#positional args

# def add(a,b,c):  # formal  (a,b)  (20,30)  a=20,b=30 c=100
#     print("a val", a)
#     print("b val", b)
#     print('C val',c)
# add(20,30,200)    #actual args

#keyword args

def add(a,b,c,d):  # formal
    a = a + 10  # 110
    b = b + 10  #
    # print("a val", a)
    # print("b val", b)
    # print("c val", c)
    # print("d val", d)
    return a,b,c,d


#add(10,20,30,40)
#a,b,c,d
# x,y,z,i=add(a=100,d=1000,c=20,b=500)  # actual args
# print(x)
# print(y)
# print(z)
# print(i)

#default args

# deafult args always right side of the fun declartion
# if we pass the val for defut args it will take ,if we dont pass the default val wil be printed
#
# def add(a,b,c=None,d=None):  # here a,b r positional  and c is default
#     print("a val", a+30)
#     print("b val", b+40)
#     print('c val',c)
#     print('d val :',d)
# add(10,20,500)
# add(a=20,b='java')

#list unpacking : assinging each and every element from the list and stroting into the variables
# the len of the list is equals to num of variables
# x=[1,2,3,100]
# a,b,c,d=x
# print(a)
# print(b)
# print(c)
# print(d)

#list packing
# a,b,c=10,20,30
# y=[]
# y.append(a)
# y.append(b)
# y.append(c)
# print(y)

#List packing
# def mul(a,b,c):
#     x=[]
#     x.append(a)
#     x.append(b)
#     x.append(c)
#     return x  #[1,2,3]
#
# out=mul(2,3,4)
# print(out)

# list unpcking using functions
# def unpack(x):
#     print(x) #[1,2,3]
#     a,b,c=x
#     return a,b,c
#
# y=[1,2,3]
# i,j,k=unpack(y)
# print(i,j,k)

# List packing
# def mul(a,b,c):
#     return a,b,c

# a,b,c=[2,3,4]
# print(a,b,c)

# # varible len args

# def mul(*a):   # it will return tuple
#     x=list(a)
#     x=[pow(i,3) for i in x]  #list comphrensiion [1,8,27]
#     return x
# y=mul(1,2,3)
# print(y)

# varlen arg

# syntax :def fun(*formal arg)
# variable len arg bydefault it will return tuple ,and it will accept n nu of args from fun callinf

# def java(*a):
#     print(a)
# java(1,2,3,4,5,6,7)
#
# def python(*c):
#     return c
# out=python(1,2)
# print(out)

# def java(a,b,*c): # positionl + variable len
#     print('c val is ',c)
#     print('b val is ',b)
#     print('a val is',a)
# java(1,2,3,4,5,6,7)

#Varibale len args :  some times n num of ars to our fun such type of args called varible len args

#synatx : def fun(*a)
# internaly these values represnted in the form of tuple

# def add(): # no return but returing some val
#     return 10+30
#
# x=add()
# print(x)

# def add(*a):
#     return a,sum(a),a[0]
# x,y,z=add(1,2,3,4,5,6)
# print(x)
# print(y)
# print(z)


# def mul(*a):
#     return a[0],a[1]*10,max(a)
# x,y,z=mul(10,20,5,2,1000)
# print(x)
# print(y)
# print(z)
#keyword vribale len
# we can declare keyword variabe len args
# syntax : def funname(**varibe_name)
# keyword args r stored in the form of dict

# def java(**x):
#     # print(type(x))  #
#     # print(list(x.keys())) #[]
#     # print(list(x.values()))
#     return x
#
# out=java(a=10,b=20,c=30)
# print(out) #{a:10}

# def java(**x):
#     return list(x.keys()),list(x.values()),200,400
#
# key,val,x,y=java(a=10,b=20,c=30) #[a,b,c],[10,20,30]
# print(key,val,x,y)

# def python(**a): # formal args
#     print(a.keys())
#     print(a.items())
#     return a
#
# x=python(a=10,b=30,c=40,d=20)     # keyword args
# print(x)

# def add(b,c,a="H"):
#     print(a)
#     print(b)
#     print(c)
# add(b=10,c='python')

# def python(*x,**y):  # variable len + keyword var len
#     return x,y
#
# a,b=python(1,2,3,4,5,a=10,b=20,c=30)
# #
# print(a)
# print(b)

# factorail given num using function

# x=input("Enter x val :")
# print(type(x))
# x=int(input("Enter x val :"))
# print(type(x))

# x=float(input("Enter x val :"))
# print(type(x))
# print(x)

# eval : it will work like it will convert the type based on the input user provided
# x=eval(input("Enter x val :"))
# print(type(x))

# f     i   f=f*i
#  1     1   f=1
#  1     2   f=2
#  2     3   f=6
#  6     4   f=24
#  24    5   f=120
#
# def fact(x):
#     f=1
#     for i in range(1,x+1):
#         f=f*i
#     return f
# x=eval(input("Enter x val :"))
# val=fact(x)
# print('factorai of {} is : {}'.format(x,val))

# def fact(x):
#     f=1
#     for i in range(1,x+1):
#         f=f*i
#     return f
# x=[2,3,5,6,7,8]
# for i in range(len(x)):
#     val = fact(x[i])
#     print('factorai of {} is : {}'.format(x[i], val))

# x="Naga" # "naga"
# def low(a):
#     return a.lower(),a.upper(),a.swapcase()
# out,b,y=low(x)
# print(out,b,y)

# x='HELLO' #hello ,olleh
# def low(b):
#     b=b.lower()
#     return b,b[::-1]
# i,j=low(x)
# print(i,j)


x=[1,2,3]  #{A:1,B:2,C:3}

# def key(**a):
#     return a
# y=key(A=1,B=2,C=3)
# print(y)

# def key(b):
#     out={}
#     keyval=['A','B','C']
#     out=dict(zip(keyval,b))
#     return out
# y=key(x)
# print(y)



# local varible
# the variable which we r defind inside the fun is called local
# def f3():
#     print("Caling f3")
#     java()
#
# def java():
#     a=100  # local var
#     print(a)
#
# def f2():
#    print("calling f2")
#    f3()
# f2()


# return statement:
# value return
# control return

# def f3():
#     print("Caling f3")
#     java()
#
# def java():
#     a=100  # local var
#     print(a)
#     return 100
#
# def f2():
#    print("calling f2")
#    f3()
#
# val=f2()
# print('val is ',val)
# val=java()
# print('val is ',val)


# control return

# def f1():
#     print('hello')
#     print('hi')
#     return
#     print('java')
#     print('python')
# x=f1()
# print(x)



# def f3():
#     print("Caling f3")
#     return java()
#
# def java():
#     a=100  # local var
#     print(a)
#     return 100
#
# def f2():
#    print("calling f2")
#    return f3()    #java() -> 100
#
# val=f2()
# print('val is ',val)


# we can redefine the global variable globally
# a=100   # outside of fun
# def java():
#     print(a)
# java()
# a=200 # outside of fun
# def python():
#     print(a)
# python()
# a=300 # outside of fun
# def C():
#     print(a)
# C()

#global
# global is keyword used for to declare the global variable inside the fun  so that we can redefine the global var inside the fun

a=200
# def python():
#     global a
#     x=100     # local
#     #print(x)
#     a=a+20
#     #print(a)
# #python()
#
#
# def java():
#     print(a)
# java()
#
# a=100
# def java():
#     global a
#     x=200
#     a=500
#     print(a)
#     print(x)
# java()
#
# def python():
#     print(a)
# python()

# if local and gobal variable have same name or do nt have same name  then we can print global variable using globals() fun

# a=500
# def java():
#     a=100
#     print(a)
#     print(globals()['a'])
# java()

# a=100
# def python():
#     global a
#     a=200
#     a=500
#     print(a)
#     a=a+10000
#     print(globals()['a'])
# python()
#
# def python():
#     global a
#     a=a+100
#     print(a)
# python()

#gobal -> the varible which we r defined outside of the fun is called global
# this varible is aplicable for all the functions
# x=10     # gobal
# def java():
#     print(x)
# java()
#
# def python():
#     print(x)
# python()
# if we want to change the global varible val inside the fun then we hve use keyword called global
#
# x=10     # gobal
# def java():
#     global x
#     x=123
#     print(x)
# java()
#
# def python():
#     print(x)      # 123
# python()
# # we can chnge the global var value in inside the fun and outside the fun also -> its applicable for all the functions
# x=10
# tmp=x
# def java():   # int a;
#     print(x)
# java()
#
# def python():
#     global x
#     x=123
#     print(x)      # 123
# python()
#
# def a():
#     print(tmp)
#     print(x)
# def b():
#     print(tmp)
#     print(x)
# a()
# b()
# x=100
# # if global and local var having same name then priority is local
# def a():
#     x=10
#     print("inside fun ",x)
#     print("global var x",globals()['x'])
# a()
# print(x)

#recursive fun
# the fun call itself is called recursive fun

# def fact(n):
#     if n==0:
#         result=1
#     else:
#         result=n*fact(n-1)    # 3*(2)
#                               # 2*(1)
#                               # 1*(0)
#                             # 1     #3*2*1*1 =6
#     return result
# x=fact(3)
# print("factorial is :" ,x)



# anonymous fun: a fun which is defined without a name is clled anonymous fun or lamba fun
# the main purpose of fun is instant use
# it is not suitable to write n num of lines inside the fun
# syntx : var_nme=lambda var1,var2..... : business logic
# def python(a):
#     return a*2
# val=python(4)
# print('val is :',val)
#
# b=lambda a:a*2
#
# print('val is :', b(5))

  # a,b  a+b
#
# def java(a,b):
#     return a+b
# z=java(10,20)
# print(z)
#
# naga=lambda a,b:a+b
# print(naga(10,20))

# a,b
#
# big=lambda a,b :a if(a>b) else b
#
# print("big is :",big(1000,500))


# def square(x):
#     return x*x
# y=square(2)
# print(y)

# x=lambda a:a*a
# print(x(2))
# #
# def add(x,y):
#     return x+y

# z=add(10,20)
# print(z)

#syntx : var_nme=lambda var..... : business logic
# z=lambda x,y:x+y
# x=z(30,50)
# print(x)
#
# c=lambda x,y:x if(x>y) else y
# print(c(110,2000))

# y=lambda x,y:x-y
# z=y(3,2)
# print(z)
# a=10
# b=20
# x= a if a>b else b
# print(x)

# a=lambda c,d :c if c>d else d
# print(a(100,3330))

#x=list(range(1,11))
# def even(i):
#         if i%2==0:
#             return i
# for i in x:
#      x=even(i)
#      if x!=None:
#          print(x,end=' ')

# filter -> it wil take 2 args one is fun nnd list  it wil fiter the perticuler elements

#synatx : var_name=list(filter(fun,iterable_obj))
#x=list(range(1,11))  #[1,10]

# x=[i for i in x if i%2==0]
# print(x)
# x=[1,2,3,4,5,6]
# a=list(filter(lambda i:i%2==0,x))   #   for i in x:
#                                            #if i%2==0                                             #return i
# print(a)

# z=lambda a: a if a%2==0 else 0
#
# print(z(10))
#
#print(y)

# filter
# syntax :filter(fun,iterableobj)

# def even(n):
#     if n%2==0:
#         return n
#
# x=list(range(1,7)) #[1,2,3,4,5,6]  # filtering only even
# out=[]
# for i in x:
#     val=even(i)
#     if val!=None:
#         out.append(val)
# print(out)


#filter() : fuseful for to filter the elements from iterble object bsed
# filter will tke two args (function , iterable obj)



# def even(i):
#     if i%2==0:
#         return i
#x=list(range(1,11))  # [1-10]

# y=list(filter(even,x))
# print(y)

# y=list(filter(lambda a:a%2==0,range(1,11)))
# print(y)

# x=list(range(1,11))
# print(x)

# z=y=list(filter(lambda i:i%2==0,x))
# print(z)

# x=list(range(1,11))
# print(x)
# y=[i for i in x if i%2==0]
# print(y)

#map() -> map will pply on each nd every on the iterable obj nad it will modify all the ele and generates the iterable obj


# syntax
# variable=map(fun,iterableobj)

# x=list(range(1,4)) #[1,2,3]
# def square(x):
#     return x*10

# z=list(map(square,x))
# print(z)

# z=list(map(lambda a:a**2,[5,2,4]))
# print(z)


# x=[1,2,3,4,5,6]
# # z=list(map(lambda i:i*10,x))
# # print(z)
# z=list(filter(lambda i:i%2==0,x))
# print(z)

# reduce -> reduce fun reduce the sequnce of ele into a single ele by applying specified fun
# syntax : reduce(fun ,sequnce)
# if we want to use reduce we have to import the module clled functools

# from functools import reduce
# # x=list(range(1,11)) #(1,10)
# # print(x)
# x=[10,20,30,40] #{10,20,}
# z=reduce(lambda a,b:a-b,x)
# print("sum",z)


# function alising : giving alious name to the existing fun is called fun alising
# def python():
#     print("Python is good")
#
# py=python
# py()
# python()
# print(id(py))
# print(id(python))


#nested fun : function inside the function is called nested function

# def python():
#     print("python is good")
#     def java():
#         print("Java is good")
#     java()
#
# python()


# nested functions : function inside the fun i called nested functions
# def python():
#     print("Python is good")
#     def java():
#         print("JAVA IS OK")
#         def C():
#             print("C is good")
#         C()
#     java()
# python()
#
# def add(a,b,c,d):
#     print("add",a+b+c+d)
#     def mul():
#         print(c*d)
#         def sub():
#             print(d-c)
#         sub()
#     mul()
# add(1,2,4,3)

# recursive fun :  fun call itsellf is called recursive fun
# fact
# def python():
#     print("Java")
#     x=int(input("Enter x val :"))
#     if x==1:
#         python()
#     else:
#         return
# python()


# import math
# print(math.factorial(4))
# def fact(n):
#     if n==0:
#         result= 1
#     else:
#         result=n*fact(n-1)          #  3 *2     #    2 *(1)    #  1 *(1)
#     return result
# print(fact(5))          #6


# return :

# return is a keyword used for return the values from fun

# value return and contorl return
# value return
# def add(a,b):
#     print("HELO javb")
#     print("HI")
#     a=a+10
#     b=b+20
#     return a,b
#     #return a, b
#
# x,y=add(20,30)
# print(x)
# print(y)


# control return -> we can come out from the function using return

#
# def python(a):
#     print("HELLO PYTHON")
#     print("helo jva")
#     a=a*10
#     return
#     print("HELLO JAAVA")
# python(10)
# c=0
# for i in range(1,11):
#     if i==5:
#         break
#     else:
#       print(i,end=" ")


# ass1 : Write a fun sum of given numbers pass 1,2,3 n return result is 6

# ass2 : write a fun to print even and odd num in list -> pass list to fun x=list(range(1,11))(1,10)

# ass3 write a program for default args and return result

# wa fun to print multiplication table in fun

# pass n of args and return list using varible len args

# pass keyword args nd return dict (a=10,b,20,c=30)  -> {a:100,b:400,c:900}

# write a fun to return only the first word from the list

x=["PYTHION IS GOOd","JAVA IS GOOD"]  # ["PYTHON","JAVA"]

# write a fun to chnage string lower to uppeer and upper to lower  and return the string

# wa fun to get only vowels from the list
# x=["PYTHION IS GOOd","JAVA IS GOOD"]   ->[I,O,I,O,O,A,A,I,O O]  -> remove the duplicates

# get the max num from list without using predefined fun

# sort the list without using sort fun

# x=[1,2,3,4,5]
#
# for i in range(len(x)):
#     x[i]=x[i]+10

