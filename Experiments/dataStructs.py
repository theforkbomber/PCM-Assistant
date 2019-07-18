class Stack:
    """Initialising the stack object"""
    def __init__(self, maxElements, mode):
        self.contents = [None] * maxElements
        self.maxElements = maxElements
        self.mode = mode #static and dynamic
        self.head = 0
        self.tail = -1
    
    """Defining the 'add' procedure"""
    def add(self, data):
        if self.mode == 'static':
            if self.tail < self.maxElements - 1:
                self.tail += 1
                self.contents[self.tail] = data #input('What would you like to store?')
            elif self.tail == self.maxElements - 1:
                print('Stack is full!')
            else:
                #raise QueueError
                print('Error encountered (cannot exceed maxElements)')
        elif self.mode == 'dynamic':
            self.tail += 1
            self.contents.append(None)
            self.contents[self.tail] = data

    """Defining the 'remove' procedure"""
    def remove(self):
        if self.mode == 'static':
            if self.tail == -1:
                print('Stack is empty, cannot remove element.')
            elif self.tail < -1:
                print('Error encountered (cannot preceed logical minumum value of \'tail\')')
            elif self.tail > self.maxElements - 1:
                print('Error encountered (cannot exceed maxElements)')
            else:
                self.contents[self.tail] = None
                self.tail -= 1
        elif self.mode == 'dynamic':
            if self.tail == -1:
                print('Stack is empty, cannot remove element.')
            else:
                self.contents[self.tail] = None
                self.contents = self.contents[:len(self.contents)-1]
                self.tail -= 1

class Queue:
    """Initialising the queue object"""
    def __init__(self, maxElements, isCircular, mode):
        self.contents = [None] * maxElements
        self.maxElements= maxElements
        self.isCircular = isCircular
        self.mode = mode #static or dynamic
        self.tail = -1
        self.head = 0
       # self.tailindex = -1
       # self.headindex = maxElements

    """Defining the 'add' procedure"""
    def add(self, data):
        if self.mode == 'static':
            if self.isCircular:
               # if -self.tail > 0:
               #     self.contents[(self.tail+1) % self.maxElements] = data
               #     self.tail += 1
                if self.tail == self.head + (self.maxElements - 1):
                    print('Queue is full!')
                elif self.tail - self.head < self.maxElements - 1:
                    self.tail += 1
                    self.contents[self.tail % self.maxElements] = data #input('What would you like to store?')
                   # self.tail += 1
                   # except IndexError:
                   #     self.tail =  (self.tail + 1) % self.maxElements
                   #     print(self.tail, self.maxElements)
                   #     self.contents[self.tail] = data
                   #     self.tail += 1
                else:
                    #raise QueueError
                    print('Error encountered (cannot exceed maxElements)')
            else:
                if self.tail < self.maxElements - 1:
                    self.tail += 1
                    self.contents[self.tail] = data #input('What would you like to store?')
                elif self.tail == self.maxElements - 1:
                    print('Queue is full!')
                else:
                    #raise QueueError
                    print('Error encountered (cannot exceed maxElements)')
        elif self.mode == 'dynamic':
            self.contents.append(None)
            self.tail += 1
            self.contents[self.tail] = data

    """Defining the 'remove' procedure"""
    def remove(self):
        if self.mode == 'static':
            if self.isCircular:
                if self.tail == self.head - 1:
                    print(self.tail == self.head - self.maxElements, self.tail == self.head - 1)
                    print('Queue is empty, cannot remove element.')
                elif (self.tail % self.maxElements) > self.maxElements:
                    print('Error encountered (cannot exceed maxElements)')
                else:
                    self.contents[self.head % self.maxElements] = None
                    self.head += 1
            else:
                if self.tail == -1:
                    print('Queue is empty, cannot remove element.')
                elif self.tail > self.maxElements:
                    print('Error encountered (cannot exceed maxElements)')
                else:
                    self.contents[self.head] = None
                    self.tail -= 1
                    self.contents = self.contents[1:]
                    self.contents.append(None)
        elif self.mode == 'dynamic':
            if self.tail == -1:
                print('Queue is empty, cannot remove element.')
            else:
                self.contents = self.contents[1:]
                #self.contents.append(None)
                self.tail -= 1


