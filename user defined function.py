def ismax(a,b):
    if a>b:
        return a
    else:
        return b
    
a = int(input("enter a: "))
b = int(input("enter b: "))

answer =  ismax(a,b)
print("maximum = ",answer)
