class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        new = [""]*len(s)
        for i in range(0,len(s)):
            new[indices[i]] = s[i]
        return "".join(new)