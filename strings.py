str1 = 'hello'
print(str1)

#multi line string.
str2 = '''\nhi,
how are you.
i am fine.
'''
print(str2)

#repetition operator(*).
print(str1*3)

str3 = 'mango'
#concatination operator(+).
print(str1+str3)

#indexing of strings.
print(str1[0])
print(str1[1])
print(str1[2])
print(str1[3])
print(str1[4])
#indexing in minus.
print(str1[-1])

#string slicing.
print(str1[1:5])
print(str1[2:])
print(str1[:4])
print(str1[-5:-2])

#reverse a string.
print(str1[::-1])

#'in' and 'not in' is known membership operator. 
print("h" in str1)
print("x" in str1)
print("h" not in str1)
print("x" not in str1)

