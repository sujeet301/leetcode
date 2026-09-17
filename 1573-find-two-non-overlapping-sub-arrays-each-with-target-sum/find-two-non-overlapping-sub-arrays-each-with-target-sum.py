class Solution(object):
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        INF = float('inf')

        # dp[i] = shortest valid subarray in arr[0:i]
        dp = [INF] * (n + 1)

        # Prefix sum -> latest index
        seen = {0: -1}

        prefix = 0
        answer = INF

        for i in range(n):
            prefix += arr[i]

            # Carry forward the previous best length
            dp[i + 1] = dp[i]

            needed = prefix - target

            if needed in seen:
                j = seen[needed]

                # Length of current subarray
                length = i - j

                # Best previous subarray ends before current starts
                previous = dp[j + 1]

                if previous != INF:
                    answer = min(answer, previous + length)

                # A single subarray is also valid
                dp[i + 1] = min(dp[i + 1], length)

            # Store the latest index
            seen[prefix] = i

        if answer == INF:
            return -1

        return answer