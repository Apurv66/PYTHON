#append
# f = open("myfile.txt",'a')
# f.write("lines\n")
# f.close()


#writeline
# f = open("myfile.txt",'w')
# f.write("line1\n")
# f.write("line2")
# f.close()


#writelines()
f = open("myfile.txt",'w')
data = ['line1\n', 'line2\n', 'line3\n']
f.writelines(data)
f.close()


#read all data from the file
# f = open("myfile.txt",'r')
# print(f.read())
# f.close()


#readline
# f = open("myfile.txt",'r')
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.close()


#readlines()
f = open("myfile.txt")
data = f.readlines()
for i in data:
    print(i)
f.close()