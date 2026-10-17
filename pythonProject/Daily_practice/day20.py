def Palindorme(data):
    result = ''
    for ch in range(len(data)-1,-1,-1):
        result += data[ch]

    if result == data:
        return 'Palindrome'
    else:
        return 'Not Palindrome'

print(Palindorme('gig'))
print(Palindorme('gigw'))

def is_prime(number):
    if number < 2:
        return 'Invalid'
    for num in range(2,number):
        if number%num == 0:
            return 'Not Prime'
    return 'Prime'

print(is_prime(43))
print(is_prime(4))

def encode(data):
    result = ''
    count = 0
    c_value = data[0]
    for i in range(0,len(data)):
        if c_value == data[i]:
            count += 1
        else:
            result = result + c_value + str(count)
            count = 1
            c_value = data[i]
    result = result + c_value + str(count)
    return result

print(encode('aaaffewwwrwaa'))


list1 = ['das','sad','get','sas']
def Palindrome_list(list1):
    for word in list1:
        result = ''
        for i in range(len(word)-1,-1,-1):
            result += word[i]
        if result == word:
            return word
    return ""

print(Palindrome_list(list1))


def word_count(data):
    result = {}
    for word in data.split():
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result

print(word_count('das das fine fin right tight'))


list2 = [1,2,3,6,342,6342,3]
def second_high(list2):
    list2.sort()
    print(list2[-2])

second_high(list2)

def fab(number):
    a = 0
    b = 1
    c = 0
    for i in range(0,number):
        print(c,end=" ")
        a = b
        b = c
        c = a + b

fab(6)
print("\n")


#missing number in array
list3 = [1,2,4,5]
def missing_num(list3):
    for i in range(1,len(list3)):
        if list3[i - 1] + 1 != list3[i]:
            return list3[i] - 1
    return 0

print(missing_num(list3))






