'''
Goal: write a method that returns all permutations of a list
Input: ['a','b','c']
Output: [['a', 'b', 'c'], ['a', 'c', 'b'], ['b', 'a', 'c'], ['b', 'c', 'a'], ['c', 'a', 'b'], ['c', 'b', 'a']]
Credit: https://www.youtube.com/watch?v=hqijNdQTBH8
'''

def perm(lst):
    # base case
    if len(lst)==0:
        return []
    # base case
    elif len(lst) == 1:
        return [lst]
    # recursive case
    else:
        # init an empty list
        l = []
        # iterate through input list
        for i in range(len(lst)):
            # grab the first elem of each perm
            x = lst[i]
            # grab the remaining elems in the list
            xs = lst[:i]+lst[i+1:]
            for p in perm(xs):
                l.append([x]+p)
        return l

print(perm(['a','b','c', 'd', 'e']))