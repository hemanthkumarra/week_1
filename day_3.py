print("Welcome to roller coaster ride.")
hight=int(input("what is your hight?"))
if hight>=120:
    bill=0
    age=int(input("How old are you?"))
    if age<=12:
        bill=7
    elif age<=18:
        bill=10
    else:
        bill=15
    want_photo=input("do you want a photo ?yes or no")
    if want_photo=="yes":
        bill+=3
    print("your total bill is",bill)
else:
    print("sorry you can't go")
