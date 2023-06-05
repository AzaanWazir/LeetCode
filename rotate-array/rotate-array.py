class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        right = nums[-k:]
        left = nums[:-k]
        new_nums = right + left
        for i in range(len(new_nums)):
            nums[i] = new_nums[i]
        
        
        """
        Do not return anything, modify nums in-place instead.
        """
        