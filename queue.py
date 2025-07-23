#   add at the end, delete happens at the beginning.
# Queue() creates am empty queue
# dequeue() removes an element at the beginning of the queue
# enqueue() adds an element at the beginning of the queue
# is_empty() checks if empty
# size() returns an integer
import random
from pythonds3.basic import Queue


def hot_potato(name_list, num):
    sim_queue = Queue()
    for name in name_list:
        sim_queue.enqueue(name)

    while sim_queue.size() > 1:
        for i in range(num):
            sim_queue.enqueue(sim_queue.dequeue())
        sim_queue.dequeue()

    return sim_queue.dequeue()  # 如果是上面给了变量，那么return的只是最后一个被淘汰的


# 而不是最后存活下来的
print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))


### printing mission
class Printer:
    def __init__(self, ppm):
        self.page_rate = ppm #set pages per minute
        self.current_task = None # initialize the task situation
        self.time_remaining = 0 # initialize

    def tick(self):
        if self.current_task is not None: 
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        return self.current_task is not None

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.page_rate


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def get_stamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.timestamp


def simulation(num_seconds, pages_per_minute):
    lab_printer = Printer(pages_per_minute)
    print_queue = Queue()
    waiting_time = []

    for current_second in range(num_seconds):
        if new_print_task(): # For each second try if 1/180 is possible
            task = Task(current_second)  # Create a timestamp here
            print_queue.enqueue(task)

        if (not lab_printer.busy()) and (not print_queue.is_empty()):
            nexttask = print_queue.dequeue()
            waiting_time.append(nexttask.wait_time(current_second)) # give current time to wait_time
            lab_printer.start_next(nexttask) # Give printer a new task so that tick starts

        lab_printer.tick()

    average_wait = sum(waiting_time) / len(waiting_time)
    print(
        f"Average Wait{average_wait: 6.2f} secs"
        + f"{print_queue.size():3d} takes remaining"
    )


def new_print_task():
    num = random.randrange(1, 181)
    return num == 180


for i in range(10):
    simulation(3600, 5)
