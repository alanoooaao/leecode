class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        single = {}
        for i in range(len(A)):
            if A[i] not in single:
                single[A[i]] = 1
            elif A[i] in single:
                single.pop(A[i])
        for num in single:
            return num