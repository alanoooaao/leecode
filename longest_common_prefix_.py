class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        # the lonest common prefix string means the longest substring
        # that strings start with in common
        common_prefix = ''
        if strs == []:
            return ''
        i = 0
        while True:
            for s in strs:
                if i < len(s) and s[i] == strs[0][i]:
                    pass
                else:
                    return common_prefix
            common_prefix += strs[0][i]
            i += 1
        