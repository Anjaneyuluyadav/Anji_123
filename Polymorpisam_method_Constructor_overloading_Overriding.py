# an Entity which represents in multipe forms is called polymorohism
# Eg1: Yourself is best example of polymorphism.In front of Your parents You will have one type of
# behaviour and with friends another type of behaviour.Same person but different behaviours at
# different places,which is nothing but polymorphism.
# Eg2: + operator acts as concatenation and arithmetic addition     # +
# print(1+2)       #3
# print('A'+'B')    #AB
# print(1*2)      #2
#print("A"*2)
# Eg3: * operator acts as multiplication and repetition operator
# Eg4: The Same method with different implementations in Parent class and child
# classes.(overriding)
# Related to polymorphism the following 4 topics are important

# +  ->   addtion
#
# a=1
# b=20
# print(a+b)
#
# a="python"
# b="JAVA"
# print(a+b)
# a=2
# b=20
# print(a*b)
#
# a="python"
# print(a*2)


# . Duck Typing Philosophy of Python
# 2. Overloading
#  1. Operator Overloading
#  2. Method Overloading
#  3. Constructor Overloading
# 3. Overriding
#  1. Method overriding
#  2. constructor overriding
#Duck Typing Philosophy of Python
# Fun name is same but actions are different
# The problem in this approach is if obj does not contain talk() method then we will get
# AttributeError
# defferent clss having same method with different functionality is called duck type polimorphisam
class Duck:
    def talk(self):
        print("Duck clss")
        print('Quack.. Quack..')

class Dog:
    def python(self):
        print("DOg clss")
        print('Bow Bow..')

class Cat:
    def talk(self):
        print("Cat class")
        print('Moew Moew ..')

class Goat:
    def talk(self):
        print("Goat class")
        print('Myaah Myaah ..')


# x=[Duck(),Dog(),Cat(),Goat()]
# for i in x:
#     i.talk()


# obj=Dog()
# obj.talk()
# obj=Duck()
# obj.talk()
# obj=Cat()
# obj.talk()
# obj=Goat()
# obj.talk()
# l=[Dog(),Duck(),Cat(),Goat()]
# for obj in l:
#     obj.talk()

# def f1(obj):
#     obj.talk()
#
# # # we can able to create object for all the clases at a time by passing cllass names into the list
# l=[Dog(),Duck(),Cat(),Goat()]   # 0->Dog Duck ->1 cat->2  Goat -3
# for obj in l:
#     f1(obj)
#we can solve this problem by using hasattr() function

# has attr useful to to check the method is exits or not in perticuler class

# how to check
# by pssing object and method name to hasattr(objnme,methodnme)

# hasatter method will take two arguments one is object and method name
#hasatter useful for to check the perticuler method is exits or not in class

# class Duck:
#     def talk(self):
#         print('Quack.. Quack..')
# class Human:
#     def talk(self):
#         print('Hello Hi...')
# class Dog:
#     def bark(self):
#         print('Bow Bow..')
#
# def f1(obj):
#     if hasattr(obj,'talk'):
#         obj.talk()
#     elif hasattr(obj,'bark'):
#          obj.bark()
#
# x=[Duck(),Human(),Dog()]
# for obj in x:
#     f1(obj)
# d=Duck()
# f1(d)
# h=Human()
# f1(h)
# d=Dog()
# f1(d)

class A:
    def python(self):
        print("Calling python")
    def java(self):
        print("Calling java")
obj=A()

# if hasattr(obj,'python') and hasattr(obj,'java'):
#     obj.python()
#     obj.java()
# elif(hasattr(obj,'NAGA')):
#     obj.NAGA()



# There are 3 types of overloading
# 1. Operator Overloading
# 2. Method Overloading
# 3. Constructor Overloading


# ope overloding

# We can use the same operator for multiple purposes, which is nothing but operator overloading.
# Python supports operator overloading.
# Eg1: + operator can be used for Arithmetic addition and String concatenation
#  print(10+20)#30
#  print('durga'+'soft')#durgasoft
# Eg2: * operator can be used for multiplication and string repetition purposes.
#  print(10*20)#200
#  print('durga'*3)#durgadurgadurga


# '+' ope loading

class Book:
    def __init__(self,pages):
        self.pages=pages
# b1=Book(100)
# b2=Book(200)
# print(b1+b2)
#
# For every operator Magic Methods are available. To overload any operator we have to override
# that Method in our class.
# Internally + operator is implemented by using __add__() method.This method is called magic
# method for + operator. We have to override this method in our class.

# a=10
# b=30
#
# print(a.__add__(b)) # +
# print(a.__mul__(b)) #*
# print(a.__sub__(b)) #-
# print(a.__ge__(b))  # a>=b     pow->**
# print(a.__pow__(b))

