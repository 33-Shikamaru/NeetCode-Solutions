
def hasDuplicate(nums: list[int]) -> bool:
    # Get all unique values and compare the set size against the nums size
    # if both are same length, we know the values are unique
    
    seen = set(nums)
    return len(seen) != len(nums)
    
def test1(nums:list[int] = [1,2,3,3]):
    print('Test 1: PASSED' if hasDuplicate(nums) else 'Test 1: FAILED')
    
def test2(nums:list[int] = [1,2,3,4]):
    print('Test 2: PASSED' if not hasDuplicate(nums) else 'Test 2: FAILED')
    
test1()
test2()