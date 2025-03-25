from collections import deque

maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

def find_positions():
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == "O":
                start = (i, j)
            if cell == "X":
                end = (i, j)
    return start, end

def bfs():
    start, end = find_positions()
    queue = deque([(start, [])])
    visited = set()

    while queue:
        (x, y), path = queue.popleft()
        if(x, y) == end:
            for px, py in path:
                if maze[px][py] not in ["O", "X"]:
                    maze[px][py] = "*"
            return True

        if(x, y) in visited:
            continue
        visited.add((x, y))

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] in [" ", "X"]:
                queue.append(((nx, ny), path + [(x, y)]))

    return False

if bfs():
    for row in maze:
        print(" ".join(row))
else:
    print("No Path Found!!!")
