from typing import List, Set
# This is the pre-testing file
# Please create tests for each function below

# 1 - Double
def double(x: int):
    return x * 2

double(4)

# 2 - Not 3
def noThree(x: List):
    return [n for n in x if n != 3]

nums = [1,2,3,4,5,6]
noThree(nums)

# 3 - Only a Set
def onlySet(x: Set):
    return x

aSet = set([1,2,3,4,5,6])
onlySet(aSet)

# 4 - Only True
def onlyTrue(x: int):
    if type(x) != int:
        return False
    return True

onlyTrue(1)

# 5 - Only Evens
def onlyEvens(x: List):
    return [n for n in x if n % 2 == 0]

nums = [1,2,3,4,5,6]
onlyEvens(nums)
