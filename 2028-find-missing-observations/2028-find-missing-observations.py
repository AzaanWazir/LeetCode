class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        #Get m
        #Note sum(rolls) + sum(unknown_rolls) / (m + n) == mean
        #Therefore sum(unknown_rolls) = mean * (m + n) - sum(rolls)
        #We can find the average roll of n by doing sum(unknown_rolls) / n
        #Lets say we get 4.5, then we would make the array of unknown rolls 4 * n.
        #We can then do sum(unknown_rolls) % n, to find out how much additional points are needed
        #Which can be evenly distributed among the die
        
        m = len(rolls)
        unknown_sum = (mean * (m + n)) - sum(rolls)
        average_n_roll = unknown_sum // n
        extra_points = unknown_sum % n
        
        if average_n_roll > 6:
            return []
        if average_n_roll == 6 and extra_points > 0:
            return []
        if average_n_roll <= 0:
            return []
        
        ans = [average_n_roll] * n
        for i in range(extra_points):
            ans[i] += 1
        return ans