s = input("Enter Some String:")
i = 0
for x in s:
    print("The Character present at positive index {} and at negative Index {} is {}".format(i, i-len(s),x))
    i = i + 1
