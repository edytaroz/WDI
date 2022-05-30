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
    curr = first
    curr2 = first2
    count = 0
    while curr.next is not None and curr2 is not None:
        if curr.val == curr2.val:
            curr2 = curr2.next
            count += 1
        curr = curr.next
    if curr2 is None:
        return True,count
    return False

tab = [11,12,1,19,2,3,4,5,6,7]
tab2 = [1,2,3,4]
first = make_link_list(tab)
first2 = make_link_list(tab2)
print_link_list(first)
f = fun(first,first2)
print(f)