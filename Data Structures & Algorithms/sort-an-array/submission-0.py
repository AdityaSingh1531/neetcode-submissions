class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            for i in range(len(nums)-1):
                if nums[i]>nums[i+1]:
                    nums[i+1],nums[i]=nums[i],nums[i+1]
        return nums
