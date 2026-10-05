def is_palindrome(data):
    result = ''
    for i in range(len(data) - 1, -1, -1):
        result = result + data[i]
    if result == data:
        print("Palindrome")
    else:
        print("Not Palindrome")


is_palindrome('saas')
is_palindrome('mad')


def is_prime(number):
    if number < 2:
        return 'Invalid'
    for i in range(2, number):
        if number % i == 0:
            return 'Not Prime'
    return 'Prime'


print(is_prime(3))
print(is_prime(10))


def wordcount(data):
    result = {}
    for i in data.split():
        if i in result:
            result[i] += 1
        else:
            result[i] = 1

    return result

print(wordcount('dad aasds dsfdsfse erew sddaa dda dad'))


def unic(data):
    result = data.split("-")
    print(result)

unic('we-qe, -w,we-,q-we, q,weq ,')


#list = [2,3,523,5,3452,66]
#list sort asc
#list of element last pick

def second_highest(data):
    c_max = data[0]
    p_max = 0
    for i in range(1,len(data)):
        if data[i] > c_max:
            p_max = c_max
            c_max = data[i]
        if data[i] < c_max and data[i] > p_max:
            p_max = data[i]
    return p_max

data = [2,3,523,5,3452,66]
print(second_highest(data))
# data.sort()
# print(data[-2])

