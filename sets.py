#Basic implementation of sets

s = set()
print(type(s))
l = [1,2,3,4]
s_from_set = set(l)
print(s_from_set)
s.add(7)
s.add(9)
s.add(9)    #it will only add the unique values/element
s.add(12)
print(s)
s.remove(9)
print(s)
s1 = {4, 15}
print(type(s))
print(s.isdisjoint(s1))
