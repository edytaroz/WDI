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

def zad(first,n,value):
    while first is not None and first != n:
        first = first.next
    if first == n:
        a = first.val
        first.val = value
        return a
    if first is None:
        return False


tab = [1,2,3,4,5]
first = make_link_list(tab)
print_link_list(first)
print(zad(first,3,9))