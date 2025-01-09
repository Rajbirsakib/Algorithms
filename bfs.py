from collections import deque

def bfs(start, adjList, V):
    visited = [False] * V
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in adjList[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

V = 11
adjList = {1:[4, 2], 2:[1, 3, 5, 7, 8], 3:[4, 2, 10, 9], 4:[1, 3], 5:[6, 2, 8, 7], 6:[5], 7:[2, 5, 8], 8:[2, 5, 7], 9:[3], 10:[3]}

print("Breadth-First Search starting from node 1:")
bfs(1, adjList, V)
