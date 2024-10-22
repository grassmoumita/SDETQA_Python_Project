# def creater():
#     i=1
#     while i<=20:
#         yield i      # yield means it will stop here, util we call the next
#         i +=1
# print(creater())
# x=creater()
# print(next(x))
# print(next(x))
# print(next(x))

# for m in creater():
#     # x=creater()
#     print("The next numbers are: ", m, next(x))


global x
# x=10
def output():
    x=10
    def inner():
        x = 20
        x += 5
        print("inner : ",x)
    inner()
    print("Out of inner func : ",x)

output()
# print("Out of Outer func : ",x)

