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
    curr = first.next
    nex = curr.next
    while nex.next is not None and nex is not None and nex.next.next is not None:
        prev.next = nex
        prev = nex
        curr = nex.next
        nex = curr.next
    if nex.next is None:
        prev.next = nex
    else:
        print("nn")
        prev.next = nex
        nex.next = None
    return first

tab = [1,2,3,4,5,6,7,8,9,10]
first = make_link_list(tab)
print_link_list(first)
f = fun(first)
print_link_list(f)