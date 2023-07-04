class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        adds = 0
        subs = 0
        for i in range(len(nums1)):
            num1 = nums1[i]
            num2 = nums2[i]
            
            if num1 - num2 != 0 and k == 0:
                return -1
            if num1 - num2 != 0 and abs(num2 - num1) % k != 0:
                return -1
            if num1 - num2 == 0:
                continue

            diff = num2 - num1
            
            if diff > 0:
                subs += diff / k
            else:
                adds += (diff * -1) / k

        return int(adds) if adds == subs else -1