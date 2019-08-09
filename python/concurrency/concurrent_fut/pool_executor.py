# https://tutorialedge.net/python/concurrency/python-threadpoolexecutor-tutorial/


from concurrent.futures import ThreadPoolExecutor
import concurrent
import threading
import random
from util import *



def demo1():

    def task():
        print("Executing our Task")
        result = 0
        i = 0
        for i in range(10):
            result = result + i
        print("I: {}".format(result))
        print("Task Executed {}".format(threading.current_thread()))
    #task end
    banner('demo 1')
    executor = ThreadPoolExecutor(max_workers=4)
    task1 = executor.submit(task)
    task2 = executor.submit(task)

def demo2():
    def task(who,n):
        print("Processing for {} with {} things".format(who,n))
    #task end
    banner('demo 2')
    print("Starting ThreadPoolExecutor")
    with ThreadPoolExecutor(max_workers=4) as executor:
        #submit accepts method name then *args and **kwargs
        future = executor.submit(task, who='mama',n=2)
        future = executor.submit(task, 'papa',3)
        future = executor.submit(task, 'nobody',4)
    print("All tasks complete")


def demo3():
    def ftask(n):
        print('working ftask on {}'.format(n))
        return(1+n*10)

    banner('future tasks gathered in iterable')
    work_methods = {'part1':ftask, 'part2':ftask }
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(work_methods)) as executor:
        tasks = {}
        i=0
        tasks={}
        for key, work_method in work_methods.items():
            task = executor.submit(work_method,i)
            tasks[task] = key
            i += 1
        results = {}
        for task in  concurrent.futures.as_completed(tasks):
            key = tasks[task]
            results[key] = task.result()
    print('results: {}'.format(results))

if __name__ == '__main__':
    demo1()
    demo2()
    demo3()