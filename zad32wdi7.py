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
    f1 = first
    f2 = first2
    f = None
    while f1 is not None and f2 is not None:
        a = f1.val - f2.val
        tmp = Node(a)
        tmp.next = f
        f = tmp
        f1 = f1.next
        f2 = f2.next
    return f

tab = [1,2,3,4,5,6,7]
tab2 = [4,6,1,8,9,2,3]
first = make_link_list(tab)
first2 = make_link_list(tab2)
print_link_list(first)
f = fun(first,first2)
print_link_list(f)