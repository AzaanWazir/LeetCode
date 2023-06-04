class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        #Keep track of max
        #Keep track of considered paths
        #For item in list
            #If I have already been considered ignore me
            #If I haven't been considered
                #Keep track of node path all the way to head ID or last calculated ID in a stack
                #Go through stack
                    #For each node in stack, define path cost in considered paths
                #If after I have been considered I am bigger than max make me max
        #Return max
        
        considered = {-1: 0}
        ans = 0
        for employee in range(n):
            if (not (employee in considered)):
                path = [employee, manager[employee]]
                while (not (path[-1] in considered)) and path[-1] != -1:
                    path.append(manager[path[-1]])
                if path[-1] in considered:
                    currentSum = considered[path.pop(-1)]
                else:
                    currentSum = 0
                while len(path) > 0:
                    currentNode = path.pop(-1)
                    currentSum += informTime[currentNode]
                    considered[currentNode] = currentSum
                    ans = max(currentSum, ans)
        return ans
                