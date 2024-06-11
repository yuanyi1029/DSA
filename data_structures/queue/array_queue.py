class ArrayQueue: 
    MINIMUM_CAPACITY = 1

    def __init__(self, capacity): 
        self.array = [None] * max(capacity, self.MINIMUM_CAPACITY)
        self.size = 0 
        self.head = 0 
        self.tail = 0 

    def is_empty(self):
        return self.size == 0 
    
    def is_full(self): 
        return self.size == len(self.array)

    def append(self, item): 
        if self.is_full(): 
            raise Exception("ArrayQueue is Full") 
        else: 
            self.array[self.tail] = item
            self.size += 1 
            self.tail = (self.tail + 1) % len(self.array) 

    def serve(self): 
        if self.is_empty():
            raise Exception("ArrayQueue is Empty")
        else: 
            item = self.array[self.head] 
            self.size -= 1
            self.head = (self.head + 1) % len(self.array)
            return item

    def peek(self): 
        item = self.array[self.head - 1]
        return item 

    def __str__(self): 
        return_string = f"{self.array}" 
        return return_string 

if __name__ == "__main__": 
    pass