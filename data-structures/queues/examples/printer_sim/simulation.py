import random

from queue import Queue 

from printer import Printer
from task import Task

def simulation(num_seconds, pages_per_minute):
    lab_printer = Printer(pages_per_minute)
    print_q = Queue()
    waiting_times = []

    # run sim, for each second:
    for current_second in range(num_seconds):
        # if new print task is created
        if new_print_task():
            task = Task(current_second)
            # add task to printer queue with time stamp 
            print_q.enqueue(task) 
        
        # if printer is not busy and printer queue is not empty.
        if(not lab_printer.busy()) and (not print_q.is_empty()):
            # print new task, poped from queue
            nexttask = print_q.dequeue()
            # get the waiting time of new task and add it to our records
            waiting_times.append(nexttask.wait_time(current_second))
            # start the new print task .
            lab_printer.start_next(nexttask)

        # tick 1s of time for printer and do the operations of printer for that second
        lab_printer.tick()

    # when all times are collected, calculate the avg_wait 
    avg_wait = sum(waiting_times) / len(waiting_times)
    print(
        f"Avg. Wait {avg_wait: 6.2f} secs" \
        + f"{print_q.size():3d} tasks remaining."
    )



def new_print_task() -> bool:
    num = random.randrange(1, 181)
    return num == 180

for i in range(10):
    simulation(3600, 10)