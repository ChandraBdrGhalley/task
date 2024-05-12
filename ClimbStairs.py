class Solution(object):
    n=0
    def climbStaries(self, n):
        n=10
        step = {}#Empty dict.
        return self.ways(n, step)

    def ways(self, n, step):
        if n in step:
            return step[n]
        if n==1:
            return 1
        elif n ==2:
            return 2
        
        step[n]= self.ways(n-1, step) + self.ways(n-2, step)
        return step[n]
        

        
