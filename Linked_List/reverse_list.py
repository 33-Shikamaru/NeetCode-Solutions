'''
Problem: Reverse Linked List
---

Given the beginning of a singly linked list `head`, reverse the list,
and return the new beginning of the list.

---
URL: https://neetcode.io/problems/reverse-a-linked-list/question?list=neetcode150
'''

# ===== Essential Tools =====
# 
from typing import Optional

# Defining the ListNode class used in this problem
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# Helper function to convert a linked list to an array
def list_to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# ===== End of Essential Tools =====

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    # We want to keep track of the next subset of nodes in the linked list
    # and then update the head to previously seen nodes. Doing this
    # will result in a reversed linked list.
    
    sol = None
    while head:
        temp = head.next
        head.next = sol
        sol = head
        head = temp
    return sol

def test1():
    head = ListNode(0, ListNode(1, ListNode(2, ListNode(3))))
    reversed_head = reverseList(head)
    print(list_to_array(reversed_head))
    assert list_to_array(reversed_head) == [3, 2, 1, 0]
    print("Test 1: PASSED")

def test2():
    head = ListNode()
    reversed_head = reverseList(head)
    print(list_to_array(reversed_head))
    assert list_to_array(reversed_head) == [0]
    print("Test 2: PASSED")

test1()
test2()