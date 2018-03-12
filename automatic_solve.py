from heapWrapper import HeapQueue

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
    solver = BFS(strategy)
    with open(file_name) as f:
        for puzzle in f:
            puzzle = puzzle.rstrip()
            puzzle = puzzle.replace(" ", "")
            print(puzzle)
            
            empty_index = puzzle.find('e')
            initial_node = Node(puzzle, empty_index)
            open_list = HeapQueue()
            open_list.push(1, initial_node)
            path = solver.search(open_list,set([initial_node]), set([]))

            with open ("solutions.txt", 'a') as s:
                s.write(puzzle)
                s.write("\nSolution = ")
                for state in path:
                    s.write(char_map[state.previous_move][0])
                s.write("\n\n")
            print(puzzle)
            print("Solution = ")
            for state in path:
                print(char_map[state.previous_move][0])



class BFS():

    def __init__(self, strategy):
        self.heuristic = strategy


    def search(self, open_heap, open_set, closed_set):

        path = []
        # for each element in the open list
        while len(open_heap) != 0:
            # remove from heap and dict
            print("Evaluating Node")
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
                    key = self.heuristic.analyze(child)
                    print("Adding to open list with key " + str(key))
                    open_heap.push(key, child)
                    open_set.add(child)

            else:
                #build path in reverse, does not include root
                while node.previous_node is not None:
                    path.insert(0,node)
                    print("Added to path")
                    node = node.previous_node
                break

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

    def __init__(self, initial_state, empty_index, previous_node = None):
        self.state = str(initial_state)
        self.empty_index = empty_index
        self.previous_node = previous_node
        self.previous_move = empty_index


    def __hash__(self):
        return hash(self.state)

    def __eq__(self, other):
        if isinstance(other, Node):
            return ((self.state == other.state))
        else:
            return False

    def find_empty_index(self):

        for index,char in self.state:
            if char is 'e':
                empty_index = index
                break

        return empty_index


    def check_goal_state(self):

        for i in range(Node.COLS):
            if (self.state[i] != self.state[i+(2*Node.COLS)]):
                return False

        print("***************Solved******************")

        return True


    def expand(self):

        children_list = []
        empty_row, empty_col = Node.string_map[self.empty_index][0], Node.string_map[self.empty_index][1]
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

        return Node("".join(string_copy), move_index, self)
