numbers = [10, 5, 20, 8, 15]

largest = second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif largest > num > second_largest:
        second_largest = num

print("Second Largest:", second_largest)