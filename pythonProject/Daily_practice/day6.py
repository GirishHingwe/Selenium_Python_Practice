def Palindrome(str):
    result = ''
    for i in range(len(str) - 1, -1, -1):
        result += str[i]

    if result == str:
        print("Palindrome")
    else:
        print("Not palindrome")


Palindrome('dance')
Palindrome('ama')

"""
aaaaabbaaacccbbb 
a5b2a3c3b3
"""


def encode(string):
    temp = string[0]
    count = 1
    result = ''
    for i in range(1, len(string)):
        if temp == string[i]:
            count += 1
        else:
            result = result + temp + str(count)
            temp = string[i]
            count = 1

    result = result + temp + str(count)
    print(result)


encode('aaaaabbaaacccbbb')


def encoding(data):
    if len(data) == 0:
        return
    temp = data[0]
    count = 1
    result = ''
    for i in range(1, len(data)):
        if temp == data[i]:
            count += 1

        else:
            result += temp + str(count)
            count = 1
            temp = data[i]
    result = result + temp + str(count)
    print(result)


encoding('aaaaabbbcccdeee')


def is_prime(number):
    if number < 2:
        print("Invalid")
    for i in range(2, number):
        if number % i == 0:
            return 'Not Prime'
    return 'Prime'


print(is_prime(3))
print(is_prime(4))


def fabonicci(number):
    a = 0
    b = 1
    c = 0

    for i in range(0, number+1):
        print(c, end=" ")
        a = b
        b = c
        c = a + b

fabonicci(6)
