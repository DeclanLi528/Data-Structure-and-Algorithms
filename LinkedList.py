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
            return #完成插入了，不需要执行后面的代码了，提前结束就可以

        tem.next = current.next
        current.next = tem


    def slice(self, start, stop):
        current = self.head
        index = 0
        new_list = UnorderedList()
   
        if self.head is None:
            return 
        
        if start >= stop or start < 0:
            return
        
        while current is not None:
            if start <= index < stop:
                new_list.append(current.data)
            elif index >= stop:
                break

            index += 1
            current = current.next
        
        return new_list

            
# 有序列表继承无序列表，但需改动add/search
class OrderList(UnorderedList):
    def __init__(self):
        super().__init__()#super().__init__()必须卸载类的方法中
        self.head = None
        self.count = 0

    def add(self, item):
        current = self.head
        previous = None
        new_code = Node(item)

        while current is not None and current.data < item:
            previous = current 
            current = current.next

        if previous is None:
            new_code.set_next(self.head)
            self.head = new_code
        else:
            new_code.set_next(current)
            previous.set_next(new_code)

        self.count += 1

    # def add(self, item): #❌❌❌❌❌❌❌
    #     current = self.head
    #     previous = None
    #     new_code = Node(item)

    #     if current is None:
    #         self.head = new_code
    #     else:
    #         if previous is None: #如果直接判断previous是否为None一定是None❌❌❌
    #             new_code.next = current
    #             self.head = new_code
    #         else:
    #             while current is not None and item > current.data:
    #                 previous = current
    #                 current = current.next
    #             new_code.next = current
    #             previous.next = new_code
    #             self.count += 1

    def add(self, item):
        current = self.head
        previous = None
        new_node = Node(item)

        if current is None:
            self.head = new_node
        else:
            while current is not None and item > current.data:
                previous = current
                current = current.next

            if previous is None:
                # 插入头部
                new_node.next = self.head
                self.head = new_node
            else:
                # 插入中间或末尾
                new_node.next = current
                previous.next = new_node

        self.count += 1


    def search(self, item):
        current = self.head

        while current is not None:
            if current.data == item:
                return True
            elif current.data > item:
                return False
            current = current.next
        
        return False
      
    #使用LinkedList 实现Stack
    #Stack的功能有push & pop

    class Stack:
        def __init__(self):
            self.head = None

        def is_empty(self):
            return self.head is None
        
        def push(self, item):
            new_code = Node(item)
            new_code.next = self.head
            self.head = new_code

        def pop(self):
            if self.is_empty():
                raise IndexError
            
            item = self.head.data
            self.head = self.head.next
            return item
        
        def peek(self):
            if self.is_empty():
                raise IndexError
            
            return self.head.data
        
        #用ListedList实现Queue(FIFO)
    class Queue:
        def __init__(self):
            self.head = None
            self.tail = None#双指针成就前后时间复杂度均为O(1)

        def is_empty(self):
            return self.head is None and self.tail is None
        
        #头出
        def dequeue(self): 
            if self.is_empty():
                raise IndexError
            
            item = self.head.data
            self.head = self.head.next

            if self.head is None:
                self.tail = None#这里如果不删除尾部,self.tail依旧存在
                #会和self.is_empty产生冲突
            return item
        #尾进 必须是自己维护tail,从头开始构建整个链表
        def enqueue(self, item): 
            new_code = Node(item)

            if self.tail is None:
                self.head = new_code
                self.tail = new_code
            else:
                self.tail.next = new_code
                self.tail = new_code

# 一个帮助设置拿到链表时自动设置好tail指针的函数
# def set_tail_from_head(self):
#     current = self.head
#     if current is None:
#         self.tail = None
#     else:
#         while current.next is not None:
#             current = current.next
#         self.tail = current

    class Deque:
        def __init__(self):
            self.head = None
            self.tail = None

        def is_empty(self):
            return self.head is None and self.tail is None

        def add_front(self, item):
            new_code = Node(item)
            if self.head is None:
                self.head = new_code
                self.tail = new_code
            else:
                new_code.next = self.head
                self.head = new_code
        
        def add_rear(self, item):
            new_code = Node(item)
            if self.tail is None:
                self.head = new_code
                self.tail = new_code
            else:
                self.tail.next= new_code
                self.tail = new_code
        
        def remove_front(self):
            if self.is_empty():
                raise IndexError
            
            item = self.head.data
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return item
            
        def remove_rear(self):
            if self.is_empty():
                raise IndexError
            
            if self.head == self.tail:
                item = self.head.data
                self.head = self.tail = None
                return item
            
            current = self.head
            while current.next != self.tail:
                current = current.next
            
            item = self.tail.data
            current.next = None
            self.tail = current
            return item


