class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
                if count[num] == 3:
                    del count[num]
            else:
                count[num] = 1
        return list(count.keys())[0]