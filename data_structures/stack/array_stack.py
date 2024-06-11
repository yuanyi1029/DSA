class ArrayStack: 
    MINIMUM_CAPACITY = 1

    def __init__(self, capacity): 
        self.array = [None] * max(capacity, self.MINIMUM_CAPACITY)
        self.size = 0 

    def is_empty(self):
        return self.size == 0  
    
    def is_full(self): 
        return self.size == len(self.array)

    def push(self, item): 
        if self.is_full(): 
            raise Exception("ArrayStack is Full") 
        else: 
            self.array[self.size] = item
            self.size += 1 

    def pop(self): 
        if self.is_empty():
            raise Exception("ArrayStack is Empty")
        else: 
            item = self.array[self.size - 1] 
            self.size -= 1 
            return item

    def peek(self): 
        item = self.array[self.size - 1]
        return item 

    def __str__(self): 
        return_string = f"{self.array}" 
        return return_string 

if __name__ == "__main__": 
    pass 