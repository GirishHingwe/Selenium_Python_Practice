list = ['sad', 'bad', 'sas']


def list_palindrome(list):
    for word in list:
        result = ""
        for i in range(len(word) - 1, -1, -1):
            result += word[i]
        if result == word:
            return word
    return ""


print(list_palindrome(list))


def encode(data):
    result = ""
    count = 0
    c_value = data[0]
    for char in data:
        if c_value == char:
            count += 1
        else:
            result = result + c_value + str(count)
            count = 1
            c_value = char
    result = result + c_value + str(count)
    return result


print(encode('aaaassdasss'))


def word_count(data):
    result = {}
    for word in data.split():
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result


print(word_count('as as as ds ds wsa was'))


def fabonicci(number):
    a = 0
    b = 1
    c = 0
    for i in range(0, number):
        print(c, end=" ")
        a = b
        b = c
        c = a + b
    return c


print(fabonicci(5))
print("\n")


def balance_parenthesis(data):
    count = 0
    for ch in data:
        if ch == "(":
            count += 1
        else:
            if count > 0:
                count -= 1
    if count == 0:
        return "balanced"
    return "Unbalanced"


print(balance_parenthesis("((())))(("))
print(balance_parenthesis("((()))"))


def is_prime(number):
    if number < 2:
        return "Invalid"
    for i in range(2, number):
        if number % i == 0:
            return "Not prime"
    return "Prime"


print(is_prime(5))
print(is_prime(9))
