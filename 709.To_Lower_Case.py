# Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.


class Solution:
    def toLowerCase(self, s: str) -> str:
        new = ""
        for c in s:
            new += c.lower()
        return new