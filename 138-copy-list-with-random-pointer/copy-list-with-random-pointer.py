class Solution(object):
    def copyRandomList(self, head):
        if head is None:
            return None

        old_to_new = {}

        # Create a copy of every node
        curr = head

        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        # Connect next and random pointers
        curr = head

        while curr:
            old_to_new[curr].next = old_to_new.get(curr.next)
            old_to_new[curr].random = old_to_new.get(curr.random)

            curr = curr.next

        return old_to_new[head]