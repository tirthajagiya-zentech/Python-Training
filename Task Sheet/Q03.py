# Implement Circular Queue
#
# You script should contain four functions
# 1. Front: Get the front item from queue.
# 2. Rear: Get the last item from queue.
# 3. enqueue(value)
# 4. dequeue()
# User will be given choice to perform action from above four.
# Script should be kept running until user chooses to exit.

#method1
class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full")
            return
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return item

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        index = self.front
        while True:
            print(self.queue[index], end=" ")
            if index == self.rear:
                break
            index = (index + 1) % self.capacity
        print()

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue[self.front]

    def add_front(self, item):
        if self.is_full():
            print("Queue is full")
            return
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.front = (self.front - 1 + self.capacity) % self.capacity
        self.queue[self.front] = item

    def remove_rear(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        item = self.queue[self.rear]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.rear = (self.rear - 1 + self.capacity) % self.capacity
        return item

my_circular_queue = CircularQueue(5)

while True : 
    n = int(input("Enter 1 for enqueue element on to the circular queue \n Enter 2 for dequeue element on to the circular queue \n Enter 3 for peek element on to the circular queue \n Enter 4 for add element from front \n Enter 5 for remove element from rear \n Enter 6 for exit from the circular queue"))
    if n == 1 : 
        element = int(input("Enter element that you want to insert into the queue : "))
        my_circular_queue.enqueue(element)
        my_circular_queue.display()
    elif n == 2 :
        print("Removed element : ", my_circular_queue.dequeue())
        my_circular_queue.display()

    elif n == 3 : 
        print("Top Most element : " , my_circular_queue.peek())
        my_circular_queue.display()
    elif n == 4 : 
        element = int(input("Enter element that you want to insert from front : "))
        my_circular_queue.add_front(element)
        my_circular_queue.display()
    elif n == 5 : 
        print("Removed element : ", my_circular_queue.remove_rear())
        my_circular_queue.display()
    elif n == 6 : 
        break
    else :
        print("Enter Valid Number")

#method2
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.circular_queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self):
        if self.front == (self.rear+1) % self.size:
            print("Cquqeu is full")
            return
        elif self.front==-1:
            self.front=0
            self.rear=0
        else:
            self.rear = (self.rear + 1) % self.size
        ele = int(input("Enter elemenet :"))
        self.circular_queue[self.rear] = ele
        self.display()
        print("enquq")
    def dequeue(self):
        if self.front==-1:
            print("queue is underfloww")
            return
        print("removed element ",self.circular_queue[self.front])
        if self.front==self.rear:
            self.front=-1
            self.rear=-1
        
        else:
            self.front=(self.front+1)%self.size
        self.display()
    def peek(self):
        if self.front==-1:
            print("queue is underflow")
            return
        print("top elemenet:",self.circular_queue[self.front])

    def display(self):
        if self.front==-1:
            print("queue is underflow")
            return
        index = self.front
        while True:
            print(self.circular_queue[index], end=" ")
            if index == self.rear:
                break
            index = (index + 1) % self.size
        print()

    def add_to_front(self):
        if self.front == (self.rear+1)%self.size:
            print("queue is full")
            return
        ele=int(input("enter element to addd"))
        if self.front==-1:
            self.front=0
            self.rear=0
        else:
            self.front=(self.front-1+self.size)%self.size
        self.circular_queue[self.front]=ele
        self.display()

    def remove_from_rear(self):
        if self.front==-1:
            print("quuee underflow")
            return
        if self.front==self.rear:
            self.front=-1
            self.rear=-1
        else:
            self.rear=(self.rear-1+self.size)%self.size
        print("removed element ", self.circular_queue[self.rear])

circular_queue = CircularQueue(4)
while True:
    n=int(input("enter 1 for enqueue\n 2 for dequeue\n 3 for add into the front\n 4 for remove from the rear\n 5 for display\n 6 for peek\n 7 for exit"))

    if n==1:
        circular_queue.enqueue()
    elif n==2:
        circular_queue.dequeue()
    elif n==3:
        circular_queue.add_to_front()
    elif n==4:
        circular_queue.remove_from_rear()
    elif n==5:
        circular_queue.display()
    elif n==6:
        circular_queue.peek()
    elif n==7:
        break
    else:
        print("enter number between 1-7")
