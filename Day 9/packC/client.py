import sys
sys.path.append("C:/Users/moumitajoardar/PycharmProjects/pythontraining/pythonProject1/Day 9/packA")
sys.path.append("C:/Users/moumitajoardar/PycharmProjects/pythontraining/pythonProject1/Day 9/packB")


#Approach 1
# import emp
# empobj=emp.Employee(101,"John",50000)
# empobj.display()
#
# import stu
# stuobj=stu.Student(100,"Moumita",3)
# stuobj.display()


#Approach 2
from emp import Employee
empobj=Employee(101,"John",50000)
empobj.display()

from stu import Student
stuobj=Student(100,"Moumita",3)
stuobj.display()