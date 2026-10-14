def Palindrome(data):
    result = ''
    for ch in range(len(data) - 1, -1, -1):
        result += data[ch]

    if result == data:
        print('Palindrome')
    else:
        print('Not palindrome')


Palindrome('daad')
Palindrome('daas')


def encoding(data):
    result = ''
    count = 0
    c_value = data[0]
    for i in data:
        if c_value == i:
            count += 1
        else:
            result = result + c_value + str(count)
            count = 1
            c_value = i
    result = result + c_value + str(count)
    return result


print(encoding('aaassdassff'))


data = "Hello World"
for i in range(0,len(data)):
    print(i,data[i])

for i in data:
    print(i)

def word_count(data):
    result = {}
    for i in data.split():
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result

print(word_count('das das as as as fg gf'))