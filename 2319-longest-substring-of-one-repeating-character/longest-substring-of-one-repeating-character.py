class Solution(object):
    def longestRepeating(self, s, queryCharacters, queryIndices):
        n = len(s)
        tree = [None] * (4 * n)

        def merge(a, b):
            if a is None:
                return b
            if b is None:
                return a

            left_char = a[0]
            right_char = b[1]

            prefix = a[2]
            suffix = b[3]
            best = max(a[4], b[4])

            # If both parts join with the same character
            if a[1] == b[0]:
                if a[2] == a[5]:
                    prefix = a[2] + b[2]

                if b[3] == b[5]:
                    suffix = b[3] + a[3]

                best = max(best, a[3] + b[2])

            return (left_char, right_char, prefix, suffix, best,
                    a[5] + b[5])

        def build(node, l, r):
            if l == r:
                c = s[l]
                tree[node] = (c, c, 1, 1, 1, 1)
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(tree[node * 2],
                                tree[node * 2 + 1])

        def update(node, l, r, index, char):
            if l == r:
                tree[node] = (char, char, 1, 1, 1, 1)
                return

            mid = (l + r) // 2

            if index <= mid:
                update(node * 2, l, mid, index, char)
            else:
                update(node * 2 + 1, mid + 1, r, index, char)

            tree[node] = merge(tree[node * 2],
                                tree[node * 2 + 1])

        build(1, 0, n - 1)

        answer = []

        for char, index in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, index, char)
            answer.append(tree[1][4])

        return answer