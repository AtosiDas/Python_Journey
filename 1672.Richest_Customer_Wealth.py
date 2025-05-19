class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for account in accounts:
            sum = 0
            for i in range(0, len(account)):
                sum += account[i]
            if max_wealth < sum:
                max_wealth = sum
        return max_wealth
        