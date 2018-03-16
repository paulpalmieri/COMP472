from collections import deque

def BFS(starting_node):
    path = []
    queue = deque([starting_node])
    closed_set = set([])
    open_set = set([starting_node])

    while len(queue) !=0:
        node = queue.popleft()
        open_set.remove(node)

        if not node.check_goal_state():

            closed_set.add(node)

            for child in node.expand():
                if child in closed_set or child in open_set:
                    continue
                queue.append(child)
                open_set.add(child)
        else:
            # build path in reverse, does not include root
            while node.previous_node is not None:
                path.insert(0, node)
                node = node.previous_node
            break

    if len(path) is 0:
        print("No solution found")

    return path
