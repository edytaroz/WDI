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

def rev(first):
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

def fun(first1,first2):
    f1 = rev(first1)
    f2 = rev(first2)
    tmp1 = f1
    tmp2 = f2
    new = Node(tmp1.val + tmp2.val)
    while tmp1.next is not None or tmp2.next is not None:
        #new.next = Node(tmp1.val+tmp2.val)
        v = 0
        if tmp1.next is not None:
            tmp1 = tmp1.next
            v += tmp1.val
        if tmp2.next is not None:
            tmp2 = tmp2.next
            v += tmp2.val
        tmp = Node(v)
        tmp.next = new
        new = tmp
    return new

tab = [1,2,3]
tab2 = [5,6,6,1]
first1 = make_link_list(tab)
first2 = make_link_list(tab2)
print_link_list(first1)
f = fun(first1,first2)
print_link_list(f)