class Node:
    def __init__(self,value=None):
        self.val = value
        self.next = None
    def __repr__(self):
        return str(self.val)

def print_link_list(first):
    while first is not None:
        print('-->',first.val,end='')
        first = first.next
    return first

def make_link_list(tab):
    first = None
    n = len(tab)
    for i in range(n-1,-1,-1):
        tmp = Node(tab[i])
        tmp.next = first
        first = tmp
    return first

def fun(first):
    f0 = Node()
    f1 = Node()
    f2 = Node()
    f3 = Node()
    f4 = Node()
    f5 = Node()
    f6 = Node()
    f7 = Node()
    f8 = Node()
    f9 = Node()
    curr = first
    while curr is not None:
        if curr.val % 10 == 0:
            tmp = Node(curr.val)
            tmp.next = f0
            f0 = tmp
            curr = curr.next
        if curr.val % 10 == 1:
            tmp = Node(curr.val)
            tmp.next = f1
            f1 = tmp
            curr = curr.next
        if curr.val % 10 == 2:
            tmp = Node(curr.val)
            tmp.next = f2
            f2 = tmp
            curr = curr.next
        if curr.val % 10 == 3:
            tmp = Node(curr.val)
            tmp.next = f3
            f3 = tmp
            curr = curr.next
        if curr.val % 10 == 4:
            tmp = Node(curr.val)
            tmp.next = f4
            f4 = tmp
            curr = curr.next
        if curr.val % 10 == 5:
            tmp = Node(curr.val)
            tmp.next = f5
            f5 = tmp
            curr = curr.next
        if curr.val % 10 == 6:
            tmp = Node(curr.val)
            tmp.next = f6
            f6 = tmp
            curr = curr.next
        if curr.val % 10 == 7:
            tmp = Node(curr.val)
            tmp.next = f7
            f7 = tmp
            curr = curr.next
        if curr.val % 10 == 8:
            tmp = Node(curr.val)
            tmp.next = f8
            f8 = tmp
            curr = curr.next
        if curr is not None and curr.val % 10 == 9:
            tmp = Node(curr.val)
            tmp.next = f9
            f9 = tmp
            curr = curr.next
    f = f0
    while f0.next is not None:
        f0 = f0.next
    f0.next = f1
    f0 = f0.next
    while f1.next is not None:
        f1 = f1.next
    f1.next = f2
    f1 = f1.next
    while f2.next is not None:
        f2 = f2.next
    f2.next = f3
    f2 = f2.next
    while f3.next is not None:
        f3 = f3.next
    f3.next = f4
    f3 = f3.next
    while f4.next is not None:
        f4 = f4.next
    f4.next = f5
    f4 = f4.next
    while f5.next is not None:
        f5 = f5.next
    f5.next = f6
    f5 = f5.next
    while f6.next is not None:
        f6 = f6.next
    f6.next = f7
    f6 = f6.next
    while f7.next is not None:
        f7 = f7.next
    f7.next = f8
    f7 = f7.next
    while f8.next is not None:
        f8 = f8.next
    f8.next = f9
    f8 = f8.next
    while f9.next is not None:
        f9 = f9.next
    return f

tab = [5,4,7,9,1,3,2,6,8,10,23,74,23,98]
first = make_link_list(tab)
print_link_list(first)
f = fun(first)
print("z")
print_link_list(f)