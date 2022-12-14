# for i in range(len(x)):  #   sum      # x[i]
#                               0          1
#     sum=sum+x[i]               1         2
#                                1+2=3      3
#                                3+3=6       4
#                                6+4=10       5
#                                10+5=15
# print(sum)
#
#
# x=[10,2,200,40,50]  #200
#
# max=0
#
# for i in range(len(x)):
#     if x[i]>max:
#         max=x[i]
#
#
# max             x[i]
# 0	10
# 10                  2
#                       200
# 200                40
#                        50
f=1
n=int(input("Enter n val :"))
for i in range(1,n+1):
    f=f*i
print("Fact of",n ,"is :",f)

#
# n         f      I          f=f*I
# 5          1    1          f=1
#              1    2         f=1*2=2
#              2     3        f=2*3=6
#               6     4      f=6*4=24
#               24    5     f=24*5=120
#             120
count=0
for i in range(1,n+1):
    if n%i==0:
        count=count+1
if count==2:
    print("%d is prime" %n)
else:
    print("%d is not prime" %n)




#
# n  Count
# 5    1
#      2





#iterative :
# if we want to execute group of statements multible times then we should for iterative statements
# python supports only two
# 1) For loop
# 2) While
#For loop:
# if we want to execute same action for ele present in some sequence then we should go for loop
#syntax : for var_nmae in collection(str,list,set,range,tuple)
                   #print()


# x=range(1,11)
# for i in x:
#     print(i,end=' ')

# for i in range(1,11):
#     print(i,end=' ')

# for i in range(11,2,-2):
#     print(i,end=' ')

# if you pass only one argument in range by default it will treate as ending indx

# if we want to generate elements in assending order stating idx < endingindx


# for i in range(10):
#     print(i,end=' ')

x=list(range(1,11))
# print(x)
# for i in x:
#     print(i, end=' ')
# print()
# for i in list(range(1,11)):
#     print(i,end=' ')
# print()
# for i in range(len(x)):
#     print("index :",i,"ele :",x[i])

# x=11
#
# if(x%2==0):
#     print("even")
# else:
#     print("odd")



x=[1,3,5,8,10,20,60]  # [8,10,20,60]
# # for i in x:
# #     print(i, end=' ')
# for i in range(len(x)):
#     print(x[i],end=' ')

# for i in range(len(x)):
#      if x[i]%2==0:
#          print(x[i])
# for i in x:
#     if i%2==0:
#         print(i)

# for i in range(11,2,-2):
#     print("python",end=' ')


# for else

# x=list(range(1,11))
# print(x)
# x=list(range(0,11,2))
# print(x)


# for else

# x=[1,3,10,11,14]
#
# for i in range(len(x)):
#     print(x[i],end=' ')
# else:
#     print("For executed successfully.....")

#*****
#*****
#*****
# for i in range(1,4):
#     print('*'*5,end=' ')
#     print()
#*
#**
#***
# for i in range(1,4):
#     print('*'*i,end=' ')
#     print()


# for i in range(1,11):
#     print(i,end=' ')

# for i in "PYTHON":
#     print(i,end=' ')
#
# x='PYTHON'
# for i in range(len(x)):
#     print(x[i],end=' ')

# when loop executed successfully then only else part will be executed

# x=input("Enter x val :")
# print(x)
# print(type(x))
# x=int(x)
# print(type(x))

# x=int(input("Enter x  val: "))
# print(type(x))

##
##
##
##

# for i in range(x):
#     print('#'*2)
#     print()

# for i in range(len('PYTHON')):
#     print('PYTHON'[i],end=' ')
# else:
#     print("for executed successfully")

x=[10,20,5,1]
# for i in x:
#     print(i,end=' ')
# for i in range(0,6):    #[0,4] # 0,3
#     print(x[i],end=' ')
# for i in range(len(x)):    #[0,4] # 0,3
#     print(x[i],end=' ')
# find the factorial of given num:
#4-> 1*2*3*4 =24
#
# n=int(input("Enter n val :"))
# f=1
# for i in range(1,n+1):  #(1,4)                             # n=4   i=1   f=1  f=f*i  =1*1
#                                                            #       i=2   f=2    f=2*3
#                                                            #       i=3   f=6    f=6*4
#                                                            #       i=4   f=24
#     f=f*i
# print("Factorial of %d is : %d" %(n,f))


# while()
# if we want to execute grup of statements iteratively until some condition false then we should go for while loop
# syntx : while(condition):
                #st1
                #st2
               #inc/dec

# 1-10
# i=1
#
# while(i<=10):
#     print(i,end=' ')
#     i=i+1


