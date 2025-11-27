# 1# to check wether a stringg is palindrom or not
# 2-to checkj weather a year is a leap year or not
# 3-a program which checks the character type vowel consonent digit special character.
# 4-make a basic calculator
# 5-program to reverse the string 
# 6-take two string and check whether they are anagram of each other or not 
# 7-even or odd using ends with fuunction and usingf indexing as well
# 8-write a program to check if and last character is same or not
# 9- write a program to check if first and last character is same or not
# 10- write a program to find if figure is triangle and find if it is equilateral scalen or isosceless triangle


# a= input("type any word:")                #q 1
# if (a[::-1] == (a[0::])):
#     print ("palimdrom")
# else:
#     print("not a palidrom")

# a= input("type any word:")                #1
# if (a[::-1] == a):
#     print ("palimdrom")
# else:
#     print("not a palidrom")

# a = int(input("enter the year:"))                 #2
# if (a%400==0 or (a%4==0 and a%100!=0)):
#     print(f"{a} is a leap year")
# else:
#     print(f"{a} is not leap year")

# a= str(input("enter:"))             #q 3
# a= a.lower()
# if a.isalpha():
#     if a in ["a","e","i","o","u"]:
#          print("vowel")
#     else:
#          print("consonent")
# elif a.isdigit():
#     print("number")
# else:
#     print("special character")

# a= (input("enter your word :"))           q5
# b=(a[::-1])
# print(b)

# a= input("type any word:")                q6
# b= input("type any word:")                     
# if (sorted(a)==sorted(b)) :
#     print ("anagram")
# else:
#     print("not a anagram")

# a=float(input("type 1 number :"))                     q 4
# b=float(input("type 2 number :"))
# c= input("enter operator +,-,*,/  :")
# if c=="+":
#     print(a+b)
# elif c=="-":
#     print(a-b)
# elif c=="*":
#     print(a*b)
# elif c=="/":
#     print(a/b)
# else:
#     print("error")


# a = str(input("enter number :"))                    #q7   by indexing
# b = a[-1]
# if b in ["0","2","4","6","8"]:
#     print(f"{a} is even")
# elif b in ["1","3","5","7","9"]:
#     print(f"{a} is odd")
# else:
#     print("invalid input")

# a = input("enter number")
# if a.endswith(("0","2","4","6","8")):
#     print("even")
# else:
#     print("odd")

# a= input("enter  :")                #Q 8
# b= input("enter  :")
# c= a[-1]
# d= b[-1]
# if (c==d) :
#     print("same character")
# else:
#     print("differentt character")

# a= input("enter  :")                                Q 9
# b= a[-1]
# c =a[0]
# print("same ") if (b==c) else print("different")
   

# a = int(input("side of triangle :"))                      #q 10
# b= int(input("side of triangle :"))
# c =int(input(" side of triangle : "))
# if (a+b>c and b+c>a and a+c> b):
#     print("it is a triangle")
#     if a==b and b==c:
#         print("it is equilateral")
#     elif (a== b and b!=c or b==c and c!=b or c==a and a!=b):
#         #(a=b or b=c or c=a)
#         print("it is isoscelles triangle")
#     else:
#         print("scallen triangle")
# else :
#     print(" it is not a triangle")

# q1 pint 1 to 10 usingg while Loop
# q2 table of 5 using while loop
# q3 pint even no from 1-50
# q4 factorial of a number 
# q5 user defined table

# i= 1                      #q1
# while i<=10:
#     print(i)
#     i+=1

# a=5                   #2
# while a<=50:
#     print(a)
#     a+=5

# b=2                             #3
# while b<=50:
#     print(b)
#     b+=2

# a=int(input("type any number"))                   # 4
# factorial=1
# i=1
# while i<=a:
#     factorial*=i  #factorial = factorial * i
#     i+=1 # i=i+1
# print(f"factorial of {a} is {factorial}")

# a=int(input("type any number"))                     #5
# i= 1
# while i<=10:
#     print(f"{a}*{i}={a*i}" )
#     i+=1


# q1 print the square of numbers from 1-5
# q 2 print the first 10 even no
# q3 print the first 10 odd number
# q4 calculate the sum of numbers from 1-n where n is user defined
# q5 print the reverse of a number
# q6 print fibonacci series upto n terms 
# q7 porint all prime no bet 1-50
# q8 print sum of digits of no.
# q9 print the sum of all even no 1-100
# q10 print armstrong no bet 1-500
# q11 print the no from 1-50 but skip multiple of 3

