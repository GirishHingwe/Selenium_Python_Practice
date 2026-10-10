def Palindrome_str(data):
    result = ''
    for char in range(len(data) - 1, -1, -1):
        result += data[char]

    if result == data:
        print('Palindrome')

    else:
        print('Not palindrome')


Palindrome_str('SAAS')
Palindrome_str('DAs')


def is_Prime(number):
    if number < 2:
        return 'Invalid'
    for num in range(2, number):
        if number % num == 0:
            return 'Not Prime'
    return 'Prime'


print(is_Prime(2))
print(is_Prime(4))


def word_count(data):
    result = {}
    for word in data.split():
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result

print(word_count('data data fes tgee sda '))


def encode(data):
    result = ''
    count = 0
    c_char = data[0]
    for i in data:
        if c_char == i:
            count += 1
        else:
            result = result + c_char + str(count)
            count = 1
            c_char = i
    result = result + c_char + str(count)
    print(result)

encode('aaaddsssvva')


arr = [1,2,3,4,5,6]
arr_str = ['das','hello','world']
arr_char = ['a','b','c','d']
data_str = 'Hello'
for i in data_str:
    print(i)
for i in range(0,len(arr)):
    print(arr[i])


mp_data = {}
# print(type(mp_data))
mp_data['i'] =1
# print(type(mp_data))
print(mp_data['i'])