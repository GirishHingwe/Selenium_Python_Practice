list = [10,20,30,40]
print(list)

# print(list[-1])
# print(list[1:3])
list[0] = 100
for i in list:
    print(i)

list = [10,10.5,'durga', True, 10]
print(list)

list = [10,20,30]
list.append("durga")
print(list)


list.remove(20)
print(list)