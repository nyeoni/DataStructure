import queue

class mQueue:
    # FIFO Queue
    def __init__(self):
        self.queue_list = list()

    def enqueue(self, data):
        self.queue_list.append(data)

    def dequeue(self):
        data = self.queue_list[0]
        del self.queue_list[0]
        return data


if __name__=="__main__":
    # Queue
    data_queue = queue.Queue()
    data_queue.put(1)
    data_queue.put(2)
    data_queue.put(3)
    print()

    print("Queue output:", data_queue.get())

    # LifoQueue
    data_queue = queue.LifoQueue() # it seems like Stack
    data_queue.put(1)
    data_queue.put(2)
    data_queue.put(3)

    print("LifoQueue output:", data_queue.get())

    # PriorityQueue
    data_queue = queue.PriorityQueue() # put tuple data (priority num, data)
    data_queue.put((1, "three"))
    data_queue.put((2, "two"))
    data_queue.put((3, "one"))

    print("PriorityQueue output:", data_queue.get())

    # mQueue
    data_queue = mQueue()
    data_queue.enqueue(1)
    data_queue.enqueue(2)
    data_queue.enqueue(3)

    print("mQueue output:", data_queue.dequeue())
    print("mQueue output:", data_queue.dequeue())
    print("mQueue output:", data_queue.dequeue())

