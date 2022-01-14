# program to depth first search

def depth_first_search(graph, start_node, visited_node=None):
    if visited_node is None:
        visited_node=set()
    visited_node.add(start_node)

    print(start_node)
    for next_node in graph[start_node] - visited_node:
        depth_first_search(graph, next_node, visited_node)
    return visited_node

graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

depth_first_search(graph, '0')