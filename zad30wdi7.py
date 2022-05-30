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

def fun(first,first2):
    #prev = first
    #f = first.next
    f = first2
    while f is not None:
        prev = Node(None)
        curr = first
        while curr.val < f.val:
            prev = curr
            curr = prev.next
        if curr.val != f.val:
            a = Node(f.val)
            prev.next = a
            a.next = curr
        f = f.next
    return first



tab = [1,2,4,5,9,16,71]
tab2 = [11,2,7,23,3]
first = make_link_list(tab)
first2 = make_link_list(tab2)
print_link_list(first)
f = fun(first,first2)
print_link_list(f)