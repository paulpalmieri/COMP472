from random import shuffle

initial = 'rrrrbbwwyyggppe'
initiallist = list(initial)
with open("input/master1000.txt", 'w') as f:
    for i in range(0, 1000):
        shuffle(initiallist)
        f.write(" ".join(initiallist) + '\n')
