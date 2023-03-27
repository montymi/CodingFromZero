import pytest
from project5 import double, noThree, onlySet, onlyTrue, onlyEvens 

# Variables
@pytest.fixture
def nums():
    return [1,2,3,4,5,6]

@pytest.fixture
def aSet(nums):
    return set(nums)

# 1 - Double
def test_double():
    assert double(4) == 8

# 2 - Not 3
def test_noThree(nums):
    assert 3 not in noThree(nums)

# 3 - Only a Set
def test_onlySet(aSet):
    assert type(onlySet(aSet)) == set

# 4 - Only True
def test_onlyTrue():
    assert onlyTrue(1) == True

# 5 - Only Evens
def test_onlyEvens(nums):
    for x in onlyEvens(nums):
        assert x % 2 == 0
