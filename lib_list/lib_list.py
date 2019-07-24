# STDLIB
import fnmatch
import sys
from typing import List

# OWN
import lib_cast


def str_in_list_non_case_sensitive(string: str, list_of_strings: List[str]) -> bool:
    """
    >>> str_in_list_non_case_sensitive('aba',['abc','cde'])
    False
    >>> str_in_list_non_case_sensitive('aBa',['abc','Aba'])
    True
    """
    string = string.lower()
    list_of_strings = lib_cast.cast_list_of_strings_to_lower(list_of_strings)
    if string in list_of_strings:
        return True
    else:
        return False


def del_double_elements(list_elements: list) -> list:
    """
    >>> del_double_elements([])
    []
    >>> sorted(del_double_elements(['c','b','a']))
    ['a', 'b', 'c']
    >>> sorted(del_double_elements(['b','a','c','b','a']))
    ['a', 'b', 'c']
    """

    if not list_elements:  # leere Liste oder None wieder unverändert retournieren
        return list_elements
    return list(set(list_elements))


def str_in_list_to_lower(list_of_strings: [str]) -> [str]:
    """
    >>> str_in_list_to_lower(['A','b','C'])
    ['a', 'b', 'c']

    """
    if not list_of_strings:  # leere Liste oder None wieder unverändert retournieren
        return list_of_strings

    return [string.lower() for string in list_of_strings]


def str_in_list_lower_and_de_double(list_of_strings: [str]) -> [str]:
    if not list_of_strings:  # leere Liste oder None wieder unverändert retournieren
        return list_of_strings
    list_of_strings_lower = str_in_list_to_lower(list_of_strings=list_of_strings)
    list_of_strings_lower_and_de_double = del_double_elements(list_elements=list_of_strings_lower)
    return list_of_strings_lower_and_de_double


def ls_strip_elements(ls_elements: [str]) -> [str]:
    """
    >>> ls_strip_elements(['  a','bbb','   '])
    ['a', 'bbb', '']
    >>> ls_strip_elements([])
    []

    """

    if (not ls_elements) or (ls_elements is None):  # leere Liste oder None wieder unverändert retournieren
        return list()
    return [s_element.strip() for s_element in ls_elements]


def ls_del_empty_elements(ls_elements: []):
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


def ls_strip_afz(ls_elements: []) -> []:
    # Entfernt die Anführungszeichen für alle Elemente einer Liste mit Strings.
    # ['"  a"',"'bbb'",'ccc'] --> ['  a','bbb','ccc']

    if (not ls_elements) or (ls_elements is None):  # leere Liste oder None wieder unverändert retournieren
        return []

    ls_newelements = []
    for s_element in ls_elements:
        # Anführungszeichen aus dem Value entfernen
        s_element = s_element.strip()
        if (s_element[0] == '"') and (s_element[-1] == '"'):
            s_element = s_element[1:-1]
        else:
            if (s_element[0] == "'") and (s_element[-1] == "'"):
                s_element = s_element[1:-1]
        ls_newelements.append(s_element)
    return ls_newelements


def is_str_in_list_elements(ls_elements: [], s_search_string: str) -> bool:
    """ delivers true, if one of the strings in the list contains (or is equal) the searchstring """

    if not ls_elements:   # leere Liste no match, return False
        return False

    for s_element in ls_elements:
        if type(s_element) == str:
            if s_search_string in s_element:
                return True
    return False


def ls_del_elements_containing(ls_elements: list, s_search_string: str) -> []:
    """
    entferne jene Elemente deren Typ str ist und die s_search_string enthalten.
    gib alle anderen Elemente unverändert retour.

    :param ls_elements:                 eine Liste mit Elementen
    :param s_search_string:             der Suchstring

    :return:                            eine Liste mit den Resultaten
    """
    if (not ls_elements) or (not s_search_string):  # leere Liste oder None wieder unverändert retournieren
        return ls_elements

    ls_results = []
    for s_element in ls_elements:
        if s_search_string not in s_element:
            ls_results.append(s_element)
    return ls_results


def get_list_elements_containing(ls_elements: list, s_search_string: str) -> []:
    """
    liefere jene Elemente deren Typ str ist und s_search_string enthalten.

    :param ls_elements:                 eine Liste mit Elementen
    :param s_search_string:             der Suchstring

    :return:                            eine Liste mit den Resultaten
    """
    if (not ls_elements) or (not s_search_string):  # leere Liste oder None wieder unverändert retournieren
        return ls_elements

    ls_results = []
    for s_element in ls_elements:
        if type(s_element) == str:
            if s_search_string in s_element:
                ls_results.append(s_element)
            else:
                continue
    return ls_results


