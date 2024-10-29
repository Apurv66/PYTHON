choice = int(input("enter your choice(1-7): "))
day = ""
match(choice):
    case 1:
        day="monday"
    case 2:
        day="tuesday"
    case 3:
        day="wednesday"
    case 4:
        day="thursday"
    case 5:
        day="friday"
    case 6:
        day="saturday"
    case 7:
        day="sunday"
    case _:
        day="invalid day"

print(day)