import doctest


def bubble_sort(seq):
    """
    Put your doctests here:

    >>> bubble_sort([])
    []

    >>> bubble_sort([1.1,3.3,5.4,4.5,10.1])
    [1.1, 3.3, 4.5, 5.4, 10.1]

    >>> bubble_sort([1,2,3,4,5])
    [1, 2, 3, 4, 5]

    >>> bubble_sort(['hello world'])
    ['hello world']
    """
    changed = True
    while changed:
        changed = False
        for i in range(len(seq) - 1):
            if seq[i] > seq[i + 1]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
                changed = True
    return seq


doctest.testmod(verbose=True)

print(bubble_sort(['hello world']))