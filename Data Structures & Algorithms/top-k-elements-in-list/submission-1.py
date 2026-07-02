class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cn=Counter(nums)
        a=[0]*len(nums)
        ans=[]
        for i in cn:
            f = cn[i]
            if a[f-1]==0:
                a[f-1]=[i]
            else:
                a[f-1].append(i)
        for i in reversed(a):
            if i!=0 and k>0:
                ans.extend(i)
                k-=len(i)
        return ans