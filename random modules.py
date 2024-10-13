import random

a = random.random()
print("give random number between 0 and 1: ",a)

b = random.randint(1,10)
print("give random number between 1 to 10(including 1 and 10): ",b)

c = random.randrange(1,10)
print("give random number between 1 to 10(including 1 but not include 10): ",c)

li = [11,22,'hello',5.4]
d = random.choice(li)
print("give random element from list: ",d)

random.shuffle(li)
print("shuffle the list: ",li)

e = random.uniform(5,7)
print("give random float number between 5 to 7: ",e)