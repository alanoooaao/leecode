class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        if s == '':
            return 0
        
        length = []
        substring = []
        for c in s:
            if c not in substring:
                substring.append(c)
            else:
                start = substring.index(c)
                substring = substring[start+1:]+[c]
            length.append(len(substring))
        
        length.sort(reverse = True)
        return length[0]