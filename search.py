import copy, time

from edge import edge
from node import node
from tree import tree


def dfs(start, end, road):
    queue = [[start]]
    extended_nodes = []
    while queue and (queue[0][len(queue[0]) - 1] is not end):
        queue.reverse()
        extended_path = queue.pop()
        connected_nodes = extended_path[len(extended_path) - 1].get_connected_nodes(road)
        extended_nodes.append(extended_path[len(extended_path) - 1])
        new_paths = []
        for nodes in connected_nodes:
            if nodes not in extended_nodes:
                temp_extended = copy.deepcopy(extended_path)
                temp_extended.append(nodes)
                new_paths.append(temp_extended)
        new_paths.reverse()
        for path in new_paths:
            queue.append(path)
        queue.reverse()
    return queue[0]


def bfs(start, end, road):
    queue = [[start]]
    extended_nodes = []
    while queue and (queue[0][len(queue[0]) - 1] is not end):
        queue.reverse()
        extended_path = queue.pop()
        connected_nodes = extended_path[len(extended_path) - 1].get_connected_nodes(road)
        extended_nodes.append(extended_path[len(extended_path) - 1])
        new_paths = []
        for nodes in connected_nodes:
            if nodes not in extended_nodes:
                temp_extended = copy.deepcopy(extended_path)
                temp_extended.append(nodes)
                new_paths.append(temp_extended)
        queue.reverse()
        for path in new_paths:
            queue.append(path)
    return queue[0]


def hill_climbing(start, end, road):
    queue = [[start]]
    extended_nodes = []
    while queue and (queue[0][len(queue[0]) - 1] is not end):
        queue.reverse()
        extended_path = queue.pop()
        connected_nodes = extended_path[len(extended_path) - 1].get_connected_nodes(road)
        extended_nodes.append(extended_path[len(extended_path) - 1])
        new_paths = []
        for nodes in connected_nodes:
            if nodes not in extended_nodes:
                temp_extended = copy.deepcopy(extended_path)
                temp_extended.append(nodes)
                new_paths.append(temp_extended)

        path_and_length = {}
        for pat in new_paths:
            p_len = 0
            for p in range(0, len(pat) - 1):
                p_len += pat[p].get_path_length(pat[p + 1], road)
            path_and_length.update({tuple(pat): p_len})
        path_and_length = dict(sorted(path_and_length.items(), key=lambda x: x[1]))

        new_paths = list(path_and_length.keys())
        new_paths.reverse()

        for path in new_paths:
            queue.append(list(path))
        queue.reverse()
    return queue[0]


def a_star(start, end, road):
    queue = [[start]]
    extended_nodes = []
    while queue and (queue[0][len(queue[0]) - 1] is not end):
        queue.reverse()
        extended_path = queue.pop()
        connected_nodes = extended_path[len(extended_path) - 1].get_connected_nodes(road)
        extended_nodes.append(extended_path[len(extended_path) - 1])
        new_paths = []
        for c_nodes in connected_nodes:
            if c_nodes not in extended_nodes:
                temp_extended = copy.deepcopy(extended_path)
                temp_extended.append(c_nodes)
                new_paths.append(temp_extended)
        for pat in new_paths:
            leaf = pat[len(pat) - 1]
            p_len = 0
            for p in range(0, len(pat) - 1):
                p_len += pat[p].get_path_length(pat[p + 1], road)
            for que in queue:
                if que[len(que) - 1] == leaf:
                    q_len = 0
                    for q in range(0, len(que) - 1):
                        q_len += que[q].get_path_length(que[q + 1], road)
                    if q_len < p_len:
                        new_paths.remove(pat)
                    else:
                        queue.remove(que)
        for path in new_paths:
            queue.append(path)

        path_and_length = {}
        for qu in queue:
            qu_len = 0
            for q in range(0, len(qu) - 1):
                qu_len += qu[q].get_path_length(qu[q + 1], road)
            path_and_length.update({tuple(qu): qu_len})
        path_and_length = dict(sorted(path_and_length.items(), key=lambda x: x[1]))

        new_paths = list(path_and_length.keys())
        new_paths.reverse()

        queue = []
        for path in new_paths:
            queue.append(list(path))
        queue.reverse()
    return queue[0]


def aug_a_star(source, goals, road):
    final_goal_path = []
    start = source
    no_goal_nodes = len(goals)
    for _ in range(0, no_goal_nodes):
        queue = [[start]]
        extended_nodes = []
        while queue and (queue[0][len(queue[0]) - 1] not in goals):
            queue.reverse()
            extended_path = queue.pop()
            connected_nodes = extended_path[len(extended_path) - 1].get_connected_nodes(road)
            extended_nodes.append(extended_path[len(extended_path) - 1])
            new_paths = []
            for c_nodes in connected_nodes:
                if c_nodes not in extended_nodes:
                    temp_extended = copy.deepcopy(extended_path)
                    temp_extended.append(c_nodes)
                    new_paths.append(temp_extended)
            for pat in new_paths:
                leaf = pat[len(pat) - 1]
                p_len = 0
                for p in range(0, len(pat) - 1):
                    p_len += pat[p].get_path_length(pat[p + 1], road)
                for que in queue:
                    if que[len(que) - 1] == leaf:
                        q_len = 0
                        for q in range(0, len(que) - 1):
                            q_len += que[q].get_path_length(que[q + 1], road)
                        if q_len < p_len:
                            new_paths.remove(pat)
                        else:
                            queue.remove(que)
            for path in new_paths:
                queue.append(path)

            path_and_length = {}
            for qu in queue:
                qu_len = 0
                for q in range(0, len(qu) - 1):
                    qu_len += qu[q].get_path_length(qu[q + 1], road)
                path_and_length.update({tuple(qu): qu_len})
            path_and_length = dict(sorted(path_and_length.items(), key=lambda x: x[1]))

            new_paths = list(path_and_length.keys())
            new_paths.reverse()

            queue = []
            for path in new_paths:
                queue.append(list(path))
            queue.reverse()
        final_goal_path.extend(queue[0])
        start = queue[0][len(queue[0]) - 1]
        goals.remove(start)

    return final_goal_path


