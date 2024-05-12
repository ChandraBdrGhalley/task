'''class Solution(object):
    n = [2,7,11,15]
    target = 9
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return''' 
    
class Solution(object):
    def twoSum(self,nums, target):
        lst = [2,7,11,15]
        num = 9
        for i in range(len(nums)):
            for j in range(len(nums)):
                num = nums[i]+nums[j]
                if num==target and i!=j:
                    lst.append(i)
                    lst.append(j)
                    return lst
        print()