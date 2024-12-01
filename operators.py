# Arithmetic Operator
a = 12
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a // b)
print(a ** b)


# Assignment Operator
x = 5
x += 5 # x = x + 5
print(x)

x -= 5 # x = x - 5
print(x)

x *= 2  # x = x * 2
print(x)

x /= 5 # x = x / 5
print(x)


# Comparison Operator
x = 5
y = 8
print(x<y)
print(x>y)
print(x<=y)
print(x>=y)
print(x==y)
print(x!=y)


# Logical Operator
x = 5
y = 8
print(a<b and a>b)
print(a<b or a>b)
print(not(a<b and a>b))


# Bitwise Operator
x = 5
y = 6
# bitwise and :- 101 & 110 = 100 (100 is binary number of 4)
print(x & y)  
# bitwise or :- 101 | 110 = 111 (111 is binary number of 7)
print(x | y)  
# xor :- 101 ^ 110 = 011 (0 ^ 0 = 0 , 1 ^ 1 = 0 , 1 ^ 0 = 1 , 0 ^ 1 = 1)
# If both value same then return 0, but both value not same then return 1.
print(x ^ y)   
# bitwise not :- formula :-   -x -1
print(~x)
# right shift operator
print(x >> 2)
# left shift operator
print(x << 2)


# Identity Operator
x = 5
print(x is 5)
print(x is not 5)


# Membership Operator
a = [1, 2, 3, 4, 5]
print(3 in a)
print(3 not in a)