# for i in range(5):
#     print("HELLO")

# print("While output")
# i=1
# while(i<=4):
#     print("HELLO")
#     i=i+1

i=1
# while(i<=10):
#     print(i,end=' ')
#     i=i+2

# while(i<=10):
#     if(i%2!=0):
#         print(i,end=' ')
#     i=i+1

# 1-10

# i=1
# while(i<=10):
#     print(i,end=' ')
#     i=i+1
# else:
#     print("While Executed successfuly....")

# n=int(input("enter n val :"))
# x=1
# while(x<=n):    #while(1) # infinity
#     print(x,end=' ')
#     x=x+1

# n=int(input("enter n val :"))
# x=1
# while(n>0):    #while(1) # infinity
#     print(n,end=' ')
#     n=n-1
#
# x=['python',10,10.3,1000]
# i=0
# while(i<len(x)):
#     print(x[i],end=' ')
#     i=i+1
# print multiplication table

#2*1=2
#2*2=4
# n=int(input("Enter n val :"))
#
# for i in range(1,11):
#     #print("%d*%d=%d" %(n,i,n*i))
#     print(n,"*",i,'=',n*i)

# ex2: sum of (1,10)
# x=list(range(1,11))
# print(x)
# print(sum(x))
# print(len(x))
# print(max(x))
# print(min(x))

# x=[2,4,6,10,3]
# print("sum",sum(x))
# l=len(x)-1
# s=0
# while(l>=0):
#     s=s+x[l]       # s=0 0+3 s=3  l=4 ,l=3
#     l-=1
# print("Sum of x:",s)

# n=int(input("Enter n val :"))
# for i in range(1,n+1):
#     print('*'*i)

#123 -> 321
# n=int(input("Enter n val :"))
# s=0
# temp=n        6-> 1,2,3
# while(n>0):
#     r=n%10
#     s=s*10+r        # 30*2=60
#     n=n//10
# print("Reverse num of %d is : %d" %(temp,s))
# if(temp==s):
#     print("num is pal %d" %temp)

# n=int(input("Enter n val :"))
# s=0
# temp=n       # 6-> 1,2,3
# while(n>0):
#     r=n%10
#     s=s+r*r*r        # 30*2=60
#     n=n//10
# print("amstrong num of %d is : %d" %(temp,s))

#153 =-> 1+125+27   -> 153
# if(temp==s):
#     print("num is pal %d" %temp)

# x=[1,2,5,4,22,33]
# odd_sum=0
# even_sum=0
# for i in x:
#     if i%2==0:
#         even_sum=even_sum+i     # even_sum=2+4=6+22=28
#     else:
#         odd_sum=odd_sum+i       #odd_sum=1+5=6+33 =39
# print("Evensum :",even_sum)
# print("odd_sum :",odd_sum)

#Nested loop: # loop inside the loop is called nested  loop
#Nested_for
# syntax:for varname in collection(list,range,tuple,set,dic):
                 #st1
                 #st2
                #for varname in collection(list,range,tuple,set,dic):
                       #st1
                       #st2
#
# for i in range(1,3):
#     print(i)
#     for j in range(1, 4):
#         print('python')


# for i in range(1,4):
#     print("i val is :",i)
#     for j in range(1,6):
#         if j==2:
#             break
#         print(j,end='')
#     print()

# n=int(input("Enter n val : "))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count=count+1
# if count==2:
#     print("%d is prime" %n)
# else:
#     print("%d is not prime" %n)

# fators of given numbers 1,2,3,6
n=int(input("Enter n val : "))
for i in range(1,n+1):
    if n%i==0:
        print("%d is factor of %d" %(i,n))









# for i in range(1,4):
#     print("i val is :",i)
#     for j in range(1,6):
#         if j==2:
#             continue
#         print(j,end=' ')
#     print()





#****
#****
#****
#****
# x=int(input("Enter n val :"))
# for i in range(1,6):
#     print(i)
#     for i in range(1, 3):
#         print("PYTHON")
#     print()
#****
#****
#****
#****
# x=int(input("Enter n val :"))
# for i in range(1,x+1):
#     for i in range(1, x+1):
#         print("*",end=' ')
# #     print()
# x=int(input("Enter n val :"))
# for i in range(1,x+1):
#     print('*'*(x))

# while():
#While inside the while is called nested while
# while(cond):
   #st1
   #st2
   #while(con):
      #st3
      #st4
      #inc/dec
   #inc/dec


# i=1
# while(i<=5):
#     print("i val is :",i)
#     j=1
#     while(j<=5):
#         print(j,end=' ')
#         j=j+1
#     print()
#     i=i+1


