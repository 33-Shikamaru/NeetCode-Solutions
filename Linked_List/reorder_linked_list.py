'''
Problem: Reorder Linked List
---

You are given the head of a singly linked-list.

The positions of a linked list of length = 7 for example, can intially be represented as:
[0, 1, 2, 3, 4, 5, 6]

Reorder the nodes of the linked list to be in the following order:
[0, 6, 1, 5, 2, 4, 3]

Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:
[0, n-1, 1, n-2, 2, n-3, ...]

You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.

---
URL: https://neetcode.io/problems/reorder-linked-list/question?list=neetcode150
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

def reorderList(head: Optional[ListNode]) -> None:    
    # The thought process is to split the linked list into two halves, 
    # reverse the second half, and then merge the two halves alternately.
    # In doing this, we can achieve the desired reordering of the linked list.
    
    if not head or not head.next:
        return
    
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next if slow else None
        fast = fast.next.next
    
    
    if not slow:
        return
    list2 = slow.next
    prev = slow.next = None
    
    while list2:
        temp = list2.next
        list2.next = prev
        prev = list2
        list2 = temp

    list1, list2 = head, prev
    while list2:
        temp1, temp2 = list1.next, list2.next
        list1.next = list2
        list2.next = temp1
        list1, list2 = temp1, temp2

def test1():
    head = ListNode(2, ListNode(4, ListNode(6, ListNode(8))))
    reorderList(head)
    assert list_to_array(head) == [2, 8, 4, 6]
    print("Test 1: PASSED")

def test2():
        head = ListNode(2, ListNode(4, ListNode(6, ListNode(8, ListNode(10)))))
        reorderList(head)
        assert list_to_array(head) == [2, 10, 4, 8, 6]
        print("Test 2: PASSED")

test1()
test2()