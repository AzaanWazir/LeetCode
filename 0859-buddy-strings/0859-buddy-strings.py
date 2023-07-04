class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        need = []
        have = []
        letters = set()
        hasDuplicate = False
        
        for i in range(len(s)):
            if s[i] in letters:
                hasDuplicate = True
            letters.add(s[i])
            if s[i] != goal[i]:
                have.append(s[i])
                need.append(goal[i])
        
        print(hasDuplicate)
        if len(need) == 0 and hasDuplicate:
            return True
        if len(need) == 2 and have[0] == need[1] and have[1] == need[0]:
            return True
        return False
                
            