def max_treasure(N, K, treasures, bridges):
    from collections import defaultdict, deque
    graph = defaultdict(list)
    for a, b in bridges:
        graph[a].append(b)
        graph[b].append(a)
    def bfs(start):
        visited = set()
        queue = deque([start])
        all_nodes = []
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                all_nodes.append(node)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        return all_nodes
    visited = set()
    max_value = 0
    for i in range(1, N + 1):
        if i not in visited:
            component_nodes = bfs(i)
            visited.update(component_nodes)
            if len(component_nodes) <= K:
                max_value += sum(treasures[node - 1] for node in component_nodes)
            else:
                max_value += sum(sorted((treasures[node - 1] for node in
component_nodes), reverse=True)[:K])
    return max_value


N, K = map(int, input().split())
treasures = list(map(int, input().split()))
bridges = []
for _ in range(N-1):
 i1, i2 = map(int, input().split())
 bridges.append((i1, i2))
print(max_treasure(N, K, treasures, bridges))