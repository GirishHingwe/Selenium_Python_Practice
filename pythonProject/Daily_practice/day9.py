def palindrome(data):
    result = ''
    for str in range(len(data) - 1, -1, -1):
        result += data[str]

    if result == data:
        print("Palindrome")

    else:
        print("Not Palindrome")


palindrome("dada")
palindrome("dad")


def is_prime(number):
    if number < 2:
        return "Invalid"
    for num in range(2, number):
        if number % num == 0:
            return "Not Prime"
    return "Prime"


print(is_prime(4))
print(is_prime(3331))
print(is_prime(1))
print(is_prime(331))
print(is_prime(10))