#
class Book:
    def __init__(self,pages):
        self.pages=pages         # 10 ,3
        print(self.pages)
    def __add__(self,other):       # magic method
        print(self.pages)
        print(other.pages)
        return self.pages+other.pages      # b1.__add__(b2)
    def __mul__(self, other):                # b1.__mul__(b2)
        return self.pages * other.pages
    def __sub__(self, other):
        return self.pages-other.pages

# b1=Book(10)       #pages=100
# b2=Book(5)       # pages=20
# print('The Total Number of Pages:',b1+b2)  #15
# print('The Total Number of Pages:',b1*b2)   #50
# print('The Total Number of Pages:',b1-b2)   #5


class A:
    def __init__(self,x):
        print("CLSS A CONST")
        self.x=x
    def __add__(self, other):
        return self.x+other.x
    def __mul__(self, other):
        return self.x*other.x

# obj=A(100)
# obj1=A(200)
# print("Add",obj+obj1)
# print("mul",obj*obj1)


# methood over loading

#Method Overloading:

# method name is same atleast one argument should be different is called method overloading
# If  methods having same name but different type of arguments then those methods are said to
# be overloaded methods.
# Eg: m1(int a)
#  m1(double d)
# But in Python Method overloading is not possible.
# If we are trying to declare multiple methods with same name and different number of arguments
# then Python will always consider only last method.
# Demo Program:
# class Test:
#
#     def m1(self):
#         print('no-arg method')
#     def m1(self,a):       #m1(self,a=None)
#         print('one-arg method')
#     def m1(self,a,b):     #m1(self,a=None,b=None)
#         print('two-arg method')
# t=Test()
#t.m1(10)
#t.m1(10)
#t.m1(10,20)

#Most of the times, if method with variable number of arguments required then we can handle
#with default arguments or variable len args

class Test:
    def sum(self,a=None,b=None,c=None):
        print(a,b,c)
        if a!=None and b!= None and c!= None:
            print('The Sum of 3 Numbers:',a+b+c)
        elif a!=None and b!= None:
            print('The Sum of 2 Numbers:',a+b)
        elif a!=None:
            print("A",a)
        else:
             print('Please provide 2 or 3 arguments')
#t=Test()
#t.sum(10,20)
#t.sum(10,20,30)
#t.sum(10)
# t.sum()

# # t.m1()
# t.m1(10)
#t.m1(10,20)

# class Test:
#     def sum(self,*a):     # it  will return tuple
#         total=0
#         for x in a:
#             total=total+x
#         print('The Sum:',total)
# t=Test()
# t.sum(10,20)
# t.sum(10,20,30)
# t.sum(10)
# t.sum()

#  Constructor Overloading:
# Constructor overloading is not possible in Python.
# If we define multiple constructors then the last constructor will be considered.
class Test:
    def __init__(self):
        print('No-Arg Constructor')
    def __init__(self,a):
        print('One-Arg constructor')
    def __init__(self,a,b):
        print('Two-Arg constructor')
#t1=Test(10,20)

#t1=Test(10)
#t1=Test(10,20)

#constructor with Default Arguments:
class T:
    def __init__(self,a=None,b=None,c=None,d=None):
        print('Constructor with 0|1|2|3|4 number of arguments')
# t1=T()
# t2=T(10)
# t3=T(10,20)
# t4=T(10,20,30)
# t5=T(10,20,30,40)

#Constructor with Variable Number of Arguments:
class T1:
    def __init__(self,*a):
        print('Constructor with variable number of arguments')
        print(a) #() ,(10,)(10,20),(10,20,30)
#
# t1=T1()
# t2=T1(10)
# t3=T1(10,20)
# t4=T1(10,20,30)
# t5=T1(10,20,30,40,50,60)

# Method overriding:
# What ever members available in the parent class are bydefault available to the child class through
# inheritance. If the child class not satisfied with parent class implementation then child class is
# allowed to redefine that method in the child class based on its requirement. This concept is called
# overriding.
# Overriding concept applicable for both methods and constructors.

# the method which is present in parent and derived class with name and sae args then  parent class  method is overridden by derived(child)
# class method

class P:
    def property(self):
        print('GOLD')
    def marry(self):
        print('SAI PALLAVI')
class C(P):
    def marry(self):      # Super().marry()
        print('ANUPAMA')
        #super().marry()
# c=C()
# c.property()
# c.marry()
# From Overriding method of child class,we can call parent class method also by using super()
# method.

class P:
    def property(self):
        print('GOLD')
    def marry(self):
        print('SAI PALLAVI')
class C(P):
    def marry(self):      # Super().marry()
        print('ANUPAMA')
        super().marry()
# c=C()
# c.property()
# c.marry()


#constructor overriding

class P:
    def __init__(self):
        print('Parent Constructor')
class C(P):
    def __init__(self):
        print('Child Constructor')
        super().__init__()       #calling parent class constr
c=C()



