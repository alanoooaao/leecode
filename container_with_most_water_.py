class Solution:
    # @return an integer
    def maxArea(self, height):
        maximum = 0
        width = len(height)
        left = 0
        right = width-1
        while left < right:
            if height[left] <= height[right]:
                area = height[left] * (right-left)
                maximum = max(maximum, area)
                i = left
                while height[i] <= height[left] and i < right:
                    i += 1
                left = i
            elif height[left] > height[right]:
                area = height[right] * (right-left)
                maximum = max(maximum, area)
                i = right
                while height[i] <= height[right] and left < i:
                    i -= 1
                right = i

        return maximum
        