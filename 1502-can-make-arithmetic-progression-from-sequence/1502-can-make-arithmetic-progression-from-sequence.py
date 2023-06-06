class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr) == 2:
            return True
        arr.sort()
        diff = arr[1] - arr[0]
        for i in range(1, len(arr)):
            if (arr[i] == arr[0] + i * diff):
                pass
            else:
                return False
        return True