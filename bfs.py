# #-*- coding: utf-8 -*-
# # by Yipeng Zhang

class node:
    def __init__(self, x=0, y=0, t=0):
        self.x = x
        self.y = y
        self.t = t  # t表示走到这个格子用的步数


class father:
    def __init__(self, x=0, y=0, cz=[]):
        self.x = x  # 当前格子的父节点坐标
        self.y = y
        self.cz = cz  # 由什么操作到达的这个格子


# mmap = [[0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 1, 1, 1, 1, 0, 1, 0],
#         [0, 0, 0, 0, 1, 0, 1, 0],
#         [0, 1, 0, 0, 0, 0, 1, 0],
#         [0, 1, 0, 1, 1, 0, 1, 0],
#         [0, 1, 0, 0, 0, 0, 1, 1],
#         [0, 1, 0, 0, 1, 0, 0, 0],
#         [0, 1, 1, 1, 1, 1, 1, 0]]


# vis = [[False]*10]*10
vis = []
for i in range(0, 27):
    vis += [[]]
    for j in range(0, 27):
        vis[i] += [False]

lj = []
for i in range(0, 27):
    lj += [[]]
    for j in range(0, 27):
        lj[i] += [father()]

xx = [1, 0, -1, 0]  # 右、下、左、上
yy = [0, 1, 0, -1]

q = []
s = node()
f = node()
n = 25
m = 25


def bfs(mmap1, val0, val1):
    mmap = mmap1[:]
    s.x = val0[0]
    s.y = val0[1]
    s.t = 0
    f.x = val1[0]
    f.y = val1[1]
    mmap[f.x][f.y] = 0
    q.append(s)
    lj[s.x][s.y].x = 1000
    lj[s.x][s.y].y = 1000
    lj[s.x][s.y].cz = 0
    vis[0][0] = True  # 标为已经访问过
    # print("vis={}".format(vis))
    while q:
        now = q[0]
        q.pop(0)
        for i in range(0, 4):
            new = node()
            new.x = now.x + xx[i]
            new.y = now.y + yy[i]
            new.t = now.t + 1
            # print("i={} new.x={} new.y={} now.x={} now.y={}".format(i, new.x, new.y, now.x, now.y))
            # print("new.x ={} new.y={} n={} m={} vis[new.x][new.y]={} mmap[new.x][new.y]={}".format(new.x, new.y, n, m, vis[new.x][new.y], mmap[new.x][new.y]))
            if new.x < 0 or new.y < 0 or new.x >= n or new.y >= m or vis[new.x][new.y] == True or mmap[new.x][
                new.y] == 1:  # 下标越界或者访问过或者是障碍物
                continue

            q.append(new)
            lj[new.x][new.y].x = now.x
            lj[new.x][new.y].y = now.y
            lj[new.x][new.y].cz = i
            # if i == 0:
            #     lj[new.x][new.y].cz = 'D'
            # elif i == 1:
            #     lj[new.x][new.y].cz = 'R'
            # elif i == 2:
            #     lj[new.x][new.y].cz = 'L'
            # elif i == 3:
            #     lj[new.x][new.y].cz = 'U'
            vis[new.x][new.y] = True
            # print("value={} ({},{}) {}\n".format(mmap[new.x][new.y], new.x, new.y, lj[new.x][new.y].cz))
            # print("=============================================================")
            if new.x == f.x and new.y == f.y:
                return new.t  # 到达终点
    return False


ans_lj = []


def dfs(x, y):
    if x == 0 and y == 0:
        return
    else:
        dfs(lj[x][y].x, lj[x][y].y)
    # print(lj[x][y].cz)
    ans_lj.append(lj[x][y].cz)


# if __name__ == '__main__':
#     # print(mmap)
#     ans = bfs(mmap)
#     if ans == False:
#         print("error")
#     else:
#         print(ans)
#         dfs(n - 1, m - 1)
#         print("迷宫行走方式{}".format(ans_lj))

def ai(mmap1, val0, val1):
    ans = bfs(mmap1, val0, val1)
    if ans:
        dfs(n-1, m-1)
        return ans_lj
    else:
        return None