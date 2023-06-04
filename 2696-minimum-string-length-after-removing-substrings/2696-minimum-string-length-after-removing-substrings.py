class Solution:
    def minLength(self, s: str) -> int:
        currentLeft = 0
        while (currentLeft < len(s)-1):
            currentRight = currentLeft + 1
            if s[currentLeft] == "A" and s[currentRight] == "B":
                s = s[:currentLeft] + s[currentRight + 1:]
                currentLeft = currentLeft - 2 if currentLeft - 2 >= 0 else 0
                continue
            if s[currentLeft] == "C" and s[currentRight] == "D":
                s = s[:currentLeft] + s[currentRight + 1:]
                currentLeft = currentLeft - 2 if currentLeft - 2 >= 0 else 0
                continue
            currentLeft += 1
        return len(s)