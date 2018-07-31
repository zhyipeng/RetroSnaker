#-*- coding: utf-8 -*-
# by Yipeng Zhang

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def pos_to_dir(func):
    def inner(maze, start, end):
        res = []
        path = maze_solver_queue(maze, start, end)
        for i in range(len(path)-1):
            if path[i+1][1]-path[i][1] == 1 and path[i+1][0]-path[i][0] == 0:
                res.append(1)
            elif path[i+1][1]-path[i][1] == -1 and path[i+1][0]-path[i][0] == 0:
                res.append(3)
            elif path[i+1][1]-path[i][1] == 0 and path[i+1][0]-path[i][0] == 1:
                res.append(0)
            elif path[i+1][1]-path[i][1] == 0 and path[i+1][0]-path[i][0] == -1:
                res.append(2)
        return res
    return inner


# 给迷宫maze的位置pos标2表示已探索
def mark(maze, pos):
    maze[pos[0]][pos[1]] = 2

# 检查迷宫maze的位置pos是否可行
def passable(maze, pos):
    try:
        return maze[pos[0]][pos[1]] == 0
    except:
        return False

# 递归
repath = []
def find_path(maze, pos, end):
    mark(maze, pos)
    if pos == end:
        # print(pos, end=' ')
        repath.append(pos)
        return True
    for i in range(4):
        nextp = (pos[0] + dirs[i][0], pos[1] + dirs[i][1])
        if passable(maze, nextp):
            if find_path(maze, nextp, end):
                # print(pos, end=' ')
                repath.append(pos)
                return True
    return False

# 栈
def maze_solver(maze, start, end):
    if start == end:
        print(start)
        return
    st = []
    mark(maze, start)
    st.append((start, 0))
    while st:
        pos, nxt = st.pop()
        for i in range(nxt, 4):
            nextp = (pos[0] + dirs[i][0], pos[1] + dirs[i][1])
            if nextp == end:
                return print_path(end, pos, st)

            if passable(maze, nextp):
                st.append((pos, i + 1))
                mark(maze, nextp)
                st.append((nextp, 0))
                break  # 退出内层循环，下次迭代将以新栈顶为当前位置继续
    print('No path found.')


def print_path(end, pos, st):
    return ([i[0] for i in st] + [pos, end])


# 队列
# @pos_to_dir
def maze_solver_queue(maze, start, end):
    if start == end:
        print('Path finds.')
        return
    qu = []
    d = {}
    mark(maze, start)
    qu.append(start)
    while qu:
        pos = qu.pop(0)
        for i in range(4):
            nextp = (pos[0] + dirs[i][0], pos[1] + dirs[i][1])
            # print(nextp)
            if passable(maze, nextp):
                d[nextp] = pos
                if nextp == end:
                    print('Path finds.')
                    p = end
                    res = [end]
                    while p in d:
                        res.append(d[p])
                        p = d[p]
                    return res[::-1]
                mark(maze, nextp)
                qu.append(nextp)
    print('No path.')







if __name__ == '__main__':
    # 12*14
    maze = [
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,1,1,0,0,0,1,0,0,0,1],
        [1,0,1,0,0,0,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,1,1,1,0,1,0,1,0,1],
        [1,0,1,0,0,0,0,0,0,1,1,1,0,1],
        [1,0,1,1,1,1,1,1,1,1,0,0,0,1],
        [1,0,1,0,0,0,0,0,0,0,0,1,0,1],
        [1,0,0,0,1,1,1,0,1,0,1,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1,0,0,1],
        [1,0,1,0,1,0,1,0,1,1,1,1,0,1],
        [1,0,1,0,0,0,1,0,0,1,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ]
    start = (1, 1)
    end = (10, 12)

    # find_path(maze, start, end)
    # print(repath[::-1])

    # print(maze_solver(maze, start, end))

    print(maze_solver_queue(maze, start, end))