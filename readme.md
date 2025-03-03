# About this repo

Simple python project to show a way to take experiental execution time to compare a set of algorithms (three in this case) in fair way.

## Sort algorithms

### Problem statement
​
The sproblem is sorting a list of integers

| Algorithm        | Best Case        | Average Case      | Worst Case       | Space Complexity |
|-----------------|-----------------|------------------|------------------|------------------|
| **Selection Sort** | \( O(n^2) \)    | \( O(n^2) \)      | \( O(n^2) \)      | \( O(1) \)       |
| **Quick Sort**   | \( O(n log n) \) | \( O(n log n) \) | \( O(n^2) \) (unbalanced) | \( O(\log n) \) (recursive calls) |
| **Heap Sort**    | \( O(n log n) \) | \( O(n \log n) \) | \( O(n log n) \) | \( O(1) \) (in-place) |



# Python version
Python 3.11.0
​
# Running locally and testing

* Note: This instructions are for mac. Windows or linux may require some changes. 
* A good idea for this project, is to use a virtual environment, you could set up one with: [virtualenv](https://virtualenv.pypa.io/en/latest/).
* To create the virtual environment: `virtualenv env`
* To activate it:`source env/bin/activate`
* To install dependencies: `pip3 install -r requirements.txt`
* To run unit testing: `./test.sh`
* To try a default example, run: `: ./run.sh`. In the file ./run.sh is just an example, you can modify it. Theck the `app.py` file to get to understand how it works.

# Current coverage

Make sure you have "coverage" in your requirements.txt file and run pip install. Then run `coverage run -m unittest discover` and after that run `coverage report` to get the following table:

```
Name                          Stmts   Miss  Cover
-------------------------------------------------
sorting\__init__.py               0      0   100%
sorting\algorithms.py            39      0   100%
sorting\constants.py              2      0   100%
sorting\data_generator.py         9      1    89%
test\__init__.py                  0      0   100%
test\test_algorithms.py          22      1    95%
test\test_data_generator.py      29      1    97%
-------------------------------------------------
TOTAL                           101      3    97%
```

# Code beautifier
This code has been beautify using black: https://github.com/psf/black. 
The command to use is `black . -l 120`.
