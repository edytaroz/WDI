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
    f = first
    new = None
    tm = f
    count = 1
    while tm.next is not None:
        tm = tm.next
        count += 1
    tmp = f
    curr = f
    for i in range(count//2):
        while tmp.next != new:
            tmp = tmp.next
        new = tmp
        curr.val, new.val = new.val, curr.val
        tmp = curr.next
        curr = curr.next
    return first

tab = [1,2,3,4,5,6,7,8,9]
first = make_link_list(tab)
print_link_list(first)
f = fun(first)
print("z")
print_link_list(f)