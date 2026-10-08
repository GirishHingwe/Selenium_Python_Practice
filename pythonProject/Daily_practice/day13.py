list1 = [1, 2, 3, 5, 6, 7]
list2 = [10, 11, 13, 14, 15]


def fun(list1):
    for i in range(0, len(list1) - 1):
        if list1[i] + 1 != list1[i + 1]:
            return list1[i] + 1
    return list1[i] + 1


print(fun(list1))
print(fun(list2))


def is_prime(number):
    if number < 2:
        return "Invalid"
    for i in range(2, number):
        if number % i == 0:
            return 'Not Prime'
    return 'Prime'


print(is_prime(4))
print(is_prime(5))


def palindrome_str(data):
    temp = ''
    for i in range(len(data)-1,-1,-1):
        temp = temp + data[i]
    if temp == data:
        print("Palindrome")
    else:
        print("Not Palindrome")

palindrome_str('saaad')
palindrome_str('SAAS')

def word_count(data):
    temp = {}
    for i in data.split():
        if i in temp:
            temp[i] += 1
        else:
            temp[i] = 1
    return temp

print(word_count('asda dada fadf asas asa dda adda dda'))


def encode(data):
    result = ''
    count = 0
    c_value = data[0]
    for i in range(0,len(data)):
        if data[i] == c_value:
            count += 1
        else:
            result = result + c_value + str(count)
            c_value = data[i]
            count = 1
    result = result + c_value + str(count)
    return result
print(encode('aaaddwweqeaa'))





