str1 = "HEllo"

print(len(str1))

print(str1.upper())
print(str1.lower())
print(str1.capitalize())

str2 = "****hello*****"
print(str2.lstrip("*"))
print(str2.rstrip("*"))
print(str2.strip("*"))

print(str1.replace("HEllo","john"))

print(str1.count('l'))

print(str1.startswith('H'))
print(str1.endswith('o'))

print(str1.find('l'))   #if string is not found then it is return -1.
print(str1.index('l'))  #if string is not found then it is trows an error.

print(str1.isalnum())   #alnum(alphanumeric) means a string which make with a-z, A-Z, 0-9.

str1 = 'hello'
print(str1.islower())
print(str1.isupper())

str1 = ' '
print(str1.isspace())

str1 = 'hello HELLO'
print(str1.swapcase())  #this method converts lowercase to uppercase and uppercase to lowercase.

