class Solution:
    # @return an integer
    def reverse(self, x):
        negative = (x < 0)
        y = 0
        if negative:
            x = -x
        while x > 0:
            y = y * 10 + x % 10
            x = x//10
        if negative:
            y = -y
        return y