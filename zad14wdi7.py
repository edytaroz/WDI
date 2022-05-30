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
    cur = prev.next
    nex = cur.next
    while nex is not None:
        if nex.val % cur.val == 0:
            prev.next = nex
            cur = nex
            nex = nex.next
        else:
            prev = cur
            cur = nex
            nex = nex.next
    return first


tab = [1,2,4,8,5,18,6]
first = make_link_list(tab)
print_link_list(first)
f = fun(first)
print_link_list(f)