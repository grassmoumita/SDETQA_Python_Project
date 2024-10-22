#Eg 1

# print("this is starting point of program")
# print("this is starting point of program")
# print("this is starting point of program")
# print("this is starting point of program")
#
# try:
#     print(x)
# except:
#     print("Exception occured")
#
# print("this is end of program")
# print("this is end of program")
# print("this is end of program")
# print("this is end of program")


#Eg 2
# print("start program")
# print("program progress")
#
# try:
#     print(10 / 0)
# except ZeroDivisionError:
#     print("Exception occured")
#
# print("program complete")



#Eg 3 : Multiple except blocks  - try, except,else, finally

# try:
#     num1,num2=10,0
#     result=num1/num2
#     print("Result is",result)
# except ZeroDivisionError:
#     print("Thrown ZeroDivisionError exception....")
# except SyntaxError:
#     print("Thrown SyntaxError exception")
# except:
#     print("Exception handled")
# else:       #when any exception is matched then else will execute
#     print("no exception occured")
# finally:     #if exception is occured or not, Finally block will always execute
#     print("always execute")


#Eg 4 : Raising our own exceptions

def enterage(num):
    if num<0:
        raise ValueError("Only integers are allowed")
    if num%2==0:
        print("Even number")
    else:
        print("odd number")

# enterage(10)
# enterage(5)
# enterage(-1)

num=-1
try:
    enterage(num)
except ValueError:
    print("valueerror is occured and handled")



