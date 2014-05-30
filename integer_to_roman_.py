class Solution:
    # @return a string
    def intToRoman(self, num):
        mapping = {0:'', 1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
        units = [1000, 100, 10, 1]
        roman = ''
        for i in units:
            count = num // i
            if count == 2:
                roman += mapping[i] + mapping[i]
            elif count == 3:
                roman += mapping[i] + mapping[i] * 2
            elif count == 4:
                roman += mapping[i] + mapping[5*i]
            elif count == 6:
                roman += mapping[5*i] + mapping[i]
            elif count == 7:
                roman += mapping[5*i] + mapping[i] * 2
            elif count == 8:
                roman += mapping[5*i] + mapping[i] * 3
            elif count == 9:
                roman += mapping[i] + mapping[10*i]
            else:
                roman += mapping[count*i]
            num = num % i
        return roman

if __name__ == '__main__':
    test = Solution()
    print test.intToRoman(3999)

    raw_input()