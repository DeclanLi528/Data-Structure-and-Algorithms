class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def set_next(self, new_next):
        self.next = new_next

class UnorderedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def is_empty(self):
        return self.head == None

    def add(self, data):
        tem = Node(data)
        tem.set_next(self.head)
        self.head = tem
        self.count += 1

    def size(self):
        return self.count

        return count
    
    def search_all(self,item):
        current = self.head
        positions = []
        index = 0

        while current is not None:
            if current.data == item:
                positions.append(index)
            current = current.next
            index += 1
            #这一行为了保证looping继续往下走 current.next /
            #index需要放在缩进前面
        return positions
    
    def remove_all(self,item):
        current = self.head
        previous = None

        found = False
        while current is not None:
            if current.data == item:
                found = True
                if previous is None:
                    self.head = current.next 
                    current = self.head
                else:
                    previous.next = current.next
                    current = current.next
            else:
                previous = current
                current = current.next

        if not found:
            raise ValueError
    
    def __str__(self):
        current = self.head
        items = []

        while current is not None:
            items.append(str(current.data))
            current = current.next

        return "[" + " ->".join(items) + "] "
    

    def append(self, data):
        current = self.head
        tem = Node(data)
        if current is None:
            self.head = tem
        else:
            while current.next is not None:
                current = current.next

            current.next = tem
    
    def index(self, item):
        current = self.head
        positions = []
        index = 0
        
        while current is not None:
            if current.data == item:
                positions.append(index)
            current = current.next 
            index += 1

        return positions
    
    def pop(self): #❌❌❌❌❌❌❌
        current = self.head
        previous = None
        pop_list = []

        if current is not None:
            while current.next != None:
                previous = current
                current = current.next
            pop_list.append(current)
            current = previous #这并不会真正的让最后一个元素被摘下

            return pop_list # pop方法通常返回的是被弹出的那个元素的数据或节点
        else:
            return None
        
    def pop(self):#✔️✔️✔️✔️✔️✔️✔️
        current = self.head
        previous = None

        if current == None:
            return None

        if current.next == None:
            data = current.data
            self.head = None
            return data

        while current.next is not None:
            previous = current
            current = current.next
        previous.next = None#删除尾部节点
        return current.data#返回弹出的数据

    def insert(self, position, data):
        current = self.head
        previous = None
        tem = Node(data)
        index = 0

        if position == 0:
            tem.next = self.head
            self.head = tem
            return

        while current is not None and index < position - 1:
            current = current.next
            index += 1

        if current is None:
            print("Position out of bounds!")
            return

        tem.next = current.next
        current.next = tem
            


            
