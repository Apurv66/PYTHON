a = int(input("enter a: "))
b = int(input("enter b: "))
c = int(input("enter c: "))
max = 0

if(a>b):
    if(a>c):
        max = a
    else:
        max = c
else:
    if(b>c):
        max = b
    else:
        max = c

print("maximum: ",max)