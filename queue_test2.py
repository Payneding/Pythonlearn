from multiprocessing import Process,Queue
import os,time
def write(q):
    for i in ['A','B','C','D','E','F','G','H']:
        print "put %s into the queue..." %i
        q.put(i)
        time.sleep(1)


def read(q):
    while True:
        value=q.get()
        print "get %s form the queue..." %value

if __name__=="__main__":
    q=Queue()
    pw=Process(target=write,args=(q,))
    pr=Process(target=read,args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
