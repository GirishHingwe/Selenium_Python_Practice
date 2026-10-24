list = ['sad', 'bad', 'dad', 'get']


def Palindrome_list(list):
    for word in list:
        result = ''
        for j in range(len(word) - 1, -1, -1):
            result += word[j]
        if result == word:
            return result
    return ""


print(Palindrome_list(list))


def encode(data):
    result = ''
    count = 1
    c_value = data[0]
    for i in range(1, len(data)):
        if c_value == data[i]:
            count += 1
        else:
            result = result + c_value + str(count)
            count = 1
            c_value = data[i]
    result = result + c_value + str(count)
    return result


print(encode('aaaaaassdddaaa'))

#((())())
def parethesis(data):
    count = 0
    for i in data:
        if '(' == i:
            count += 1
        else:
            if count > 0:
                count -= 1
            # else:
            #     return False
    if count == 0:
        return True
    return False
print(parethesis('(((())))'))
print(parethesis(')('))

def parenthesis_1(data):
    stack = []
    for i in data:
        if '(' == i:
            stack.append('(')
        else:
            if len(stack) > 0:
                stack.pop()
    if len(stack) == 0:
        return True
    return False

print(parenthesis_1('(((())))'))
print(parenthesis_1(')('))


def parenthesis_2(data):
    stack = []
    open_braces = ['{','[','(']
    for i in data:
        if i in open_braces:
            stack.append(i)
        else:
            if len(stack) > 0:
                if i == ')' and stack[-1]=='(':
                    stack.pop()
                if i == '}' and stack[-1]=='{':
                    stack.pop()
                if i == ']' and stack[-1]=='[':
                    stack.pop()
    if len(stack) == 0:
        return True
    return False

print(parenthesis_2('[{()}]'))
print(parenthesis_2(')({{(())]]]]}'))
print(parenthesis_2('[{()}]'))


def word_count(data):
    result = {}
    for word in data.split():
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result
print(word_count('dad dad as as as son nsie isa'))
