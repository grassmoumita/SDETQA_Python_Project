#Eg 1
# def func(i,j):
#     print(i,j)
#
# # func(10,20)      #positional Argument
# func(j=20,i=10)      #Keyword Argument


#Eg 2      Positional Argument
# def func(i,j=10):
#     print(i,j)
#
# func(100,200)     #100 200, default value of j will update in 200
# func(100)             #100 10, default value of j will take as not passing any value for j


#Eg 3      Keyword Argument
# def func(name,greetmsg):
#     print(greetmsg+" "+name)
#
# func(name="John",greetmsg="hello")    #hello John


#Eg 4
# def my_func(a,b,c):
#     print(a,b,c)
#
# # my_func(10,20,30)      #positional argument
# # my_func(a=10,b=20,c=30)         #keyword argument
# my_func(10,20,c=30)       #10 20 30   combination of positional and keyword argument
# my_func(10,b=20,c=30)        #10 20 30
# # my_func(10,b=20,30)          #Error, positional arug must be before keyword argu in case of combination
# my_func(10,30,b=20)      #Incorrect because for b already taken 30

#Eg 5    function can return multiple values in tuples
def largest(a,b):
    if a>b:
        return a,b
    else:
        return b,a

# print(largest(100,200))
# print(largest(20,10))
res=largest(10,20)
print(res)    #(20, 10)   returning multiple values in tuple



