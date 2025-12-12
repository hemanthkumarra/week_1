# #string cancat
# print("hello"+" "+"world")
# name= input("what is your name?")
# print("hello "+name)
# length=len(name)
# print(length)

#pluse one
def addOne(n:list[int]):
    n=n[::-1]
    i=0
    while True:
        if i<len(n):
            if n[i]==9:
                n[i]=0
            else:
                n[i]+=1
                break
        else:
            n.append(1)
            break
        i+=1
    return n[::-1]
n=list(map(int,input("enter number digits with space:").split()))
print(addOne(n))