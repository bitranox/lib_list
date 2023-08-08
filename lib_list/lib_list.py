# STDLIB
import fnmatch
import sys
from typing import Any, List, Optional, Tuple, Union


# deduplicate{{{
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
    # deduplicate}}}

    if not elements:
        return elements
    return list(set(elements))


# del_elements_containing{{{
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
    # del_elements_containing}}}
    if (not elements) or (not search_string):
        return elements

    ls_results = []
    for element in elements:
        if search_string not in element:
            ls_results.append(element)
    return ls_results


# filter_contains{{{
def filter_contains(elements: List[Any], search_string: str) -> List[str]:
    """Retrieve a list of string elements that contain the specified search string.

    >>> filter_contains([], 'bc')
    []
    >>> filter_contains(['abcd', 'def', 1, None], 'bc')
    ['abcd']
    """
    # filter_contains}}}
    if (not elements) or (not search_string):
        return elements

    ls_results = []
    for element in elements:
        if isinstance(element, str):
            if search_string in element:
                ls_results.append(element)
            else:
                continue
    return ls_results


# filter_fnmatch{{{
def filter_fnmatch(elements: List[Any], search_pattern: str) -> List[str]:
    """Retrieve a list of string elements which are matching the fnmatch search pattern

    >>> filter_fnmatch([], 'a*')
    []
    >>> filter_fnmatch(['abc', 'def', 1, None], 'a*')
    ['abc']
    """
    # filter_fnmatch}}}
    if not elements:
        return elements

    ls_results: List[str] = []
    for element in elements:
        if isinstance(element, str):
            if fnmatch.fnmatch(element, search_pattern):
                ls_results.append(element)
    return ls_results


# is_element_containing{{{
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
    # is_element_containing}}}
    if not elements:
        return False

    for element in elements:
        if isinstance(element, str):
            if search_string in element:
                return True
    return False


# is_fnmatching{{{
def is_fnmatching(elements: List[Any], search_pattern: str) -> bool:
    """True if at least one element is matching the searchpattern

    >>> is_fnmatching([], 'bc')
    False
    >>> is_fnmatching(['abcd', 'def', 1, None], '*bc*')
    True
    >>> is_fnmatching(['abcd', 'def', 1, None], '*1*')
    False

    """
    # is_fnmatching}}}
    if (not elements) or (elements is None):
        return False

    b_is_fnmatching = False
    for element in elements:
        if isinstance(element, str):
            if fnmatch.fnmatch(element, search_pattern):
                b_is_fnmatching = True
                break

    return b_is_fnmatching


# is_fnmatching_one_pattern{{{
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
    # is_fnmatching_one_pattern}}}
    if not elements:
        return False

    if not search_patterns:
        return False

    for search_pattern in search_patterns:
        if is_fnmatching(elements, search_pattern):
            return True

    return False


# substract_all_keep_sorting{{{
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
    # substract_all_keep_sorting}}}
    if not minuend:
        return minuend

    if not subtrahend:
        return minuend

    subtrahend = set(subtrahend)
    for element in subtrahend:
        while element in minuend:
            minuend.remove(element)
    return minuend


# substract_all_unsorted_fast{{{
def substract_all_unsorted_fast(minuend: List[Any], subtrahend: List[Any]) -> List[Any]:
    """substract the list l_subtrahend from list l_minuend
    if the same element is more than once in l_minuend, so all of that elements are subtracted.
    the sorting order of the minuend is NOT preserved

    >>> my_minuend = ['a','a','b']
    >>> my_subtrahend = ['a','c']
    >>> substract_all_unsorted_fast(my_minuend, my_subtrahend)
    ['b']
    """
    # substract_all_unsorted_fast}}}
    result = list(set(minuend) - set(subtrahend))
    return result


def ls_del_empty_elements(ls_elements: List[Any]) -> List[Any]:
    """
    >>> ls_del_empty_elements([])
    []
    >>> ls_del_empty_elements(['',''])
    []
    >>> ls_del_empty_elements(['','','a',None,'b'])
    ['a', 'b']
    >>> ls_del_empty_elements(['   ','','a',None,'b'])
    ['   ', 'a', 'b']
    >>> ls_del_empty_elements(['   ','','a',None,'b',0])
    ['   ', 'a', 'b']

    """

    return list(filter(None, ls_elements))


