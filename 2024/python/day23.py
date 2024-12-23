from utils import *

start_time: float = get_start_time()

graph: dict[str, set[str]] = {}
t_names: set[str] = set()

for line in get_input_lines("day23.txt"):
    cpu1, cpu2 = line.split("-")
    if cpu1.startswith("t"):
        t_names.add(cpu1)
    if cpu2.startswith("t"):
        t_names.add(cpu2)
    graph.setdefault(cpu1, set()).add(cpu2)
    graph.setdefault(cpu2, set()).add(cpu1)

triangles: list[set[str]] = []
for t_name in t_names:
    adj = list(graph[t_name])
    for i, cpu1 in enumerate(adj):
        for cpu2 in adj[i + 1:]:
            if cpu2 in graph[cpu1]:
                triangle = {t_name, cpu1, cpu2}
                if triangle not in triangles:
                    triangles.append(triangle)
print(len(triangles))

max_group: set[str] = set()
for start_name, start_adjs in graph.items():
    if len(start_adjs) <= len(max_group):
        continue
    remaining_start_adjs = start_adjs.copy()
    while remaining_start_adjs:
        group: set[str] = {start_name}
        frontier: set[str] = {remaining_start_adjs.pop()}
        while frontier:
            name = frontier.pop()
            if name in group:
                continue
            adjs = graph[name]
            if not group.issubset(adjs):
                continue
            group.add(name)
            remaining_start_adjs.discard(name)
            frontier.update(adjs.difference(group))
        if len(group) > len(max_group):
            max_group = group
print(",".join(sorted(max_group)))

print_time_elapsed(start_time)
