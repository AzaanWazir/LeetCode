class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        aPos, bPos, cPos = -1, -1, -1
        firstSetFound = False
        ans = 0
        left = -1
        right = 0
        
        for i, letter in enumerate(s):
            leftChange = False
            
            if letter == "a":
                aPos = i
            if letter == "b":
                bPos = i
            if letter == "c":
                cPos = i
            
            if aPos != -1 and bPos != -1 and cPos != -1:  
                newLeft = min(aPos, bPos, cPos)
                if (newLeft > left):
                    leftChange = True
                    if left == -1:
                        left = 0
                right = i

                    
                if leftChange:
                    if not firstSetFound:
                        leftTiles = newLeft - left + 1
                        firstSetFound = True
                    else:
                        leftTiles = newLeft - left
                    rightTiles = len(s) - right
                    ans += leftTiles * rightTiles
                    left = newLeft
        return ans