def ls_double_quote_if_contains_blank(ls_elements: List[str]) -> List[str]:
    """double quote all elements in a list of string which contain a blank

    >>> ls_double_quote_if_contains_blank([])
    []
    >>> ls_double_quote_if_contains_blank([''])
    ['']
    >>> ls_double_quote_if_contains_blank(['', 'double quote'])
    ['', '"double quote"']

    """
    if (not ls_elements) or (ls_elements is None):
        return []

    ls_newelements = []
    for s_element in ls_elements:
        if " " in s_element:
            s_element = '"' + s_element + '"'
        ls_newelements.append(s_element)
    return ls_newelements


def ls_elements_replace_strings(ls_elements: List[str], s_old: str, s_new: str) -> List[str]:
    """
    führe ein <str>.replace(s_old, s_new) in allen Elementen der Liste durch, welche vom Typ str sind

    >>> ls_elements_replace_strings(['a', 'b', 'c', 1], 'a', 'z')
    ['z', 'b', 'c', 1]
    >>> ls_elements_replace_strings([], 'a', 'z')
    []

    """

    if not ls_elements:
        return ls_elements

    ls_results = []
    for s_element in ls_elements:
        if isinstance(s_element, str):
            s_element = s_element.replace(s_old, s_new)
        ls_results.append(s_element)
    return ls_results


def ls_lstrip_list(list_of_strings: List[str], chars: str = "") -> List[str]:
    """
    strips list elements on the beginning of a list, were the value is chars
    >>> testlist = ['','','a','b','c','','']
    >>> ls_lstrip_list(testlist)
    ['a', 'b', 'c', '', '']
    >>> testlist = []
    >>> ls_lstrip_list(testlist)
    []
    """
    while list_of_strings and list_of_strings[0] == chars:
        list_of_strings = list_of_strings[1:]
    return list_of_strings


def ls_rstrip_elements(ls_elements: List[str], chars: Union[None, str] = None) -> List[str]:
    """
    >>> ls_rstrip_elements(['  a','bbb','c   '])
    ['  a', 'bbb', 'c']
    >>> ls_rstrip_elements([])
    []

    """

    if (not ls_elements) or (ls_elements is None):
        return list()
    return [s_element.rstrip(chars) for s_element in ls_elements]


def ls_rstrip_list(list_of_strings: List[str], chars: str = "") -> List[str]:
    """
    strips list elements on the end of a list, were the value is chars
    >>> testlist = ['','','a','b','c','','']
    >>> ls_rstrip_list(testlist)
    ['', '', 'a', 'b', 'c']
    >>> testlist = []
    >>> ls_rstrip_list(testlist)
    []

    """
    while list_of_strings and list_of_strings[-1] == chars:
        list_of_strings = list_of_strings[:-1]
    return list_of_strings


def ls_strip_afz(ls_elements: Optional[List[str]]) -> List[str]:
    """
    Entfernt die Anführungszeichen für alle Elemente einer Liste mit Strings.

    >>> ls_strip_afz(['"  a"',"'bbb'",'ccc', "   'ddd'"])
    ['  a', 'bbb', 'ccc', 'ddd']
    >>> ls_strip_afz([])
    []
    >>> ls_strip_afz(None)
    []

    """

    # ['"  a"',"'bbb'",'ccc'] --> ['  a','bbb','ccc']

    if (not ls_elements) or (ls_elements is None):
        return []

    ls_newelements = []
    for s_element in ls_elements:
        # Anführungszeichen aus dem Value entfernen
        s_element = s_element.strip()
        if (s_element.startswith('"') and s_element.endswith('"')) or (s_element.startswith("'") and s_element.endswith("'")):
            s_element = s_element[1:-1]
        ls_newelements.append(s_element)
    return ls_newelements


def ls_strip_elements(ls_elements: List[str], chars: Union[None, str] = None) -> List[str]:
    """
    >>> ls_strip_elements(['  a','bbb','   '])
    ['a', 'bbb', '']
    >>> ls_strip_elements([])
    []

    """

    if (not ls_elements) or (ls_elements is None):
        return list()
    return [s_element.strip(chars) for s_element in ls_elements]


