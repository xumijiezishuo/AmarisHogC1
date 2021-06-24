# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2021/6/11 9:49 下午
# @Author :Amaris
# @File   :for_demo.py

# count=0
# for i in range(101):
#     print(i)
#     count += i
# print(count)
#
# import math
#
# print(math.ceil(5.4))
# print(math.floor(5.6))
# print(math.sqrt(4))
import _thread
from time import sleep, ctime
import logging
# 配置日志等级
logging.basicConfig(level=logging.INFO)

loops=[2,4]
# nloop用于标识当前loop处于第几个(如0，1)，nsec告诉loop循环多久，lock锁
# 首先会传进一个已经锁上的锁，当loop执行结束会有一个解锁的操作，如果所有的loop执行完毕，
# 所有的锁都会解开，这样主线程就可以结束了
def loop(nloop,nsec,lock):
    logging.info("start loop "+str(nloop) + "at" + ctime())
    sleep(nsec)
    logging.info("start loop "+str(nloop) +  "at" + ctime())
    lock.release()

def main():
    logging.info("start all at"+ctime())
    locks = []
    nloops = range(len(loops))
    for i in nloops:
        lock = _thread.allocate_lock()
        lock.acquire()
        locks.append(lock)
    for i in nloops:
        _thread.start_new_thread(loop, (i,loops[i],locks[i]))
    for i in nloops:
        while locks[i].locked(): pass
    logging.info("end all at"+ctime())

if __name__ == '__main__':
    main()

