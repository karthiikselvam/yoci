# pylint: disable=too-many-nested-blocks, no-else-return
def find_cycle(graph):
    """find a cycle in an undirected graph

    :param graph: undirected graph in listlist or listdict format
    :returns: list of vertices in a cycle or None
    :complexity: `O(|V|+|E|)`
    """
    n = len(graph)
    prec = [None] * n  # ancestor marks for visited vertices
    for u in range(n):
        if prec[u] is None:  # unvisited vertex
            S = [u]  # start new DFS
            prec[u] = u  # mark root (not necessary for this algorithm)
            while S:
                u = S.pop()
                for v in graph[u]:  # for all neighbors
                    if v != prec[u]:  # except arcs to father in DFS tree
                        if prec[v] is not None:
                            cycle = [v, u]  # cycle found, (u,v) back edge
                            while u not in (prec[v], prec[u]):  # directed
                                u = prec[u]  # climb up the tree
                                cycle.append(u)
                            return cycle
                        else:
                            prec[v] = u  # v is new vertex in tree
                            S.append(v)
    return None

graph = [[1,2],[0,2],[1,0],[2]]
result = find_cycle(graph)
print(result)