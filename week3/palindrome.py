class Stacks:
    def __init__(self):
        self.top = []
    
    def push(self, e):
        self.top.append(e)
    
    def pop(self):
        if (len(self.top) != 0):
            return self.top.pop(-1)
        else:
            return None

    def size(self): 
        return len(self.top)
    
    def isEmpty(self):
        return self.top == []

    def peek(self): 
        if (len(self.top) != 0):
            return self.top[-1]
        else:
            return None



class Queues:
    def __init__(self):
        self.queue = []

    def enQueue(self, x):
        self.queue.append(x)
    
    def deQueue(self):
        if (len(self.queue) != 0):
            return self.queue.pop(0)
        else:
            return None
        
    def size(self):
        return len(self.queue)

    def isEmpty(self):
        return self.queue == []
    
    def peek(self):
        if (len(self.queue) > 0):
            return self.queue[0]
        else:
            return None

# Create a function called "isPalindrome" that accepts a string as a parameter and returns either True or False if the string is a Palindrome.
# A Palindrome String is a collection of alphabets which remains the exact same way when read backwards.  
# Note: This function must use both the Stack and Queue class.

def isPalindrome(data):
    stacks = Stacks()
    queues = Queues()
    for x in data:
        stacks.push(x)
        queues.enQueue(x)
    while stacks.isEmpty() != True:
        x = stacks.peek()
        z = queues.peek()
        if (x == z):
            stacks.pop()
            queues.deQueue()
        else:
            return False
    return True
    
print(isPalindrome('racecar'))
print(isPalindrome('noon'))
print(isPalindrome('python'))
print(isPalindrome('madam'))


myStack = Stacks()
myStack.push('p')
myStack.push('y')
myStack.push('t')
myStack.push('h')
myStack.push('o')
myStack.push('n')

print(myStack.top)
print(myStack.size())
print(myStack.peek())
print(myStack.pop())


myQueue = Queues()
myQueue.enQueue('p')
myQueue.enQueue('y')
myQueue.enQueue('t')
myQueue.enQueue('h')
myQueue.enQueue('o')
myQueue.enQueue('n')

print(myQueue.queue)
print(myQueue.size())
print(myQueue.peek())
print(myQueue.deQueue())















