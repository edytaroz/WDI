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
    prev = first
    curr = prev.next
    while curr.next is not None and curr.next.next is not None:
        if prev.val > curr.val:
            prev.next = curr.next
            curr = curr.next
        prev = prev.next
        curr = curr.next
    if curr.next is None or curr.next.next is None:
        if prev.val > curr.val:
            prev.next = curr.next
    return first

tab = [3,4,1,6,2,9,1]
first = make_link_list(tab)
print_link_list(first)
f = fun(first)
print_link_list(f)