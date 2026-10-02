# check odd or even
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


# def test_even():
#     list = [2, 4, 6]
#     for i in list:
#         assert is_even(i), "abcd"
#
#
# def test_odd():
#     list = [1, 3, 5, 7]
#     for i in list:
#         assert not is_even(i)


# def is_prime(number):
#     for i in range(2,number):
#         if number%i == 0:
#             return False
#     return True

# def test_prime():
#     test_data = [1,2,3,5,7]
#     for i in test_data:
#         assert is_prime(i)
#
#     test_data = [4,6,8,9]
#     for i in test_data:
#         assert not is_prime(i)
#
# print(is_prime(30))

def is_prime(number):
    for i in range(2,number):
        if number%i == 0:
            return "Not Prime"
    return "Prime"

def test_prime():
    test_data = [1,2,3,5]
    for i in test_data:
        assert is_prime(i) == "Prime"

print(is_prime(4))