# Test tree 1
nodeW = node()
nodeH = node()
nodeT = node()
nodeO = node()
nodeS = node()
nodeB = node()
nodeC = node()

nodeW.name = 'W'
nodeH.name = 'H'
nodeT.name = 'T'
nodeO.name = 'O'
nodeS.name = 'S'
nodeB.name = 'B'
nodeC.name = 'C'

edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9 = edge(), edge(), edge(), edge(), edge(), edge(), edge(), edge(), edge()
edge1.line = [nodeW, nodeH, 1]
edge2.line = [nodeH, nodeO, 2]
edge3.line = [nodeH, nodeT, 4]
edge4.line = [nodeT, nodeS, 2]
edge5.line = [nodeT, nodeO, 2]
edge6.line = [nodeO, nodeS, 3]
edge7.line = [nodeS, nodeC, 3]
edge8.line = [nodeS, nodeB, 2]
edge9.line = [nodeB, nodeC, 3]

road_ife = tree()
road_ife.name = 'Test'
road_ife.points = [edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9]

# Test tree 2
nA = node()
nB = node()
nC = node()
nD = node()
nE = node()
nF = node()
nG = node()
nH = node()
nI = node()
nJ = node()
nK = node()
nL = node()

nA.name = 'A'
nB.name = 'B'
nC.name = 'C'
nD.name = 'D'
nE.name = 'E'
nF.name = 'F'
nG.name = 'G'
nH.name = 'H'
nI.name = 'I'
nJ.name = 'J'
nK.name = 'K'
nL.name = 'L'

e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20 = edge(), edge(), edge(), edge(), edge(), edge(), edge(), edge(), edge(), edge(), edge(), edge(), edge(), edge(), edge(), edge(), edge(), edge(), edge(), edge()
e1.line = [nA, nB, 2]
e2.line = [nA, nC, 3]
e3.line = [nA, nD, 5]
e4.line = [nB, nC, 2]
e5.line = [nB, nD, 4]
e6.line = [nD, nE, 2]
e7.line = [nD, nG, 4]
e8.line = [nE, nF, 1]
e9.line = [nE, nG, 2]
e10.line = [nF, nG, 1]
e11.line = [nF, nH, 3]
e12.line = [nG, nH, 2]
e13.line = [nH, nJ, 3]
e14.line = [nH, nK, 4]
e15.line = [nH, nL, 5]
e16.line = [nI, nJ, 11]
e17.line = [nI, nK, 12]
e18.line = [nJ, nK, 8]
e19.line = [nJ, nL, 3]
e20.line = [nK, nL, 2]

road_ife_exp = tree()
road_ife_exp.name = 'Real road'
road_ife_exp.points = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20]

# Test tree 3
ndA = node()
ndB = node()
ndC = node()

ndA.name = 'A'
ndB.name = 'B'
ndC.name = 'C'

ed1, ed2, ed3 = edge(), edge(), edge()
ed1.line = [ndA, ndB, 3]
ed2.line = [ndA, ndC, 1]
ed3.line = [ndB, ndC, 1]

road_test = tree()
road_test.name = 'Simple'
road_test.points = [ed1, ed2, ed3]

home = nG
destination = nK
multiple_destination = [nA, nJ, nC, nK]
road_map = road_ife_exp

start_time = time.time()

goal_path_dfs = dfs(home, destination, road_map)
goal_path_bfs = bfs(home, destination, road_map)
goal_path_hill_climbing = hill_climbing(home, destination, road_map)
goal_path_a_star = a_star(home, destination, road_map)
goal_path_aug_a_star = aug_a_star(home, multiple_destination, road_map)



path_dfs = ''
path_bfs = ''
path_hill_climbing = ''
path_a_star = ''
path_aug_a_star = ''

for nodes in goal_path_dfs:
    path_dfs += ' -> ' + nodes.name
for nodes in goal_path_bfs:
    path_bfs += ' -> ' + nodes.name
for nodes in goal_path_hill_climbing:
    path_hill_climbing += ' -> ' + nodes.name
for nodes in goal_path_a_star:
    path_a_star += ' -> ' + nodes.name
for ind in range(0, len(goal_path_aug_a_star)):
    if goal_path_aug_a_star[ind].name == goal_path_aug_a_star[ind - 1].name:
        continue
    else:
        path_aug_a_star += ' -> ' + goal_path_aug_a_star[ind].name

end_time = time.time()
final_time = end_time - start_time

print('DFS Solution:               ', path_dfs)
print('BFS Solution:               ', path_bfs)
print('Hill Climbing Solution:     ', path_hill_climbing)
print('A* Solution:                ', path_a_star)
print('Augmented A* Solution:      ', path_aug_a_star)

print("\n" + "Search took: " + str(final_time) + " s to complete")
