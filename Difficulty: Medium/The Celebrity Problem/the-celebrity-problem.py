class Solution:
    def celebrity(self, mat):
        n = len(mat)
        stack = [i for i in range(n)]

        # Step 1: Find potential celebrity
        while len(stack) > 1:
            a = stack.pop()
            b = stack.pop()
            if mat[a][b] == 1:
                stack.append(b)  # a knows b → a can't be celebrity
            else:
                stack.append(a)  # a doesn't know b → b can't be celebrity

        if not stack:
            return -1

        celeb = stack.pop()

        # Step 2: Verify celebrity
        for i in range(n):
            if i != celeb:
                if mat[celeb][i] == 1 or mat[i][celeb] == 0:
                    return -1

        return celeb
