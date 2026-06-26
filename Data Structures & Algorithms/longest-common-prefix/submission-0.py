class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def commonPre(x,y):
            s=[]
            for i in range(len(x)):
                if x[i]==y[i]:
                    s.append(x[i])
                else:
                    break
            return ''.join(s)
        it=iter(strs)
        a = next(it)
        for i in it:
            a=commonPre(a,i)
        return a
