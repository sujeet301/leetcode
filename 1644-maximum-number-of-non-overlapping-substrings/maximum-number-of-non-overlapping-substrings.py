class Solution(object):
    def maxNumOfSubstrings(self, s):
        n = len(s)

        first = [n] * 26
        last = [-1] * 26

        # Find first and last occurrence of each character
        for i in range(n):
            x = ord(s[i]) - ord('a')

            first[x] = min(first[x], i)
            last[x] = i

        intervals = []

        # Build valid intervals
        for c in range(26):
            if first[c] == n:
                continue

            left = first[c]
            right = last[c]
            i = left
            valid = True

            while i <= right:
                x = ord(s[i]) - ord('a')

                if first[x] < left:
                    valid = False
                    break

                right = max(right, last[x])
                i += 1

            if valid:
                intervals.append((right, left))

        # Sort by ending position
        intervals.sort()

        answer = []
        previous_end = -1

        # Greedy selection
        for right, left in intervals:
            if left > previous_end:
                answer.append(s[left:right + 1])
                previous_end = right

        return answer