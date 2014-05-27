class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        y = 0
        t = x
        while t > 0:
            y = t % 10 + 10 * y
            t = t // 10
        return x == y