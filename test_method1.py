import pytest
from Testpackage.classtotest import Add

@pytest.mark.usefixtures("onetime","SetUp")
class testmytest():

    @pytest.fixture(autouse=True)
    def test_method(self):
        self.abc = Add(10)

    def test_md1(self):
        result = self.abc.addall(8, 2)
        assert result == 21
        print("method1 running")



