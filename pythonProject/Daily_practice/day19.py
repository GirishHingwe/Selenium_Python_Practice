def Palindrome(data):
    result = ''
    for char in range(len(data) - 1, -1, -1):
        result = result + data[char]

    if result == data:
        return 'Palindrome'

    else:
        return 'Not Palindrome'


print(Palindrome('Pass'))
print(Palindrome('DAD'))


def word_count(data):
    result = {}
    for i in data.split():
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result


print(word_count('das das as as if are time'))


def encoding(data):
    result = ''
    count = 0
    c_value = data[0]
    for i in range(0, len(data)):
        if c_value == data[i]:
            count += 1
        else:
            result = result + c_value + str(count)
            count = 1
            c_value = data[i]
    result = result + c_value + str(count)
    return result


print(encoding('aaassssssddaasww'))


def fab(number):
    a = 0
    b = 1
    c = 0
    for i in range(0, number):
        print(c, end=" ")
        a = b
        b = c
        c = a + b
    print("\n")


fab(6)

list1 = [1, 2, 4, 5]


def missing(list1):
    for i in range(1, len(list1)):
        if list1[i] != list1[i - 1] + 1:
            return list1[i] - 1
    return list1[0] - 1


print(missing(list1))


def is_prime(number):
    if number < 2:
        return 'Invalid'
    for i in range(2, number):
        if number % i == 0:
            return 'Not Prime'
    return 'Prime'


print(is_prime(2))
print(is_prime(4))

list2 = ['ab', 'bcs', 'fsdf', 'dfa', 'cac']


def Palindrome_list(list2):
    for word in list2:
        result = ''
        for ch in range(len(word) - 1, -1, -1):
            result += word[ch]
        if result == word:
            return word
    return " "


print(Palindrome_list(list2))
