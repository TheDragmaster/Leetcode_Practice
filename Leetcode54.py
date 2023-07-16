class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Time complexity is 0(m*n) which is the dimensions of the matrix , 0(1) is the memory complexity because we arent saving anything just running the code

        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # First go left to right and get every value in the top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # Get every i in the right most column
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break
