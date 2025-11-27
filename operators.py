# print(5=='5')           #comparison operator
# print(5!=3)
# print(580<789)
# print(4>=4)
# print(4.00>=4)

# print(5>3 and 7<5)              #logical operator
# print(5>3 or 7<5)
# print(not(5>3) )

# x=5                                  #identity operator
# y=4
# print(x is not y)

# a= "boss is "                       #membership operator
# print("b" in a )
# print("m" not in a )

# print(6&3)          #AND                #BITWISE OPERATOR
# print(6|3)          #OR
# print(6^3)          #XOR
# print(~6)           #NOT
# print(3<<2)         #LEFT SHIFT
# print(8>>3)         #RIGHT SHIFT

# x=(10+3)*2**2             #operator precedence
# print(x)

# a=24                                              #IF ELSE STATEMENTS
# b=214
# if a>b:
#     print("a is greater than b")
# elif a<b:
#     print("hello")
# else:
#     print("house")    

#QUESTIONS
# 1. if 90<= exccellent 75-89 good 50-74 average 50>fail
# 2. yes if character is vowel anf no if character is consoenet
# 3. age 18>age use bicycle 18-25 age use motorcycle 25-55 car and above 55 hire a driver 
# 4. number is even or odd 
# 5. num. positive or negative or 0
# 6. find the greatest of three numbers
# 7. number divisible by both 3 & 5
# a= int(input("enter your marks"))
# if (a>90):
#     print("excellent")
# elif (a>75 and a<=89) :
#     print("good")
# elif (a>50 and a<=75) :
#     print("average")
# else:
#     print("fail")

# a= str(input("enter alphabet :"))             #q 2
# a= a.lower()
# if a.isalpha():
#     if a in ["a","e","i","o","u"]:
#          print("vowel")
#     else:
#          print("consonent")
# else:
#      print("not alphabet")
    

# a= int(input("enter your age :"))               #q 3

# if (a<=18) :
#     print("use bicycle")
# elif (a>18 and a<=25):
#     print("use motorcycle")
# elif (a>25 and a<=55):
#     print("drive car")
# else:
#     print("hire driver")

# a = str(input("enter number :"))                    #q4
# b = a[-1]
# if b in ["0","2","4","6","8"]:
#     print(f"{a} is even")
# elif b in ["1","3","5","7","9"]:
#     print(f"{a} is odd")
# else:
#     print("invalid input")

# a = int(input("enter number"))                        # q4

# if(a%2==0):
#     print(f"{a} is even")
# else:
#     print("odd")

# a= int(input("type any number :"))                    # q 5
# if (a<=-1):
#     print("negative")
# elif (a>=1):
#     print("positive")
# else:
#     print("zero")

# a= int(input("type first number :"))                  #q6
# b= int(input("type second number :"))  
# c= int(input("type third number : "))  
# if (b>a and b>c):
#     print(b)
# elif (a>b and a>c):
#     print(a)
# elif (c>a and c>b):
#     print(c)
# else:
#     print("not applicable")


a = int(input("enter number :"))                        # q7

if(a%3==0 and a%5==0):
    print(f"{a} is divisible by 3&5")
else:
    print("not divisible")




