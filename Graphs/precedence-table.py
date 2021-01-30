def dfs_tree(graph, start=0):
    """DFS, build DFS tree in unweighted graph

       :param graph: directed graph in listlist or listdict format
       :param int start: source vertex
       :returns: precedence table
       :complexity: `O(|V|+|E|)`
       """
    to_visit = [start]
    prec = [None] * len(graph)
    while to_visit:              # an empty queue equals False
        node = to_visit.pop()
        for neighbor in graph[node]:
            if prec[neighbor] is None:
                prec[neighbor] = node
                to_visit.append(neighbor)
    return prec                


graph = [[1,2,5],[0,2],[0,1,3,4],[2,4,5],[2,3],[0,3]]
result = dfs_tree(graph,0)
print(result)