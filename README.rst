lib_list
========


Version v1.1.9 as of 2023-08-08 see `Changelog`_

|build_badge| |codeql| |license| |jupyter| |pypi|
|pypi-downloads| |black| |codecov| |cc_maintain| |cc_issues| |cc_coverage| |snyk|



.. |build_badge| image:: https://github.com/bitranox/lib_list/actions/workflows/python-package.yml/badge.svg
   :target: https://github.com/bitranox/lib_list/actions/workflows/python-package.yml


.. |codeql| image:: https://github.com/bitranox/lib_list/actions/workflows/codeql-analysis.yml/badge.svg?event=push
   :target: https://github.com//bitranox/lib_list/actions/workflows/codeql-analysis.yml

.. |license| image:: https://img.shields.io/github/license/webcomics/pywine.svg
   :target: http://en.wikipedia.org/wiki/MIT_License

.. |jupyter| image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/bitranox/lib_list/master?filepath=lib_list.ipynb

.. for the pypi status link note the dashes, not the underscore !
.. |pypi| image:: https://img.shields.io/pypi/status/lib-list?label=PyPI%20Package
   :target: https://badge.fury.io/py/lib_list

.. |codecov| image:: https://img.shields.io/codecov/c/github/bitranox/lib_list
   :target: https://codecov.io/gh/bitranox/lib_list

.. |cc_maintain| image:: https://img.shields.io/codeclimate/maintainability-percentage/bitranox/lib_list?label=CC%20maintainability
   :target: https://codeclimate.com/github/bitranox/lib_list/maintainability
   :alt: Maintainability

.. |cc_issues| image:: https://img.shields.io/codeclimate/issues/bitranox/lib_list?label=CC%20issues
   :target: https://codeclimate.com/github/bitranox/lib_list/maintainability
   :alt: Maintainability

.. |cc_coverage| image:: https://img.shields.io/codeclimate/coverage/bitranox/lib_list?label=CC%20coverage
   :target: https://codeclimate.com/github/bitranox/lib_list/test_coverage
   :alt: Code Coverage

.. |snyk| image:: https://snyk.io/test/github/bitranox/lib_list/badge.svg
   :target: https://snyk.io/test/github/bitranox/lib_list

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black

.. |pypi-downloads| image:: https://img.shields.io/pypi/dm/lib-list
   :target: https://pypi.org/project/lib-list/
   :alt: PyPI - Downloads

some convenience functions for lists

----

automated tests, Github Actions, Documentation, Badges, etc. are managed with `PizzaCutter <https://github
.com/bitranox/PizzaCutter>`_ (cookiecutter on steroids)

Python version required: 3.8.0 or newer

tested on recent linux with python 3.8, 3.9, 3.10, 3.11, 3.12-dev, pypy-3.9, pypy-3.10 - architectures: amd64

`100% code coverage <https://codeclimate.com/github/bitranox/lib_list/test_coverage>`_, flake8 style checking ,mypy static type checking ,tested under `Linux, macOS, Windows <https://github.com/bitranox/lib_list/actions/workflows/python-package.yml>`_, automatic daily builds and monitoring

----

- `Try it Online`_
- `Usage`_
- `Usage from Commandline`_
- `Installation and Upgrade`_
- `Requirements`_
- `Acknowledgements`_
- `Contribute`_
- `Report Issues <https://github.com/bitranox/lib_list/blob/master/ISSUE_TEMPLATE.md>`_
- `Pull Request <https://github.com/bitranox/lib_list/blob/master/PULL_REQUEST_TEMPLATE.md>`_
- `Code of Conduct <https://github.com/bitranox/lib_list/blob/master/CODE_OF_CONDUCT.md>`_
- `License`_
- `Changelog`_

----

Try it Online
-------------

You might try it right away in Jupyter Notebook by using the "launch binder" badge, or click `here <https://mybinder.org/v2/gh/{{rst_include.
repository_slug}}/master?filepath=lib_list.ipynb>`_

Usage
-----------

the library provides following functions:

