class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        
        nums.sort()
        left = 0
        right = left + k - 1
        minimum = nums[right] - nums[left]
        while (right < len(nums)):
            minimum = min(minimum, nums[right] - nums[left])
            left += 1
            right = left + k - 1
        return minimum
                
                