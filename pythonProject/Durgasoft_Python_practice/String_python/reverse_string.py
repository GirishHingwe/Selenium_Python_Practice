#1st way
# s = input("Enter some string: ")
# print(s[::-1])


#2nd way
# s = input("Enter Some String: ")
# print(''.join(reversed(s)))

#3rd way
s = input("Enter Some String: ")
i = len(s) - 1
target = ''
while i>=0:
    target = target + s[i]
    i = i-1
print(target)

