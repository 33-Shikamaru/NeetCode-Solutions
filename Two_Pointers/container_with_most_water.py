'''
Problem: Container With Most Water
-------

You are given an integer array `heights` where `heights[i]` represents the height of the 
ith bar. 

You may choose any two bars to form a container. Return the maximum amound of water a 
container can store.

-------
URL: https://neetcode.io/problems/max-water-container?list=neetcode150
'''

def maxArea(heights: list[int]) -> int:
    # We want to create pointers (one on each side) such that we can find the
    # maximum between the two highest points, but along the way we will keep a 
    # max counter to ensure we find the largest area possible.

    
    left, right = 0, len(heights) - 1
    sol = 0
    for height in heights:
        distance = right - left
        sol = max(sol, min(heights[left], heights[right]) * distance)
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return sol
    
    
def test1(heights: list[int] = [1,7,2,5,4,7,3,6]):
    sol = 36
    print('Test 1: PASSED' if maxArea(heights) == sol else 'Test 1: FAILED')
    
def test2(heights: list[int] = [2,2,2]):
    sol = 4
    print('Test 2: PASSED' if maxArea(heights) == sol else 'Test 2: FAILED')
    
test1()
test2()