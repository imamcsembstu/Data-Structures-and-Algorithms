class queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item) 
    def dequeue(self):
        return self.items.pop(0) # return for print()
    
    def is_empty(self):
        if self.items == []:
            return True
        return False

if __name__ == "__main__":
    obj_queue = queue()

    obj_queue.enqueue(12)

    obj_queue.enqueue(13)

    obj_queue.enqueue(14)
   

    print("\nInitial Queue: ", obj_queue.items)

    while not obj_queue.is_empty():
        deque_item = obj_queue.dequeue()
        print("Dequeue Item or Element: ", deque_item)

    print("\nQueue after items are Dequeue: ", obj_queue.items)



