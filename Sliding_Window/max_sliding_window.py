'''
Problem: Sliding Window Maximum
-------

You are given an array of integers `nums` and an integer `k`. There is a sliding 
window of size `k` that starts at the left edge of the array. The window slides 
one position to the right until it reaches the right edge of the array.

Return a list that contains the maximum element in the window at each step.

-------
URL: https://neetcode.io/problems/sliding-window-maximum/question?list=neetcode150
'''

def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    # My approach is to take the maximum value of the current window
    # and append it to the solution list which works for small arrays
    # and small windows sizes (k values). Optimized approaches would
    # involve using a deque to keep track of the max values in the window.
    
    left = 0
    sol = []
    for right in range(k-1, len(nums)):
        sol.append(max(nums[left:right+1]))
        left+= 1
    return sol

def test1(nums: list[int] = [1,2,1,0,4,2,6], k: int = 3):
    assert maxSlidingWindow(nums, k) == [2,2,4,4,6]
    print("Test 1: PASSED")

def test2(nums: list[int] = [1, 2, 3, 4, 5, 6, 7, 8], k: int = 3):
    assert maxSlidingWindow(nums, k) == [3, 4, 5, 6, 7, 8]
    print("Test 2: PASSED")

def test3(nums: list[int] = [1, -1], k: int = 1):
    assert maxSlidingWindow(nums, k) == [1, -1]
    print("Test 3: PASSED")

test1()
test2()
test3()