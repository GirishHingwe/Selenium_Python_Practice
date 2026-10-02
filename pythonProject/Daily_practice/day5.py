def palindrome(number):
    result = 0
    temp = number
    while temp>0:
        v = temp%10
        result = result*10 + v
        temp = temp//10
    if result == number:
        print("No. is Palindrome")
    else:
        print("Not palindrome")

palindrome(1234)

def Palindrome_string(string):
    result = ''
    for i in range(len(string)-1,-1,-1):
        result += string[i]
    if result == string:
        print("String is Palindrome")
    else:
        print("String is not Palindrome")

Palindrome_string("madam")


def is_prime(number):
    if number<2:
        return 'Invalid'
    for i in range(2,number):
        if number%i == 0:
            return 'Not Prime'
    return 'Prime'

def test_assert():
    assert is_prime(12) == 'Not Prime'
    assert is_prime(5) == 'Prime'

print(is_prime(3))