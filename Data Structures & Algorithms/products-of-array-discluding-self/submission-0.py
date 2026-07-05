class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=[1]
        post=[1]
        for i in range(len(nums)-1):
            pre.append(pre[-1]*nums[i])
            post.append(post[-1]*nums[len(nums)-1-i])
        post.reverse()
        ans=[]
        for i in range(len(nums)):
            ans.append(post[i]*pre[i])
        return ans