from heapWrapper import HeapQueue
import time

char_map = {
    0: 'A',
    1: 'B',
    2: 'C',
    3: 'D',
    4: 'E',
    5: 'F',
    6: 'G',
    7: 'H',
    8: 'I',
    9: 'J',
    10: 'K',
    11: 'L',
    12: 'M',
    13: 'N',
    14: 'O'
}

def solve(file_name, strategy):

    time_stamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    output_file = "output/Solution_" + time_stamp + ".txt"
    answer_file = "output/Answer_" + time_stamp + ".txt"
    solver = ASearch(strategy)
    total_moves = 0
    total_time = 0
    puzzle_counter = 0

    with open(file_name) as f:
        for puzzle in f:
            puzzle_counter += 1

            print(puzzle)
            initial_node = parse(puzzle)
            open_list = HeapQueue()
            open_list.push(1, initial_node)

            start_time = time.time()
            path = solver.search(open_list,set([initial_node]), set([]))
            solve_time= time.time() - start_time
            total_time += solve_time

            print("Puzzle {} solved".format(puzzle_counter))
            with open (output_file, 'a') as s, open (answer_file, 'a') as a:
                a.write("Puzzle {} answer:\n\n".format(puzzle_counter))
                a.write(initial_node.print() + "\n\n")
                s.write(initial_node.state)
                s.write("\nSolution = ")
                for node in path:
                    s.write(char_map[node.previous_move][0])
                    total_moves += 1
                    a.write(node.print()+"\n\n")
                s.write("\nTime to solve: {:.5f}".format(solve_time))
                s.write("\n\n")

        with open (output_file, 'a') as s:
            s.write("\nTotal Time: {:.5f}\nTotal Moves: {}".format(total_time, total_moves))

def parse(file_line):
    initial_state = file_line.rstrip().replace(" ","")
    empty_index = initial_state.find('e')

    return Node(initial_state, empty_index, 0)



class ASearch():

    def __init__(self, strategy):
        self.heuristic = strategy


    def search(self, open_heap, open_set, closed_set):

        path = []
        # for each element in the open list
        while len(open_heap) != 0:
            # remove from heap and set
            node = open_heap.pop()
            open_set.remove(node)

            #check if goal state
            if not node.check_goal_state():

                #add state to closed list
                closed_set.add(node)

                #expand node
                for child in node.expand():
                    #check not in closed or open lists
                    if child in closed_set or child in open_set:
                        continue
                    #run heuristic and add to open list
                    key = self.heuristic.analyze(child) #+ child.path_length
                    #print(str(key))
                    key = key + child.path_length
                    #print("--Debug: Adding to open list with key " + str(key))
                    open_heap.push(key, child)
                    open_set.add(child)

            else:
                #build path in reverse, does not include root
                while node.previous_node is not None:
                    path.insert(0, node)
                    node = node.previous_node
                break

        if len(path) is 0:
            print("No solution found")

        return path



class Node():

    COLS = 5
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

    def __init__(self, initial_state, empty_index, path_length, previous_node = None):
        self.state = str(initial_state)
        self.empty_index = empty_index
        self.path_length = path_length
        self.previous_node = previous_node
        self.previous_move = empty_index

    def __hash__(self):
        return hash(self.state)

    def __eq__(self, other):
        if isinstance(other, Node):
            return ((self.state == other.state))
        else:
            return False


    def check_goal_state(self):

        for i in range(Node.COLS):
            if (self.state[i] != self.state[i+(2*Node.COLS)]):
                return False

        return True


    def expand(self):

        children_list = []
        empty_row, empty_col = Node.string_map[self.empty_index][0], Node.string_map[self.empty_index][1]
        #find valid moves
        up = empty_row - 1 >= 0
        down = empty_row + 1 <= 2
        left = empty_col - 1 >= 0
        right = empty_col + 1 <= 4

        if up:
            move_index = self.empty_index - Node.COLS
            children_list.append(self.move(move_index))

        if down:
            move_index = self.empty_index + Node.COLS
            children_list.append(self.move(move_index))

        if left:
            move_index = self.empty_index - 1
            children_list.append(self.move(move_index))

        if right:
            move_index = self.empty_index + 1
            children_list.append(self.move(move_index))

        return children_list


    def move(self,move_index):

        string_copy = [character for character in self.state]
        string_copy[self.empty_index], string_copy[move_index] = string_copy[move_index], 'e'

        return Node("".join(string_copy), move_index, (self.path_length + 1), self)

    def print(self):

        return " ".join(self.state[:5]) + "\n" + " ".join(self.state[5:10]) + "\n" + " ".join(self.state[10:])

