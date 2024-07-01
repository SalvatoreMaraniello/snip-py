# Sphinx

To generate documentation, use Sphinx. Refer to https://github.com/SalvatoreMaraniello/projects-templates


# Doctest

This is a native Python package, which allows python to look into your code, search for example and run them as a test. Is a good way to implement TDD.
For usage, see example [here](examples/factoral_doctest_example.py) taken from [official documentation here](https://docs.python.org/3/library/doctest.html). 

Add examples on how to use the object you define in the docstring, e.g.:
```
def factorial(n):
    """Return the factorial of n, an exact integer >= 0.
    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    """
    pass
```
Then add
```
if __name__ == "__main__":
    import doctest
    doctest.testmod()
```
in the module where the function is defined. 

You can now run tests using `python MODULE-NAME.py` (use option `-v` for verbose), or `python -m doctest -v MODULE-NAME.py` (this may not work if module is part of a package).



# Docstring styles

- `doctest` module: searches for pieces of text that look like interactive sessions. :) 

- `numpydoc`: `style for docstring`

    - https://numpydoc.readthedocs.io/en/latest/format.html

- Code style PEP8: https://www.python.org/dev/peps/pep-0008/

