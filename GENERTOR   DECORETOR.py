# Iterator in python is an object that is used to iterate over iterable objects like lists, tuples, dicts, and sets.
# The iterator object is initialized using the iter() method. It uses the next() method for iteration.

#__iter(iterable)__ method that is called for the initialization of an iterator. This returns an iterator object

#next ( __next__ in Python 3) The next method returns the next value for the iterable.

#iter -> iter is an object  will take one arguemnt that is iterabale object

# x=list(range(1,5)) #[1-4]
# y=iter(x)
# print(y.__next__())
# print(y.__next__())
# print(y.__next__())

# iterable_value = 'Python'
# # for i in iterable_value:
# #     print(i,end=' ')
#
# iterable_obj = iter(iterable_value)
# for i in iterable_value:
#     print(iterable_obj.__next__())
# #
# x=[10,20,30,40,50]
# y=iter(x)
# print(y.__next__()) #1
# print(y.__next__()) #2
# print(y.__next__())
# print(y.__next__())
# print(y.__next__())
#
# for i in range(len(x)): #[0,4]
#     print(y.__next__())

# for idx,ele in enumerate(x):
#     print("index :",idx,"ele :",ele)

# for idx in range(len(x)):
#     print("index :",idx,"ele :",x[idx])



# genertors :
#
# Generator is a function which is responsible to generate a sequence of values.
# We can write generator functions just like ordinary functions, but it uses yield keyword to
# return values
# a fun which contains yeild keyword is called  generator
#genertor by default having iterator and __next__()

# def fun():
#     return "Fun"
#
# x=fun()
# print(x)

def mygen():
    yield 'A'
    yield 'B'
    yield 'C'
    yield 'D'
    yield "F"
    yield 'G'
    yield 'H'

g=mygen()  #iter(['A','B','C'.....'H'])
#
# for i in g:
#     print(i,end=' ')

# for i in g:
#     print(i, end=' ')
#     if i=='D':
#         break
#
# print(g.__next__())   # A
# print(g.__next__())   # B
# print(g.__next__())   # C
# #
# for i in g:
#     print("loop 2")   # loop 2    'D'    loop 2 f
#     print(i)

#
# print(g.__next__())
# print(next(g))
# print(next(g))
# print(next(g))
# #
# def countdown(num):
#     print("Start Countdown")
#     while(num>0):
#         yield num        # 5 4 3 2 1
#         num=num-1
# values=countdown(5)
# for x in values:
#     print(x,end=' ')

# def countdown(num):
#     numlist=[]
#     print("Start Countdown")
#     while(num>0):
#         #yield num        # 5 4 3 2 1
#         numlist.append(num)
#         num=num-1
#     return numlist
# values=countdown(5)
# for x in values:
#     print(x)


# decorators:
# decorator is a function which can take a function as argument and extend its functionality
# and returns modified function with extended functionality.
# without touching existing functionality adding new feature to the fun is called decortor
#
# def python():
#     print("PYTHON IS GOOD")
#     def java():
#         print("JAVA is good")
#     return  java()
#
# python()




# def java():
#     print("JAVA is good")
#     def python():
#         print("python")
#     return python()
# java()

# def python():
#     print("python")
#     def java():
#         print("java")
#     return java()
# python()


def python(fun):
    print("python")
    def java():
        print("java")
        return fun()      # ravi
    return java()

# @python  #python(ravi)
# def ravi():
#     print("ravi is good lan")

#python(ravi)



def python(fun):    #  fun arg is a function   fun is C()
    print("Python is good ")
    def java():
        print("JAVA")
        fun()            # C()
#     return java()
# @python       #-> python(C)
# def C():
#     print("C is good lanuage")

# Call_fun=python(C)
# Call_fun()

# def python(fun):    # fun is C()
#     print("Python is good ")
#     fun()
#     def java():
#         print("JAVA")
#         fun()
#     return java()
# def C():
#     print("C is good lanuage")
# python(C)


# def python(fun):    # fun is C(name)
#     print("Python is good ")
#     def java(name):
#         print("JAVA",name)
#         fun(name)    # atlast it is calling
#     return java
# @python   # -> python(C(name))
# def C(name):
#     print(name," is good lanuage")
# C("RUBY")

#function alising   -> giving alious name to the existing fun is caled function alising
# def python():
#     print("Python is good")
# naga=python
# #naga()
# rama=naga
# rama()
# naga()
# python()


# input :1234 -> ['O','T','T','F','F','S','S','E','N','Z']
#output :OTTF
#1000  -> OZZZ
#4322 ->FTTT

#x=['O','T','T','F','F','S','S','E','N','Z']

#picling and unpilcling
# pickling -> the process of writing object data to the file is called pickling
#pickle.dump(obj,f)  will take two args (object,file)
# we have to open file in write binary mode (wb)

#unpickling : the process of extracting object data from file is called unpickling
#pickle.load(f) only one atrgunent that is file pointer
#we have to open file in read binary mode (rb)



import pickle
class A:
    def __init__(self,name,rno):
        self.name=name
        self.rno=rno
    def disply(self):
        print("name :",self.name)
        print("rno :",self.rno)
#
# with open("Student.txt",'wb') as f:
#     obj=A("NAGA",10)
#     pickle.dump(obj,f)
#     obj = A("RAMA", 20)
#     pickle.dump(obj, f)

with open("Student.txt",'rb') as f:
    ob=pickle.load(f)
    ob.disply()
    ob = pickle.load(f)
    ob.di
