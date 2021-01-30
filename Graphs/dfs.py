def depth_first_search_recursive(graph,node,seen):
    seen[start] = True
    for neighbhor in graph[start]:
        if neighbhor not in seen:
            depth_first_search_recursive(graph,neighbhor,seen)



def depth_first_search_iterative(graph,start=0):
    seen[start] = True
    to_visit = [start]
    while to_visit:
        current_node = to_visit.pop()
        for neighbhor in graph[current_node]:
            if not seen[neighbhor]:
                to_visit.append[neighbhor]
                seen[neighbhor] = True

