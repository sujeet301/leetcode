class Solution(object):
    def removeOuterParentheses(self, s):
        answer = []
        depth = 0

        for ch in s:
            if ch == '(':
                depth += 1

                if depth > 1:
                    answer.append(ch)

            else:
                depth -= 1

                if depth > 0:
                    answer.append(ch)

        return ''.join(answer)