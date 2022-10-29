#operator is a symbol that perform certain opertions
# operators ->Arthematic,Relational(Comparision),logical,bitwiseASsignment,specialope

# Arthmetic -> [+,-,*,/,%,//(floor div),**(Exponent or power)]
import  math as m
a=9
b=2
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b) #-> coefficient  2.5
# print(a//b) # -> floor val  2
# print(m.floor(5/2))
# print(a%b)  #-> reminder    1
# print(a**3) # 5*5*5 # exponent
# print(pow(a,2)) # 9*9
# print(5/2)

# print(math.pow(4,3))
# print(pow(4,3))
# print((4**3))

# + * these two r already overloaded
# + useful for concantinte two strings  here two variables should b strings  only
# * when we do multipliction on strings the varibles(one should b string and another one should b integer)

# x=10
# y=20
# print(x+y)
# x="NAGA"
# y="PYTHON"
# print(x+y)

# x=10
# y=2
# print(x*2)
# x="python"
# y=2
# print(y*x)


# x="Python"   #python2
# y=str(2)
# print(x+y)





# a=22
# a=str(a)
# b ="JAva"
# print(a+b)
# a="python"
# b=3
# print(a*b)
#
# x=[1,2,3]
# y=[4,5,6]
# print(x+y)
# print(x*3)

#
# if u want to multifly the string one operend should be integer
# a=a*"java"
# print(a)

# Relational operators <,>,<=,>=
# it shows the relation b/w two operends
# if condition True it will return True if condition false return False

#Relational ope (<,>,<=,>=)
# it shows the relation bitween two operands
#it will retrun the result is True /false
a=10
b=5
#print(a>b) #True
#print(a<b) #False
#print(a>=a) #True
#print(b<=b) #True
# print(a<=9) #False
# print(b>=6) #False
# print(a>=5) #True
# print(5<=b) #True
a=5
b=2

#print(a<3)
#print(a>b)
#print(b<4)
#print(5>a)
#print(b<a)
# print(a<=5)
# print(len("hi")>5)

#A-z ->ascci values 65 to 90
#a-z  ->ascci values  97-122


# a="AB" # 97-122
# b='AB' # 65-90
# # print("acii",ord(a))
# # print("acii",ord(b))
# # print("ascci",ord(' '))
# print(a>=b)
#
# a='B'
# print(ord(a))
#
# a='C'
# print(ord(a))
#
# a='a'
# print(ord(a))
# a='z'
# print(ord(a))
#
# a='Z'
# print(ord(a))
#
# a='1'
# print(ord(a))

# a=32
# print(chr(a))




# equity operators ==, !=
# if condition True it will return True if condition false return False
# a=10
# b=5
# print(a==b) #False
# print(a==a) #True
# print(a!=b) #True
# print(b!=b) #False
# print(a!=a) #False
# print(a==10) #True
# print(5==b) #True
# a="A"
# b='a'
# print(a==b)

# a=ord("A")+32  # 97
# b=ord('a')
# print(a==b)

# a=97
# print(chr(a))
# a='A'
# print(ord(a))
# a='B'
# b=ord(a)+31  # 66+31 =97
# print(chr(b))

# Logical Operators and or not     # And

# a b  a and b
# 1 1    1
# 1 0    0
# 0 1    0
# 0 0    0
# if first condtion is flase no need to check the second condition
# if first condtion is True need to check the second condition either true or false
# print(1 and 0) # 0
# print(1 and 1)  # 1
# a=10 # True or 1
# b=0 #  False or 0
# print(a<=10 and b<=0) #True
# print(0 and b<=0)    #False 0
# print(1 and a<0)     # False
# print(a>b and b<0)  #False 1 0
a=10
# b=20
# print(a>=1 and b>=10)
# print(a<5 and b>a)
# print(a==10 and b!=0)
# print(a>=5 and b>=10)
# print(a>=100 and b==30)


# or opertor
# a b  a or b
# 1 1    1
# 1 0    1
# 0 1    1
# 0 0    0
# print(1 or 0) # 1
# print(1 or 1)  # 1
# a=10
# b=5
# print(a>=10 or b<=0) #True
# print(0 or b<=0)    #Fase
# # print(1 or a<0)     # True
# print(b>a or b!=0)  #True

