#Given an array of integers, find two numbers such that they add up to a specific target number.

#The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

#You may assume that each input would have exactly one solution.

#Input: numbers={2, 7, 11, 15}, target=9
#Output: index1=1, index2=2

import unittest
#solution
class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        returnList = []
        
        #using sort O(nlog n) to reduce time complexity
        #sort index in num[k] order, from small to large
        
        indexSort = sorted(range(len(num)), key = lambda k: num[k])

        head = 0
        tail = len(num) - 1
        
        while head != tail:
            
            s = num[indexSort[head]] + num[indexSort[tail]]
            
            if s == target:
                return min([indexSort[head]+1,indexSort[tail]+1]), max([indexSort[head]+1,indexSort[tail]+1]) #example list index start with 1
                
            elif s < target:
                head += 1
                
            else:
                tail -= 1

        
# test
class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
        self.m = [2, 7, 11, 15] #sample
        self.m1 = [0,4,3,0] #duplicate number
        self.m2 = [3,2,4] #more than one pair

    def test_search(self):
        self.assertEqual(self.sol.twoSum(self.m, 9), (1,2))

    def test_search1(self):
        self.assertEqual(self.sol.twoSum(self.m1, 0), (1,4))

    def test_search2(self):
        self.assertEqual(self.sol.twoSum(self.m2, 6), (2,3))
suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
unittest.TextTestRunner(verbosity=2).run(suite)
