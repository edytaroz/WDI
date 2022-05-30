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
    prev = first
    prev2 = first2
    curr = prev.next
    curr2 = prev2.next
    count = 0
    while curr2.next is not None:
        while curr.next is not None and curr.next.next is not None and curr.val < curr2.val:
            prev = curr
            curr = curr.next
        if curr.val == curr2.val:
            count += 2
            prev.next = curr.next
            if curr.next is not None and curr.next.next is not None:
                prev = prev.next
                curr = prev.next
        prev2 = curr2
        curr2 = curr2.next
        prev = first
        curr = first.next
    return first

tab = [1,2,3,4,5,6,7]
tab2 = [19,4,10,2,78,34,6]
first = make_link_list(tab)
first2 = make_link_list(tab2)
print_link_list(first)
f = fun(first,first2)
print_link_list(f)