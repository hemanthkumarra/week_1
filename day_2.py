# # name=input("What's your name?\n")
# # length=len(name)
# # print("length of your name: "+ str(length))
# #
# # print(f"length od the name : {length}")
#
# print(type(6/2))
# print(type(6//2))

print("Welcome to the tip calculator!")
bill=int(input("what was the total bill?"))
tip=int(input("how much tip would you like to give? 10 12 15\n"))
t=bill*(1+(tip/100))
n=int(input("how many people to split the bill?"))
div=(t/n)
print(f"total of {t} Each person should pay: ${div}")