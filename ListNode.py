# 节点类
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self._next = next

# 链表类异常
class LinkedListUnderflow(ValueError):
    pass

# 单向链表类
class LinkList:

    def __init__(self):
        self._head = None
        self.count = 0

    def is_empty(self):     # 判断是否为空表
        return self._head is None

    def prepend(self, listnode):    # 在表头插入元素
        self._head = ListNode(listnode, self._head)
        self.count += 1

    def pop(self):      # 去除表头元素并返回
        if not self._head:  # 无节点，引发异常
            raise LinkedListUnderflow('in pop')
        else:
            res = self._head.val
            self._head = self._head._next
            self.count -= 1
            return res

    def append(self,val):      # 在表后插入元素
        if not self._head:
            self._head = ListNode(val)
            self.count += 1
            return
        p = self._head
        while p._next:
            p = p._next
        p._next = ListNode(val)
        self.count += 1

    def pop_last(self):     # 删除表最后一个元素并返回
        if not self._head:
            raise LinkedListUnderflow('in pop_last')
        p = self._head
        if not p._next:
            self._head._next = None
            self.count -= 1
            return p.val
        while p._next._next is not None:
            p = p._next
        res = p._next
        p._next = None
        self.count -= 1
        return res.val

    def find(self, pred):   # 找到满足条件的第一个元素
        p = self._head
        while p:
            if pred(p.val):
                return p.val
            p = p._next

    def filter(self, pred):     # 筛选满足条件的元素
        p = self._head
        while p:
            if pred(p.val):
                yield p.val
            p = p._next

    def printall(self):     # 输出表
        p = self._head
        while p:
            print(p.val, end='')
            if p._next is not None:
                print(', ', end='')
            p = p._next
        print('')

    def for_each(self, proc):     # 遍历每个元素并进行操作
        p = self._head
        while p:
            proc(p.val)
            p = p._next

    def elements(self):     # 迭代器
        p = self._head
        while p:
            yield p.val
            p = p._next

    '''
    linklist = LinkList()
    for i in linklist.elements():
    '''

    def __len__(self):      # 返回链表长度
        if not self._head:
            raise LinkedListUnderflow('in len')
        return self.count

    def insert(self, n, val):    #定位插入数据
        if n > self.count-1:
            raise LinkedListUnderflow('in insert')
        p = self._head
        for j in range(n-1):
            p = p._next
        temp = p._next
        p._next = ListNode(val)
        p._next._next = temp
        self.count += 1

    def dele(self, n):  #删除指定位置元素
        if n > self.count-1:
            raise LinkedListUnderflow('in del')
        p = self._head
        for j in range(n-1):
            p = p._next
        p._next = p._next._next
        self.count -= 1

    def rev(self):      # 翻转链表
        p = None
        while self._head is not None:
            q = self._head
            self._head = self._head._next
            q._next = p
            p = q
        self._head = p

    def sort(self):     #基于改变链接的插入排序
        p = self._head
        if p is None or p._next is None:
            return
        rem = p._next
        p._next = None
        while rem is not None:
            p = self._head
            q = None
            while p is not None and p.val <= rem.val:
                q = p
                p = p._next
            if q is not None:
                self._head = rem
            else:
                q._next = rem
            q = rem
            rem = rem._next
            q._next = p


# 带尾节点引用的单向链表
# 可以O(1)时间内方便的在链表尾端操作
class LListwithTail(LinkList):

    def __init__(self):
        self._head = None
        self._rear = None

    def prepend(self, listnode):    # 在表头插入元素
        if self._head is None:
            self._head = ListNode(listnode, self._head)
            self._rear = self._head
            self.count += 1
        else:
            self._head = ListNode(listnode, self._head)
            self.count += 1

    def append(self,listnode):      # 在表后插入元素
        if self._head is None:
            self._head = ListNode(listnode, self._head)
            self._rear = self._head
            self.count += 1
        else:
            self._rear.next = ListNode(listnode)
            self._rear = self._rear.next
            self.count += 1

    def pop_last(self):     # 删除表最后一个元素并返回
        if not self._head:
            raise LinkedListUnderflow('in pop_last')
        p = self._head
        if not p.next:
            self._head.next = None
            self.count -= 1
            return p.val
        while p.next.next is not None:
            p = p.next
        res = p.next.val
        p.next = None
        self._rear = p
        self.count -= 1
        return res


# 循环单链表类
class CycleLList(LinkList):

    def __init__(self):
        self._rear = None

    def is_empty(self):
        return self._rear is None

    def prepend(self, listnode):
        p = ListNode(listnode)
        if self._rear is None:
            p.next = p
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear.next = p
        self.count += 1

    def append(self, listnode):
        self.prepend(listnode)
        self._rear = self._rear.next
        self.count += 1

    def pop(self):
        if self._rear is None:
            raise LinkedListUnderflow('in pop')
        p = self._rear.next
        if self._rear == p:
            self._rear = None
        else:
            self._rear.next = p.next
        self.count -= 1
        return p.val

    def printall(self):
        if self.is_empty():
            return
        p = self._rear.next
        while 1:
            print(p.val)
            if p == self._rear:
                break
            p = p.next


# 双链表节点类
class DLNode(ListNode):

    def __init__(self, val, prev=None, next=None):
        ListNode.__init__(self, val, next)
        self.prev = prev


# 双链表类
class DLList(LListwithTail):

    def __int__(self):
        LListwithTail.__init__(self)

    def prepend(self, val):
        p = DLNode(val, None, self._head)
        if self._head is None:
            self._head = p
        else:
            p.next.prev = p
        self._head = p
        self.count += 1

    def append(self, val):
        p = DLNode(val, self._rear, None)
        if self._head is None:
            self._head = p
        else:
            p.prev.next = p
        self._rear = p
        self.count += 1

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow('in pop')
        res = self._head.val
        self._head = self._head.next
        if self._head.next is not None:
            self._head.prev = None
        self.count -= 1
        return res

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow('in pop_last')
        res = self._rear.val
        self._rear = self._rear.prev
        if self._rear is None:
            self._head = None
        else:
            self._rear.next = None
        self.count -= 1
        return res



if __name__ == '__main__':
    ll = LinkList()
    for i in range(5):
        ll.append(i)
    ll.insert(2, 5)
    ll.printall()
    ll.dele(2)
    ll.printall()