#
# i=1
# while(i<=5):
#     print("i val is :",i)  # 1 2 3
#     if i==3:
#         break
#     j=1
#     while(j<=5):
#         print(j,end=' ')
#         j=j+1
#     print()
#     i=i+1


# i=1
# while(i<=5):
#     print("i val is :",i)  # 1 2 3
#     if i==3:
#         continue
#     j=1
#     while(j<=5):
#         print(j,end=' ')
#         j=j+1
#     print()
#     i=i+1


#12345
#12345
#12345
#12345
# x=5
#
# while(x>0):                       #x=5  5>0    y=1 1<=5,2<=5 ,3<=5,4<=5 ,5<=5
#     y = 1                              #x=4
#     while(y<=x):
#         print("*",end=' ')  # 1 2 3 4 5 y=6
#         y=y+1
#     print()
#     x=x-1
#
# for i in range(1,5):
#     print('* '*i,end=' ')
#     print()

# tranfer control statements
#break,continue,pass
# break
# break is transfer control statement  it is used for to come out the loop execution based on some condition

# for i in range(1,6):
#     if i==4:
#         break
#     else:
#         print(i)

#print(list(range(0,11,2)))

# x=[1,10,20,600,200,500,800]
# for i in x:
#     if i>500:
#         break
#     else:
#         print(i,end=' ')

# x=[1,2,3]
# for i in x :
#     if i==2:
#         break
#     else:
#         print(i,end=' ')
# else:
#     print("For executed sucessfully..")






# for i in range(1,10):
#     if(i==6):
#         break
#     print(i,end=' ')
# for i in range(1,3): # 1,2
#     for i in range(1, 11):
#         if (i == 6):
#             break
#         print(i, end=' ')
#     print()

# x=['A','B','C','D','E','F'] #
#
# for i in range(len(x)):
#     print(x[i],end=' ')


# x=list(range(1,6))
# s=sum(x)
# print(s)
# # print(x)
# # sum=0
# # for i in range(len(x)):  #   sum      # x[i]
# #     sum=sum+x[i]
# # print("sum :",sum)

# find the max ele from the list

# x=[10,2,200,40,50,400,399,2000,2,1]  #200
# print("Maximum ele is:",max(x))
# print("Minimum ele is:",min(x))
# max=0
#
# for i in range(len(x)):
#     if x[i]>max:
#         max=x[i]
# print("Maximum ele is:",max)

#5=1*2*3*4*5=120
#import math
# f=1
#n=int(input("Enter n val :"))
# for i in range(1,n+1):
#     f=f*i
# print("Fact of",n ,"is :",f)
#print(math.factorial(n))


#continue:
# continue is transfer control statement  it is used for to skip the current iteration based on some condition
# for i in range(1,6):
#     if i==3 or i==4:
#         continue
#     print(i,end=' ')

# x=[1,2,8,6,11,17,4,13] # 1,11,17,13
#
# for i in x:
#     if i%2==0:
#         continue
#     print(i,end=' ')
#
# n=int(input("Enter n val :"))
#
# for i in range(1,11):    # 2*1=2
#     print(n,'*',i,'=',n*i)              # 2*2=4


#pass : if we dont want to write any stateent under if then we can simply write pass

# x=200
# if(x>100):
#     pass
# else:
#     print("HELO")
#
# while(con):
#     st1
#     st2
# inc/dec
# else:
#     st3
#     st4

# x=1
# while(x<=5):
#     print(x,end=' ')
#     x=x+1
# else:
#     print("While Executed Successfully.....")

# for else
# for i in range(1,6):
#     if(i==2):
#         continue
#     elif(i==5):
#         break
#     else:
#         print(i,end=' ')
# else:
#     print("For Executed Succesfuly ....")

# whenever while/for execute until the last value then it will go to else part

#for i in range()

# x=['hello','world','python']   # [h e l l o]
# for i in range(len(x)):
#     temp=list(x[i])
#     temp=chr(ord(temp[i][0])-32)
#     print(temp,end=' ')
    # temp=ord(x[i][0])
    # temp=chr(temp-32)
    # print(temp,end=' ')
    # x[i][0]=temp
    #print(x[i],end=' ')
#print(x)

#del : del is a keyword
# after using the var ,it is highly recommanded to del the var
# whenever you use del interpreter internlly knows the var is not going to use in future
#how to use del
# a=10
# print(a)
# a=a+10
# print(a)
# del a
# print(a)
#
# x="python"
# print(x[0])
# del x
# print(x)





























