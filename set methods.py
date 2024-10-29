s1 = {1,2,3}
s2 = {12,9,5}
print(s1.union(s2))

s1 = {3,4,5}
s2 = {6,4,3}
print(s1.intersection(s2))

s1 = {3,4,5,7,'wow'}
s2 = {6,4,3,'hi'}
print(s1.difference(s2))

s1 = {3,4,5,7,'wow'}
s2 = {6,4,3,'hi'}
print(s1.symmetric_difference(s2))

s1 = {3,4,5,11}
s1.add(8)
print(s1)

s1 = {3,6,11,5}
s2 = {2,'hello'}
s1.update(s2)
print(s1)

s1 = {3,4,5,11}
s1.clear()
print(s1)

s1 = {3,5,7,10}
s1.remove(7)
print(s1)

s1 = {3,5,7,10}
s1.discard(7)
print(s1)

s1 = {3,5,7,10}
print(s1.pop())
print(s1)

s1 = {3,6,11,5}
s2 = {3,11}
print(s1.issuperset(s2))

s1 = {3,6,11,5}
s2 = {3,11}
print(s2.issubset(s1))

