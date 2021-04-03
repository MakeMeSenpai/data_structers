from linked_list import LinkedList

from linked_list_stack import LinkedListStack

from linked_list_queue import LinkedListQueue

'''ll_stack = LinkedList()
ll_stack.print_list()

#put top of stack at head of linked list

#PUSH
ll_stack.prepend(30)
ll_stack.prepend(40)
ll_stack.prepend(50)
ll_stack.print_list()

#POP
print("POP")
ll_stack.delete_from_head()
ll_stack.delete_from_head()
ll_stack.print_list()

#PEEK
print(ll_stack.head.data)'''

'''ll_stack = LinkedListStack()

ll_stack.push(30)
ll_stack.push(100)
ll_stack.push(25)

ll_stack.pop()

print(ll_stack.peek())'''

#build a queue using a linked list
#front queue at head
#back of queue at tail

'''ll_queue = LinkedList()

#enqueue
ll_queue.append(40)
ll_queue.append(49)
ll_queue.append(50)

#ll_queue.print_list()

#front
#print(ll_queue.head.data)

#dequeue

ll_queue.delete_from_head()
print(ll_queue.head.data)'''

ll_queue = LinkedListQueue()

ll_queue.enqueue(6)
ll_queue.enqueue(20)
ll_queue.enqueue(16)
ll_queue.enqueue(5)

ll_queue.dequeue()

print(ll_queue.front())

