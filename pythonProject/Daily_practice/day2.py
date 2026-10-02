# def is_prime(number):
#     for i in range(2,number):
#         if number%i == 0:
#             return "Not Prime"
#     return "Prime"
#
# print(is_prime(4))

# def Factorial(number):
#     result = 1
#     for i in range(1, number+1):
#         result = result * i
#         # print(result)
#     return result
#
#
# print(Factorial(4))

"""
Square of a number
"""

# def square(number):
#     result = 0
#     for i in range(1,number+1):
#         result = result + number
#     print("Square number is :",result)
#     return result
#
# def test_square():
#     assert square(5) == 25, "Number should be square"


"""
Palindrome
"""


def Palindrome(number):
    result = 0
    temp = number
    while temp > 0:
        v = temp % 10
        # print(v)
        result = result * 10 + v
        # print(result)
        temp = temp // 10
        # print(temp)
    if number == result:
        print("palindrome")
    else:
        print("Not palindrome")


Palindrome(121)


def string_palindrome(str):
    if str[::-1] == str:
        print("Palindrome")
    else:
        print("Not palindrome")

string_palindrome("madama")

def str_palindrome(str):
    result =''
    for i in range(len(str)-1,-1,-1):
        result = result + str[i]
    if result == str:
        print("Palindrome")
    else:
        print("Not Palindrome")
str_palindrome("dada")
