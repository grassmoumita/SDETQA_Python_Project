#Eg 1
#Create class and method

# class Myclass:
#     def myfunc(self):      #method, default aurgument self when create a method in a class
#         pass
#     def display(self):
#         print("John")
#     def display1(self,name):
#         print(name)
#
# mc1=Myclass()      #creating objects of the class Myclass
# mc2=Myclass()      #creating another object of the class Myclass
#
# mc1.myfunc()     #calling methods for object mc1
# mc1.display()     #John
# mc1.display1("moumita")     #moumita


#Eg 2
# class Myclass:
#     def m1(self):
#         print("this is instance method")
#     @staticmethod
#     def m2(self,number):      #for static method the self is a parameter, so when call this need to pass the self parameter
#         print(self,number)
#
# mc1=Myclass()
# mc1.m1()
# mc1.m2(100,200)     #100 200   calling instance method, instance method only call by object
# Myclass.m2(10,20)    #10 20  calling static method with class, static method call be called with object and class also


#Eg 3
# class Myclass:
#     a,b=10,20    #class variables
#     def add(self):
#         print(self.a+self.b)    #when using class variable need to give self.a like this
#     def multi(self):
#         print(self.a*self.b)
#
# mc=Myclass()
# mc.add()     #30
# mc.multi()    #200


#Eg 4
# i,j=15,25     #global variable
# class Myclass:
#     a,b=10,20       #class variables
#     def add(self,x,y):      #x,y are local variable
#        print(x+y)          #accesing local var
#        print(self.a+self.b)       #accesing class var
#        print(i+j)           #accessing global var
#
# mc=Myclass()
# mc.add(100,200)


#Eg 5
# a,b=15,25     #global variable
# class Myclass:
#     a,b=10,20       #class variables same name as global var name
#     def add(self,a,b):      #x,y are local variable
#        print(a+b)          #accesing local var
#        print(self.a+self.b)       #accesing class var
#        #print(a+b)           #accessing global var,but it will take as local var as the name is same
#        print(globals()['a']+globals()['b'])   #when global var name is same with local then we have to use globals() functtion to access the global var in the method
#
# mc=Myclass()
# mc.add(100,200)


#Eg 6: One class have multiple objects
# class Myclass:
#     def display(self,name):
#         print("this is a display method")
#         print(name)
#
# obj1=Myclass()
# obj1.display("john")
#
# obj2=Myclass()
# obj2.display("mou")


#Eg 7 : Constructor example
# class Myclass:
#     def __init__(self):           #creating constructor
#         print("this is constructor")     #__init__ Constructor does not return any value
#     def n1(self):
#         print("hello")
#     def m2(self,x,y):
#         return (x+y)     #returning the value, so need to print it when calling the method with object
#
# mc=Myclass()    #this is constructor    invoked constructor automatically/by default constructor will call when we making a object
# mc.n1()        #hello  we have to call explicitly methods
# result = mc.m2(10,20)
# print(result)


#Eg 8:
# class Myclass:
#     name="John"
#     def __init__(self,name):     #Constructor exception one argument
#         print(name)
#         print(self.name)     #accesing the class variable with self.name
#
# obj=Myclass("David")    #passing parameter for constructor


#Eg 9
# class Emp:
#     def __init__(self,eid,ename,sal):
#         self.eid=eid       #we are converting the local constructor variable into class variable, because class variabke we can use also in other methods
#         self.ename=ename
#         self.sal=sal
#     def display(self):
#         print(self.eid,self.ename,self.sal)
#
# obj1=Emp(101,"John",50000)      #passing the constructor parameter
# obj1.display()      #calling the instance method
#
# obj2=Emp(102,"Mou",51000)
# obj2.display()

#Eg 10
class Emp:
    def __init__(self,eid,ename,sal):
        self.eid=eid
        self.ename=ename
        self.sal=sal
    def __str__(self):     #__str__ is another constructor which will only return only string values
        return (self.ename)

obj1=Emp(101,"John",50000)      #passing the constructor parameter
print(obj1)   #John only print this because __str__ will print only string

