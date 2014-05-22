class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        sort_num = num[:]
        sort_num.sort()
        i = 0
        j = len(num) - 1
        while i < j:
            if sort_num[i] + sort_num[j] < target:
                i += 1
            elif sort_num[i] + sort_num[j] > target:
                j -= 1
            elif sort_num[i] + sort_num[j] == target:
                break

        res = []
        for index in range(len(num)):
            if num[index] == sort_num[i] or num[index] == sort_num[j]:
                res.append(index)

        return (res[0]+1, res[1]+1)


if __name__ == '__main__':
    s = Solution()
    print s.twoSum([3, 2, 4], 6)

    raw_input()