from Stack import Stack

'''#Implementing a stack with a dynamic array

#CREATE
my_stack = []

#UPDATE
#ADD
item = "A"
my_stack.append(item)
my_stack.append("B")
my_stack.append("C")

#DELETE
#remove the last item
my_stack.pop(len(my_stack) - 1)

#READ
print(my_stack[len(my_stack) - 1])'''

my_stack = Stack()

my_stack.push("hello")
my_stack.push("hey")
my_stack.push("hi")

print(my_stack.peek())

my_stack.my_pop()

print(my_stack.peek())

