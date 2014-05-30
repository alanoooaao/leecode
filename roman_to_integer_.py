class Solution:
    # @return an integer
    def romanToInt(self, s):
        mapping = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        num = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1 and mapping[s[i]] < mapping[s[i+1]]:
                num += mapping[s[i+1]] - mapping[s[i]]
                i += 2
            else:
                num += mapping[s[i]]
                i += 1
        return num

if __name__ == '__main__':
    test = Solution()
    r = 'CXIX'
    print test.romanToInt(r)

    raw_input()