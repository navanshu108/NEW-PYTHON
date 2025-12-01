# MyTuple=("apple", "banana", "cherry")
# print(type(MyTuple))

# #single touple
# mtuple=("navanshu",)
# print(type(mtuple))

# thisSet=set(("appla","banana","cherry","cherry","cherry"))
# print(thisSet)

# print(len(thisSet))
# [print(x) for x in thisSet]
# for x in thisSet:
#     print(x)
    
#check if item is in touple
# thisSet=("apple", "banana", "cherry")
# print("cherry"in thisSet)


##accessing items
# indexing(positive)
# thisTuple=("apple","banana","cherry")
# print(thisTuple[1])

# #indexing(negative)
# print(thisTuple[-1])

# #range of indexes(slicing)
# t=("a","b","c","d","e","f","g")
# print(t[2:5])

# #range of negative indexes
# t=("a","b","c","d","e","f","g")
# print(t[-5:-2])

# #check item exists
# t=("a","b","c","d","e","f","g")
# print("b" in t)



# #####updating touple
# #1. touple to list
# t=("a","b","c","d","e","f","g")
# l=list(t)
# l[2]="navanshu"
# t=tuple(l)
# print(t)

# #2. add item method 1
# t=("a","b","c","d","e","f","g")
# l=list(t)
# l.append("navanshu")
# t=tuple(l)
# print(t)
#    ##method 2 concatination
# t=("a","b","c","d","e","f","g")
# t+=("navanshu",)
# print(t)

#3. remove item
# fruit=("apple","banana","cherry","orange")
# l=list(fruit)
# l.remove("banana")
# fruit=tuple(l)
# print(fruit)

# fruit=("apple","banana","cherry","orange")
# del fruit
# print(fruit)
# print(fruit) #this will raise an error because the tuple no longer exists

# #unpacking touple
# fruit=("apple","banana","cherry")
# (green,yellow,red)=fruit
# print(green)
# print(yellow)
# print(red)

# # #using asterisk*
# #at last variable
# fruit=("apple","banana","cherry","strawberry","raspberry")
# (green,yellow,*red)=fruit
# print(green)
# print(yellow)
# print(red)

# #at start variable
# fruit=("apple","banana","cherry","strawberry","raspberry")
# (*green,yellow,red)=fruit
# print(green)
# print(yellow)
# print(red)
# #in middle variable
# fruit=("apple","banana","cherry","strawberry","raspberry")
# (green,*yellow,red)=fruit
# print(green)
# print(yellow)
# print(red)

# # #looping touple(iteration)
# thistuple=("apple","banana","cherry")
# for x in thistuple:
#     print(x)

# # #looping touple using index
# thistuple=("apple","banana","cherry")
# length=len(thistuple)
# for i in range(length):
#     print(thistuple[i])
# # #using while loop
# thistuple=("apple","banana","cherry")
# i=0
# while i <len(thistuple):
#     print(thistuple)
#     i=i+1

# ####join and multiply
# tuple1=("a","b","c")
# tuple2=(1,2,3)
# tuple3=tuple1+tuple2
# print(tuple3)

# #multiply
# fruits=("apple","banana","cherry")
# mytuple=fruits*2
# print(mytuple)

# ###built in methods
# # 1.count
# thisTuple=(1,2,3,4,5,7,7,7,7,5,5,6)
# count_seven=thisTuple.count(7)
# print(count_seven)
# #index method
# thistuple=("apple","banana","cherry","banana")
# position=thistuple.index("banana")
# print(position)
# ##only shows index of 1st banana
# count_banana=thistuple.count("banana")
# print(count_banana)

    
