#Eg 1: writing data in a text file

# file = open("C:\demofiles\myfile.txt",'w')
# file.write("This is my 1st statement..\n")
# file.write("This is my 2nd statement\n")
# file.write("This is my 3rd statement\n")
# file.write("This is my 4th statement\n")
# file.close()
# print("program completed")


#Eg 2: Reading data from text file
# file = open("C:\demofiles\myfile.txt",'r')
# # print(file.read())    #print all the data
# print(file.readline())    #print 1st line only
# file.close()


#Eg 3: Appending data into text file
# file = open("C:\demofiles\myfile.txt",'a')
# file.write("This is my 5th statement..\n")
# file.write("This is my 6th statement..\n")
# file.write("This is my 7th statement..\n")
# file.close()
# print("program complete")


# x = 5
# while x > 0:
#     print(x, end=" ")
#     x -= 2
#     if x == 1:
#         break
# else:
#     print("Done")

# for i in range(5):
#     if i == 2:
#         continue
#     print(i, end=" ")

# num = 0
# while num < 5:
#     print(num)
#     num += 1
# else:
#     print("Loop completed.")
#
# for i in range(3):
#     for j in range(3):
#         print(i * j, end=' ')
#     print()

# for i in range(3):
#     pass
# print(i)

# for i in range(1, 6):
#     if i % 2 == 0:
#         print(i)
#         continue
#     print("*")

for i in range(1, 6):
    if i == 3:
        break
    print(i)
else:
    print("Loop completed.")