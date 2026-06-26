class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m=1;cand=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==cand: m+=1
            else: m-=1
            if m==0:
                m=1
                cand=nums[i]
        return cand

