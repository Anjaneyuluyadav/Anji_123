#control flow
# conditional
#Transfer control
# iterative (Loops)

# Condtional _
#if -> used for to check the condition whether true or false if it is true it will execute the under the if statements will b executed
# any condition should b ends with : in python
# # syntax : if(con):
#               #st1
#               #
#  # st2
#  #              ---
#  #              ---
# a=10
# if(a):
#     print("hi")
#     print("Helo")
# print("HI PYTHON")
# a=2
# if(a>1 and a<=5):
#     print("HI")
#     print("Hello")
#     print("JAVA")
#     print("PYTHON")
# print("C,C++")
#
# a=10
# if(a>0):
#     print(a)
#     print("python")
#     print("HELO")
#     print("I am good")
# print("HI not belongs if")
#if-else :
#if -> used for to check the condition whether true or false if it is true it will execute the under the if statements will b executed
# if con is false it wil execute esle statements
# syntax:
#if(con):
   #st1
   #st2
   #st3
#else:
  #st4
  #st5
  #---

# a=5
# if(a>10 or a>2):
#     print("HI")
#     print("JAVA")
#     print("PYTHON")
# else:
#     print("C")
#     print("C++")

# a=10
# b=2
#
# if (a<5 or b>1):
#     print("HI")
# else:
#     print("HELO")


# find the biggest num in two var
# a=int(input("Enter a val :"))
# b=int(input("Enter b val :"))
# if(a>b):
#     print("Biggest num :%d" %a)
# else:
#     print("Biggest num :%d" %b)
# a=0
# if(a):
#     print("Hello")
# else:
#     print("Hi")

# a=" "
# if(a):
#     print("Hello")
# else:
#     print("Hi")
# if-elif-else
#syntax:
#if(con):
  #st1
  #st2
#eif(con):
   #st3
   #st4
#elif(con):
   #st10
#elif(con)
  #st7
#else:
  #st5
  #st6

# if all con are fail it will go to else part and we dont check any con with else
# a=10
# b=20
# c=20
# d=10
#
# if(a<5):
#     print("HELO")
# elif(a==b):
#     print("HI")
# elif(a>b):
#     print("python is good")
# elif(b>c and a<11):
#     print("HI HELlo")
# else:
#     print("JAVA")

#
# if(a>15):
#     print("HI")
# elif(a>10):
#     print("Hello")
# else:
#     print("HI JAVA")
# find the biggest of three numbers
# a=200
# b=500
# c=1000
# if(a>b and a>c):
#     print("Biggest num is :",a)
# elif(b>c):
#     print("Biggest num is :", b)
# else:
#     print("Biggest num is :", c)

# nested if: if inside the if called nested if
#
# a=10
# b=5
# if(a>5):
#     print("C")
#     if(b>10 and b<2):
#         print("C++")
#     else:
#         print("python")
# else:
#     print("JAVA")


#syntax :
# if(con):
     #st1
    #if(con):
       #st2
     #elif(con):
       #st3
    #else:
    #st4
#else:
  #st5

# a=10
# if(a):
#     print("A val :",a) #10
#     if(a>5):
#         print("hello")  #hello
#         if(a==10):      #python
#             print("PYTHON")
#         else:
#             print("JAVA")
# else:
#     print("10")

# a=10
# b=200
# if(a>5):
#     print("A val :",a) #10
#     if(a==200):
#         print("hello")  #hello
#         if(a==10):      #python
#             print("PYTHON")
#         else:
#             print("JAVA")
# else:
#     print("HELLO WORLD")
#     if(b>100):
#         print("JAVA IS OK")
#     else:
#         print("Python is good")

# a=100
# b=20
# if(a>b):
#     print("HELLO")
#     if(b==20):
#         print("HI")
#     elif(a<b):
#         print("A")
#     else:
#         print("B")
# elif(b>a):
#     print("JAVA")
# else:
#     print("PYTHON")
#
# a,b=10,20
# if(a<20):
# print("HI")
# if(a==10):    # if 2
# print("HELLO")
# if(b>100 or b<10):
# print("python")
# if(b!=20):   #b==20
# print("JAVA")
# elif(b!=0):
# print("C")
# else:
# print("B")
# else:
# print("JAVA IS GOOD")
# else:   #if -2
# # print("HELLO WORLD")
# # else:
# # print("CON IS FALSE")
#
# nem=7
# for i in range(1,11):
#     print(nem,"x",i,"=",nem*i)
#     # print(nem,'x',i,'=',nem*i)
#
a=4
b=7
# a=a^b
# b=a^b
# a=a^b
# print(bin(a))
# print(bin(b))
a,b=b,a
print(a,b)
x={'a':7,'b':9}
keys=list(len(x.keys()))
values=list(len(x.values()))
print(keys)
out=[]
for values:keys,values in (x.values():
