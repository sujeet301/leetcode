class Solution(object):
    def lexPalindromicPermutation(self, s, target):
        n = len(s)
        half_len = n // 2

        # Count characters
        count = [0] * 26

        for ch in s:
            count[ord(ch) - 97] += 1

        # A palindrome can have at most one odd frequency
        odd = 0
        middle = ""

        for i in range(26):
            if count[i] % 2 == 1:
                odd += 1
                middle = chr(i + 97)

        if odd > 1:
            return ""

        # Characters available for the left half
        half = [0] * 26

        for i in range(26):
            half[i] = count[i] // 2

        def make_palindrome(left):
            return left + middle + left[::-1]

        # First, try to make the left half exactly equal
        # to target's left half.
        remaining = half[:]
        possible = True

        for i in range(half_len):
            x = ord(target[i]) - 97

            if remaining[x] == 0:
                possible = False
                break

            remaining[x] -= 1

        if possible:
            left = target[:half_len]
            candidate = make_palindrome(left)

            if candidate > target:
                return candidate

        # Try making the first difference from right to left.
        for p in range(half_len - 1, -1, -1):

            remaining = half[:]
            possible = True

            # Keep target[0 ... p-1] exactly the same
            for i in range(p):
                x = ord(target[i]) - 97

                if remaining[x] == 0:
                    possible = False
                    break

                remaining[x] -= 1

            if not possible:
                continue

            # At position p, choose the smallest
            # character greater than target[p]
            x = ord(target[p]) - 97

            for j in range(x + 1, 26):

                if remaining[j] > 0:
                    remaining[j] -= 1

                    # Keep the prefix equal to target
                    left = target[:p]

                    # Make this position bigger
                    left += chr(j + 97)

                    # Put remaining characters in smallest order
                    for k in range(26):
                        left += chr(k + 97) * remaining[k]

                    return make_palindrome(left)

        return ""