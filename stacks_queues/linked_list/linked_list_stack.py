from linked_list import LinkedList

class LinkedListStack:

  def __init__(self):
    self.ll_stack = LinkedList()

  def push(self, item):
    self.ll_stack.prepend(item)

  def pop(self):
    self.ll_stack.delete_from_head()

  def peek(self):
    return self.ll_stack.head.data