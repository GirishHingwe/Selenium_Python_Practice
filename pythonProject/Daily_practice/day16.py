def Palindrome(data):
    result = ''
    for i in range(len(data)-1,-1,-1):
        result += data[i]

    if result == data:
        print("Palindrome")
    else:
        print("Not palindrome")

Palindrome("SAAS")
Palindrome("DAS")

def word_count(data):
    result = {}
    for word in data.split():
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result

print(word_count('fast fast type read'))

def encode(data):
    result = ''
    count = 0
    c_char = data[0]
    for i in range(0,len(data)):
        if c_char == data[i]:
            count += 1
        else:
            result = result + c_char + str(count)
            count = 1
            c_char = data[i]
    result = result + c_char + str(count)
    return result

print(encode('aaaasssdfaaabb'))

def is_prime(number):
    if number < 2:
        return 'Invalid'
    for i in range(2,number):
        if number%i == 0:
            return 'Not prime'
    return 'Prime Number'
print(is_prime(3))
print(is_prime(6))

list = [1,2,3,4,5,6]
def missing(list): #list = [1,2,3,5,6]
    for num in range(1, len(list)): # num = 3
        if 1+list[num-1] != list[num]: # 1 + 3 != 5
            return list[num]-1 # 4
    return list[0]-1

print(missing(list))

def fabonicci(number):
    a = 0
    b = 1
    c = 0
    for i in range(0,number):
        print(c,end=" ")
        a = b
        b = c
        c = a + b
fabonicci(10)




