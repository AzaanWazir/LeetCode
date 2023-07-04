class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        if threshold < 0:
            return 0
        m = len(mat)
        n = len(mat[0])
        prefixSum = [[0]*(n+1) for _ in range(m+1)]
        
        for i, j in product(range(m), range(n)):
            prefixSum[i+1][j+1] = prefixSum[i+1][j] + prefixSum[i][j+1] - prefixSum[i][j] + mat[i][j]


        def canSideLength(sideLength):
            if sideLength > m or sideLength > n:
                return False
            
            for i in range(m - sideLength + 1):
                for j in range(n - sideLength + 1):
                    if prefixSum[i+sideLength][j+sideLength] - prefixSum[i][j+sideLength] - prefixSum[i+sideLength][j] + prefixSum[i][j] <= threshold:
                        return True
            return False
        
        mid = -1
        left = 0
        right = 300
        while left != right:
            mid = (left + right) // 2
            if canSideLength(mid):
                left = mid + 1
            else:
                right = mid
        return left - 1