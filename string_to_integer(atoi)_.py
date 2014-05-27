class Solution:
    # @return an integer
    def atoi(self, str):
        num_str = ['1','2','3','4','5','6','7','8','9','0']
        num = 0
        met_num = False
        negative = False
        for i in range(len(str)):
            if met_num == False and str[i] == ' ':
                pass
            elif met_num == False and str[i] == '-':
                negative = True
                met_num = True
            elif met_num == False and str[i] == '+':
                negative = False
                met_num = True
            elif str[i] not in num_str:
                break
            else:
                met_num = True
                num *= 10
                num += int(str[i])
        if negative:
            if num > 2**31:
                num = 2**31
            num = -num
        else:
            if num > 2**31-1:
                num = 2**31-1
        return num

if __name__ == '__main__':
    test = Solution()
    s1 = "010"
    s2 = "+-2"  # should be converted to 0
    s3 = "   +0 123" # should return 0
    s4 = "    -0012a42"  # should return -12
    s5 = "2147483648" # should return 2147483647
    print test.atoi(s5)

    raw_input()