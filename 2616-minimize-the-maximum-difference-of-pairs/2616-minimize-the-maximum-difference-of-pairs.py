class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0
        
        nums.sort()
    
        def canMakeDiff(diff):
            validPairs = 0
            skip = False
            for i in range(len(nums)):
                if skip:
                    skip = False
                    continue
                if (abs(nums[i-1] - nums[i]) <= diff):
                    validPairs += 1
                    skip = True
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
    