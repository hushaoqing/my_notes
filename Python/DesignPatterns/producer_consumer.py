# !usr/bin/python
# coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from threading import Thread, Condition
import time
import random
from Queue import Queue

# 1
l = []
MAX_NUM = 10
lock = Condition()
class ProducerThread(Thread):
    """docstring for ProducerThread"""
    def run(self):
        global l
        while 1:
            num = random.choice(range(6))
            lock.acquire()
            if len(l) == MAX_NUM:
                print "queue full"
                lock.wait()
            l.append(num)
            print "produce", num
            lock.notify()
            lock.release()
            time.sleep(1)

class ConsumerThread(Thread):
    """docstring for ConsumerThread"""
    def run(self):
        global l
        while 1:
            lock.acquire()
            if not l:
                print "noting to consuming"
                lock.wait()
            num = l.pop(0)
            print "consumer", num
            lock.notify()
            lock.release()
            time.sleep(1)

ProducerThread().start()
ConsumerThread().start()
# 2
queue = Queue(10)

class ProducerThread(Thread):
    def run(self):
        nums = range(5)
        global queue
        while True:
            num = random.choice(nums)
            queue.put(num)
            print "Produced", num

class ConsumerThread(Thread):
    def run(self):
        global queue
        while True:
            num = queue.get()
            queue.task_done()
            print "Consumed", num
            time.sleep(random.random())

ProducerThread().start()
ConsumerThread().start()

# 3
def consumer():
    print 's'
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER]Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    print "ss"
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER]Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER]Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)