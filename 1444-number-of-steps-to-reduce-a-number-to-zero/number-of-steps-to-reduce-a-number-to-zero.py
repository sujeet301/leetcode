class Solution(object):
    def numberOfSteps(self, num):
        step=0
        while (num!=0):
            step+=1
            if(num%2==0):
                num/=2
            else:
                num-=1
        return step