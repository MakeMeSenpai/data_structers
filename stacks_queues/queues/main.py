from Queue import Queue

'''#CREATE a queue
#front at index 0
#back at index n - 1
my_queue = []

#UPDATE, ADD
#enqueue
my_queue.append("A")
my_queue.append("B")
my_queue.append("C")

#DELETE
#dequeue
my_queue.pop(0)

#READ 
#front
print(my_queue[0])'''

#CREATE
my_queue = Queue()

my_queue.enqueue("A")
#["A"]
my_queue.enqueue("B")
#["A", "B"]
my_queue.enqueue("C")
#["A", "B", "C"]

print(my_queue.front())