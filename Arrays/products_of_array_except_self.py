'''
Problem: Products of Array Except Self
-------

Given an integer array `nums`, return an array `output` where `output[i]` is the product
of all the elements of `nums` except `nums[i]`.

Each product is **guaranteed** to fit in a 32-bit integer.

Follow up: Could you solve it in O(n) time without using the division operation?

-------
URL: https://neetcode.io/problems/products-of-array-discluding-self?list=neetcode150
'''

def productExceptSelf(nums: list[int]) -> list[int]:
    # We want to try and build and prefix and postfix table such that we only multiply
    # all digits that are not the index of the list. We make two passes to build this
    # and return the solution.
    # 
    # NOTE: Our solution did not use division.
    
    sol = [1] * len(nums)
    pre = 1
    for i in range(len(nums)):
        sol[i] = pre
        pre *= nums[i]
    post = 1
    for i in range(len(nums) - 1, -1, -1):
        sol[i] *= post
        post *= nums[i]
    return sol
    

    
def test1(nums: list[int] = [1,2,4,6]):
    sol = [48,24,12,8]
    print('Test 1: PASSED' if productExceptSelf(nums) == sol else 'Test 1: FAILED')
    
def test2(nums: list[int] = [-1,0,1,2,3]):
    sol = [0,-6,0,0,0]
    print('Test 2: PASSED' if productExceptSelf(nums) == sol else 'Test 2: FAILED')
    
test1()
test2()