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
    g = first
    while first is not None:
        prev = first
        curr = prev.next
        while curr is not None:
            a = first.val[0]
            b = first.val[1]
            c = curr.val[0]
            d = curr.val[1]
            if (a <= d and a >= c) or (b >= c and b <= d) or (c >= a and c <= b) or (d >= a and d <= b) :
                first.val[0] = min(a,c)
                first.val[1] = max(b,d)
                prev.next = curr.next
                #curr = prev.next
            else:
                prev = curr
            curr = prev.next
        first = first.next
    return g

tab = [[15,19],[2,5],[7,11],[8,12],[5,6],[13,17]]
first = make_link_list(tab)
print_link_list(first)
f = fun(first,12)
print_link_list(f)