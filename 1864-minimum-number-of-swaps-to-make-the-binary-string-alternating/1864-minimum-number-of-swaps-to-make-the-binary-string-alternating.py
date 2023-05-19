class Solution:
    def minSwaps(self, s: str) -> int:
        Os = 0
        Is = 0
        EvenOs = 0
        EvenIs = 0
        for i, letter in enumerate(s):
            if letter == '0':
                Os += 1
                if i % 2 == 0:
                    EvenOs += 1
                
            else:
                Is += 1
                if i % 2 == 0:
                    EvenIs += 1
        if abs(Os - Is) > 1:
            return -1
        else:
            if Os == Is:
                return min(EvenOs, EvenIs)
            elif Os > Is:
                return Os - EvenOs
            else:
                return Is - EvenIs


