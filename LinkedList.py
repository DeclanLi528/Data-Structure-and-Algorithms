class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def set_next(self, new_next):
        self.next = new_next

class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, data):
        tem = None(data)
        tem.set_next(self.head)
        self.head = tem

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next

        return count
    
    def search(self,item):
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next

        return False
    
    def remove(self,item):
        current = self.head
        previous = None

        while current is not None:
            if current.data == item:
                break
            previous = current
            current = current.next

        #item不存在
        if current is None:
            raise ValueError(f"{item} is not in the list")
        #链表首个元素就是需要被删除的item
        if previous is None:
            self.head = current.next
        #正确删除(分两种情况，在中间删除和在结尾删除)
        else:
            previous.next = current.next