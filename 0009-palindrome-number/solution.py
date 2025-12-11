class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x_copy = x
        reverse = 0
        while x != 0:
            digit = x % 10
            reverse = reverse * 10 + digit
            x //= 10

        return x_copy == reverse
        