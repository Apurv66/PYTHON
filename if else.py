choice = int(input("enter your choice(1-7): "))
day=""

if(choice==1):
    day="monday"
elif(choice==2):
    day="tuesday"
elif(choice==3):
    day="wednesday"
elif(choice==4):
    day="thursday"
elif(choice==5):
    day="friday"
elif(choice==6):
    day="saturday"
elif(choice==7):
    day="sunday"
else:
    day="invalid day"

print(day)
