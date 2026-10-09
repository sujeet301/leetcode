class Solution(object):
    def minInsertions(self, s):
        insertions = 0
        open_count = 0
        i = 0
        n = len(s)

        while i < n:
            if s[i] == '(':
                open_count += 1

            else:
                # Check whether two consecutive ')' exist
                if i + 1 < n and s[i + 1] == ')':
                    i += 1
                else:
                    # Insert a missing ')'
                    insertions += 1

                if open_count == 0:
                    # Insert a missing '('
                    insertions += 1
                else:
                    open_count -= 1

            i += 1

        # Each unmatched '(' needs two ')'
        insertions += open_count * 2

        return insertions