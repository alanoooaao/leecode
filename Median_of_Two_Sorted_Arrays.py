#There are two sorted arrays A and B of size m and n respectively. 
#Find the median of the two sorted arrays. 
#The overall run time complexity should be O(log (m+n)).
import unittest

class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        # merge sort 
        mergeList = []
        count = countA  =  countB = 0
        

        while count <= len(A) + len(B) - 1:
            # A, B are not done
            if countA < len(A) and countB < len(B):
                # A is smaller
                if A[countA] <= B[countB]:
                    mergeList.append(A[countA])
                    countA += 1
                    count += 1  
                # B is smaller  
                elif A[countA] > B[countB]:
                    mergeList.append(B[countB])
                    countB += 1
                    count += 1
            # list A is done
            elif countA == len(A):
                mergeList.extend(B[countB:])
                break
            # list B is done
            elif countB == len(B):
                mergeList.extend(A[countA:])
                break
            
        # return median value
        target = len(mergeList)
        if target % 2 == 0: #even
            return (mergeList[target/2] + mergeList[target/2 - 1])/2.0
        else: #odd
            return float(mergeList[target/2])


# test
class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
        self.A = [2, 7, 11, 15] 
        self.B = [4 ,7, 20] #odd
        self.C = [4, 7, 8, 30] #even
        self.D = [] # empty set
        
    def test_search(self):
        self.assertEqual(self.sol.findMedianSortedArrays(self.A, self.B), 7)

    def test_search1(self):
        self.assertEqual(self.sol.findMedianSortedArrays(self.A, self.C), 7.5)

    def test_search2(self):
        self.assertEqual(self.sol.findMedianSortedArrays(self.A, self.D), 9)
        
suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
unittest.TextTestRunner(verbosity=2).run(suite)
