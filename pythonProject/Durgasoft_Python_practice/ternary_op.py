# a,b = 10,20
# x = 30 if a<b else 40
# print(x)

#Read two number from keyboard and print minimum value
# a= int(input("Enter First number :"))
# b = int(input("Enter Second Number: "))
# min=a if a<b else b
# print("Minimum Value :", min)

#Program for minimum of 3 Numbers
a= int(input("Enter First Number: "))
b= int(input("Enter Second Number: "))
c= int(input("Enter Third Number: "))
min = a if a<b and a<c else b if b<c else c
print("Minimum Number: ", min)