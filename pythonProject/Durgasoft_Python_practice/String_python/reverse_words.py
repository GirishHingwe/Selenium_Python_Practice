s = input("Enter Some String: ")
#Converts the string into a list of words:
l = s.split()
#Create an empty list
l1 = []
#Start from the last word
i = len(l) - 1
while i>=0:
    l1.append(l[i])
    i=i-1
#Join the words
output= ' '.join(l1)
print(output)

"""
split()[::-1] → reverses the order of words.
[::-1] → reverses the characters in the string.

"""