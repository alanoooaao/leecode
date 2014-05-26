class Solution:
    # @return a string
    def longestPalindrome(self, s):
        max_length = 0
        palindromic_substring = ''
        for i in range(len(s)):
        # if the palindrome length is odd
            side = 0
            while i-side>=0 and i+side<len(s):
                if s[i-side] == s[i+side]:
                    side += 1
                else:
                    break
            if max_length < 2 * side - 1:
                max_length = 2 * side - 1
                palindromic_substring = s[i-side+1:i+side]
        
        for i in range(len(s)-1):
        # if the palindrome length is even
            side = 0
            while i-side>=0 and i+1+side<len(s):
                if s[i-side] == s[i+1+side]:
                    side += 1
                else:
                    break
            if max_length < 2 * side:
                max_length = 2 * side 
                palindromic_substring = s[i-side+1:i+side+1]
                
        return palindromic_substring


if __name__ == '__main__':
    test = Solution()
    s1 = "whdqcudjpisufnrtsyupwtnnbsvfptrcgvobbjglmpynebblpigaflpbezjvjgbmofejyjssdhbgghgrhzuplbeptpaecfdanhlylgusptlgobkqnulxvnwuzwauewcplnvcwowmbxxnhsdmgxtvbfgnuqdpxennqglgmspbagvmjcmzmbsuacxlqfxjggrwsnbblnnwisvmpwwhomyjylbtedzrptejjsaiqzprnadkjxeqfdpkddmbzokkegtypxaafodjdwirynzurzkjzrkufsokhcdkajwmqvhcbzcnysrbsfxhfvtodqabvbuosxtonbpmgoemcgkudandrioncjigbyizekiakmrfjvezuzddjxqyevyenuebfwugqelxwpirsoyixowcmtgosuggrkdciehktojageynqkazsqxraimeopcsjxcdtzhlbvtlvzytgblwkmbfwmggrkpioeofkrmfdgfwknrbaimhefpzckrzwdvddhdqujffwvtvfyjlimkljrsnnhudyejcrtrwvtsbkxaplchgbikscfcbhovlepdojmqybzhbiionyjxqsmquehkhzdiawfxunguhqhkxqdiiwsbuhosebxrpcstpklukjcsnnzpbylzaoyrmyjatuovmaqiwfdfwyhugbeehdzeozdrvcvghekusiahfxhlzclhbegdnvkzeoafodnqbtanfwixjzirnoaiqamjgkcapeopbzbgtxsjhqurbpbuduqjziznblrhxbydxsmtjdfeepntijqpkuwmqezkhnkwbvwgnkxmkyhlbfuwaslmjzlhocsgtoujabbexvxweigplmlewumcone"
    s2 = 'a'
    s3 = 'adfasdfasdottttoadfasgsodg'
    print test.longestPalindrome(s3)

    raw_input()