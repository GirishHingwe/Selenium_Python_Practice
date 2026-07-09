numbers = [10,10,10,5,30]
largest = second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif largest > num > second_largest:
        second_largest = num

print("Second Largest : ", second_largest)

# unique = list(set(numbers))
# unique.sort()
# print("Second largest: ", unique[-2])