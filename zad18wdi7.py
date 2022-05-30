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
    curr = first
    prev = first
    f = first.next
    while curr.next is not None:
        while f.next is not None:
            if curr.val == f.val:
                prev.next = f.next
                prev = prev.next
                f = prev.next
            else:
                prev = f
                f = f.next
        curr = curr.next
        prev = curr
        f = prev.next
    return first

tab = [1,2,8,2,5,7,1,8,4,9,10]
first = make_link_list(tab)
print_link_list(first)
f = fun(first)
print_link_list(f)