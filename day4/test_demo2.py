import pytest


def mul(num1,num2):
    return num1*num2

def add(num1,num2):
    return num1+num2

@pytest.fixture
def init():
    print('Test method execution started')
    yield
    print('Test method execution ended')


def test_m1(init):
    actuals = mul(10,20)
    assert actuals == 200

# @pytest.mark.skip
# @pytest.mark.xfail
def test_m2(init):
    actuals = add(10,20)
    assert actuals == 30


