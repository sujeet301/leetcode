class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        reserved = {}

        for row, seat in reservedSeats:
            if row not in reserved:
                reserved[row] = set()

            reserved[row].add(seat)

        answer = (n - len(reserved)) * 2

        for row in reserved:
            seats = reserved[row]

            left = 2 not in seats and 3 not in seats and \
                   4 not in seats and 5 not in seats

            middle = 4 not in seats and 5 not in seats and \
                     6 not in seats and 7 not in seats

            right = 6 not in seats and 7 not in seats and \
                    8 not in seats and 9 not in seats

            if left and right:
                answer += 2
            elif left or middle or right:
                answer += 1

        return answer