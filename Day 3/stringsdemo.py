#create sring variable
#below 4 ways we can declare or create variable

# s="Welcome"
# s='Welcome'
# s=str("Welcome")
# s=str('Welcome')
#
# #creating empty string variable
# name=""
# name=''
# name=str()
#
# #mutable variable - cannot change the value of the variable
# #immutable variable - can change the value of the variable
# #string is immutable
# #if the value is changed after updation then it is immutable
#
#
# str1="welcome"
# # print(id(str1))  #output 2012483518208
#
# str1=str1+"to python"
# print(id(str1))   #output 2606325234224
#
#
# # + and * with string
#
# str1="welcome"
# print(str1+"programming")  #concatenation
#
# print(str1*3)  #output = welcomewelcomewelcome, print multiple times
#
# #slicing stings
#
# str1="welcome"  #index start from 0
# print(str1[1:3])  #output - el, 1 starting index, 3 ending index
# print(str1[:6])   #output - welcom, no starting index so will start from 0, 6 ending index
# print(str1[2:])   #output - lcome, 2 starting index, no ending index so will go till last
#
# print(str1[1:-1])   #output - elcom, starting index from 1, -1 means will not print last index
# print(str1[1:-2])   #output - elco, starting index from 1, -2 means will not print last two index
#
#
# #ord() and chr() in strings
#
# print(ord('A'))    #ascii code of A
# print(chr(65))     #character of any ascii number
#
# # max,min,len in string
# print(max('abc'))   #output c
# print(min('abc'))    #output a
# print(len('welcome'))   #output 7
#
#
# #not in operator in string
#
# s="welcome"
# print("come" in s)  #output true
# print("lose" in s)  #output false
#
# print("come" not in s)  #output false
# print("lose" not in s)  #output true
#
# #string comparison
# print('tim'=='tie')    #false
# print('free' != 'freedom')   #true

#testing strings  True/false

# s="welcome to python"
#
# print(s.isalnum())   #false
# print("welcome".isalpha())
# print("2012".isdigit())  #true
# print("first number".isidentifier())  #false
# print(s.islower())
# print(s.isupper())
# print(s.isspace())

#Searching for substrings  true/false

s="welcome to python"
print(s.endswith("thon"))   #true
print(s.startswith("py"))   #false
print(s.find("come"))    #output 3, starting position number
print(s.find("become"))    #output -1, when not found in string
print(s.count('t'))   #output 2, how many times 't' comes in the string



#converting string

s="String in PYTHON"
s1=s.capitalize()
print(s1)     #String in python, only the 1st letter will capital


#Reverse a string
#method 1:looping
s="welcome"
rev_s=""
for i in s:
    rev_s=i+rev_s
print(rev_s)   #emoclew

#method 2 : slicing
s="welcome"
rev_s=s[::-1]   #[start value:end value:increment/decreement]
print(rev_s)







