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

def fun(first,key):
    def fun(first, key):
        f = first.next
        prev = f
        flag = True
        while f.next is not None:
            if f.val == key:
                prev.next = f.next
                flag = False
            prev = f
            f = f.next
        if flag:
            f.next = Node(key)
        return first

tab = [1,2,3,4,5,6,7]
first = make_link_list(tab)
print_link_list(first)
f = fun(first,5)
print_link_list(f)