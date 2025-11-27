# # #list
# # my_list=["apple","banana","cherry"]
# # print(my_list)
# # fruits=["apple","banana","cherry"]
# # #properties of lists
# # # 1.ordered
# # print(fruits[0])
# # print(fruits[2])
# # #2 changeable(mutable)
# # my_list[1]="mango"
# # # 3 allow duplicates
# # fruit=["apple","banana","mango","apple"]
# # print(fruit)
# # #4 indexed means start from left 0---infinite
# #   # length of the list 
# #             #use len() function
# # print(len(fruits))
# # print(len(fruit))

# # a=[5,3,8,9,2,1,6]
# # a.sort()
# # print(a)


# #change by slicing multiple elements

# # fruit=["apple","banana","cherry"]

# # # print(fruit)

# # # fruit[-1]='mango'
# # # print(fruit)

# # # fruit[1:3]=['grapes','melon']
# # # print(fruit)

# # # fruit.insert(0,"kiwi")
# # # print(fruit)
# # # num=[10,20,3,40,50]
# # # num[2:3]=25 ,27
# # # print(num)
# # fruit[-2:]=["pear"]
# # print(fruit)

  
# #python add list items
# #using append()
# MyList=[1,5,6,8,44,9]
# MyList.append(5)
# print(MyList)
# #using insert(index,value)
# fruits=["apple","banana","cherry"]
# fruits.insert(0,"grapes")
# print(fruits)
# #using extend
# list1=[1,2,3]
# list2=[4,5,6]
# list1.extend(list2)
# print(list1)
# #using extend and insert
# list=[2,56,6,4,8,5,"ambt"]
# # list.insert(1,"abc")
# list.extend("abc")
# print(list)

# list0=['grapes', 'apple', 'banana', 'cherry','kiwi']
# list0.insert(5,"mango")
# print(list0)

# [print(x) for x in list0]

# matrix=[[1,2,3],[4,5,6]]
# flattened=[num for row in matrix for num in row]
# print(flattened)
  
###looping

##q1 page`33`

# fruit=['grapes', 'apple', 'banana', 'cherry']
# # [print(x,fruit[x]) for x in range(len(fruit)) ]
 
# for i in range(len(fruit)):
     
#     print(i, fruit[i])

# q2

# fruit=['grapes', 'apple', 'banana', 'cherry']
# [print(x.upper()) for x in fruit]
# for x in fruit:
#     print(x.upper())

#3

# list=['apple','banana','avocado','cherry','apricot']
# a=[]
# for x in list:
#     if x.startswith('a'):
#         a.append(x)
# print(a)

# #4

# num=[1,2,3,4,5,6,7,8]
# a=[]
# for i in num:
#     if i%2==0:
#         a.append(i)
# print(a)
    
# #5
# number= [10,20,30,40]
# sum=int()           # sum=0
# for x in number:
#     a=x
#     sum= a+sum
# print(sum)

# # # #6
# num=[1,2,3,4,52,5,7,6,41]
# num.sort()
# print(num[-1])

# a=max(num)
# print(num)
# print(max(num))

# #7
# list=['apple','banana','avocado','cherry','apricot']
# a=[]
# for x in list[-1::-1]:
#     print(x)
#     a.append(x)
# print(a)

#8
# list=['apple','banana','avocado','cherry','apricot']
# for index,list in enumerate(list):
#     print(index,list)

# #9
# number= [1,5,6,74,2,3,9,10]
# square=[]
# for x in number:
#     square.append(x*x)
    
# print(square)

# #10
# num=[1,2,3,4,52,5,7,6,41,54,6,4,22,2,6666,66,44,44,7,7,8,8,99,9999,99,8,505]
# for x in num:
#     if x>50:
#         print(x)
    

# #11

# [print(x) for x in range(1,10,2)]  #jugaad by me

# [print(x) for x in range(1,10) if x%2!=0]

# #12
# fruit=['grapes', 'apple', 'banana', 'cherry','apple','apple','apple']
# # print(fruit.count('apple'))
# count=0
# for i in fruit:   
#     if i=='apple':
#         count+=1
# print(count)
   

#13

# list=['apple','banana','avocado','cherry','apricot']
# for i in list[::2]:
#     print(i)

#14

# fruit=['apple','banana','avocado','cherry','apricot','kiwi']
# a=[]
# for x in fruit:
#     if len(x)>5:
        
#         a.append(x)
# print(a)

#15

# fruit=['apple','banana','avocado','cherry','apricot','kiwi']
# count=0
# for i in fruit:
#     count+=1
# print(count)





# # q1
# integers=[10,50,4,7,8,9,4,5,6,2,3,21,1]
# integers.sort()
# print(integers)
# integers.sort(reverse=True)
# print(integers)

##2
# fruit=['apple','banana','avocado','cherry','Apricot','Kiwi',"kiwi",'Apple']
# fruit.sort(key=str.upper)# also use str.lower
# print(fruit)

# #3
# num=[10,144,65959,55,822,6,633,4144,2,22,5474,653,548,10525,5000,150,]

    
# a=sorted(num,key= lambda x:x%10)
# print(a)

# #4
# fruit=['apple','banana','avocado','cherry','apricot','kiwi']
# a=sorted(fruit,key=len)  #a=sorted(fruit,key=lambda x:len(x))
# print(a)

#5
fruit=['apple','banana','avocado','cherry','apricot','kiwi']
a=[]
for x in fruit[len(fruit)::-1]:
    a.append(x)
print(a)

     