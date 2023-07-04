class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        maximumIndex = 0
        minimumIndex = 0
        
        for i, num in enumerate(nums):
            if num > nums[maximumIndex]:
                maximumIndex = i
            if num < nums[minimumIndex]:
                minimumIndex = i
        
        length = len(nums)
        left = min(maximumIndex, minimumIndex)
        right = max(maximumIndex, minimumIndex)
        
        return min(left + 1 + (length - right), right + 1, length - (left))
        