# Not -> if variable is non zero it returns False
# if it is zero it returns True
# a=0  #false
# print(not a)  #
# print(not 0)  # True
a=5 #True
# print(not a ) # True
# print( not 0)
# print( not 1)
# b=3
# print(not(a>1 and b<a))
# print((not(a>1) or b>1))
# print(not(a))


# Assignment ope  -> WE can combine assignmnetopertor with any other ope
# this the combination of two operators but the operation should be in two variables
b=5
a=10
# a=a+b # 10+5
# print(a)
# a+=b  # a=a+b # a=15
# a/=b # a=a/b
# print(a)
# a=b//a
# print(a)
# b*=a #b=b*a
# print(b)
# a//=b # a=a//b(2.0)
# print(a)
# b-=a #b=b-a # 5-2=3
# print(b)
# a*=b # a=a*b
# print(a)

# c=None
# a+=b # a=a+b   # a+=b
# a+=b #a=a+b
# print(a)
# print(a+b)
# a-=b # a=a-b
# print(a)
# print(a-b)
# a*=b # a=a*b
# print(a)
# print(a*b)

#a+=b # a=a+b ->15
# print(a)
# a-=b   # a=15-5 10
# print(a)
# a*=b   # a=a*5 -> 50
# print(a)
# a//=b
# print(a)   # 10
# a//=2       # 5
# print(a)   # a=5
# a%=2
# print(a)

# Ternary ope -> if con is true first vlue will be considered else second value will be considered
# a=10
# b=0

a,b=10,20
# print(a)
# print(b)
# a=a+20
# b=b+30
# c=50
# a,b,c=a+20,b+30,50
# print(a,b,c)

# syntax ->varibale = varibale if cond else val
a,b=10,20
# print(a)
# print(b)
# c=b if not(0) else 100
# #print(c)
# d= c+50 if (a!=b) else a
# d*=10
# print(d)

# if((a>5 and b<3)):
#     print(b)
# else:
#     print("HI python")
#print(c)

# logical
#And or No
# And  -> a ,b and b
# a b  a and b
# 1 1    1
# 1 0    0
# 0 1    0
# 0 0    0

a,b=10,100

# print((a>b)and (a<b))
# print((a>=a)and (a<b))
# print((a>=100)and (b>=100))
# if(a and b):
#     print("hello")
# or
# a b  a and b
# 1 1    1
# 1 0    1
# 0 1    1
# 0 0    0
# print((a>b)or (a<b))
# print((a>=a) or (a<b))
# print((a>=100)or (b>=100))
# print((a>b)or (a<b))
# a,b=10,100 #  a=10, b=100
# print(((a>=a)and (a<b))or(b>10))
# print((a>=200 or b<=50)and(a==10))


# x=[1,2,3,4,5]
# print(x[1:4])
# print(x[1:len(x)-1])
# print(x[1:-1])
#
# _=10
# _____=200
# print(_+_____)
# a=10
# b=20
#print(a+b)
# a=10
# b=20
# c=a-(-b)
# print(c)
#print(_.__add__(__))
# print(a.__sub__(b))
# print(a.__mul__(b))
# print(a.__add__(b))
# print(a.__ge__(b))
# print(a.__le__(b))
#membership Operators
#in ,not in
#we can use membership ope to check whether the object is present or not in given list(set,tuple,dic,str)
# if it is present it wil return true else it wil return false
# x=[1,2,3,4]
# print(1 in x)
# print(3 in x)
# print(10 in x)
# y="HELLOPYTHON"
# print("PY" not in y)
# x=(1,2,3,10)
# print( 1 in x)
# print(2 not in x)
# x={10,20,30,10,20}
# print(x)
# print(50 in x)
# a=3
# a=a*3 #9
# print(a in x)
# x="python"
#print('P' in x)
# x="aythAon"
# y=chr(97) #'a'
# print(y)
# print(chr(97-32) in x)
# ord is the fun to find the ascii val of any char
#print('a' not in x)

# x="python"
# print('h' in x)
# x=list(range(1,20))
# print(x,end=' ')
# print()
# y=[1,2,25,30,100]
#
# for i in y:
#     if i in x:
#         print(i)
#     else:
#         print(i ,"is not Exist in List",end=' ')


#identity opertors

#is is not

