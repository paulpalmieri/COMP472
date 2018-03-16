from automatic_solve import Node
from collections import deque

class Strategy:

    ROW_LENGTH = 5

    def __init__(self, func):
        if func:
            self.analyze = func

    def analyze(self, node):
        pass


def matching(node):
    value = Strategy.ROW_LENGTH
    for i in range(Strategy.ROW_LENGTH):
        if node.state[i] is node.state[i + (2 * Strategy.ROW_LENGTH)]:
            value -= 1

    return value

def matching_plus_local_manhattan(node):
    value = 10
    adjacency_list = [[1,5], [0,6,2], [1,7,3], [2,8,4], [3,9],
                      [0,6,10], [1,5,7,11], [2,6,12,8], [3,7,13,9], [4,8,14],
                      [5,11], [10,6,12], [11,7,13], [12,8,14], [13,9]]

    for i in range(Strategy.ROW_LENGTH):
        goal = i + (2 * Strategy.ROW_LENGTH)
        if node.state[i] is node.state[goal]:
            value -= 2
            continue
        elif node.state[i] is 'e':
            value -= 1
            continue
        else:
            for j in adjacency_list[goal]:
                if node.state[j] is node.state[i]:
                    value -=1
                    break

    return value