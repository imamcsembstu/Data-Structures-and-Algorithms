class stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        return self.items.append(item) 
    def pop(self):
        return self.items.pop() # return for print()
    
    def is_empty(self):
        if self.items == []:
            return True
        return False

if __name__ == "__main__":
    obj_stack = stack()

    obj_stack.push(12)

    obj_stack.push(13)

    obj_stack.push(14)
   

    print("\nInitial Stack: ", obj_stack.items)

    while not obj_stack.is_empty():
        pop_item = obj_stack.pop()
        print("Pop Item or Element: ", pop_item)

    print("\nStack after items are Popped: ", obj_stack.items)



# Time and Space Complxity : O(1)
