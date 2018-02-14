from queue import Queue
import timeit


string_map = {
    0: (0, 0),
    1: (0, 1),
    2: (0, 2),
    3: (0, 3),
    4: (0, 4),
    5: (1, 0),
    6: (1, 1),
    7: (1, 2),
    8: (1, 3),
    9: (1, 4),
    10: (2, 0),
    11: (2, 1),
    12: (2, 2),
    13: (2, 3),
    14: (2, 4)
}

list_map = [
    [0, 1, 2, 3, 4],
    [5, 6, 7, 8, 9],
    [10, 11, 12, 13, 14]
]

class Node():
    def __init__(self, initial_state, empty_index):
        self.state = str(initial_state)
        self.empty_index = empty_index

    def goal_test(self):
        for i in range(5):
            print(str(i))
            if(self.state[i] != self.state[i + 10]):
                return False

        print("----- SOLVED: " + str(self.state) + " -----")
        return True

    def expand(self):
        node_list = []
        empty_row, empty_col = string_map[self.empty_index][0], string_map[self.empty_index][1]
        up = empty_row - 1 >= 0
        down = empty_row + 1 <= 2
        left = empty_col - 1 >= 0
        right = empty_col + 1 <= 4

        print("Expanding...")
        print("Current board: " + self.state)
        print("Empty index: " + str(self.empty_index))

        if up:
            string_copy = [character for character in self.state]
            move_index = list_map[empty_row - 1][empty_col]
            print("Move index: " + str(move_index))
            # swap the current index with the step
            string_copy[self.empty_index], string_copy[move_index] = string_copy[move_index], 'e'
            print("Board after swap: " + "".join(string_copy))
            node_list.append(Node("".join(string_copy), move_index))

        if down:
            string_copy = [character for character in self.state]
            move_index = list_map[empty_row + 1][empty_col]
            print("Move index: " + str(move_index))
            # swap the current index with the step
            string_copy[self.empty_index], string_copy[move_index] = string_copy[move_index], 'e'
            print("Board after swap: " + "".join(string_copy))
            node_list.append(Node("".join(string_copy), move_index))

        if left:
            string_copy = [character for character in self.state]
            move_index = list_map[empty_row][empty_col - 1]
            print("Move index: " + str(move_index))
            # swap the current index with the step
            string_copy[self.empty_index], string_copy[move_index] = string_copy[move_index], 'e'
            print("Board after swap: " + "".join(string_copy))
            node_list.append(Node("".join(string_copy), move_index))

        if right:
            string_copy = [character for character in self.state]
            move_index = list_map[empty_row][empty_col + 1]
            print("Move index: " + str(move_index))
            # swap the current index with the step
            string_copy[self.empty_index], string_copy[move_index] = string_copy[move_index], 'e'
            print("Board after swap:\n" + "".join(string_copy))
            node_list.append(Node("".join(string_copy), move_index))

        return node_list





class BFS():
    def __init__(self, initial_node):
        self.initial_node = initial_node

    def solve(self):
        cur_branches = 0
        cur_already_visited = 0
        visited = 0
        frontier = Queue()
        frontier.put(self.initial_node)
        explored = set()

        goals = []

        i = 0
        while frontier:
            node = frontier.get()
            explored.add(node.state)
            visited += 1

            for child in node.expand():
                if child.state not in explored:
                    if child.goal_test():
                        if(len(goals) < 10):
                            if child.state[0:5] not in goals:
                                goals.append(child.state[0:5])
                                continue
                        else:
                            print("Branches: " + str(cur_branches))
                            print("Already closed count: " + str(cur_already_visited))
                            print("Visited: " + str(visited))
                            print("Goal states: " + str(len(goals)))

                            print("Length of array: " + str(len(goals)))
                            print("Length of set: " + str(len(set(goals))))
                            return goals
                                # for e in goals:
                                #     print(e)
                                # return
                    else:
                        print("Adding child state to open list")
                        frontier.put(child)
                        print(child.state)
                        i += 1
                        cur_branches += 1
                else:
                    print("ALREADY VISITED")
                    cur_already_visited += 1


            # if(i > 10000):
            #     print("REACHING 10000 loops")
            #     break

        return None



st = "rebwrbbbrrrbrbw"
n = Node(st, 1)
solver = BFS(n)
goals = solver.solve()
for e in goals:
    print(e)

se = set(goals)
print(se)
