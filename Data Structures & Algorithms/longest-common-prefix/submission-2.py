class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        class TrieNode:
            def __init__(self):
                self.children={}
                self.end=False
        
        root=TrieNode()
        for word in strs:
            node=root
            for i in word:
                if i not  in node.children:
                    node.children[i]=TrieNode()
                node=node.children[i]
            node.end=True
        
        node=root
        ans=[]
        while len(node.children)==1 and (not node.end):
            ch = next(iter(node.children))
            ans.append(ch)
            node = node.children[ch]
        return ''.join(ans)