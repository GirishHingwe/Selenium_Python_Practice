# Palindrome string
def Palindrome(data):
    result = ''
    for ch in range(len(data) - 1, -1, -1):
        result += data[ch]

    if result == data:
        return 'Palindrome'

    else:
        return 'Not Palindrome'


print(Palindrome('FAAST'))
print(Palindrome('PAP'))


# Palindrome Number
def Palindrome_num(number):
    temp = number
    result = 0
    while temp > 0:
        a = temp % 10
        result = a + result * 10
        temp = temp // 10
    if result == number:
        return 'Palindrome'
    else:
        return 'Not Palindrome'


print(Palindrome_num(123))
print(Palindrome_num(121))


#Character count encode pattern
def encode(data):
    result = ''
    count = 0
    c_string = data[0]
    for i in range(0,len(data)):
        if c_string == data[i]:
            count += 1
        else:
            result = result + c_string + str(count)
            count = 1
            c_string = data[i]
    result = result + c_string + str(count)
    return result

print(encode('aaasssddfaaaeeee'))


#Word Count function
def word_count(data):
    result = {}
    for word in data.split():
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result

print(word_count('das das sasa sasa sasa dd ffd'))

#Prime number
def is_prime(number):
    if number < 2:
        return 'Invalid'
    for num in range(2,number):
        if number%num == 0:
            return 'Not Prime'
    return 'Prime'

print(is_prime(4))
print(is_prime(31))

# Reverse String
def R_string(data):
    result = data[::-1]
    return result

print(R_string('Deaf'))

