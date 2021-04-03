from linked_list import LinkedList
class LinkedListQueue:

  def __init__(self):
    self.ll_queue = LinkedList()

  def enqueue(self, item):
    self.ll_queue.append(item)

  def dequeue(self):
    self.ll_queue.delete_from_head()

  def front(self):
    return self.ll_queue.head.data