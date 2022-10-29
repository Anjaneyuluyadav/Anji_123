# in any programming languges there are two types of errors
# syntax error
# runtime errors

# syntx error : the errors which are raised at compile time is called syntax errors
# 1a=300
# if a
#     print("HI")
# runtime errors :the errors which are raised at run time is called runtime errors
# a=10
# b=0
# print(a/b) #division by zero

# Exception : exception is an event it interpts the normal flow of execution
# exception : is an unwanted and unexpected event it distrubs the normal flow of execution
# a=10
# b=0
# print(a/b) #division by zero
# print("HI")
# print("Hello")

# Ex : Zero division error
# TypeError
#Value error
#EOF Error
# File Not Found error

# basic syntax:
# # try :
#    st1
#    st2
#   Except :
#     st3
#     st4
# try:
#     a = 10
#     b = 2
#     print(a / 0)
# except Exception as e:
#     print(e)

# its highly recommaned to handle exceptions using exception handling'
# the main objective of exception handling is Graceful Termination
#by default python having exception handling
#
# a=10
# b=0
# print(a/b)
# print("HI")
# try:
#     a = 10
#     b = 2
#     print(a / 0)
# except Exception as e:
#     print(e)
#     print("HI")
#     print("Hello")

# try : this block useful for to read the data  # we can write our business logic
# in try if any error occures then it automaticaly jumps toexcept block
# Except block : it will acccepts the exceptions if any exceptions raised in try block
# one try block can have multiple except block
# defulut exceprct always should be last (before finally block)
# when ever exception raised in try block automaticlly it wil check for corresponding except block
# case 1
# try :
#     a=10
#     b=0
#     print(a/b) #zero division
#
# except ZeroDivisionError :
#     print("HI")
#     print("HELLO")

# case 2 :
# in except block if any error occurs it is always abnormal termination
# try :
#     a=10
#     b=0
#     print(a/b) #zero division
# except Exception as e :
#     print(e)
#     print("HI")
#     print("HELLO")
#
#cae 3
# try :
#     print("HI")
#     a=10
#     b=0
#     print(a/b) #zero division
# except ZeroDivisionError as e :
#     print(e)
#     print("HI")
#     print("HELLO")

# try :
#     print("HI")
#     a=eval(input("Enter A val :"))
#     b=eval(input("Enter b val"))
#     c=a/b
# except (NameError,ValueError,ZeroDivisionError,FileExistsError,FileNotFoundError) as e :
#     print(e)
#     print("HI")
#     print("HELLO")
# except :
#     print("HI")
# print("PYTHON")
# print("JAVA")
# Finally block :  its not recommanded to maintain the code in try block because expection may raise in try block
#its not recommanded to maintain the code in Expect block because we are not sure Except block will execute or not
# hence we required some place to maintain and clean up the code ,that block is finally block
# finally block does not cares about whether exception raising try bock and handing in except block
# the main purpose of finallly block is to maintain clean up code
# suppose any exception comes in finally block it is always abnorml termination
# syntax :
# try :
#     st1
#     st2
# except Exception as e:
#     st3
#     st4
# finally:
#     st5
#     st6
# print("HI")
# a = eval(input("Enter A val :"))
# b = eval(input("Enter b val"))
# c = a / b
#
# try :
#     print("HI")
#     a=eval(input("Enter A val :"))
#     b=eval(input("Enter b val"))
#     c=a/b
#     print("val :",c)
# except (NameError,ValueError,ZeroDivisionError,FileExistsError,FileNotFoundError) as e :
#     print(e)
#     print("HI")
#     print("HELLO")
# except :
#     print("defult except")
# finally:
#     print("HI python")
#     print("Hello java")
#     print(10/0)

# nested Exception handling :
# one try try block can have multiple try-except-finally blocks then its  nested Exception handling

# try :
#     st1
#     try:
#     st2
#     st3
#     except Exception as e:
#     st4
#     st5
#     finally:
#     st7
#     st8
# except Exception as e:
#     st9
# finally:
#     st10

# try :
#     a=10
#     b=2
#     print("res :",a/b)
#     try :
#         print("if NO exception in outer try then only this wil exceute")
#     except Exception as e  :
#         print("inside Exception :",e)
#     finally:
#         print("Inside FInally block")
# except Exception as e:
#     print("outsdie Except block")
# finally:
#     print("outside Finally block")
# try :
#     a=10
#     b=2
#     print("res :",a/b)
#     print("outer try block")
#     print("Outer try block data")
#     try :
#         print("if NO exception in outer try then only this wil exceute")
#     except Exception as e  :
#         print("inside Exception :",e)
#     finally:
#         print("Inside FInally block")
# except Exception as e:
#     print("outsdie Except block",e)
# finally:
#     print("outer finally block")
#     for i in range(1,6):
#         print(i,end=' ')

# try :
#     for i in range(1, 6):
#         if i/0==0:
#             print("hi")
#     print("outer try block")
#     print("Outer try block data")
#     try :
#         print("if NO exception in outer try then only this wil exceute")
#     except Exception as e  :
#         print("inside Exception :",e)
#     finally:
#         print("Inside FInally block")
# except Exception as e:
#     print("outsdie Except block",e)
# finally:
#     print("outer finally block")
#     for i in range(1,6):
#         print(i,end=' ')

# else : we can use else block with try-except-finally block
# else-bock will execute if and only if there is no exception in try block otherwise it wont execute

# try :
#    a=10
#    b=2
#    c=a/b
#    print("val :",c)
# except (NameError,ValueError,ZeroDivisionError,FileExistsError,FileNotFoundError) as e :
#     print(e)
#     print("HI")
#     print("HELLO")
# except :
#     print("defult except")
# else:
#     print("NO error in try")
# finally:
#     print("HI python")
#     print("Hello java")

# Custom Exceptopon handling :
# some times we have to define and raise the exceptions  explicitly to indiate somethig goes wrong

#programmer is responsible to define exceptions  python does not any idea bout these exceptions  hence we have to raise explicitly
# based on our requirememt
# Ex : InsufficientFunds Funds Execptions
# Ex :Tooyoung Exceptions
# Ex: Tooold Exceptions'

# how to define and raise the customized Exceptions

# syntax :
#  class clasname(Exception):
#      def __init__(self,args):
#          self.msg=arg

# class TooYoungException(Exception):
#     def __init__(self,arg):
#         self.msg=arg
#
# class TooOldException(Exception):
#     def __init__(self,arg):
#         self.msg=arg
# class getmarry(Exception):
#     def __init__(self,arg):
#         self.msg=arg
# age=int(input("Enter age :"))
# if age <18:
#     raise TooYoungException("PLease wait some more time")
# elif age>40:
#     raise TooOldException("Ur age is already crossed")
# elif age>=18:
#     raise getmarry("U R eligible to get marry")



