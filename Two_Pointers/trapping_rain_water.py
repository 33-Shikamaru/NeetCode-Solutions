'''
Problem: Trapping Rain Water
-------

You are given an array of non-negative integers `height` which represent an 
elevation map. Each value `height[i]` represents the height of a bar, which 
has a width of `1`.

Return the maximum area of water that can be trapped between the bars.

-------
URL: https://neetcode.io/problems/trapping-rain-water?list=neetcode150
'''

def trap(height: list[int]) -> int:
    # We want to use two pointers to traverse the array from both ends
    # and calculate the maximum area of water that can be trapped. We 
    # take note of maximums on either side so we know when we are entering
    # a dip in which we can trap some water.
    
    if not height:
        return 0
        
    sol = 0
    left, right = 0, len(height) - 1
    l_highest, r_highest = height[0], height[-1]

    while left < right:
        if height[left] < height[right]:
            left += 1
            l_highest = max(l_highest, height[left])
            sol += l_highest - height[left]
        else:
            right -= 1
            r_highest = max(r_highest, height[right])
            sol += r_highest - height[right]
    return sol


    
def test1(height: list[int] = [0,2,0,3,1,0,1,3,2,1]):
    sol = 9
    print('Test 1: PASSED' if trap(height) == sol else 'Test 1: FAILED')
    
def test2(height: list[int] = [0,0,0,0,4,2,0,0,0,0]):
    sol = 0
    print('Test 2: PASSED' if trap(height) == sol else 'Test 2: FAILED')
    
test1()
test2()