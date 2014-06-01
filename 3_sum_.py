import unittest

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num.sort()
        result = []
        i, j, k = 0, 1, len(num) - 1
        while i < len(num) - 2 and num[i] <= 0:
            if i > 0 and num[i] == num[i-1]:
                i, j = i+1, i+2
                continue
            while j < k:
                if j > i + 1 and num[j] == num[j-1]:
                    j += 1
                    continue
                if k < len(num) - 1 and num[k] == num[k+1]:
                    k -= 1
                    continue

                if num[i] + num[j] + num[k] == 0:
                    result.append([num[i], num[j], num[k]])
                    j += 1
                    k -= 1
                elif num[i] + num[j] + num[k] < 0:
                    j += 1
                elif num[i] + num[j] + num[k] > 0:
                    k -= 1
            i, j, k = i+1, i+2, len(num)-1
        
        return result
                        
class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

        self.num1 = [0,0,0,0]
        self.ans1 = [[0,0,0]]

        self.num2 = [0,7,-4,-7,0,14,-6,-4,-12,11,4,9,7,4,-10,8,10,5,4,14,6,0,-9,5,6,6,-11,1,-8,-1,2,-1,13,5,-1,-2,4,9,9,-1,-3,-1,-7,11,10,-2,-4,5,10,-15,-4,-6,-8,2,14,13,-7,11,-9,-8,-13,0,-1,-15,-10,13,-2,1,-1,-15,7,3,-9,7,-1,-14,-10,2,6,8,-6,-12,-13,1,-3,8,-9,-2,4,-2,-3,6,5,11,6,11,10,12,-11,-14]
        self.ans2 = []

        self.num3 = [7,5,-8,-6,-13,7,10,1,1,-4,-14,0,-1,-10,1,-13,-4,6,-11,8,-6,0,0,-5,0,11,-9,8,2,-6,4,-14,6,4,-5,0,-12,12,-13,5,-6,10,-10,0,7,-2,-5,-12,12,-9,12,-9,6,-11,1,14,8,-1,7,-13,8,-11,-11,0,0,-1,-15,3,-11,9,-7,-10,4,-2,5,-4,12,7,-8,9,14,-11,7,5,-15,-15,-4,0,0,-11,3,-15,-15,7,0,0,13,-7,-12,9,9,-3,14,-1,2,5,2,-9,-3,1,7,-12,-3,-1,1,-2,0,12,5,7,8,-7,7,8,7,-15]
        self.ans3 = []

        self.num4 = [0,-4,-1,-4,-2,-3,2]
        self.ans4 = [[-2,0,2]]

        self.num5 = [-1,0,1,2,-1,-4]
        self.ans5 = [[-1,-1,2],[-1,0,1]]

    # def test_search(self):
    #     self.assertEqual(self.sol.threeSum(self.num1), self.ans1)

    def test_search(self):
        self.assertEqual(self.sol.threeSum(self.num5), self.ans5)


suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
# unittest.TextTestRunner(verbosity=2).run(suite)

            
if __name__ == '__main__':
    test = Solution()
    num0 = [0, 0, 0]
    num1 = [0,0,0,0]
    num2 = [0,7,-4,-7,0,14,-6,-4,-12,11,4,9,7,4,-10,8,10,5,4,14,6,0,-9,5,6,6,-11,1,-8,-1,2,-1,13,5,-1,-2,4,9,9,-1,-3,-1,-7,11,10,-2,-4,5,10,-15,-4,-6,-8,2,14,13,-7,11,-9,-8,-13,0,-1,-15,-10,13,-2,1,-1,-15,7,3,-9,7,-1,-14,-10,2,6,8,-6,-12,-13,1,-3,8,-9,-2,4,-2,-3,6,5,11,6,11,10,12,-11,-14]
    num3 = [-1,0,1,2,-1,-4]
    print test.threeSum(num2)

    raw_input()