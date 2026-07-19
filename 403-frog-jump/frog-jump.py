class Solution(object):
    def canCross(self, stones):
        stone_set = set(stones)
        last = stones[-1]
        memo = {}

        def dfs(position, jump):
            if (position, jump) in memo:
                return memo[(position, jump)]

            if position == last:
                return True

            for step in [jump - 1, jump, jump + 1]:
                if step > 0 and position + step in stone_set:
                    if dfs(position + step, step):
                        memo[(position, jump)] = True
                        return True

            memo[(position, jump)] = False
            return False

        return dfs(0, 0)