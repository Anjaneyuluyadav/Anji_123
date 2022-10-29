one class data accessing in another class using HAS-A RELATION
#creating one class object inside the another class init method is called HAS-A relation
# class A:
#     def __init__(self):
#         print("CLLING CLASS A INIT METHOD ")
#   #   def python(self):
#         print("CALLING CLASS A PYTHON METHOD")
# class B:
#     def __init__(self):
#         print("CALLING CLASS B INIT METHOD")
#         self.obj=A()
#         print("CLLING CLASS B ")
#     def JAVA(self):
#         print("CALLING CLASS B JAVA METHOD")
#         self.obj.python()
# out=B()
# out.JAVA()
# iS -A RelationSHIP
# accessing parent class class data inside the child class by inheriting parent class to child class
# class A:
#     def __init__(self):
#         print("CLLING CLASS A INIT METHOD ")
#     def python(self):
#         print("CALLING CLASS A PYTHON METHOD")
# class B(A):
#     pass
# obj=B()
# obj.python()
# inheritnce : getting properties from super(parent) class to child class is called inheritance
# single inheritance : the concept of inheriting properties from one class to another class
# class A:
#     def __init__(self):
#         print("CLLING PARENT CLASS A INIT METHOD ")
#     def python(self):
#         print("CALLING PARENT CLASS A PYTHON METHOD")
# class B(A):
#     def __init__(self):
#         print("CHILD CLASS B INIT method")
#     def java(self):
#         print("CHILD calling B Class JAVA")
# out=B()
# out.python()
# out.java()

#multilevel : the concept of getting peroperties from mutiple classes to single class with the concept of one after another is caledd
#mutilevel
# class A:
#     def __init__(self):
#         print("CLLING PARENT CLASS A INIT METHOD ")
#     def python(self):
#         print("CALLING PARENT CLASS A PYTHON METHOD")
# class B(A):
#     def __init__(self):
#         print("CHILD CLASS B INIT method")
#     def java(self):
#         print("CHILD calling B Class JAVA")
# class C(B):
#     def __init__(self):
#         print("CHILD CLASS C INIT method")
#     def C(self):
#         print("CHILD calling C Class C")
# out=C()
# out.python()
# out.java()
# out.C()

#Hierarical inheritance : the concept of inheriting properties from one clss to mutiple classses which are same parent class
class A:
    def __init__(self):
        print("CLLING PARENT CLASS A INIT METHOD ")
    def python(self):
        print("CALLING PARENT CLASS A PYTHON METHOD")
class B(A):
    def __init__(self):
        print("CHILD CLASS B INIT method")
    def java(self):
        print("CHILD calling B Class JAVA")
class C(A):
    def __init__(self):
        print("CHILD CLASS C INIT method")
    def C(self):
        print("CHILD calling C Class C")
class D(A):
    def __init__(self):
        print("CHILD CLASS D INIT method")
    def GO(self):
        print("CHILD calling GO LANG")
# out=D()
# out.GO()
# out.python()
# out1=C()
# out1.C()
# out1.python()
# mutiple iheritance : the concept of inheriting peroperties from mutiple classes to single clss is called multiple inheritance

class A:
    def __init__(self):
        print("CLLING PARENT CLASS A INIT METHOD ")
    def python(self):
        print("CALLING PARENT CLASS A PYTHON METHOD")
class B():
    def __init__(self):
        print("CHILD CLASS B INIT method")
    def java(self):
        print("CHILD calling B Class JAVA")
class C():
    def __init__(self):
        print("CHILD CLASS C INIT method")
    def C(self):
        print("CHILD calling C Class C")
class D(A,B,C):
    def __init__(self):
        print("CHILD CLASS D INIT method")
    def GO(self):
        print("CHILD calling GO LANG")

# out=D()
# out.python()
# out.java()
# out.C()
# out.GO()
# hybrid inheritnce : the combination of mofre than one inheritnance is called hybrid inheritance
class A:
    def __init__(self):
        print("CLLING PARENT CLASS A INIT METHOD ")
    def python(self):
        print("CALLING PARENT CLASS A PYTHON METHOD")
class B(A):
    def __init__(self):
        print("CHILD CLASS B INIT method")
    def java(self):
        print("CHILD calling B Class JAVA")
class C(B):
    def __init__(self):
        print("CHILD CLASS C INIT method")
    def C(self):
        print("CHILD calling C Class C")
class D(B):
    def __init__(self):
        print("CHILD CLASS D INIT method")
    def GO(self):
        print("CHILD D calling GO LANG")

# out=D()
# out.GO()
# out.java()
# out.python()

#Super() : super() method is a inbuilt method  useful for to call super class construtors(init method) varuables,methods

class A:
    def __init__(self,name,RNo):
        self.name=name
        self.RNO=RNo
        print("CLLING PARENT CLASS A INIT METHOD ")
    def python(self):
        print("CALLING PARENT CLASS A PYTHON METHOD")
        print("name",self.name)
        print("name", self.RNO)

class B(A):
    def __init__(self,name,RNO,x,y):
        super().__init__(name,RNO)
        self.a=x
        self.b=y
        print("CHILD CLASS B INIT ")
    def java(self):
        print("CHILD calling B Class JAVA")
        print("a val :",self.a)
        print("b val :", self.b)
        super().python()

# out=B("HI",8,100,200)
# out.java()

# we are not allowed to access parent class instance variables dorectly in child class using super()
# we are allowed to access parent class static variables , class methods and static method inside the child class


class A:
    x=1000
    def __init__(self):
        print("CLLING PARENT CLASS A INIT METHOD ")
    @staticmethod
    def python():
        print("CALLING PARENT CLASS A STATIC METHOD")
    @classmethod
    def C(cls):
        print("CALLING PARENT CLASS METHOD")
    def HI(self):
        print("Class A instance method")



class B(A):
    def __init__(self):
        print("CHILD CLASS B INIT ")
        super().__init__()
    def java(self):
        super().python()
        super().C()
        super().HI()
        print("CLASS A varible ",super().x)

# out=B()
# out.java()

# print("Name :",out.name)
# print("RNO",out.RNO)


