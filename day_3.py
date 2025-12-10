# print("Welcome to roller coaster ride.")
# hight=int(input("what is your hight?"))
# if hight>=120:
#     bill=0
#     age=int(input("How old are you?"))
#     if age<=12:
#         bill=7
#     elif age<=18:
#         bill=10
#     else:
#         bill=15
#     want_photo=input("do you want a photo ?yes or no")
#     if want_photo=="yes":
#         bill+=3
#     print("your total bill is",bill)
# else:
#     print("sorry you can't go")
def Pizza():
    size=input("what size of pizza do you want?S, M OR L: ")
    bill=0
    if size == "S":
        bill=15
    elif size == "M":
        bill=20
    elif size == "L":
        bill=25
    else:
        print("please enter a valid size")
        return 0
    want_pepperoni=input("do you want pepperoni?Y or N: ")
    if want_pepperoni == "Y":
        if size == "S":
            bill+=2
        else:
            bill+=3
    want_cheese=input("do you want cheese?Y or N: ")
    if want_cheese == "Y":
        bill+=1
    return bill
print("Welcome to PizzaPY")
bill=Pizza()
print("total bill is:",bill)