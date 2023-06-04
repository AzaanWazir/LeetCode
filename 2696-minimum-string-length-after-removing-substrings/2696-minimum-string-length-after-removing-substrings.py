class Solution:
    def minLength(self, s: str) -> int:
        word = []
        for letter in s:
            word.append(letter)
            if len(word) >= 2:
                if word[-1] == "B" and word[-2] == "A":
                    word = word[:-2]
                elif word[-1] == "D" and word[-2] == "C":
                    word = word[:-2]
        return len(word)