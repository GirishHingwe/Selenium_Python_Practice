#Any pytest file should start with test_ or end with _test
#pytest method names should start with test
# py.test -k CreditCard -v -s ---- this command select only with matching name keyword (eg: creditcard) and Run the particular function
# Any code should have sense
# -k stands for method names execution, -s logs in output, -v stands for more info like metadata
# you can run specific file with py.test <filename>
# you can mark (tag) tests and then run with -m
# you can skip test with @pytest.mark.skip
#@pytest.mark.xfail
#fixtures are used as setup and tear down methods for test cases - conftest file to generalise fixture
#fixture and make it available to all test cases
#datadriven and parameterization can be done with return statements in tuple format
#when you define fixture scope to class only, it will run once before class is initiated and at the end

import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    print("Hello")

@pytest.mark.xfail
def test_greet():
    print("Good Morning")

@pytest.mark.skip
def test_SecondCreditCard():
    print("Credit Information")

def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])