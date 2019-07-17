# Making data structures with head/tail logic (no explicit internal data comparisons made
# i.e.
# [x for x in self.contents if x] could represent the filled data, but it isn't made use of here

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
        if mode == 'static':
            # If tail is less than the index of the last possible element in the entire list
            # then tail is in the correct range, and depending on the follow-up procedure's
            # functionality, tail cannot go too far low and preceed the logical minimum
            # A stack is a 'first in, last out' [FILO] data structure, ergo, a stack adds data
            # at the head index, which is always 0. A FILO data structure is like an actual
            # stack of things, you could add to the stack from the bottom but in most cases that's
            # a bit inconvenient, so you add to the stack of, let's say, plates from the top
            if self.tail < self.maxElements - 1:
                self.tail += 1
                self.contents[self.tail] = data #input('What would you like to store?')
            # Otherwise, if tail is equal to the index of the last possible element in the entire
            # list, then the stack is assumed to be full
            elif self.tail == self.maxElements - 1:
                print('Stack is full!')
            # If all else fails, then the entire logic of the structure is compromised,
            # as of such an error is assumed to have occurred, which could be because the
            # values of the stack were modified manually at runtime or because there is a
            # bug in the code
            else:
                #raise QueueError
                print('Error encountered (cannot exceed maxElements)')
        elif mode == 'dynamic':
            self.tail += 1
            self.contents.append(None)
            self.contents[self.tail]

    """Defining the 'remove' procedure"""
    def remove(self):
        if mode == 'static':
            # If the tail is -1, what is designated as the logical value that
            # represents the logical minimum (if the tail is -1, then the stack
            # is assumed to be empty, and a negative capacity is not compatible with
            # this logic
            if self.tail == -1:
                print('Stack is empty, cannot remove element.')
            # If the tail is less than -1, then the entire logic of the structure is compromised
            # and an error is relayed to the end-user
            elif self.tail < -1:
                print('Error encountered (cannot preceed logical minumum value of \'tail\')')
            # If the tail is greater than the index of the last possible element in the list
            # then a logical failure has occurred and the end-user is notified
            elif self.tail > self.maxElements - 1:
                print('Error encountered (cannot exceed maxElements)')
            # If all the other checks have failed, then logically the stack can have an element removed.
            # As a stack is a FILO data structure, when an element is to be removed
            # it will be the last element that was added to the stack. Following on from the previous explanation,
            # you could remove a thing from a stack of things from the bottom, but that's still a bit inconvenient
            # in most cases. So, using the plates again, you remove the last added plate, ergo the top plate
            else:
                self.contents[self.tail] = None
                self.tail -= 1
        elif mode == 'dynamic':
            if self.tail == -1:
                print('Stack is empty, cannot remove element.')
            else:
                self.contents[self.tail] = None
                self.contents = self.contents[1:]
                tail -= 1

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
        if mode == 'static':
            # If the queue is circular, the logic differs a bit compared to a non-circular queue,
            # so the procedure heads down the circular route
            if self.isCircular:
               # if -self.tail > 0:
               #     self.contents[(self.tail+1) % self.maxElements] = data
               #     self.tail += 1

               # If the tail is equal to the sum of the head and the index of the last possible
               # element in the list, then the queue is assumed to be full. I've yet to determine
               # how exactly this logic works, but it's a behaviour that was observed during testing
               # and at the time of writing this it is an axiom that works
                if self.tail == self.head + (self.maxElements - 1):
                    print('Queue is full!')
                # If the difference between the tail and head is less than the index of the last possible
                # element in the list, then this procedure assumes the follow-up procedure works and thus
                # determines that the queue has neither exceeded the capacity nor has the tail been
                # altered outside of the procedure
                # A queue is a 'first in, first out' data structure [FIFO], so data is added at the tail index,
                # as each element has to wait its turn to be removed, like an actual queue
                elif self.tail - self.head < self.maxElements - 1:
                    self.tail += 1
                    self.contents[self.tail % self.maxElements] = data #input('What would you like to store?')
                   # self.tail += 1
                   # except IndexError:
                   #     self.tail =  (self.tail + 1) % self.maxElements
                   #     print(self.tail, self.maxElements)
                   #     self.contents[self.tail] = data
                   #     self.tail += 1
                # If all else fails, the queue us assumed to have exceeded the capacity
                # and the end-user is notified
                else:
                    #raise QueueError
                    print('Error encountered (cannot exceed maxElements)')
            #If the queue is non-circular, then the procedure heads down the non-circular route
            else:
                # If tail is less than the capacity, then the queue is assumed to contain some free space, this of course
                # depends on the functionality of the follow-up procedure. For an explanation as to why a queue behaves this way,
                # refer to the commenting in the previous branch
                if self.tail < self.maxElements - 1:
                    self.tail += 1
                    self.contents[self.tail] = data #input('What would you like to store?')
                # If the tail is equal to the index of the last possible element in the list,
                # then the queue is assumed to be full
                elif self.tail == self.maxElements - 1:
                    print('Queue is full!')
                # If all else fails, the queue is assumed to have exceeded its capacity, and the error
                # is reported
                else:
                    #raise QueueError
                    print('Error encountered (cannot exceed maxElements)')
        elif mode == 'dynamic':
            self.contents.append(None)
            self.tail += 1
            self.contents[self.tail] = data

    """Defining the 'remove' procedure"""
    def remove(self):
        if mode == 'static':
            if self.isCircular:
                # DEBUNKED
                # A bit rudimentary, as this logic was also only determined with testing and hasn't been
                # proven logically thus yet, however my theory is that this is actually correct because
                # after learning about reverse engineering compiled code using disassemblers,
                # both data structures (stacks and queues) can be said to start from the end or the beginning.
                # The stack begins from the beginning and so does the non-circular queue, but when making a circular
                # queue both motions are possible within the range of the actual queue, BUT if head and tail were to
                # be placed on a number line like so:
                # CAPACTITY = 5
                # -1 0 1 2 3 4 5 6 7 8 9 10 11 head 13 14 15 tail
                # Only the left to right motion is observed
                # if self.tail == self.head - self.maxElements
                # can ONLY work if the queue begins from the end, the theory was rather far-fetched and a bit flimsy because
                # if the number line works itself from left to right, why would the queue's motion change?
                #
                # Back to what this is actually doing though; if the tail is equal to what preceeds head, then the queue is 
                # assumed to be empty
                if self.tail == self.head - 1:
                    #print(self.tail == self.head - self.maxElements, self.tail == self.head - 1)
                    print('Queue is empty, cannot remove element.')
                # If the actual index (found by using modulus to get the remainder of tail / maxElements) is
                # greater than maxElements itself, the list has exceeded its capacity and the error is reported
                elif (self.tail % self.maxElements) > self.maxElements:
                    print('Error encountered (cannot exceed maxElements)')
                # If all else fails that means the tail is of a value that complies with the logic of the queue
                # Since a queue is a FIFO data structure, as with a real queue the person at the front is served
                # first
                else:
                    self.contents[self.head % self.maxElements] = None
                    self.head += 1
                   # except IndexError:
                   #     self.head %= self.maxElements
                   #     self.contents[self.head] = ''
                   #     self.head += 1
            else:
                # Since this queue never has a tail that exceeds a certain range,
                # will always signify an empty queue
                # e.g.
                # CAPACITY = 5
                # -1 0 1 2 3 4
                #    H
                #  t t t t t t
                # H is constant, so it remains at 0 at all times whereas
                # t can vary, but it can only be in the range shown above
                if self.tail == -1:
                    print('Queue is empty, cannot remove element.')
                # If the tail is greater than maxElements (relying on the previous function to make sure
                # tail is capped at the capacity), then the queue has exceeded its capacity, and you get the gist now
                elif self.tail > self.maxElements:
                    print('Error encountered (cannot exceed maxElements)')
                # If all else fails that means tail must logically be within the valid
                # range, for an explanation as to why the front is removed, refer to the
                # circular queue's remove logic
                else:
                    self.contents[self.head] = None
                    self.tail -= 1
                    self.contents = self.contents[1:]
                    self.contents.append(None)
        elif mode == 'dynamic':
            self.contents = self.contents[1:]
            self.contents.append(None)
            tail -= 1

#TODO
# [x] Make static data structures
#   [x] Make queues
#     [x] Circular
#       [x] Determine if theory is correct
#   [x] Non-circular
#     [x] Make stack
# [x] Comment static data structures
# [x] Make dynamic data structures
#   [x] Make queue
#   [x] Make stack
# [.] Comment dynamic data structures
# [x] Connect program to end-user program
