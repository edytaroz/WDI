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
    if first is None:
        return first2
    if first2 is None:
        return first
    g = Node()
    g.next = first
    prev = g
    a = g
    while first is not None and first2 is not None:
        if first.val < first2.val:
            prev = first
            first = first.next
        elif first.val == first2.val:
            tmp = first.next
            prev = first
            first.next = first2
            tmp2 = first2.next
            first2.next = tmp
            first2 = tmp2
            first = first.next
        else:
            tmp = first
            prev.next = first2
            tmp2 = first2.next
            first2.next = tmp
            prev = prev.next
            first = prev.next
            first2 = tmp2
    return a.next



tab = [1,2,6,12,13,23]
tab2 = [5,6,9,11]
first1 = make_link_list(tab)
first2 = make_link_list(tab2)
#first = rek(first1,first2)
#print_link_list(first)
f = fun(first1,first2)
print("z")
print_link_list(f)