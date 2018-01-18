# algorithms
I built this package to help study sort algorithms and the fundamental data structures in computer science.
Currently, I'm working on implementing balanced trees in structs/*tree.py
I should point out that I wrote the sort algorithms a couple years ago, and I'll be cleaning them up / writing tests in the future.

To use this package:

-Clone the repo locally
-Install the package: pip install -e algorithms/
-Install nose: pip install nose
-Change to structs/ directory and run the tests: "cd structs/; python -m nose tests/"
-Change to scripts/ directory and run the sort benchmark: "bash test_sort.sh"

Example ^ output:
structs/tests:
"""python -m nose tests
...................................
----------------------------------------------------------------------
Ran 35 tests in 5.094s

OK
"""


test_sort.sh::
"""
Bash sort
real	0m0.811s
user	0m0.791s
sys	0m0.009s

Quick Sort
real	0m0.675s
user	0m0.630s
sys	0m0.034s

Merge Sort
real	0m13.664s
user	0m13.573s
sys	0m0.069s
"""
