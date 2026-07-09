t = (10,20,30,40)
print(type(t))

# t[0] = 100
# print(t)
# TypeError: 'tuple' object does not support item assignment
t.append("girish") #AttributeError: 'tuple' object has no attribute 'append'
print(t)