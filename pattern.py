# rows=int(input("no of rows"))
# # columns=int(input("no of columns"))
# for i in range(rows):
#     for j in range(rows):
#         print("*" ,end ="  " )
#     print()

# side=int(input("side"))


# # for i in range(1,side +1):
#       for j in range(i):
#           print("*",end=" ")
        
#     print()
                    
# *
# * *
# * * *
# * * * *
# * * * * *
#     
# n=int(input("side"))


# for i in range(1,n+1):
#     print(" "*(n-i),end=" ")
#     print("*"*(2*i-1))

# #      *
#     ***
#    *****
#   *******
#  *********

#  n=int(input("side"))


# for i in range(n,0,-1):
#     print(" "*(n-i),end=" ")
#     print("*"*(2*i-1))

#  *********
#   *******
#    *****
#     ***
#      *


# n=int(input("enter no."))
# for i in range(1,n+1):
#     print(" "*(n-i),end=" ")
#     print("*"*i)
#      *
#     **
#    ***
#   ****
#  *****


# a=int(input("enter"))

# for i in range(1,a+1):
#     for j in range(i):
#         print(i,end=" ")
        
#     print()

# 1 
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# n=int(input("enter"))

# for i in range(n,0,-1):
#     for j in range(i):
#         print(i,end=" ")
        
#     print()




# n=int(input("enter no  of rows"))

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
        
#     print()

# 1 
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# n=int(input("enter"))

# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
        
#     print()

# 1 2 3 4 5 
# 1 2 3 4
# 1 2 3
# 1 2
# 1

# n=int(input("enter"))

# for i in range(1,n+1):
#     for j in range(65,65+i):
#         print(chr(j),end=" ")
        
#     print()

# A 
# A B
# A B C
# A B C D
# A B C D E

# n=int(input("enter"))

# for i in range(n,0,-1):
#     for j in range(65,65+i):
#         print(chr(j),end=" ")
        
#     print()

# A B C D E 
# A B C D
# A B C
# A B
# A

# n= int(input("type no of rows"))
# num=1
# for i in range(1,n+1):
    
#     for j in range(1,i+1):
#         print(num,end="  ")
#         num= num+1
#     print()


# a= int(input("type no of rows"))
# for i in range(1,a+1):
#     m= "*"*(i)
#     n= " "*(2*(a-i))
#     o= "*"*(i)
#     print(m+n+o)

# for i in range(a,0,-1):
#     m= "*"*(i)
#     n= " "*(2*(a-i))
#     o= "*"*(i)
#     print(m+n+o)
# n=5

# for i in range(1,n+1):
#     if i==1 or i==n:
#         print('*'*n)
#     else:
#         print("*"+" "*(n-2)+"*")
# *****
# *   *
# *   *
# *****

# n= 5
# for i in range(1,n+1):
#     print(" "*(n-i),end=" ")
#     if i==n:
        
#         print("*"*(2*i-1))
#     elif i==1:
#         print("*")
#     else:
#         print("*"+" "*(2*i-3)+"*")
#      *
#     * *
#    *   *
#   *     *
#  *********

# n= 5
# for i in range(n,0,-1):
#     print(" "*(n-i),end=" ")
#     if i==n:
        
#         print("*"*(2*i-1))
#     elif i==1:
#         print("*")
#     else:
#         print("*"+" "*(2*i-3)+"*")

#  *********
#   *     *
#    *   *
#     * *
#      *

# n=5
# for i in range(1,n+1):
#     print(" "*(n-i), end=" ")    
#     if i==1:
#         print("*")
#     else:
#         print("*"+" "*(2*i-3)+"*")
# for i in range(n,0,-1):
#     print(" "*(n-i), end=" ")    
#     if i==1:
#         print("*")
#     else:
#         print("*"+" "*(2*i-3)+"*")

#      *
#     * *
#    *   *
#   *     *
#  *       *
#  *       *
#   *     *
#    *   *
#     * *
#      *

n= 15
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==i or j==n-i+1 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

