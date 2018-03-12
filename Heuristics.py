
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



def manhattan_distance(node):
    value = 0
    if node.empty_index < 5:
        print("bottom")
    else:
        print("top")

    return value
