import pytest

@pytest.mark.userfixtures("dataLoad")
class TestExample2:

    def test_editProfile(self, dataLoad):
        print(dataLoad[0])
        print(dataLoad[2])