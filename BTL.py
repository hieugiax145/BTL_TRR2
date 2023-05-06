import random
import matplotlib.pyplot as plt
import numpy as np

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
# Tạo dữ liệu ngẫu nhiên cho đỉnh và tọa độ
n = 1000
?
f=open('3456.csv','r')
for line in f:
        x,y=np.loadcsv['3456.csv',dtype=float,delimiter=',']
        P.append(Point(x,y))
        # vertices = [(x, y) for _ in range(n)]
# vertices = [(random.uniform(0, 20), random.uniform(0, 20)) for _ in range(n)]

# Hàm tính khoảng cách giữa 2 điểm
def distance(v1, v2):
    return ((v1.x - v2.x)**2 + (v1.y - v2.y)**2)**0.5

# Hàm DFS
# def dfs(v, visited, component):
#     visited[v] = True
#     component.append(v)
#     for i in range(n):
#         if not visited[i] and distance(P[v], P[i]) <= d:
#             dfs(i, visited, component)

def dfs(v,visited,component):
    # if v not in visited:        
    visited[v] = True
    stack=[]
    stack.append(v)
    while stack:
        u=stack.pop(0)
        component.append(u)
        for i in range(n):
            if not visited[i] and distance(P[u], P[i]) <= d:
                    # stack.append(u)
                    stack.append(i)
                    visited[i] = True
                    # break

d = 0.4 # Khoảng cách d
visited = [False] * n
components = []
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

# Tìm thành phần liên thông
for i in range(n):
    if not visited[i]:
        component = []
        dfs(i, visited, component)
        components.append(component)

# In kết quả và vẽ đồ thị
print(f"Số lượng thành phần liên thông: {len(components)}")
for i, component in enumerate(components):
    print(f"Thành phần {i + 1}: {component}")
    x = [P[v].x for v in component]
    y = [P[v].y for v in component]
    plt.scatter(x, y, color=random.choice(colors), s=50)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Connected Components with Distance d')
plt.show()