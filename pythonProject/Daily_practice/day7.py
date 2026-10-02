def factorial(number):
    result = 1
    for i in range(1, number + 1):
        result = result * i

    print(result)


factorial(4)

def is_prime(number):
    if number< 2:
        return "Invalid"
    for i in range(2,number):
        if number%i == 0:
            return "Not prime"
    return "Prime"

print(is_prime(3))
print(is_prime(4))

"""
encoding: aaaaabbcccaaddee
        a5b2c3a2d2e2
"""
def encode(string):
    count = 0
    current_value = string[0]
    result = ''
    for i in string:
        if current_value == i:
            count += 1
        else:
            result= result+current_value+str(count)
            count = 1
            current_value = i

    result = result + current_value + str(count)
    return result
print(encode('aaaaabbcccaaddee'))


def fabonicci(number):
    a = 0
    b = 1
    c = 0
    for i in range(1,number+1):
        print(a,end=" ")
        c = a + b
        a = b
        b = c

fabonicci(7)
print("\n")


"""
dasdsa dasd adsasd asdsda dasdsa dasd adsasd asdsda dasdsa dasd adsasd asdsda

"""
def get_count(data):
    result = {}
    for i in data.split():
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    print(result)

get_count('dasdsa dasd adsasd asdsda dasdsa dasd adsasd asdsda dasdsa dasd adsasd asdsda')



















