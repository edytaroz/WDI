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

def three(x):
    a = x
    count1 = 0
    count2 = 0
    sum = 0
    count = 0
    while a > 0:
        sum += (a % 3) * (10 ** count)
        count += 1
        if a%3 == 1:
            count1 += 1
        if a%3 == 2:
            count2 += 1
        a = a // 3
    if count1 > count2:
        return True
    return False



def fun(first):
    prev = first
    curr = prev.next
    while three(prev.val):
        if three(prev.val):
            first = first.next
            prev = first
            curr = prev.next
    while curr.next is not None and curr.next.next is not None:
        if three(curr.val):
            prev.next = curr.next
            prev = curr.next
            curr = prev.next
        else:
            prev = curr
            curr = curr.next
    if curr.next is None:
        if three(curr.val):
            prev.next = curr.next
    if curr.next.next is None:
        if three(curr.val):
            prev.next = curr.next
        if three(curr.next.val):
            curr.next = curr.next.next
    return first

tab = [12,37,65,61,101]
first = make_link_list(tab)
print_link_list(first)
f = fun(first)
print(three(101))
print_link_list(f)