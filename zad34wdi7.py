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

def fun(first,k):
    f = first.next
    count = 0
    a = first
    while a.next != first:
        while f != a:
            if f.val == a.val:
                count += 1
            f = f.next
        if count == k:
            prev = first
            curr = prev.next
            while curr != a:
                if curr.val == a.val:
                    prev.next = curr.next
                    curr = prev.next
                else:
                    prev = curr
                    curr = curr.next
        a = a.next
    return first


tab = [1,2,3]
first = make_link_list(tab)
print_link_list(first)