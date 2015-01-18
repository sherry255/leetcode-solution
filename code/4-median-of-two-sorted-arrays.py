"""
>>> findMedianSortedArrays([1,2], [1,2])
1.5
>>> findMedianSortedArrays([1,2,3], [4,5])
3
"""

def kth(A, B, k):
    i1, i2 = 0, len(A)
    j1, j2 = 0, len(B)

    while True:
        if i2 <= i1:
            return B[j1+k]
        if j2 <= j1:
            return A[i1+k]

        i = (i1+i2) // 2
        j = (j1+j2) // 2

        if (i-i1)+(j-j1) < k:
            if A[i] < B[j]:
                k -= i + 1 - i1
                i1 = i+1
            else:
                k -= j + 1 - j1
                j1 = j+1
        else:
            if A[i] > B[j]:
                i2 = i
            else:
                j2 = j


def findMedianSortedArrays(A,B):
    l = len(A) + len(B)
    if l % 2:
        return kth(A, B, l//2)
    else:
        return 0.5 * (kth(A, B, l//2-1) + kth(A, B, l//2))
