# will prove that the binary search has better time and space complexity compared to naive search
# naive search: go through every single element in the list and ask if it equals target

def naive_search(l, target):
    for i in range(l):
        if l[i] == target:
            return i
    return -1

# would want to sort list in binary search algorithm

#def sort(self,list):


def binary_search(l,target,low=None,high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l)-1

    if high < low:
        return -1

    midpoint = (low+high) // 2

    if l[midpoint] == target:
        return target
    elif l[midpoint] < target:
        return binary_search(l, target, midpoint+1, high)
    else: #l[midpoint] > target:
        return binary_search(l, target, low, midpoint-1)

if __name__ == '__main__':
    l=[0,1,5,3,9,2,7,11,19,17,13,12]
    target = 11
    print(naive_search(l,target))
    print(binary_search(l, target))
