class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for j in range(len(matrix)):
            for i in matrix[j]:
                if i == target:
                    return True

        return False   
                
