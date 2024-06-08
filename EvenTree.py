from collections import defaultdict

def evenForest(t_nodes, t_edges, t_from, t_to):
    tree = defaultdict(list)
    for u, v in zip(t_from, t_to):
        tree[u].append(v)
        tree[v].append(u)

    subtree_size = [0] * (t_nodes + 1)
    
    def dfs(node, parent):
        subtree_size[node] = 1
        for neighbor in tree[node]:
            if neighbor != parent:
                dfs(neighbor, node)
                subtree_size[node] += subtree_size[neighbor]

    dfs(1, -1)

    removable_edges = 0
    for i in range(2, t_nodes + 1):
        if subtree_size[i] % 2 == 0:
            removable_edges += 1
    
    return removable_edges

print(evenForest(10,9,[2, 3, 4, 5, 6, 7, 8, 9, 10],[1, 1, 3, 2, 1, 2, 6, 8, 8]))