##creation
# thisset={"apple", "banana", "cherry"}
# print(type(thisset))
# 
# #using constructer
# thisset=set(("apple", "banana", "cherry"))
#
##duplicate equivalence
# True and 1 ,0 and False are same thing 
# set= {"sbc",35,True,40,1,False,0}
# print(set)
####output---{False, True, 35, 40, 'sbc'}



###acess and immutability
# #looping(iteration)
# thisset={'apple','banana','cherry'}
# for x in thisset:
#     print(x)
# #checking presence
# thisset={'apple','banana','cherry'}
# print("banana" in thisset)
# print("grape" not in thisset)

# # # add item to set
# Myset={"apple", "banana", "cherry"}
# Myset.add("orange")
# print(Myset)

# #adding multiple items to set          ##we can add list tuple or set by this method
# Myset={"apple", "banana", "cherry"}
# fruit=("orange","mango","grapes")
# Myset.update(fruit)
# print(Myset)


# #####removing a specific item
# mySet = {"apple","banana","cherry"}               ##shows error if item not present
# mySet.remove("apple")
# print(mySet)

#using discard
# Myset={"apple","banana","cherry"}                 ##shows no error
# Myset.discard("banana")
# print(Myset)


 #remove arbitrary (random) item
# Myset={"apple","banana","cherry"}
# Myset.pop()
# print(Myset)

######clearing and deleting the set
# thisset={"apple","banana"}
# thisset.clear()
# print(thisset)

# thisset={"apple","banana"}            
# del thisset
# print(thisset)                ##this will show error bec set is removed completely



###### looping iteration
# thisset={'apple','banana','cherry'}
# for x in thisset:
#     print(x)

########python set join and set operations#########
# set1={"a","b"}              ##union
# set2={1,2}
# set3=set1.union(set2)
# print(set3)

set1={'a'}
set1.update({1,2})               ##update
print(set1)

##finding common items(intersection)
# set1={"apple","banana"} 
# set2={"apple","banana",'orange'} 
# set3=set1.intersection(set2)    
# print(set3)                             #{'banana', 'apple'}

# ##finding difference
# # A
# set1={"apple","banana","mango"} 
# set2={"apple","banana",'orange'}
# set3=set1.difference(set2)                  #mango
# print(set3)
# # B symmetric difference (exclusive OR)
# set1={"apple","banana","mango"} 
# set2={"apple","banana",'orange'}
# set3=set1.symmetric_difference(set2)        #{'orange', 'mango'}
# print(set3)

####frozen set
# creation
# x=frozenset({"apple","banana","mango"})
# print(type(x))      ##<class 'frozenset'>

####frozenset is immutable so add,remove,update does not work in it
set1={"apple","banana","mango"} 
set2={"apple","banana",'orange'}
# set3=set1.copy()
# print(set3)

# set3=set1&set2          ##intersection
# print(set3)

# set3=set1|set2          ##union
# print(set3)

# set3=set1-set2          ##difference
# print(set3)   

# set3=set1^set2          ##symmetric difference
# print(set3)

# set3=set1.intersection_update(set2)   ##intersection update
# print(set1)

# set3=set1.difference_update(set2)     ##difference update
# print(set1)
# # print(set3)

# set3=set1.symmetric_difference_update(set2)   ##symmetric difference update
# print(set1)
# print(set3)
# set3=set1.union(set2)                  ##union update
# print(set1)
# print(set3)

# set3=set1.isdisjoint(set2)            ##is disjoint
# print(set3)

# set3=set1.issubset(set2)              ##is subset
# print(set3)

# set3=set1.issuperset(set2)            ##is superset
# print(set3)

# set3=set1.pop()                       ##pop
# print(set1)