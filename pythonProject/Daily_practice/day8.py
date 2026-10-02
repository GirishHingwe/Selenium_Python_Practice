def encoding(data):
    char_current = data[0]
    result = ''
    count = 0
    for i in data:
        if char_current == i:
            count += 1
        else:
            result = result + char_current + str(count)
            count = 1
            char_current = i
    result = result + char_current + str(count)
    print(result)


encoding("aaaaadddddvvddgge")


def is_prime(number):
    if number < 2:
        return "Invalid"
    for num in range(2, number):
        if number % num == 0:
            return "Not Prime"
    return "Prime"


print(is_prime(5))
print(is_prime(10))


def Palindrome(number):  #1221
    temp = number #temp = 1221
    result = 0    # result = 0
    while temp > 0:  #temp = 0,
        c_value = temp % 10   # c_value = 1
        result = result * 10 + c_value  #result = 122*10 + 1 = 1221

        temp = temp // 10 # temp = 0
    if result == number:
        print("Palindrome")
    else:
        print("Not Palindrome")


Palindrome(1222)
Palindrome(1221)

def Palindrome_str(data): #madam
    result =''
    for i in range(len(data)-1,-1,-1):  # i = -1

        result = result + data[i]  # '' + m = m+ a = ma+d = mad+ a = mada + m =madam

    if result == data: # madam = madam
        print("Palindrome")
    else:
        print("Not palindrome")

Palindrome_str("wink")
Palindrome_str("madam")

