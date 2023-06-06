class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if nums[0] > nums[1]:
            largest = 0
            secondLargest = 1
        else:
            largest = 1
            secondLargest = 0
        
        for i, num in enumerate(nums):
            if i == 0 or i == 1:
                continue
            if nums[i] > nums[largest]:
                secondLargest = largest
                largest = i
            else:
                if nums[i] > nums[secondLargest]:
                    secondLargest = i
        
        return largest if nums[largest] >= nums[secondLargest] * 2 else -1
            