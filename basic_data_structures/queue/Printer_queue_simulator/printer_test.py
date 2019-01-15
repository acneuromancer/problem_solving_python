from Task import Task
from Printer import Printer
from Queue import Queue

import random

def new_print_task():

    num = random.randrange(1, 181)
    return num == 180


def simulation(num_seconds, pages_per_minute):

    lab_printer = Printer(pages_per_minute)
    print_queue = Queue()
    waiting_times = []

    for current_second in range(num_seconds):

        if new_print_task():
            task = Task(current_second)
            print_queue.enqueue(task)

        if (not lab_printer.busy()) and (not print_queue.is_empty()):
            next_task = print_queue.dequeue()
            waiting_times.append(next_task.wait_time(current_second))
            lab_printer.start_next(next_task)

        lab_printer.tick()

    average_wait = sum(waiting_times) / len(waiting_times)
    print("Average wait %6.2f secs %3d tasks remaining." % (average_wait, print_queue.size()))


for i in range(10):
    simulation(3600, 5)
