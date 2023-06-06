class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        #For every word in dictionary
            #Skip word if len(word) < len(ans)
            #Skip word if len(word) > len(s)
            #Go through s letter by letter and see if we can respell the word
            
        ans = ""
        for word in dictionary:
            if len(word) < len(ans):
                continue
            if len(word) == len(ans):
                if word > ans:
                    continue
            if len(word) > len(s):
                continue
                
            
            runningIndex = 0
            currentLetterIndex = 0
            while (runningIndex < len(s)):
                if s[runningIndex] == word[currentLetterIndex]:
                    currentLetterIndex += 1
                runningIndex += 1
                if currentLetterIndex == len(word):
                    break
            if currentLetterIndex == len(word):
                ans = word
        return ans