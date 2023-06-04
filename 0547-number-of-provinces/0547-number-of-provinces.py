class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #Keep track of considered nodes
        #For each index
            #Keep a list of connected nodes
            #Go in my column and see who I am connected to
            #Add connections to queue
            #While queue is not empty:
                #Add node to connected nodes
                #See if neighbours in connected node
                    #if in connected nodes ignore
                    #else add into queue array
            #After done sorting add list of connected nodes to considered therefore to skip
        #At the end return length of graphs
        ans = 0
        considered = {}
        for i in range(len(isConnected)):
            if i in considered:
                continue
            considered[i] = True
            queue = [i]
            # for j, connection in enumerate(isConnected[i]):
            #     if connection == 0:
            #         continue
            #     connectedNodes.add(j)
            #     queue.append(j)
            while len(queue) > 0:
                index = queue.pop(-1)
                for j, connection in enumerate(isConnected[index]):
                    if j in considered:
                        continue
                    if connection == 0:
                        continue
                    queue.append(j)
                    considered[j] = True
            ans += 1
        return ans
