class Node:
    def __init__(self,val=None):
        self.val = val
        self.next = None

    def check(self,x):
        while self.next is not None:
            if self.val == x:
                return True
            self.val = self.next
        return False

    def put(head,val,n,a):
        i = 0
        while i < n:
            head = head.next
            i += 1
        b = head.val
        head.val = a
        head.next = b

    def __repr__(self):
        return str(self.val)

x = Node(1)
y = 3
z = 7
print(x,y,z)

class Node:
    def __init__(self, x = None):
        self.val = x
        self.next = None

class zbior:
    def __init__(self, f = None):
        self.first = f

    def add(self, x):
        p = self.first
        q = None
        while p is not None and p.val < x:
            q = p
            p = p.next
        if p is not None and p.val == x:
            return
        tmp = Node(x)
        if q is not None:
            tmp.next = p
            q.next = tmp
            return
        tmp.next = p
        self.first = tmp

    def find(self, x):
        p = self.first
        while p.val > x:
            p = p.next
        return p.val == x
