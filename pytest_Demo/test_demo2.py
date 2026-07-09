#Any pytest file should start with test_ or end with _test
#pytest method names should start with test


import pytest


def test_assert():
    msg = "Hello"
    assert msg == "Hi", "Test Failed because strings do not match"

def test_SecondProgram():
    a = 4
    b = 6
    assert a+2 == 6, "Addition do not match"

@pytest.mark.smoke
def test_SecondGreetCreditCard():
    print("Good Morning")