def ls_strip_list(list_of_strings: List[str], chars: str = "") -> List[str]:
    """
    strips list elements of a list, were the value is chars
    >>> testlist = ['','','a','b','c','','']
    >>> ls_strip_list(testlist)
    ['a', 'b', 'c']

    """

    list_of_strings = ls_lstrip_list(list_of_strings, chars)
    list_of_strings = ls_rstrip_list(list_of_strings, chars)
    return list_of_strings


def ls_substract(ls_minuend: List[Any], ls_subtrahend: List[Any]) -> List[Any]:
    """
    subtrahiere Liste l_subtrahend von Liste l_minuend
    wenn ein Element in Liste l_minuend mehrfach vorkommt, so wird nur ein Element abgezogen :

    >>> l_minuend = ['a','a','b']
    >>> l_subtrahend = ['a','c']
    >>> ls_substract(l_minuend, l_subtrahend)
    ['a', 'b']

    """
    for s_element in ls_subtrahend:
        if s_element in ls_minuend:
            ls_minuend.remove(s_element)
    return ls_minuend


def split_list_into_junks(source_list: List[Any], junk_size: int = sys.maxsize) -> List[List[Any]]:
    """
    divides a List into Junks

    >>> result = split_list_into_junks([1,2,3,4,5,6,7,8,9,10],junk_size=11)
    >>> assert result == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]

    >>> result = split_list_into_junks([1,2,3,4,5,6,7,8,9,10],junk_size=3)
    >>> assert result == [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]

    >>> result = split_list_into_junks([1,2,3,4,5,6,7,8,9,10])
    >>> assert result == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]

    """
    l_lists = []
    remaining_list = source_list

    while len(remaining_list) > junk_size:
        part_list = remaining_list[:junk_size]
        l_lists.append(part_list)
        remaining_list = remaining_list[junk_size:]
    l_lists.append(remaining_list)
    return l_lists


def str_in_list_lower_and_de_double(list_of_strings: List[str]) -> List[str]:
    """
    to lower and deduplicate - does not keep order !

    str_in_list_lower_and_de_double(['a', 'b', 'c', 'b', 'A'])  --> 'a', 'b', 'c'

    >>> assert len (str_in_list_lower_and_de_double(['a', 'b', 'c', 'b', 'A'])) == 3
    >>> str_in_list_lower_and_de_double([])
    []

    """
    if not list_of_strings:
        return list_of_strings
    list_of_strings_lower = str_in_list_to_lower(list_of_strings=list_of_strings)
    list_of_strings_lower_and_de_double = deduplicate(elements=list_of_strings_lower)
    return list_of_strings_lower_and_de_double


def str_in_list_non_case_sensitive(string: str, list_of_strings: List[str]) -> bool:
    """
    >>> str_in_list_non_case_sensitive('aba',['abc','cde'])
    False
    >>> str_in_list_non_case_sensitive('aBa',['abc','Aba'])
    True
    """
    string = string.lower()
    list_of_strings = [my_string.lower() for my_string in list_of_strings]
    if string in list_of_strings:
        return True
    else:
        return False


def str_in_list_to_lower(list_of_strings: List[str]) -> List[str]:
    """
    >>> str_in_list_to_lower(['A','b','C'])
    ['a', 'b', 'c']
    >>> str_in_list_to_lower([])
    []

    """
    if not list_of_strings:
        return list_of_strings

    return [string.lower() for string in list_of_strings]


def strip_and_add_non_empty_args_to_list(*args: Optional[str]) -> List[Any]:
    """
    erzeuge eine Liste von Argumenten, leere Argumente werden nicht in die Liste aufgenommen

    Input :        eine beliebige Anzahl von Argumenten z.Bsp. "a","b","c","","d"
    Output:        ["a","b","c","d"]
    Exceptions:    Exception bei Fehler

    >>> strip_and_add_non_empty_args_to_list('a  ', '  b', 'c', '', '  ')
    ['a', 'b', 'c']

    >>> strip_and_add_non_empty_args_to_list()
    []

    >>> strip_and_add_non_empty_args_to_list()
    []


    """

    if (not args) or (args is None):
        return list()

    ls_args = []
    for s_arg in args:
        s_arg = s_arg.strip()
        if s_arg:
            ls_args.append(s_arg)
    return ls_args
