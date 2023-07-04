class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        asc = sorted(nums)
        right = len(asc) - 1
        left = len(asc) - 2
        ans = 0
        print(asc)
        while (left >= 0):
            if asc[right] > asc[left]:
                right -= 1
                left -= 1
                ans += 1
            elif left == 0:
                right -= 1
                left = right - 1
            else:
                left -= 1
        return ans