class Solution:
    def maxPower(self, s: str) -> int:
        ans = 0
        runningSum = 0
        currLetter = ""
        for letter in s:
            if letter == currLetter:
                runningSum += 1
            else:
                ans = max(ans, runningSum)
                runningSum = 1
                currLetter = letter
        ans = max(ans, runningSum)
        return ans