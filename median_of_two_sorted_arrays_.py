class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        length = len(A) + len(B)
        if length%2 == 0:
            return (self.findKthSmallest(A, B, length/2) + self.findKthSmallest(A, B, length/2 + 1))/2.0
        else:
            return self.findKthSmallest(A, B, length/2 + 1)

    def findKthSmallest(self, A, B, k):
        # k <= len(A) + len(B) and k > 0
        if len(A) == 0:
            return B[k-1]
        elif len(B) == 0:
            return A[k-1]
        elif k == 1 and A[0] <= B[0]:
            return A[0]
        elif k == 1 and B[0] < A[0]:
            return B[0]
        else:
            ia = int(k/2)
            ib = k - ia
            if ia > len(A):
                ia = len(A)
                ib = k - ia
            elif ib > len(B):
                ib = len(B)
                ia = k - ib
                
            if A[ia - 1] <= B[ib - 1]:
                return self.findKthSmallest(A[ia:], B, k-ia)
            elif A[ia - 1] > B[ib - 1]:
                return self.findKthSmallest(A, B[ib:], k-ib)


if __name__ == '__main__':
    s = Solution()
    print s.findMedianSortedArrays([2,3,4],[1])

    raw_input()