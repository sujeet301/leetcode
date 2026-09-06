class Solution(object):
    def numDistinct(self, s, t):
        m = len(s)
        n = len(t)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Empty t can always be formed in exactly 1 way
        for i in range(m + 1):
            dp[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):

                # Don't use s[i-1]
                dp[i][j] = dp[i - 1][j]

                # Use s[i-1] if it matches t[j-1]
                if s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]

        return dp[m][n]