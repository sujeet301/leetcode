class Solution(object):
    def maximumWeight(self, intervals):
        n = len(intervals)

        # [start, end, weight, original_index]
        arr = []

        for i in range(n):
            arr.append([
                intervals[i][0],
                intervals[i][1],
                intervals[i][2],
                i
            ])

        # Sort by start
        arr.sort()

        # Store all starting positions
        starts = [0] * n

        for i in range(n):
            starts[i] = arr[i][0]

        # dp(i, k):
        # best answer from i onward using at most k intervals
        memo = {}

        def find_next(end):
            # First index whose start > end
            left = 0
            right = n

            while left < right:
                mid = (left + right) // 2

                if starts[mid] <= end:
                    left = mid + 1
                else:
                    right = mid

            return left

        def dp(i, k):
            if i == n or k == 0:
                return (0, ())

            if (i, k) in memo:
                return memo[(i, k)]

            # Don't take current interval
            skip = dp(i + 1, k)

            start, end, weight, index = arr[i]

            # Take current interval
            j = find_next(end)

            next_weight, next_indices = dp(j, k - 1)

            take_weight = weight + next_weight
            take_indices = tuple(sorted((index,) + next_indices))

            # Choose the better answer
            if take_weight > skip[0]:
                answer = (take_weight, take_indices)

            elif take_weight < skip[0]:
                answer = skip

            else:
                # Same weight -> lexicographically smaller
                if take_indices < skip[1]:
                    answer = (take_weight, take_indices)
                else:
                    answer = skip

            memo[(i, k)] = answer
            return answer

        return list(dp(0, 4)[1])