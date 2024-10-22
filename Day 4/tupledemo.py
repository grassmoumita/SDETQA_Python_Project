#creating tuple
# mytuple=("apple","banana","orange")
# print(mytuple)    #('apple', 'banana', 'orange')

#access tuple items
# mytuple=("apple","banana","orange")
# print(mytuple[1])   #banana
# print(mytuple[-1])    #-1 means last item, orange

#Range of indexes
# mytuple=('apple', 'banana', 'orange', 'berry', 'mango', 'cherry', 'guava')
# print(mytuple[2:5])   #('orange', 'berry', 'mango')
# print(mytuple[-4:-1])     #('berry', 'mango', 'cherry')


#Change in Tuple items/values
#by default cannot do modify,append,insert,remove from a tuple
#indirect process to change in Tuple -> make the tuple in list, modify the list, again make the list into tuple
# mytuple=('apple', 'banana', 'orange', 'berry', 'mango', 'cherry', 'guava')
# mylist=list(mytuple)
# mylist[0]="litchi"
# mytuple=tuple(mylist)
# print(mytuple)      #print the modified tuple ('litchi', 'banana', 'orange', 'berry', 'mango', 'cherry', 'guava')


#Reading tuple items using loop
# mytuple=('apple', 'banana', 'orange', 'berry', 'mango', 'cherry', 'guava')
# for i in mytuple:
#     print(i)


#Check if the item exist in tuple
# mytuple=('apple', 'banana', 'orange', 'berry', 'mango', 'cherry', 'guava')
# if "adc" in mytuple:
#     print("yes")
#
# else:
#     print("no")

#Tuple length
# mytuple=('apple', 'banana', 'orange', 'berry', 'mango', 'cherry', 'guava')
# print(len(mytuple))   #7

#Add items to tuple ---> not possible
# mytuple=('apple', 'banana', 'orange', 'berry', 'mango', 'cherry', 'guava')
# mytuple[0]="litchi"
# print(mytuple)     #TypeError: 'tuple' object does not support item assignment


#Copy tuple
# mytuple=('apple', 'banana', 'orange', 'berry', 'mango', 'cherry', 'guava')
# mytuple1=mytuple
# print(mytuple1)    #('apple', 'banana', 'orange', 'berry', 'mango', 'cherry', 'guava')


#Join/Combine tuple
# mytuple=('apple', 'banana', 'orange', 'berry', 'mango', 'cherry', 'guava')
# mytuple1=(1,2,3)
# mytuple2=mytuple+mytuple1
# print(mytuple2)     #('apple', 'banana', 'orange', 'berry', 'mango', 'cherry', 'guava', 1, 2, 3)


#compare tuples
mytuple=('apple', 'banana', 'orange', 'berry', 'mango', 'cherry', 'guava')
mytuple1=('apple', 'banana', 'orange', 'berry', 'mango', 'cherry', 'guava')
if mytuple==mytuple1:
    print("equal")
else:
    print("Not equal")