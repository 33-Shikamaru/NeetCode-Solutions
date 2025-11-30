'''
Problem: Linked List Cycle Detection
---

Given the beginning of a linked list `head`, return `true` if there is a cycle in the linked list.
Otherwise, return `false`.

There is a cycle in a linked list if at least one node in the list can be visited again by 
following the `next` pointer.

Internally, `index` determines the index of the beginning of the cycle, if it exists. The 
tail node of the list will set it's next pointer to the index-th node. If index = -1, then 
the tail node points to null and no cycle exists.

**Note:** `index` is not given to you as a parameter.

---
URL: https://neetcode.io/problems/linked-list-cycle-detection/question?list=neetcode150
'''

# ===== Essential Tools =====

from typing import Optional

# Defining the ListNode class used in this problem
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ===== End of Essential Tools =====

def hasCycle(head: Optional[ListNode]) -> bool:
    # We want to check for a cycle in a linked list by using a two-pointer 
    # approach. One fast pointer and one slow pointer would allow us to accomplish 
    # this by moving the fast pointer twice as fast as the slow pointer. If there is 
    # a cycle, the fast pointer will eventually catch up to the slow pointer.
    
    if not head:
        return False

    fast, slow = head, head
    while fast and fast.next:
        slow = slow.next if slow else None
        fast = fast.next.next
        if fast == slow:
            return True
    return False

def test1():
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2
    assert hasCycle(node1)
    print("Test 1: PASSED")

def test2(linked_list: Optional[ListNode] = ListNode(1, ListNode(2))):
    assert not hasCycle(linked_list)
    print("Test 2: PASSED")

test1()
test2()
