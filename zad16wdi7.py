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

def osemkowe(x):
    count = 0
    while x > 0:
        if x%8 == 5:
            count += 1
        x = x // 8
    if count > 0 and count%2 == 0:
        return True
    return False

def fun(first):
    prev = None
    curr = first
    prev.next = curr
    a = prev
    while curr.next is not None:
        if osemkowe(curr.val):
            tmp = curr
            prev.next = curr.next
            curr = prev.next
            a.next = tmp
            tmp.next = first
        else:
            prev = curr
            curr = curr.next
    return a.next


tab = [12,54,45,75,83]
first = make_link_list(tab)
print_link_list(first)
f = fun(first)
print(osemkowe(45))
print_link_list(f)