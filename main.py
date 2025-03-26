import random, time
import tabulate
import sys
sys.setrecursionlimit(100000)

def ssort(a):
    ### selection sort
    if (len(a) == 1):
        return(a)
    else:
        m = a.index(min(a))
        # print('selecting minimum %s' % a[m])       
        a[0], a[m] = a[m], a[0]
        # print('recursively sorting L=%s\n' % a[1:])
        return [a[0]] + ssort(a[1:])

def qsort(a, pivot_fn):
    if len(a) <= 1:
        return a
    pivot = pivot_fn(a)
    left = [x for x in a if x < pivot]
    middle = [x for x in a if x == pivot]
    right = [x for x in a if x > pivot]
    return qsort(left, pivot_fn) + middle + qsort(right, pivot_fn)

def time_search(sort_fn, mylist):
    """
    Return the number of milliseconds to run this
    sort function on this list.

    Note 1: `sort_fn` parameter is a function.
    Note 2: time.time() returns the current time in seconds. 
    You'll have to multiple by 1000 to get milliseconds.

    Params:
      sort_fn.....the search function
      mylist......the list to search
      key.........the search key 

    Returns:
      the number of milliseconds it takes to run this
      search function on this input.
    """
    start = time.time()
    sort_fn(mylist)
    return (time.time() - start) * 1000
    ###

def compare_sort(sizes=[1, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]):
    """
    Compare the running time of different sorting algorithms.

    Returns:
      A list of tuples of the form
      (n, linear_search_time, binary_search_time)
      indicating the number of milliseconds it takes
      for each method to run on each value of n
    """
    qsort_fixed_pivot = lambda a: qsort(a, lambda x: x[0])
    qsort_random_pivot = lambda a: qsort(a, lambda x: random.choice(x))
    tim_sort = sorted
    result = []
    for size in sizes:
        # create list in ascending order
        mylist = list(range(size))
        # shuffles list if needed
        random.shuffle(mylist)
        result.append([
            len(mylist),
            time_search(ssort, mylist),
            time_search(qsort_fixed_pivot, mylist),
            time_search(qsort_random_pivot, mylist),
            time_search(tim_sort, mylist),
        ])
    return result
    ###
def print_results(results):
    print(tabulate.tabulate(results,
                            headers=['n', 'ssort', 'qsort-fixed-pivot', 'qsort-random-pivot', 'tim-sort'],
                            floatfmt=".3f",
                            tablefmt="github"))


def test_print():
    print_results(compare_sort())

random.seed()
test_print()