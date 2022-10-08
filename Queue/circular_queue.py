class circular_queue:
    def __init__(self, size):
        self.items = [0] * size

        self.max_size = size
        self.head, self.tail, self.size = 0, 0, 0

    def enqueue(self, item):
        if self.is_full():
            print("\nQueue is full.")
            return
        print("Inserting Item: ",item)
        self.items[self.tail] = item
        self.tail = (self.tail+1) % self.max_size
        self.size += 1

    def dequeue(self):
        item = self.items[self.head] 
        self.head = (self.head + 1) % self.max_size
        self.size -= 1 
        
        return item
    
    def is_empty(self):
        if self.size == 0:
            return True
        return False

    def is_full(self):
        if self.size == self.max_size:
            return True
        return False

if __name__ == "__main__":
    obj_cq = circular_queue(3)
    obj_cq.enqueue("hasan")
    obj_cq.enqueue("rafi")
    obj_cq.enqueue("sifat")
    obj_cq.enqueue("soikot")

    while not obj_cq.is_empty():
        person = obj_cq.dequeue()
        print("Dqueue item: ",person)
    
    obj_cq.enqueue("soikot")
    print(obj_cq.items)
    print("head: ", obj_cq.head)
    print("tail: ", obj_cq.tail)
    








