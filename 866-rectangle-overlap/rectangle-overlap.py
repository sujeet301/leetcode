class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        if rec1[0] >= rec2[2]:
            return False

        if rec2[0] >= rec1[2]:
            return False

        if rec1[1] >= rec2[3]:
            return False

        if rec2[1] >= rec1[3]:
            return False

        return True