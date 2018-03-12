import heapq


class HeapQueue():
    counter = 0

    def __init__(self):
        self._data = []

    def push(self, key, item):
        heapq.heappush(self._data, (key, HeapQueue.counter, item))
        HeapQueue.counter += 1

    def pop(self):
        return heapq.heappop(self._data)[2]

    def __len__(self):
        return len(self._data)