'''
 --- Directions
 Implement a Queue datastructure using two stacks.
 *Do not* create an array inside of the 'Queue' class.
 Queue should implement the methods 'add', and 'remove'.
 For a reminder on what each method does, look back
 at the Queue exercise.
 --- Examples
     const q = new Queue();
     q.add(1);
     q.add(2);
     q.remove(); // returns 1
     q.remove(); // returns 2
     q.remove(); // returns "No Item"
'''
class Queue:
    first_stack = []
    second_stack = []
    def add(self,record):
        #adds record to first_stack
        self.first_stack.append(record)
        
    def remove(self):
        #transfers items from first_stack to second_stack and returns top item
        if self.first_stack == []:
            return "No Item"
        
        while self.first_stack != []:
            self.second_stack.append(self.first_stack.pop())
            
        record = self.second_stack.pop()
        
        while self.second_stack != []:
            self.first_stack.append(self.second_stack.pop())
            
        return record
