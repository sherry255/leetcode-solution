def list_node_from_iter(it):
    try:
        e = next(it)
    except StopIteration:
        return None

    node = ListNode(e)
    node.next = list_node_from_iter(it)
    return node


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __iter__(self):
        while self is not None:
            yield self.val
            self = self.next

    @staticmethod
    def from_iter(iterable):
        return list_node_from_iter(iter(iterable))
