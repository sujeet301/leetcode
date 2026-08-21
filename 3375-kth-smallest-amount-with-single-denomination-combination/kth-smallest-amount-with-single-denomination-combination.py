class Solution(object):
    def findKthSmallest(self, coins, k):

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return (a * b) // gcd(a, b)

        def count(x):
            total = 0
            n = len(coins)

            for mask in range(1, 1 << n):
                value = 1
                bits = 0

                for i in range(n):
                    if mask & (1 << i):
                        value = lcm(value, coins[i])
                        bits += 1

                        if value > x:
                            break

                if value <= x:
                    amount = x // value

                    if bits % 2 == 1:
                        total += amount
                    else:
                        total -= amount

            return total

        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left