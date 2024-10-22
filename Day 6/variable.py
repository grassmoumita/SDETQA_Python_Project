#Eg 1
# global_var=20   #global variable
#
# def func():
#     local_var=10     #local variable
#     print(local_var)
#     print(global_var)
#
# func()
# # print(local_var)    #invalid because local_var is local variable of func()
# print(global_var)     #valid because global_var is global variable

#Eg 2
# xy=100
# def cool():
#     xy=200
#     print(xy)
# cool()    #200, will print the local variable


#Eg 3

# xy=100
# def cool():
#     global xy     #mentioning the global XY var here, it is not local XY
#     xy=200     #here XY become global variable, as before that we take global XY
#     print(xy)
# cool()


#Eg 4

# x=100
# def cool():
#     global x
#     x=500
#     print(x)
# cool()     #500
# print(x)    #500 global x value changed in the func


#Eg 5

def cool():
    global x    #taking X as global varibale without mentioning it globally
    x=100
    print(x)
cool()
print(x)