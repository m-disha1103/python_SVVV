# 11 may 2026
#leetcode question 01
#two sum
class solution(object):
    def twoSum(self,nums,target):
        dict={}
        for i in range(len(nums)):
            if dict.get(target-nums[i])!=None:
                return [dict[target-nums[i]],i]
            dict[nums[i]]=i
        return []
    