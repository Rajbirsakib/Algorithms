def dfs(node, adjList, visited):
    visited[node] = True
    print(node, end=" ")

    for neighbor in adjList[node]:
        if not visited[neighbor]:
            dfs(neighbor, adjList, visited)

V = 11
adjList = {1:[4, 2], 2:[1, 3, 5, 7, 8], 3:[4, 2, 10, 9], 4:[1, 3], 5:[6, 2, 8, 7], 6:[5], 7:[2, 5, 8], 8:[2, 5, 7], 9:[3], 10:[3]}

visited = [False] * V
print("Depth-First Search starting from node 1:")
dfs(1, adjList, visited)
