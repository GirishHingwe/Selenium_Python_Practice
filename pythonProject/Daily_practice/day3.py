# def is_prime(number):
#     if number < 2:
#         return "Invalid"
#     for i in range(2, number):
#         if number % i == 0:
#             return "Not Prime"
#     return "Prime"
#
#
#
# print(is_prime(11))

def Palindrome(str):
    result = ''
    for i in range(len(str) - 1, -1, -1):
        result = result + str[i]
    if result == str:
        print("Palindrome")
    else:
        print("Not Palindrome")


Palindrome('madam')
