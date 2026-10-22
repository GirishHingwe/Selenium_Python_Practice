def Palindrome(data):
    result = ""
    for ch in range(len(data)-1,-1,-1):
        result += data[ch]
    if result == data:
        return 'Palindrome'
    else:
        return 'Not Palindrome'

print(Palindrome('dasd'))
print(Palindrome('dad'))

def encoding(data):
    result = ""
    count = 1
    c_value = data[0]
    for i in range(1,len(data)):
        if c_value == data[i]:
            count += 1
        else:
            result = result + c_value + str(count)
            count = 1
            c_value = data[i]
    result = result + c_value + str(count)
    return result

print(encoding('aaasrwwrqeqeqe'))

def is_Prime(number):
    if number < 2:
        return 'Invalid'
    for num in range(2,number):
        if number%num == 0:
            return 'Not prime'
    return 'Prime'

print(is_Prime(3))
print(is_Prime(4))


number = [2,42,223,5232,5252,55,5]
def second_highest(number):
    number.sort()
    second = number[-2]
    return second

print(second_highest(number))


def word_count(data):
    result = {}
    for word in data.split():
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result
print(word_count('daas dassa fsda aaa aaa dd dsw dd'))

list_string = ['fas','das','gas','dad']
def Palindrome_word(list_string):
    for word in list_string: # fas
        result = ''
        for ch in range(len(word)-1,-1,-1): #ch = 3-1 = 2-1 = 1-1=0
            result += word[ch] #result = saf
            # print(result)
        if result == word:
            return word
    return "no palindrome"

print(Palindrome_word(list_string))
        
