"""
>>> list(removeNthFromEnd(ListNode.from_iter([1,2,3,4,5]), 2))
[1, 2, 3, 5]
"""

from leetcode import ListNode
from linked_list import new_node, list_node_to_iter
from iterator import foldr

def removeNthFromEnd(head, n):
    return foldr(
        lambda (head,m,n),i: ((head if m==n else new_node(i,head)),m+1,n),
        (None, 1, n),
        list_node_to_iter(head))[0]
