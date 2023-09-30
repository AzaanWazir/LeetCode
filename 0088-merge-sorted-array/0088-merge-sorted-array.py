class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        currIndex1 = len(nums1) - len(nums2) - 1
        currIndex2 = len(nums2) - 1
        writeIndex = len(nums1) - 1

        while (currIndex2 >= 0):
            if nums1[currIndex1] > nums2[currIndex2] and currIndex1 >= 0:
                nums1[writeIndex] = nums1[currIndex1]
                currIndex1 -= 1
            else:
                nums1[writeIndex] = nums2[currIndex2]
                currIndex2 -= 1
            writeIndex -= 1

        """
        Do not return anything, modify nums1 in-place instead.
        """
        