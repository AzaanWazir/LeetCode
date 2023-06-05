class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        currentIndex = 0
        lookDistance = 0
        while (currentIndex + lookDistance < len(nums)):
            if (nums[currentIndex] == 0):
                while (nums[currentIndex + lookDistance] == 0):
                    lookDistance += 1
                    if currentIndex + lookDistance >= len(nums):
                        return
                nums[currentIndex] = nums[currentIndex + lookDistance]
                nums[currentIndex + lookDistance] = 0
            
            currentIndex += 1
                
                
                
                
        """
        Do not return anything, modify nums in-place instead.
        """
        