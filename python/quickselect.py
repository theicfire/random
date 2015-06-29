import math
import random

def get_kth(l, k):
    if len(l) == k:
        return max(l)
    if all(map(lambda x: x == l[0], l)):
        return l[0] # If everything's the same, then the median is that

    pivot = l[int(random.random() * len(l))]
    left = filter(lambda x: x <= pivot, l)
    right = filter(lambda x: x > pivot, l)
    if k > len(left):
        return get_kth(right, k - len(left))
    return get_kth(left, k)

def get_midpoint(l):
    if len(l) % 2 == 1:
        return get_kth(l, math.ceil(len(l) / 2.0))
    center = len(l) / 2
    return (get_kth(l, center) + get_kth(l, center + 1)) / 2.0

def slow_midpoint(l):
    l = sorted(l)
    if len(l) % 2 == 1:
        return l[len(l) / 2]
    return (l[len(l) / 2] + l[(len(l) / 2) - 1]) / 2.0

def eq(l):
    return slow_midpoint(l) == get_midpoint(l)

def all_good():
    for x in range(500):
        l = [random.randint(0, 100) for x in range(random.randint(1, 100))]
        if not eq(l):
            return False
    return True

print all_good()
