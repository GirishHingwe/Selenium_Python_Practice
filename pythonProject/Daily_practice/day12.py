array_num = [1, 342, 45, 2341, 41]


def second_max(array_num):
    array_num.sort()
    return array_num[-2]


print(second_max(array_num))


def is_prime(number):
    if number < 2:
        return "Invalid Number"
    for i in range(2, number):
        if number % i == 0:
            return 'Not Prime'
    return 'Prime'


print(is_prime(3421))
print(is_prime(37))


def Palindrome_str(data):
    result = ''
    for i in range(len(data) - 1, -1, -1):
        result = result + data[i]
    if result == data:
        return 'Palindrome'
    else:
        return 'Not Palindrome'


print(Palindrome_str('str'))
print(Palindrome_str('saas'))


def word_count(data):
    result = {}
    for word in data.split():
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result


print(word_count('das das sas sa ffee ddw'))

"""
aaabbca
a3b2c1a1
"""


def encode(data):
    result = ''
    count = 0
    c_data = data[0]
    for i in data:
        if c_data == i:
            count += 1
        else:
            result = result + c_data + str(count)
            c_data = i
            count = 1
    result = result + c_data + str(count)
    return result


print(encode('aaaabbccab'))

list_new = [1, 2, 3, 4, 6, 7, 8]


def missing(list_new):
    for i in range(1, len(list_new)):
        if i != list_new[i - 1]:
            return i
    return -1


print(missing(list_new))

list_new = [3, 4, 5, 6, 7,8]


def missing_2(list_new):
    for i in range(1, len(list_new)):
        if list_new[i] != list_new[i-1]+1:
            return list_new[i] - 1
    return list_new[0] - 1


print(missing_2(list_new))
