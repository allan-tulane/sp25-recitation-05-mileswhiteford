# CMPS 2200 Reciation 5
## Answers

**Name:** Miles Whiteford, Aaron Gershkovich


Place all written answers from `recitation-05.md` here for easier grading.







- **1b.**
Sorted:
|     n |    ssort |   qsort-fixed-pivot |   qsort-random-pivot |   tim-sort |
|-------|----------|---------------------|----------------------|------------|
|     1 |    0.001 |               0.002 |                0.001 |      0.001 |
|    20 |    0.029 |               0.073 |                0.041 |      0.002 |
|    50 |    2.341 |               0.624 |                0.086 |      0.002 |
|   100 |    0.283 |               0.647 |                0.237 |      0.003 |
|   200 |    0.840 |               2.560 |                0.499 |      0.004 |
|   500 |    9.496 |              21.990 |                1.933 |      0.010 |
|  1000 |   79.985 |             121.966 |                3.567 |      0.015 |
|  2000 |  197.476 |             393.238 |                4.525 |      0.015 |
|  5000 |  776.661 |            1963.769 |               14.361 |      0.050 |
| 10000 | 2202.947 |            5792.638 |               26.976 |      0.095 |

Random:
|     n |    ssort |   qsort-fixed-pivot |   qsort-random-pivot |   tim-sort |
|-------|----------|---------------------|----------------------|------------|
|     1 |    0.001 |               0.002 |                0.001 |      0.001 |
|    20 |    0.020 |               0.019 |                0.031 |      0.002 |
|    50 |    0.060 |               0.041 |                0.059 |      0.003 |
|   100 |    0.246 |               0.109 |                0.124 |      0.007 |
|   200 |    0.688 |               0.207 |                0.257 |      0.015 |
|   500 |    9.395 |               0.897 |                1.142 |      0.054 |
|  1000 |   26.184 |               2.028 |                2.206 |      0.124 |
|  2000 |  162.481 |               3.887 |                4.101 |      0.224 |
|  5000 |  686.645 |              11.691 |               13.994 |      0.675 |
| 10000 | 2424.923 |              21.307 |               25.488 |      1.407 |

Selection Sort matches its theoretical time of O(n^2), which is the theoretical bound for it in both sorted and random lists. This is true because the data shows that as the numbers increase the time complexity increase exponentially.

Fixed Pivot Quicksort has very slow O(n^2) complexity for sorted lists because it picks the worst pivot (degenerate partition) each time, but on a random list it has O(nlogn) complexity because it is effectively picking a random term, which allows for many 'good' pivots to be picked. For the sorted array as the size of the list increases, the time increases exponentially, but for random it is O(nlogn).

Random Pivot Quicksort: Has O(nlogn) complexity for both sorted and unsorting because since it is always picking a random pivot, it will average out and eventually many 'good' pivots will be picked in the long run and avoids many bad pivots. 



- **1c.**
Timsort: Far and away the best, works incredibly well with sorted data, and marginally better than the other functions for unsorted data. It is about 10 times faster for a sorted array than for a random array.