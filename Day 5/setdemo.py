#creating a Set

# myset={"apple","banana","cherry"}
# print(myset)   #{'banana', 'apple', 'cherry'}, Set is unindexed and unordered

#Accessing items from Set
# myset={"apple","banana","cherry"}
# for i in myset:
#     print(i)


#To check a value in Set or not
# myset={"apple","banana","cherry"}
# print("banana" in myset)   #True

#Add a new item in Set with 2 methods
#add() func  or  update()
#add() - for single item add at a time
# myset={"apple","banana","cherry"}
# myset.add("orange")
# print(myset)   #{'apple', 'orange', 'banana', 'cherry'}

#update() for add multiple item at a time
# myset={"apple","banana","cherry"}
# myset.update(["mango","grapes"])
# print(myset)

#Length of a Set
# myset={"apple","banana","cherry"}
# print(len(myset))     #3

#Remove Items from Set  -remove() or discard() func can use
# myset={"apple","banana","cherry"}
# myset.remove("banana")
# print(myset)      #{'apple', 'cherry'}
# myset.remove("xyz")
# print(myset)      #KeyError: 'xyz', will throw error when remove a non eliment from a set

# myset.discard("banana")
# print(myset)    #{'apple', 'cherry'}
# myset.discard("xyz")    #do not give any error

#Clear all items from Set
# myset={"apple","banana","cherry"}
# myset.clear()
# print(myset)   #set()
#
# #to delete the set
# del myset
# print(myset)  #give error NameError: name 'myset' is not defined


#Joining 2 Sets   by Union() and update()
# set1={'a','b','c'}
# set2={1,2,3}
# set3=set1.union(set2)
# print(set3)      #{1, 'a', 2, 3, 'c', 'b'}

set1={'a','b','c'}
set2={1,2,3}
set1.update(set2)
print(set1)


