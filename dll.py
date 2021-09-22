class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def addToFront(self, newNode):
        if self.size == 0:
            self.head = newNode
            self.tail = newNode
            self.size += 1
        else:
            temp = self.head
            temp.prevVal = newNode
            newNode.nextVal = temp
            self.head = newNode
            self.size += 1

    def addToBack(self,newNode):
        if self.size == 0:
            self.head = newNode
            self.tail = newNode
            self.size += 1
        else:
            temp = self.tail
            temp.nextVal = newNode
            newNode.prevVal = temp
            self.tail = newNode
            self.size += 1

    def removeFromBack(self):
        if self.size == 0:
            print("Error: list is empty")
        elif self.size == 1:
            self.head = None
            self.tail = None
            self.size -= 1
        else:
            temp = self.tail.prevVal
            temp.nextVal = None
            self.tail = temp
            self.size -= 1

    def removeFromFront(self):
        if self.size == 0:
            print("Error: list is empty")
        elif self.size == 1:
            self.head = None
            self.tail = None
            self.size -= 1
        else:
            temp = self.head.nextVal
            temp.prevVal = None
            self.head = temp
            self.size -= 1

    def printList(self):
        print_val = self.head
        while print_val is not None:
            print(str(print_val.dataval))
            print_val = print_val.nextVal

    def averageList(self):
        iter1 = self.head
        sum_val = 0
        while iter1 is not None:
            sum_val += int(iter1.dataval)

            iter1 = iter1.nextVal
        return sum_val / self.size

    def getSize(self):
        return self.size
