class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        first = -1
        previous = -1
        minimum = float('inf')
        maximum = -1

        index = 1
        prev = head
        curr = head.next

        while curr and curr.next:
            if ((curr.val > prev.val and curr.val > curr.next.val) or
                (curr.val < prev.val and curr.val < curr.next.val)):

                if first == -1:
                    first = index
                else:
                    minimum = min(minimum, index - previous)
                    maximum = index - first

                previous = index

            prev = curr
            curr = curr.next
            index += 1

        if maximum == -1:
            return [-1, -1]

        return [minimum, maximum]