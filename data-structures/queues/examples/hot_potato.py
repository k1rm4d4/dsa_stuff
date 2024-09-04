from queue2 import Queue

def hot_potato2(players, turns = 2):
    q = Queue()
    for p in players:
        q.enqueue(p)

    print(q)
    while q.size() > 1:
        for i in range(turns):
            q.enqueue(q.dequeue())
            # print(f"Ball is in hands of {p}.")

        elim = q.dequeue()
        print(f"{elim} eliminated from the game.")

    last = q.dequeue()
    print(f"{last} is the last player.")
    print(q)


def hot_potato(name_list, num):
    sim_queue = Queue()
    for name in name_list:
        sim_queue.enqueue(name)

    while sim_queue.size() > 1:
        for i in range(num):
            sim_queue.enqueue(sim_queue.dequeue())

        sim_queue.dequeue()

    return sim_queue.dequeue()

print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7)) # Susan