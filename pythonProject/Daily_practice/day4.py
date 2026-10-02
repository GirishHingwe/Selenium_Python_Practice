def is_prime(number):
    if number < 2:
        return 'Invalid'
    for i in range(2, number):
        if number % i == 0:
            return 'Not Prime'
    return 'Prime'


print(is_prime(5))


def Palindrome(str):
    result = ""
    for i in range(len(str) - 1, -1, -1):
        result += str[i]

    if result == str:
        print('Palindrome')
    else:
        print("Not Palindrome")


Palindrome('saas')


def Pal(number):
    result = 0
    temp = number
    while temp > 0:
        v = temp % 10
        result = result * 10 + v
        temp = temp // 10
    if result == number:
        print("Palindrome")
    else:
        print("Not Palindrome")


Pal(123)
Pal(121)