.. code-block:: python

    def deduplicate(elements: List[Any]) -> List[Any]:
        """get deduplicated list, does NOT keep Order !
        >>> deduplicate([])
        []
        >>> sorted(deduplicate(['c','b','a']))
        ['a', 'b', 'c']
        >>> sorted(deduplicate(['b','a','c','b','a']))
        ['a', 'b', 'c']
        >>> sorted(deduplicate(['x','x','x','y','y']))
        ['x', 'y']
        """

.. code-block:: python

    def del_elements_containing(elements: List[str], search_string: str) -> List[str]:
        """ delete the elements which contain (or are equal) the search_string

        >>> del_elements_containing(['a', 'abba', 'c'], 'b')
        ['a', 'c']
        >>> del_elements_containing(['a', 'abba', 'c'], 'z')
        ['a', 'abba', 'c']
        >>> del_elements_containing(['a', 'abba', 'c'], '')
        ['a', 'abba', 'c']
        >>> del_elements_containing([], 'b')
        []
        """

.. code-block:: python

    def filter_contains(elements: List[Any], search_string: str) -> List[str]:
        """Retrieve a list of string elements that contain the specified search string.

        >>> filter_contains([], 'bc')
        []
        >>> filter_contains(['abcd', 'def', 1, None], 'bc')
        ['abcd']
        """

.. code-block:: python

    def filter_fnmatch(elements: List[Any], search_pattern: str) -> List[str]:
        """Retrieve a list of string elements which are matching the fnmatch search pattern

        >>> filter_fnmatch([], 'a*')
        []
        >>> filter_fnmatch(['abc', 'def', 1, None], 'a*')
        ['abc']
        """

.. code-block:: python

    def is_element_containing(elements: List[str], search_string: str) -> bool:
        """delivers true, if one of the strings in the list contains (or is equal) the searchstring

        >>> is_element_containing([], '')
        False

        >>> is_element_containing(['abcd', 'def', 1, None], '')
        True

        >>> is_element_containing(['abcd', 'def', 1, None], 'bc')
        True

        >>> is_element_containing(['abcd', 'def', 1, None], 'fg')
        False
        """

.. code-block:: python

    def is_fnmatching(elements: List[Any], search_pattern: str) -> bool:
        """True if at least one element is matching the searchpattern

        >>> is_fnmatching([], 'bc')
        False
        >>> is_fnmatching(['abcd', 'def', 1, None], '*bc*')
        True
        >>> is_fnmatching(['abcd', 'def', 1, None], '*1*')
        False

        """

.. code-block:: python

    def is_fnmatching_one_pattern(elements: List[Any], search_patterns: List[str]) -> bool:
        """True if at least one element is matching at least one of the searchpatterns

        >>> is_fnmatching_one_pattern([], [])
        False

        >>> is_fnmatching_one_pattern(['abcd', 'def', 1, None], [])
        False

        >>> is_fnmatching_one_pattern(['abcd', 'def', 1, None], ['*bc*', '*fg*'])
        True

        >>> is_fnmatching_one_pattern(['abcd', 'def', 1, None], ['*fg*', '*gh*'])
        False
        """

.. code-block:: python

    def substract_all_keep_sorting(minuend: List[Any], subtrahend: List[Any]) -> List[Any]:
        """substract the list l_subtrahend from list l_minuend
        if the same element is more than once in l_minuend, so all of that elements are subtracted.
        the sorting order of the minuend is preserved

        >>> substract_all_keep_sorting([], ['a'])
        []
        >>> substract_all_keep_sorting(['a', 'a'], [])
        ['a', 'a']

        >>> my_l_minuend = ['a','a','b']
        >>> my_l_subtrahend = ['a','c']
        >>> substract_all_keep_sorting(my_l_minuend, my_l_subtrahend)
        ['b']
        """

.. code-block:: python

    def substract_all_unsorted_fast(minuend: List[Any], subtrahend: List[Any]) -> List[Any]:
        """substract the list l_subtrahend from list l_minuend
        if the same element is more than once in l_minuend, so all of that elements are subtracted.
        the sorting order of the minuend is NOT preserved

        >>> my_minuend = ['a','a','b']
        >>> my_subtrahend = ['a','c']
        >>> substract_all_unsorted_fast(my_minuend, my_subtrahend)
        ['b']
        """

Usage from Commandline
------------------------

