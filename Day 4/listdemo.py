#how to create list

# mylist1=[10,20,30,40,50]
# mylist2=["apple","banana","orange","berry"]
# mylist3=["apple",10,"banana",20]
# mylist=list() # empty list
#
# print(mylist1)
# print(mylist2)
# print(mylist3)
# print(mylist)


#How to access items from list

# mylist1=[10,20,30,40,50]
# mylist2=["apple","banana","orange","berry"]
# print(mylist2[0])  #1st value
# print(mylist2[2])
# print(mylist2[-1])    #-1 means last value of list


#Range of Indexes

# mylist1=[10,20,30,40,50]
# mylist2=["apple","banana","orange","berry","mango","cherry","guava"]
# print(mylist2[2:5])
# print(mylist2[-4:-1])   #['berry', 'mango', 'cherry']


#How to change items/values in List
# mylist1=[10,20,30,40,50]
# mylist2=["apple","banana","orange","berry","mango","cherry","guava"]
#
# mylist2[0]="kiwi"
# print(mylist2)  #['kiwi', 'banana', 'orange', 'berry', 'mango', 'cherry', 'guava']


#Loop in list
# mylist1=[10,20,30,40,50]
# mylist2=["apple","banana","orange","berry","mango","cherry","guava"]
#
# for i in mylist2:
#     print(i)


#Check if the item is in the List or not
# mylist1=[10,20,30,40,50]
# mylist2=["apple","banana","orange","berry","mango","cherry","guava"]
#
# if "lemon" in mylist2:
#     print("yes apple is present")
# else:
#     print("No")


#List length
# mylist1=[10,20,30,40,50]
# mylist2=["apple","banana","orange","berry","mango","cherry","guava"]
#
# print(len(mylist2))     #7


#Add new item in list
#append()  or  #insert()
# mylist1=[10,20,30,40,50]
# mylist2=["apple","banana","orange","berry","mango","cherry","guava"]
#
# # mylist2.append("lemon")   #for append new item will add at end of list
# print(mylist2)
#
# mylist2.insert(1,"litchi")    #with Insert we can insert in any index of list
# print(mylist2)


#Remove item from list  pop() or del  or clear
# mylist1=[10,20,30,40,50]
# mylist2=["apple","banana","orange","berry","mango","cherry","guava"]
# # mylist2.pop(0)     #For pop() need to specify the index
# # print(mylist2)
#
# # del mylist2[2]    # del keyword is only accept index
# print(mylist2)
#
# mylist2.clear()    #clear all the items
# print(mylist2)


#Copy List   list() func or Copy() func
# mylist1=[10,20,30,40,50]
# mylist2=["apple","banana","orange","berry","mango","cherry","guava"]
# # mylist1=list(mylist2)   #using list func
# mylist1=mylist2.copy()    #using copy func
# print(mylist1)
# # print(mylist2)


#Combine or Join List
#using + operator
# mylist1=[10,20,30,40,50]
# mylist2=["apple","banana","orange","berry","mango","cherry","guava"]
# mylist3=mylist1+mylist2
# print(mylist3)      #[10, 20, 30, 40, 50, 'apple', 'banana', 'orange', 'berry', 'mango', 'cherry', 'guava']

#using loop statement
# for i in mylist2:
#     mylist1.append(i)
# print(mylist1)   #[10, 20, 30, 40, 50, 'apple', 'banana', 'orange', 'berry', 'mango', 'cherry', 'guava']

#Using extend() func
# mylist1.extend(mylist2)
# print(mylist1)    #[10, 20, 30, 40, 50, 'apple', 'banana', 'orange', 'berry', 'mango', 'cherry', 'guava']


