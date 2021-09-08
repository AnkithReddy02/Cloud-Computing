import random
from typing import List, Any
import functools

# Question 1


def split_givenstring(givenstring: str) -> list:
    """splits the given string into list of characters
    >>> split_givenstring("abc")
    ['a', 'b', 'c']
    >>> split_givenstring("ankith")
    ['a', 'n', 'k', 'i', 't', 'h']
    """

    list_char = []

    for c in givenstring:
        list_char.append(c)

    return list_char


# Question 2


def charlistToString(char_list: List[chr]) -> str:
    """returns the given char_list to string
    >>> charlistToString(['a','b','c'])
    'abc'
    >>> charlistToString(['a','n','k','i','t','h'])
    'ankith'
    """

    string_result = ""
    for c in char_list:
        string_result += c
    return string_result


# Question 3


def randomnumbers_list(n: int) -> List[int]:
    """ "" returns the list of the random numbers

    >>> random.seed(11)
    >>> randomnumbers_list(3)
    [58, 72, 60]
    >>> random.seed(13)
    >>> randomnumbers_list(6)
    [34, 38, 88, 24, 84, 30]
    """

    return random.sample(range(1, 100), n)


# Question 4


def sortnumbers_list(nums: List[int]) -> List[int]:
    """returns the sorted list in descending ordere
    >>> sortnumbers_list([1,2,3,4,5])
    [5, 4, 3, 2, 1]
    >>> sortnumbers_list([3,6,1,4,8])
    [8, 6, 4, 3, 1]
    """

    nums.sort(reverse=True)

    return nums


# Question 5


def frequency_numbers(nums: List[int]) -> dict[int, int]:

    """ "returns the frequency of each number in the list
    >>> frequency_numbers([1,1,3,2,3,2,3,2,2])
    {1: 2, 3: 3, 2: 4}
    >>> frequency_numbers([3,3,3,1,1,15,2,109])
    {3: 3, 1: 2, 15: 1, 2: 1, 109: 1}
    """

    freqdict = {}

    for x in nums:
        if x in freqdict:
            freqdict[x] = freqdict[x] + 1
        else:
            freqdict[x] = 1

    return freqdict


# Question 6


def unique_elements(nums: List[int]) -> set[int]:
    """returns the unique elements in the nums(list)
    >>> unique_elements([1,1,3,2,3,2,3,2,2])
    {1, 2, 3}
    >>> unique_elements([4,4,10,10,2,7,4,2,6,1])
    {1, 2, 4, 6, 7, 10}
    """
    myset = set()
    for x in nums:
        myset.add(x)

    return myset


# Question 7


def firstrepeating_number(nums: List[int]) -> int:
    """returns the first repeating number
    >>> firstrepeating_number([1,2,3,4,5,1,2])
    1
    >>> firstrepeating_number([2,3,1,2,5,3])
    2
    """

    myset = set()

    for x in nums:
        if x in myset:
            return x
        else:
            myset.add(x)

    # considering as there is no repeating element and there are only non-negative integers in list
    return -1


# Question 8


def square_cube_n(n: int) -> dict[int, list[int]]:
    """returns dict which contains square cube of elements from 0 to n
    >>> square_cube_n(3)
    {0: [0, 0], 1: [1, 1], 2: [4, 8], 3: [9, 27]}
    >>> square_cube_n(4)
    {0: [0, 0], 1: [1, 1], 2: [4, 8], 3: [9, 27], 4: [16, 64]}
    """
    mydict = dict()

    for i in range(0, n + 1):
        mydict[i] = list([i ** 2, i ** 3])

    return mydict


# Question 9


def create_tuples(list1: List[any], list2: List[any]) -> list[tuple]:
    """creates tuples from the given 2 lists of same size
    >>> create_tuples([1,2,3,4], ['a','b','c','d'])
    [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
    >>> create_tuples([5,1,2,3,4], [2,4,'b','c',3])
    [(5, 2), (1, 4), (2, 'b'), (3, 'c'), (4, 3)]
    """

    res = zip(list1, list2)
    reslist = list(tuple(res))
    return reslist


# Question 10


def squares_list(n: int) -> List[int]:
    """returns the list of squares of numbers from 0 to n
    >>> squares_list(5)
    [0, 1, 4, 9, 16, 25]
    >>> squares_list(7)
    [0, 1, 4, 9, 16, 25, 36, 49]
    """

    reslist = []
    for i in range(0, n + 1):
        reslist.append(i * i)
    # print(reslist)

    return reslist


# Question 11


def squares_dict(n: int) -> dict[int, int]:
    """returns the dict
    >>> squares_dict(5)
    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    >>> squares_dict(7)
    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}
    """
    mydict = {x: x ** 2 for x in range(0, n + 1)}

    return mydict


# Question 12


class MyClass:
    def __init__(self, mylist):
        self.list = mylist

    def apply(self, func) -> any:
        """doctests:
        >>> a = MyClass([1,2,3,4])
        >>> a.apply(lambda x: x**2)
        [1, 4, 9, 16]
        >>> a = MyClass(['a',6,'7',8])
        >>> a.apply(lambda x: x**2)
        'Unable to apply lambda function'
        """
        try:
            return [func(x) for x in self.list]
        except TypeError:
            return "Unable to apply lambda function"


# Question 13


def captialise_words(words: List[str]) -> List[str]:
    """it returns the list of given words with capitalized
    >>> captialise_words(['aa','bb','cd','e'])
    ['AA', 'BB', 'CD', 'E']
    >>> captialise_words(['AaB','AnkIth','HeLLO','Cc'])
    ['AAB', 'ANKITH', 'HELLO', 'CC']
    """

    def func(word: str) -> str:
        return word.upper()

    res = list(map(func, words))

    return res


# Question 14


def productlist(nums: list[int]) -> int:
    """returns product of all the elemnets in the given list
    >>> productlist([1,2,3,4,5])
    120
    >>> productlist([5,12,33,44,25])
    2178000
    """

    resproduct = functools.reduce(lambda a, b: a * b, nums)
    return resproduct


if __name__ == "__main__":
    import doctest

    doctest.testmod()
