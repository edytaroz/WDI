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
    m = 0
    count = 0
    while curr.next is not None:
        if prev.val < curr.val:
            count += 1
            if count > m:
                m = count
        else:
            count = 0
        prev = curr
        curr = curr.next
    if curr.next is None:
        if prev.val < curr.val:
            count += 1
            if count > m:
                m = count
    if m == 0:
        return count
    return m + 1

tab = [6,4,7,9,2,3,4,5,6,1]
first = make_link_list(tab)
print_link_list(first)
f = fun(first)
print(f)