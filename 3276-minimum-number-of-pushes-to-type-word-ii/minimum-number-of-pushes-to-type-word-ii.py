from collections import Counter

class Solution(object):
    def minimumPushes(self, word):
        freq = Counter(word)

        counts = sorted(freq.values(), reverse=True)

        pushes = 0

        for i in range(len(counts)):
            pushes += counts[i] * (i // 8 + 1)

        return pushes