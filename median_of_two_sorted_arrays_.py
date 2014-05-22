class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        merge_list = []

        index_a = 0
        index_b = 0

        while index_a < len(A) and index_b < len(B):
            if A[index_a] <= B[index_b]:
                merge_list.append(A[index_a])
                index_a += 1
            elif A[index_a] >= B[index_b]:
                merge_list.append(B[index_b])
                index_b += 1

        if index_a == len(A):
            merge_list.extend(B[index_b:])
        elif index_b == len(B):
            merge_list.extend(A[index_a:])

        length = len(merge_list)
        if length%2 == 0:
            return (merge_list[length/2-1]+merge_list[length/2])/2.0
        else:
            return merge_list[length/2]

if __name__ == '__main__':
    s = Solution()
    print s.findMedianSortedArrays([1,2,3,6],[4,5,7,8])

    raw_input()