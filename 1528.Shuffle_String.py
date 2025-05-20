# You are given a string s and an integer array indices of the same length. The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

# Return the shuffled string.


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        new = [""]*len(s)
        for i in range(0,len(s)):
            new[indices[i]] = s[i]
        return "".join(new)