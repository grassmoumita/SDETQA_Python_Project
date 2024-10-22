#Eg 1 : Single Inheritence
# class A:
#     def m1(self):
#         print("this is m1 method for class A")
#
# class B(A):       # Single Inheritence : B is now child of class A, A is parent now
#     def m2(self):
#         print("this is m2 method for class B")
#
# bobj=B()
# bobj.m2()
# bobj.m1()     # can access of Class A method also, as B is child of A, and the object is class B


#Eg 2: Single Inheritence
# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A):
#     a,b=100,200
#     def m2(self):
#         print(self.b-self.a)
#
# bobj=B()
# bobj.m1()
# bobj.m2()


#Eg 3: Multilevel Inheritence
# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A):
#     a,b=100,200
#     def m2(self):
#         print(self.b-self.a)
#
# class C(B):
#     i,j=5,2
#     def m3(self):
#         print(self.i*self.j)
#
# cobj=C()
# cobj.m1()
# cobj.m2()
# cobj.m3()


#Eg 4: Heirarchy Inheritence
# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A):      # B is a child of A
#     a,b=100,200
#     def m2(self):
#         print(self.b-self.a)
#
# class C(A):    #C is also child of A
#     i,j=5,2
#     def m3(self):
#         print(self.i*self.j)
#
# bobj=B()
# bobj.m1()
# bobj.m2()
#
# cobj=C()
# cobj.m1()
# cobj.m3()


#Eg 5: Multiple Inheritence
# class A:    # A is a parent
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B:      # B is a parent
#     a,b=100,200
#     def m2(self):
#         print(self.b-self.a)
#
# class C(A,B):    #C is a child of A and child of B, multiple parent and one child
#     i,j=5,2
#     def m3(self):
#         print(self.i*self.j)
#
# cobj=C()
# cobj.m1()
# cobj.m2()
# cobj.m3()


#Eg 6 - Overridding methods
# class A:
#     def m1(self):
#         print("This is m1 method from class A")
#
# class B(A):
#     def m1(self):      #Over-ridding - same method again in the child class
#         print("This is m1 method from class B")
#         super().m1()       #Using super invoking for parent class parent method
#
# bobj=B()
# bobj.m1()    #This is m1 method from class B
#
#
# #Eg 7
# class A:
#     a,b=10,20
#
# class B(A):
#     i,j=100,200
#     def m(self,x,y):
#         print(x+y)
#         print(self.i + self.j)
#         print(self.a+self.b)     #taking class variable of class A, as B is a child of A
#
# bobj=B()
# bobj.m(1000,2000)


#Eg 8
# class Parent:
#     name="Moumita"
#
# class Child(Parent):
#     name = "John"
#     def test(self):
#         print(super().name)
#
# obj=Child()
# print(obj.name)    #John, after override John will print as name
# obj.test()


#Eg 9: Override methods
# class Bank:
#     def rateOfInterest(self):
#         return 0
#
# class xBank(Bank):
#     def rateOfInterest(self):
#         return 10
#
# class YBank(Bank):
#     def rateOfInterest(self):
#         return 12
#
# xobj=xBank()
# print(xobj.rateOfInterest())
#
# yobj=YBank()
# print(yobj.rateOfInterest())


#Eg 10 : Overloading Concept

class Human:
    def sayhello(self,name=None):
        if name is not None:
            print("hello" + name)
        else:
            print("hello")

h=Human()
h.sayhello("Moumita")
h.sayhello()

#Eg 11: overloading 2
class Calculation:
    def add(self,a=0,b=0,c=0):
        print(a+b+c)

obj=Calculation()
obj.add()     #0
obj.add(10,20)    #30
obj.add(100,200,300)     #600
