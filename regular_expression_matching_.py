class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        if s == p:
            return True
        elif p == '':
            return False

        p_char = []
        p_flexible = []
        for i in range(len(p)-1):
            if p[i] != '*' and p[i+1] == '*':
                p_char.append(p[i])
                p_flexible.append(True)
            elif p[i] != '*' and p[i+1] !='*':
                p_char.append(p[i])
                p_flexible.append(False)
        
        if p[len(p)-1] != '*':
            p_char.append(p[len(p)-1])
            p_flexible.append(False)

        # print p_char
        # print p_flexible
        # print "~~~~~~~~~~~~~~~~~~~~~~~~"

        slices = []
        flexible = []
        for i in range(len(p_char)):
            if i == 0:
                j = 0
                slices.append([p_char[i]])
                flexible.append(p_flexible[i])
            elif p_flexible[i] == p_flexible[i-1]:
                slices[j].append(p_char[i])
            elif p_flexible[i] != p_flexible[i-1]:
                j += 1
                slices.append([p_char[i]])
                flexible.append(p_flexible[i])


        if flexible[0] == False:
            slices = [['']] + slices
            flexible = [True] + flexible

        # print slices
        # print flexible
        # print "------------------------"

        return self.checkMatch(s,slices,flexible)


    def checkMatch(self, s, slices, flexible):
        if s == '' and len(slices) <= 1:
            return True
        elif s != '' and len(slices) == 1 and self.ifSuperMatch(s, slices[0]):
            return True
        elif s == '' and len(slices) > 1:
            return False
        elif s != '' and len(slices) == 1 and (not self.ifSuperMatch(s, slices[0]) ):
            return False
        elif s != '' and len(slices) > 1:
            i = -1
            while True:
                i = self.findMatch(s, i, slices[0], slices[1])
                if i == -2:
                    break
                j = i + len(slices[1])
                if self.checkMatch(s[j:], slices[2:], flexible[2:]):
                    return True
                else:
                    pass
            return False

    def ifSuperMatch(self, s, l):
        # s is a string, l is a list of single characters
        for c in s:
            for i in range(len(l)):
                if self.isEqual(c, l[i]):
                    l = l[i:]
                    break
                elif i == len(l) - 1:
                    return False
                else:
                    pass
        return True

    def ifNormalMatch(self, s, l):
        # s is a string, l is a list of single characters
        for i in range(len(s)):
            if self.isEqual(s[i],l[i]) == False:
                return False
        return True

    def isEqual(self, c1, c2):
        # c1, c2 are both single character
        if c1 == c2 or c2 == '.':
            return True
        else:
            return False

    def findMatch(self, s, i, l1, l2):
        # s is a string, i is index num, l1 and l2 are two lists of single characters
        # l1 is flexible, l2 is not flexible
        # returns a new value of i, and -2 means cannot find match
        if len(s) < len(l2) or i + len(l2) > len(s):
            return -2
        else:
            i += 1
            while i + len(l2) <= len(s):
                if self.ifNormalMatch(s[i:i+len(l2)], l2) and self.ifSuperMatch(s[:i], l1):
                    return i
                else:
                    i += 1
            return -2


if __name__ == '__main__':
    test = Solution()
    print test.isMatch("aa", "a")

    raw_input()