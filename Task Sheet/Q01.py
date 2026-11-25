# Implement Stack
#
# Your script should contain three functions
# 1. push
# 2. pop
# 3. peep
# User will be given choice to perform action from above three.
# Script should be kept running until user chooses to exit.

#method2
class Stack : 
    def __init__(self) : 
        self.stack = []

    def push(self, item) : 
        self.stack.append(item)

    def pop(self) : 
        if self.is_empty():
            print("Stack Underflow")
            return None
        return self.stack.pop()

    def peep(self) : 
        if self.is_empty():
            print("Stack Underflow")
            return None
        return self.stack[-1]

    def is_empty(self) : 
        return len(self.stack) == 0

    def display(self) : 
        if self.is_empty() : 
            print("Stack is emepty")
            return

        for item in reversed(self.stack):
            print(item , end = " ")

# if __name__ == "__main__" : 
#     my_stack = Stack()

#     my_stack.push(10)    
#     my_stack.push(20)    
#     my_stack.push(30)

#     print(my_stack.peep())  

#     print(my_stack.pop())  
#     print(my_stack.pop())

#     print(my_stack.peep())  

#     print(my_stack.pop())
#     print(my_stack.peep())  

my_stack = Stack()

while True : 
    n = int(input("Enter 1 for Push element on to the stack \n Enter 2 for pop element on to the stack \n Enter 3 for peep element on to the stack \n Enter 4 for exit from the stack"))

    if n == 1 : 
        element = int(input("Enter element that you want to insert into the stack : "))
        my_stack.push(element)
        my_stack.display()
    elif n == 2 :
        print("Removed element : ", my_stack.pop())
        my_stack.display()

    elif n == 3 : 
        print("Top Most element : " , my_stack.peep())
        my_stack.display()
    elif n == 4 : 
        break
    else :
        print("Enter Valid Number")

#method2
stack = []

def push():
    n = int(input("enterr elemant"))
    stack.append(n)
    display()

def pop():
    if len(stack) == 0:
        print("stack is  emepty")
    else:
        print("deleted element:",stack.pop())
        display()

def peek():
    if len(stack) == 0:
        print("stack is emepty")
    else:
        print("top most element is:", stack[-1])

def display():
    if len(stack) == 0:
        print("stack is empty")
    else:
        for i in range(len(stack)):
            print(stack[i], end = ",")

while True:
    n=int(input("1 for push, 2 for pop, 3 for peek, 4 for display and 5 for exit"))

    if n==1:
        push()
    elif n==2:
        pop()
    elif n==3:
        peek()
    elif n==4:
        display()
    elif n==5:
        break
    else:
        print("enter number between 1-5")
