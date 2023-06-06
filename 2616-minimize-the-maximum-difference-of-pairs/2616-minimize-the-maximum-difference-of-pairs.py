class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
    
        if p == 0:
            return 0
    
        def canMakeDiff(diff):
            i = 1
            validPairs = 0
            while (i < len(nums)):
                if (abs(nums[i-1] - nums[i]) <= diff):
                    validPairs += 1
                    i += 1
                i += 1
                if validPairs == p:
                    return True
            return False

        left = 0
        right = nums[-1]
        mid = (left + right) // 2
        while left < right:
            if canMakeDiff(mid):
                right = mid
            else:
                left = mid + 1
            mid = (left + right) // 2

        return left
    