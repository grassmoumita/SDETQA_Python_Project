#Create a dict
# mydict={101:"x",102:"y",103:"z"}
# print(mydict)

#Access items of a dict
# mydict={
#     "brand":"Hyundai",
#     "model":"110",
#     "year":2024
# }
# print(mydict["brand"])    #Hyundai
# print(mydict["model"])    #110
#
# #Using Get() func can access item
# x=mydict.get("brand")
# print(x)    #Hyundai

#Change values in dict
# mydict={
#     "brand":"Hyundai",
#     "model":"110",
#     "year":2024
# }
# mydict["year"]=2023
# print(mydict)   #{'brand': 'Hyundai', 'model': '110', 'year': 2023}


#Access items using loop from dict
# mydict={
#     "brand":"Hyundai",
#     "model":"110",
#     "year":2024
# }
# for i in mydict:
#     print(i)    #print only the key
#
# for i in mydict:
#     print(mydict[i])    #print only the values
#
# for i in mydict.values():
#     print(i)        #print only the values
#
# for x,y in mydict.items():
#     print(x,y)       #print keys with values


#Check key is exist in dict or not
# mydict={
#     "brand":"Hyundai",
#     "model":"110",
#     "year":2024
# }
# if "model1" in mydict:
#     print("exist")
# else:
#     print("not exist")


#Find number of items in dict

# mydict={
#     "brand":"Hyundai",
#     "model":"110",
#     "year":2024
# }
# print(len(mydict))   #3

#Adding items to dict
# mydict={
#     "brand":"Hyundai",
#     "model":"110",
#     "year":2024
# }
# mydict["color"]="blue"
# print(mydict)   # {'brand': 'Hyundai', 'model': '110', 'year': 2024, 'color': 'blue'}


#Remove items from dict
# mydict={
#     "brand":"Hyundai",
#     "model":"110",
#     "year":2024
# }
# mydict.pop("year")
# print(mydict)     #{'brand': 'Hyundai', 'model': '110'}

# del mydict["year"]
# print(mydict)      #{'brand': 'Hyundai', 'model': '110'}

# del mydict    #fully delete the dictionary
# print(mydict)    #NameError: name 'mydict' is not defined. Did you mean: 'dict'?

# mydict.clear()    #to clear the keys and values
# print(mydict)     #{}


#Copying Dict
mydict={
    "brand":"Hyundai",
    "model":"110",
    "year":2024
}
# mydict2=mydict    #first approach
# print(mydict2)    #{'brand': 'Hyundai', 'model': '110', 'year': 2024}

#using Copy() func
mydict2=mydict.copy()
print(mydict2)      #{'brand': 'Hyundai', 'model': '110', 'year': 2024}

