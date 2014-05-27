class Solution:
    # @return a string
    def convert(self, s, nRows):
        result = ''
        if nRows == 1:
            return s
        interval = 2 * (nRows - 1)
        times, remainder = divmod(len(s), interval)
        for i in range(nRows):
            if i == 0 or i == nRows - 1:
                for j in range(times):
                    result += s[i+interval*j]
                if i <= remainder-1:
                    result += s[i+interval*times]
            else:
                for j in range(times):
                    result += s[i+interval*j]
                    result += s[interval-i+interval*j]
                if i<=remainder-1:
                    result += s[i+interval*times]
                if interval-i<=remainder-1:
                    result += s[interval-i+interval*times]
        return result

if __name__ == '__main__':
    test = Solution()
    print test.convert('ABC', 3)

    raw_input()