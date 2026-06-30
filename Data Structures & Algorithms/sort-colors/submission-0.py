class Solution:
    def sortColors(self, nums: List[int]) -> None:
        cnt=[0,0,0]
        for i in nums:
            cnt[i]+=1
        j=i=0
        while i<(len(nums)):
            if cnt[j]!=0:
                nums[i]=j
                cnt[j]-=1
                i+=1
            else:
                j+=1