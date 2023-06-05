class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        currDigit = 0
        while currDigit < len(digits):
            if digits[len(digits) - currDigit - 1] + 1 > 9:
                digits[len(digits) - currDigit - 1] = 0
                currDigit += 1
            else:
                digits[len(digits) - currDigit - 1] += 1
                return digits
        digits = [1] + digits
        return digits