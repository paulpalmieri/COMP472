from random import shuffle

initial = 'rrrrbbbbyywwgge'
initiallist = list(initial)
with open("input/expert.txt", 'w') as f:
    for i in range(0, 100):
        shuffle(initiallist)
        f.write(" ".join(initiallist) + '\n')
