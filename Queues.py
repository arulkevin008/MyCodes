print("\t\t\tQueue Algorithm")
class Stack:
  def __init__(self):
    self.stack=[]

  def enqueue(self,value):
    self.value=value
    self.stack.append(self.value)
    return self.stack

  def dequeue(self):
    if self.stack == []:
      return "Stack is empty"
    return self.stack.pop(0)

  def peek(self):
    if self.stack == []:
      return "Stack is empty"
    return self.stack[0]

  def empty(self):
    if self.stack == []:
      return "Empty:True"
    return "Empty:False"

  def size(self):
    if len(self.stack) == 0:
      return "Stack Length is Zero"
    return len(self.stack)

myStack=Stack()

print("Queue Operations")
print("\n1.Enqueue")
print("2.Dequeue")
print("3.Peek")
print("4.isEmpty")
print("5.Size")
print("6.Exit")

while True:
  try:
    operation=int(input("\nEnter the operation no:"))

    if operation == 1:
      enqueue_element=input("Enter the enqueue element:")
      print(myStack.enqueue(enqueue_element))

    elif operation == 2:
      print(myStack.dequeue())

    elif operation == 3:
      print(myStack.peek())

    elif operation == 4:
      print(myStack.empty())

    elif operation == 5:
      print(myStack.size())

    elif operation == 6:
      print("Program exited...")
      exit()

  except Exception as e:
    print("\nError:",e)
    


