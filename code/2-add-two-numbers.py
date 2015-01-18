"""
>>> list(addTwoNumbers(*map(ListNode.from_iter, [[2,4,3],[5,6,4]])))
[7, 0, 8]
"""

from leetcode import ListNode
from iterator import izip_longest
from linked_list import list_node_to_iter, list_node_from_iter


def add_by_one_digit(it):
    c = 0
    for a, b in it:
        r = a+b+c
        yield r%10
        c = r/10
    if c > 0:
        yield c


def addTwoNumbers(l1, l2):
    return list_node_from_iter(
        add_by_one_digit(
            izip_longest(
                *map(list_node_to_iter, [l1,l2]),
                fill=0)))
