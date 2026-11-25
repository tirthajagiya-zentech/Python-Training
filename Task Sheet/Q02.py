# Implement Queue
#
# You script should contain three functions
# 1. enqueue
# 2. dequeue
# 3. peek
# User will be given choice to perform action from above three.
# Script should be kept running until user chooses to exit.

#method1
class Queue : 
    def __init__(self) : 
        self.queue = []

    def enqueue(self,item) : 
        self.queue.append(item)

    def dequeue(self) : 
        if self.is_empty() : 
            print("Queue Underflow")
            return None

        return self.queue.pop(0)

    def peek(self) : 
         if self.is_empty() : 
            print("Queue Underflow")
            return None
         return self.queue[-1]

    def is_empty(self) : 
        return len(self.queue) == 0

    def display(self) : 
            if self.is_empty() : 
                print("Queue is empty")
                return
    
            for item in self.queue:
                print(item , end = ",")

my_queue = Queue()

while True : 
    n = int(input("Enter 1 for enqueue element on to the queue \n Enter 2 for dequeue element on to the queue \n Enter 3 for peek element on to the queue \n Enter 4 for exit from the queue"))

    if n == 1 : 
        element = int(input("Enter element that you want to insert into the queue : "))
        my_queue.enqueue(element)
        my_queue.display()
    elif n == 2 :
        print("Removed element : ", my_queue.dequeue())
        my_queue.display()

    elif n == 3 : 
        print("Top Most element : " , my_queue.peek())
        my_queue.display()
    elif n == 4 : 
        break
    else :
        print("Enter Valid Number")

#method2
queue = []

def enqueue():
    n = int(input("enter element:"))
    queue.append(n)
    display()

def dequeue():
    if len(queue) == 0:
        print("queue underflow")
    else:
        print("removed element is : ",queue.pop(0))
        display()

def peek():
    if len(queue) == 0:
        print("queue underflow")
    else:
        print("top element is ", queue[-1])

def display():
    if len(queue) == 0:
        print("queue underflow")
    else:
        for i in range(len(queue)):
            print(queue[i], end=",")
        print()

while True:
    n=int(input("1 for enqueue, 2 for dequqeue, 3 for peek, 4 for display and 5 for exit"))

    if n==1:
        enqueue()
    elif n==2:
        dequeue()
    elif n==3:
        peek()
    elif n==4:
        display()
    elif n==5:
        break
    else:
        print("enter number between 1-5")
