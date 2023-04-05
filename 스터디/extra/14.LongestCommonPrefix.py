class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=''
        # if not strs: # [""]
        #     return ans
        for letters in zip(*strs):
            if len(set(letters))==1:
                ans+=letters[0]
            else:
                return ans
        return ans