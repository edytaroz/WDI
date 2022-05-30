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

def in_list(curr,first2):
    f = first2
    while f is not None and curr >= f.val:
        if f.val == curr:
            return True
        f = f.next
    return False

def fun(first,first2):
    prev = Node(None)
    prev2 = Node(None)
    curr = first
    curr2 = first2
    count = 0
    while curr.next is not None and curr.next.next is not None:
        if in_list(curr.val,first2):
            prev = curr
            curr = curr.next
        else:
            count += 1
            prev.next = curr.next
            curr = curr.next
    if curr.next.next is None:
        if in_list(curr.val,first2):
            prev = curr
            curr = curr.next
        else:
            count += 1
            prev.next = curr.next
            curr = curr.next
    if curr.next is None:
        if in_list(curr.val,first2) == False:
            count += 1
            prev.next = curr.next
    while curr2.next is not None and curr2.next.next is not None:
        if in_list(curr2.val,first):
            prev2 = curr2
            curr2 = curr2.next
        else:
            count += 1
            prev2.next = curr2.next
            curr2 = curr2.next
    if curr2.next.next is None:
        if in_list(curr2.val,first):
            prev2 = curr2
            curr2 = curr2.next
        else:
            count += 1
            prev2.next = curr2.next
            curr2 = curr2.next
    if curr2.next is None:
        if in_list(curr2.val,first) == False:
            count += 1
            prev2.next = curr2.next
    return count

tab = [1,3,5,6,7,9,11,12]
tab2 = [1,4,7,8,10,11]
first = make_link_list(tab)
first2 = make_link_list(tab2)
print_link_list(first)
f = fun(first,first2)
print(f)
#print_link_list(f)
#print(in_list(11,first2))