class Solution:
    def knightDialer(self, n: int) -> int:
        # moves = [
        #     set([4,6]),
        #     set([6,8]),
        #     set([7,9]),
        #     set([4,8]),
        #     set([3,9,0]),
        #     set([]),
        #     set([1,7]),
        #     set([2,6]),
        #     set([1,3]),
        #     set([2,4]),
        #     set([4,6])
        # ]
        
        # 1 * 4, 2 * 2, 4 * 2, 0 * 1
        
        # 1 -> 4 & 2
        # 2 -> 1 & 1
        # 4 -> 1 & 1 & 0
        # 0 -> 4 & 4
        
        if n == 1:
            return 10
        
        relevantNums = {
            1: 4,
            2: 2,
            4: 2,
            0: 1,
        }
        
        paths = {
            1: [4, 2],
            2: [1, 1],
            4: [1, 1, 0],
            0: [4, 4]
        }
        
        ans = 0
        for num, multiplier in relevantNums.items():
            queue = {num: 1}
            count = 1
            while count < n:
                next_queue = {
                    1: 0,
                    2: 0,
                    4: 0,
                    0: 0
                }
                for value, amountOfValue in queue.items():
                    for path in paths[value]:
                        next_queue[path] += amountOfValue
                queue = next_queue.copy()
                count += 1
            ans += sum(queue.values()) * multiplier
            ans = ans % (10**9 + 7)
        return ans % (10**9 + 7)
            