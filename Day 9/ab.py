#Approach 1 for importing classes
# import a
# import b
#
# obj=a.Animal()
# obj.display()
#
# obj1=b.Bird()
# obj1.display()

#Approach 2  using From
from a import Animal
from b import Bird

obj=Animal()
obj.display()

obj1=Bird()
obj1.display()