'''
Problem: Merge Two Sorted Linked Lists
---

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

The new list should be made up of nodes from `list1` and `list2`.

---
URL: https://neetcode.io/problems/merge-two-sorted-linked-lists/question?list=neetcode150
'''

# ===== Essential Tools =====

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

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # We want to create a new linked list with a head pointer to keep track of the beginning
    # and a tail pointer to let us add nodes to the end of the list. We then compare
    # the values of the two lists and determine which one to add to the new list.
    
    head = ListNode()
    tail = head
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
        
    if list1:
        tail.next = list1
    else:
        tail.next = list2            
    return head.next

def test1():
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(5)))
    result = mergeTwoLists(list1, list2)
    print(list_to_array(result))
    assert list_to_array(result) == [1,1,2,3,4,5]
    print("Test 1: PASSED")

def test2():
    list1 = None
    list2 = ListNode(1, ListNode(2))
    result = mergeTwoLists(list1, list2)
    print(list_to_array(result))
    assert list_to_array(result) == [1,2]
    print("Test 2: PASSED")
    
def test3():
    list1 = None
    list2 = None
    result = mergeTwoLists(list1, list2)
    print(list_to_array(result))
    assert list_to_array(result) == []
    print("Test 3: PASSED")

test1()
test2()
test3()