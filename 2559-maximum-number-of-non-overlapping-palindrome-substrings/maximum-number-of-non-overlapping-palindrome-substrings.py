class Solution(object):
    def maxPalindromes(self, s, k):
        n = len(s)
        count = 0
        last_end = -1

        for right in range(n):
            found = False

            # Try every possible starting position
            for left in range(last_end + 1, right + 1):
                
                if right - left + 1 < k:
                    continue

                # Check palindrome
                i = left
                j = right

                while i < j and s[i] == s[j]:
                    i += 1
                    j -= 1

                if i >= j:
                    count += 1
                    last_end = right
                    found = True
                    break

            if found:
                continue

        return count