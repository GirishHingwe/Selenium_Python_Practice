def Palindrome(data):
    result = ''
    for word in range(len(data)-1,-1,-1):
        result += data[word]

    if result == data:
        return 'Palindrome'
    else:
        return 'not palindrome'

print(Palindrome('dss'))
print(Palindrome('sas'))

def encode(data):
    result = ''
    count = 1
    c_var = data[0]
    for ch in range(1,len(data)):
        if c_var == data[ch]:
            count += 1
        else:
            result = result + c_var + str(count)
            count = 1
            c_var = data[ch]
    result = result + c_var + str(count)
    print(result)

encode('aaassddddadw')


def word_count(data):
    result = {}
    for ch in data.split():
        if ch in result:
            result[ch] += 1
        else:
            result[ch] = 1
    return result
print(word_count('das das das wer wer ter '))

def is_prime(number):
    if number < 2:
        return 'Invalid'
    for num in range(2,number):
        if number%num == 0:
            return 'Not Prime'
    return 'Prime'

print(is_prime(3))
print(is_prime(4))