# a=10
# b=10
#
# print(a is b)   # ==
#
# a=20
# b=30
# print(a is not b) !=

# a=True
# b=False
# print(a is b)
# a=True
# b=True
# print(a is b)



#bitwise ope
# & ,|,^,<<,>>,~
# a b  a and b
# 1 1    1
# 1 0    0
# 0 1    0
# 0 0    0

# a=4
# b=3
# print(a&b)

# a=10
# b=6
# print(a&b)

# a=15
# b=7
# print(a&b)

# a=15
# b=7
# print(a|b)




# print(a|b)
#XOR ->(^) where two conndtions are true and two condtions are false then only will become false
# else if only one condition is true then it will return True

a=15
b=6
# a b  a and b
# 1 1    0
# 1 0    1
# 0 1    1
# 0 0    0
print(a^b)

# #          32 16  8  4  2  1
#                   0   0   0   1
#                   0    0  1   1
#                            1
#
#print(a^b)


# left shift(<<)
# a=2
# b=3
# print(a<<b) # 2*2*2*2

# a=7
# print(a<<4)
#
# a=8
# print(a<<3)

#a=10*2=20*2=40*2

#>>

# a=10
# print(a>>3)     # 10/2=5 -> 5/2=2
#
#
# a=100
# print(a>>4) # 100/2 =50 50/2=25 25/2=12 12/2 =6


# a=7
# a=a<<3
# print(a)
#
# a*=2 # a=a*2
# print(a)
# print(a>>3) # 112/2 =56 =56/2=28/2=14
# a=7
# print(a<<2)
# a=3
# b=2  # 3*2 =6*2
# print(a<<2)

# a=5 # 5*2 =10*2=20 20*2
# b=3
# print(a<<3)
#
# a=4
# b=2
# print(a<<b) # 4*2=8 ,8*2 =16

# a=10
# b=2
# print(a>>b)     # 10/2=5   5/2 =2

# a=30
# b=3
# print(a>>b)
#
# a=4
# b=3
# print(a<<b)




# special ope
#identity ope  -> is, is not
# membership ope -> in ,not in
a=5    # 4  4     a=[]
b=10
# c= a is b
# print(c) # a=b
# c= a is not b
# print(c)
# print(a is not b)
# print(a is b)
# print(a)
# print(b)
# #membership
# x="python"
# print('h' in x)
# x=[1,2,3]
# print(3 not in x)
# print('h' not in x)

# bitwise ope -> it wil do opertion on bits

# & |,^ ~ ,<<,>>

# x=21
# y=17
# print(x ^ y)             #   x   y   x ^ y
                         #   1   1     0
                         #   1   0     1
                         #   0   1     1
                         #   0   0     0
# x=13   # if num is +ve it will add +1 whole result will be negative
# print(~x)
#
# x=-10   # if num is -ve it will subtract 1 whole result will be positive
# print(~x)

# x=17
# print(~(x))
#
# x=-4
# print(~(x))

#keyword : keyword is reserved word the meaning cant be while executing the program
#keyword should not b used a variable name

# to know how many keywords in current version
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))

# min,max,len,pow ..etc  are predefined functions -> no need to import any module
# True ,False None these three starts with caps

# <<multify the num with 2 n times

# x=3         #    5 *2 =10 -> 10*2 ->20  *2 =40
# y=5
# print(x<<y)
#
# x=50     #-> divide by 2
# y=3
# print(x>>y)
# two zero or two ones it becomes false(or zero)
# swap two numbers using bitwise
# a=1                  # 0 0 0 1
# b=2                  # 0 0 1 0
# a=a^b #a=            # 0 0 1 1 -> a=3
# #print("a val :",a)   # 0 0 1 0  -> b=2
# b=a^b #b=            # 0 0 0 1  -> b=1
# #print("b val :",b)
# a=a^b #a             #0 0 1 1 -> a=3
#                      # 0 0 0 1  -> b=1
#                     # 0 0 1 0  -> 2 # a=2
# print("a val :",a)
# print("b val :",b)
# complement (~)
# x=10  #x=-(x+1)
# print(x)
# # print(~(x))
# x=-5 # (-(-5+1)) #-(-4)
# print(~(x))
# x=8
# print(~(x)) # -9
# x=-7
# print(~(x)) # 6