.. code-block::

   Usage: lib_list [OPTIONS] COMMAND [ARGS]...

     some convenience functions for lists

   Options:
     --version                     Show the version and exit.
     --traceback / --no-traceback  return traceback information on cli
     -h, --help                    Show this message and exit.

   Commands:
     info  get program informations

Installation and Upgrade
------------------------

- Before You start, its highly recommended to update pip and setup tools:


.. code-block::

    python -m pip --upgrade pip
    python -m pip --upgrade setuptools

- to install the latest release from PyPi via pip (recommended):

.. code-block::

    python -m pip install --upgrade lib_list


- to install the latest release from PyPi via pip, including test dependencies:

.. code-block::

    python -m pip install --upgrade lib_list[test]

- to install the latest version from github via pip:


.. code-block::

    python -m pip install --upgrade git+https://github.com/bitranox/lib_list.git


- include it into Your requirements.txt:

.. code-block::

    # Insert following line in Your requirements.txt:
    # for the latest Release on pypi:
    lib_list

    # for the latest development version :
    lib_list @ git+https://github.com/bitranox/lib_list.git

    # to install and upgrade all modules mentioned in requirements.txt:
    python -m pip install --upgrade -r /<path>/requirements.txt


- to install the latest development version, including test dependencies from source code:

.. code-block::

    # cd ~
    $ git clone https://github.com/bitranox/lib_list.git
    $ cd lib_list
    python -m pip install -e .[test]

- via makefile:
  makefiles are a very convenient way to install. Here we can do much more,
  like installing virtual environments, clean caches and so on.

.. code-block:: shell

    # from Your shell's homedirectory:
    $ git clone https://github.com/bitranox/lib_list.git
    $ cd lib_list

    # to run the tests:
    $ make test

    # to install the package
    $ make install

    # to clean the package
    $ make clean

    # uninstall the package
    $ make uninstall

Requirements
------------
following modules will be automatically installed :

.. code-block:: bash

    ## Project Requirements
    click
    cli_exit_tools

Acknowledgements
----------------

- special thanks to "uncle bob" Robert C. Martin, especially for his books on "clean code" and "clean architecture"

Contribute
----------

I would love for you to fork and send me pull request for this project.
- `please Contribute <https://github.com/bitranox/lib_list/blob/master/CONTRIBUTING.md>`_

License
-------

This software is licensed under the `MIT license <http://en.wikipedia.org/wiki/MIT_License>`_

---

Changelog
=========

- new MAJOR version for incompatible API changes,
- new MINOR version for added functionality in a backwards compatible manner
- new PATCH version for backwards compatible bug fixes

v1.1.9
---------
2023-07-30:
    - flake 8 E721 do not compare types, for instance checks use `isinstance()`

v1.1.8
---------
2023-07-14:
    - add codeql badge
    - move 3rd_party_stubs outside the src directory to ``./.3rd_party_stubs``
    - add pypy 3.10 tests
    - add python 3.12-dev tests

v1.1.7
---------
2023-07-13:
    - require minimum python 3.8
    - remove python 3.7 tests
    - introduce PEP517 packaging standard
    - introduce pyproject.toml build-system
    - remove mypy.ini
    - remove pytest.ini
    - remove setup.cfg
    - remove setup.py
    - remove .bettercodehub.yml
    - remove .travis.yml
    - update black config
    - clean ./tests/test_cli.py

v1.1.6
--------
2022-03-25: implement github actions

v1.1.5
--------
2020-10-09: service release
    - update travis build matrix for linux 3.9-dev
    - update travis build matrix (paths) for windows 3.9 / 3.10

v1.1.4
--------
2020-08-08: service release
    - fix documentation
    - fix travis
    - deprecate pycodestyle
    - implement flake8

v1.1.3
---------
2020-08-01: fix pypi deploy

v1.1.2
--------
2020-07-31: fix travis build

0.1.1
--------
2020-07-29: feature release
    - use the new pizzacutter template
    - use cli_exit_tools

0.1.0
--------
2020-07-16: feature release
    - fix cli test
    - enable traceback option on cli errors
    - manage project with PizzaCutter

0.0.1
--------
2019-09-03: Initial public release

