def encode(data):
    result = ''
    count = 0 # 0
    current_value = data[0]   #a
    for i in range(0,len(data)): #i = 4
        if current_value == data[i]:
            count += 1 # 3
        else:
            result = result + current_value + str(count)
            count = 1
            current_value = data[i]
    result = result + current_value + str(count)
    print(result)

encode('aaaabbcccba')


def palindrome(data):
    result = ''
    for i in range(len(data)-1,-1,-1):
        result += data[i]

    if result == data:
        print('Palindrome')

    else:
        print('Not palindrome')

palindrome('dad')
palindrome('sase')


def word_count(data):
    result = {}
    for i in data.split():
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result

print(word_count('fadsf sda asa fdsw a a dw'))

def fabonnici(number):
    a = 0
    b = 1
    c = 0
    for i in range(0,number):
        print(c, end=" ")
        a = b
        b = c
        c = a + b
    return c
print(fabonnici(8))

def second_highest():
    list1 = [2,3,4,5,2,1,444,5,88]
    list1.sort()
    print(list1)

    second_h = list1[-2]
    print(second_h)

second_highest()