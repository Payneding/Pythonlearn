from multiprocessing import Process, Queue

def f(q):
    q.put('XYZ' * 10000)

if __name__ == '__main__':
    queue = Queue()
    p = Process(target=f, args=(queue,))
    p.start()
    p.join()                    # this deadlocks
    obj = queue.get()
    print obj
~             