def ls_elements_replace_strings(ls_elements: list, s_old: str, s_new: str) -> []:
    """
    führe ein <str>.replace(s_old, s_new) in allen Elementen der Liste durch, welche vom Typ str sind

    :param ls_elements:                 eine Liste mit Elementen
    :param s_old:                       die zu Ersetzenden Zeichen
    :param s_new:                       die neuen Zeichen

    :return:                            eine Liste mit den Resultaten

    """

    if not ls_elements:  # leere Liste oder None wieder unverändert retournieren
        return ls_elements

    ls_results = []
    for s_element in ls_elements:
        if type(s_element) == str:
            s_element = s_element.replace(s_old, s_new)
        ls_results.append(s_element)
    return ls_results


def is_list_element_fnmatching(ls_elements: list, s_fnmatch_searchpattern: str) -> bool:
    """
    liefere True wenn einer der Elemente den s_searchstring (fnmatch) enthält

    :param ls_elements:                 eine Liste mit Elementen
    :param s_fnmatch_searchpattern:     der Suchstring

    :return:                            b_ls_fnmatching_searchstring
    """

    if (not ls_elements) or (ls_elements is None):  # leere Liste no match, return False
        return False

    b_ls_fnmatching_searchstring = False
    for s_element in ls_elements:
        if type(s_element) == str:
            if fnmatch.fnmatch(s_element, s_fnmatch_searchpattern):
                b_ls_fnmatching_searchstring = True
                break

    return b_ls_fnmatching_searchstring


def get_elements_fnmatching(ls_elements: [], s_fnmatch_searchpattern: str) -> []:
    """
    liefere jene Elemente deren Typ str ist und s_fnmatch_searchpattern enthalten.

    :param ls_elements:                 eine Liste mit Elementen
    :param s_fnmatch_searchpattern:     der Suchstring

    :return:                            eine Liste mit den Resultaten

    """
    if not ls_elements:  # leere Liste oder None wieder unverändert retournieren
        return ls_elements

    ls_results = []
    for s_element in ls_elements:
        if type(s_element) == str:
            if fnmatch.fnmatch(s_element, s_fnmatch_searchpattern):
                ls_results.append(s_element)
            else:
                continue
    return ls_results


def is_list_element_l_fnmatching(ls_elements: [], ls_fnmatch_searchpattern: [str]) -> bool:
    """
    liefere True wenn eines der ls_elements einen der ls_searchstrings (fnmatch) enthält

    :param ls_elements:                 eine Liste mit Elementen
    :param ls_fnmatch_searchpattern:   eine Liste von Suchstrings

    :return:    True, wenn eines der Listenelemente einen der searchpatterns enthält.
    :raises:    None

    """

    if not ls_elements:                 # leere Liste no match, return False
        return False

    if not ls_fnmatch_searchpattern:   # leere Liste no match, return False
        return False

    for s_fnmatch_searchpattern in ls_fnmatch_searchpattern:
        if fnmatch.filter(ls_elements, s_fnmatch_searchpattern):
            return True

    return False


def strip_and_add_non_empty_args_to_list(*args):
    """
    erzeuge eine Liste von Argumenten, leere Argumente werden nicht in die Liste aufgenommen
    Status:        Production
    Input :        eine beliebige Anzahl von Argumenten z.Bsp. "a","b","c","","d"
    Output:        ["a","b","c","d"]
    Exceptions:    Exception bei Fehler
    """

    if (not args) or (args is None):  # leere Liste oder None wieder unverändert retournieren
        return list()

    ls_args = []
    for s_arg in args:
        s_arg = s_arg.strip()
        if s_arg:
            ls_args.append(s_arg)
    return ls_args


def ls_substract(ls_minuend: [], ls_subtrahend: []) -> []:
    """
    subtrahiere Liste ls_subtrahend von Liste ls_minuend
    wenn ein Element in Liste ls_minuend mehrfach vorkommt, so wird nur ein Element abgezogen :

    >>> ls_minuend = ['a','a','b']
    >>> ls_subtrahend = ['a','c']
    >>> ls_substract(ls_minuend, ls_subtrahend)
    ['a', 'b']

    """
    for s_element in ls_subtrahend:
        if s_element in ls_minuend:
            ls_minuend.remove(s_element)
    return ls_minuend


def ls_substract_all(ls_minuend: [], ls_subtrahend: []) -> []:
    """
    subtrahiere Liste ls_subtrahend von Liste ls_minuend
    wenn ein Element in Liste ls_minuend mehrfach vorkommt, so werden alle Elemente abgezogen :
    >>> ls_minuend = ['a','a','b']
    >>> ls_subtrahend = ['a','c']
    >>> ls_substract_all(ls_minuend, ls_subtrahend)
    ['b']

    """
    for s_element in ls_subtrahend:
        while s_element in ls_minuend:
            ls_minuend.remove(s_element)
    return ls_minuend


def split_list_into_junks(source_list: list, junk_size: int = sys.maxsize) -> List[list]:
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
