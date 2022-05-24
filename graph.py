
x = [x for x in range(-3, 4)]
y = [y ** 2 + 2 * y for y in x]
n = max(max(x, y))
graph = [[" " for x in range(n*2+1)] for x in range(n*2+1)]

for x, y in zip(x, y):
    graph[y + n][x + n] = "0"

with open("graph.txt", "w") as file:
    for line in graph:
        file.write("".join(line) + "\n")

#	TERMINAL VERSION
# for line in graph:
#     print("".join(line))
