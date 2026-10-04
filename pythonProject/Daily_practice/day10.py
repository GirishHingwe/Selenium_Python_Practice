def wordCount(para):
    mapCount = {}
    for word in para.split():
        if word in mapCount:
            mapCount[word] += 1
        else:
            mapCount[word] = 1

    print(mapCount)


wordCount("map pap map epw apet tewp a erer pppp map")


def fabonicci(number):
    a = 0
    b = 1
    c = 0
    for i in range(0, number):
        print(c, end=" ")
        a = b
        b = c
        c = a + b


fabonicci(10)
print("\n")


def is_prime(number):
    if number < 2:
        return "invalid"
    for num in range(2, number):
        if number % num == 0:
            return "Not Prime"
    return "Prime"


print(is_prime(2))
print(is_prime(10))


def Palindrome_str(data):
    result = ''
    for i in range(len(data) - 1, -1, -1):
        result = result + data[i]

    if result == data:
        print("Palindrome")

    else:
        print("Not Palindrome")


Palindrome_str("dad")
Palindrome_str("faer")


def encode(data):
    result = ''
    count = 0
    current = data[0]
    for char in data:
        if char == current:
            count += 1
        else:
            result =result + current + str(count)
            current = char
            count = 1
    result = result + current + str(count)
    print(result)

encode('aaaabbbbccccdddee')
encode('asasasasad')

