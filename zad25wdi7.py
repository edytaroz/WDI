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
    one_step = first
    two_step = first.next
    while one_step != two_step:
        one_step = one_step.next
        two_step = two_step.next.next
    # is _ in cykl
    f = first
    flag = True
    while flag:
        f = f.next
        while one_step != two_step:
            if f == one_step:
                flag = False
            one_step = one_step.next
    a = first
    while a.next != f:
        a = a.next
    return a


tab = [1,2,3]
first = make_link_list(tab)
print_link_list(first)