class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        adj_matrix = [[] for i in range((A+1))]
        number_of_edge = len(B)
        for i in range(number_of_edge):
            adj_matrix[B[i][0]].append(B[i][1])
        visited = [0] * (A+1)
        from collections import deque
        q = deque()
        q.append(1)
        visited[1] = 1
        while q:
            v = q.popleft()
            for i in adj_matrix[v]:
                if visited[i] != 1:
                    q.append(i)
                    visited[i] = 1
        if visited[A] == 1:
            return 1
        return 0

if __name__ == "__main__":
    A= 4
    B= [[1, 2],  [2, 3], [4, 3]]
    obj = Solution()
    print(obj.solve(A,B))