# a= int(input("type any number"))
# i= 1 
# while i<=a:
#     print(f"square of {i} is {i*i}")
#     i+=1

# a = int(input("type any no. :"))                
# i =1
# while i<=a:
#     prnt(i*2)
#     i+=1
    

# a = int(input("type atarting no. :"))
# b = int(input("type ending no. :"))
# for i in range(a,b,2):
#     print(i)
    
# a = int(input("type any no. :"))
# for i in range(1,a+1):
#     print((i*2)-1)

# a = int(input("type any no. :"))
# for i in range(0,a+1,2):
#     print(i+1)

# a = int(input("type any no. :"))                
# i =1
# while i<=a:
#     print((i*2)-1)
#     i+=1

# a = int(input("type any no. :"))
# i =1
# while i<=a:
#     print(i)
#     i+=2

# a = int(input("type any no. :"))
# for i in range(0,a,2):
#     print(i)

# n = int(input("type anny no. :"))                         #q4
# sum = 0
# i = 1
# while i<=n:
#     sum += i
#     i+=1
# print(f"the sum of first {n} number is {sum}")


# sum=0                                                             #q4
# a= int(input("type any no :"))
# for i in range(1,a+1):
#     sum+=i
# print(sum)

# num= int(input("type any no. :"))
# rev=0
# while num>0 :
#     b= num%10
#     rev=rev*10+b
#     num= num//10
# print(rev)

# num= int(input("type any no. :"))
# rev= 0
# i=1
# for i in str(num):
#     i=num%10
#     rev=rev*10+i
#     num=num//10
#     print(type(num))
# print(rev)
# print(type(num))

# num= (input("type any no. :"))
# rev=""

# for digit in num:
#     rev= digit+rev
#     print(rev)

# num= int(input("type number"))           #q6        
# a,b=0,1
# count=0
# while count<num:
#     print(a,end =" ")
#     next_term=a+b
#     a=b
#     b=next_term
#     count+=1
      
# num= int(input("type number"))
# a,b=0,1
# for i in range(num):
#     print(a,end =" ")
#     next_term=a+b
#     a=b
#     b=next_term

# a=int(input("type any no. :"))
# b=int(input("type any no. :"))
# for i in range(a,b+1):
#     print(a)
#     if (a%a==0):
#         print(a)
#     else:
#         print(" ") 
#     a+=1
# i=1
# a=int(input("type no"))
# for i in range(1,a):
#     if ==1:
#         print(i)

#     else :
#         print("")
#     i+=1


# num= int(input("type any no. :"))
# digitSum= 0

# while num>0:
#     digit=num%10
#     digitSum+=digit
#     num=num//10
    
# print(digitSum)

# num =int(input("type any no. :"))         
# digit_sum=0
# for i in str(num):
#     i=int(num)%10
#     digit_sum+=i
#     num=num//10
# print(digit_sum)




# for i in range(0,102,2):                 
#     sum = 0
#     z = 1
#     while z>=i:
#         sum += i
#         z+=1
# print(f"the sum of first even number is {sum}")

# sum=0
# for i in range(0,101,2):
#     sum+=i
# print(f"sum of first 100 no is{sum}")

# a=int(input("type start no.: "))
# b=int(input("type end no.: "))
# print(f"prime no between({a},{b}) are ")
# for num in range(a,b+1):
#     if num>1:
#         for i in range(2,num):
#             if num%i == 0 :
#                 break
#         else:
#             print(num)
            
# to check palindrom no.

# num= (input("type any no. :"))
# rev= ""

# for digit in num:
#     rev= digit+rev
# if rev==num:
#     print(  num , "is palindrome")
# else:
#     print("not a palindrome")

# num = (input("type any no. :"))
# a= num
# rev= ""
# for digit in num:
#     rev= digit+rev
#     i*i*i==sum
#     sum+=rev
#     if rev>0:
        
#         print("it is armstrong")

# num = int(input("type any no. :"))
# original= num
# sum=0
# digits=len(str(num))
# while num>0:
#     digit= num%10

#     sum+=digit**digits
#     num=num//10
# if sum==original:
#     print(f"{original} is armstrong")
# else:
#     print("not")

num = int(input("type any no. :"))
original= num
sum=0
digits=len(str(num))
for i in str(num):
    digit= num%10
    sum+=digit**digits
    num=num//10
if sum==original:
    print(f"{original} is armstrong")
else:
    print("not")