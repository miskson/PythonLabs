import sys
import random
import re
from collections import namedtuple
# 1.1
def quicksort(somelist):
    """
    quick sort of list
    :param list: list with numeric values
    :return: list: sorted list
    """
    if len(somelist) <= 1:
        return somelist
    else:
        pivot = somelist[int(len(somelist)/2)]
        startnumbers = []
        middlenumbers = []
        endnumbers = []
        for i in somelist:
            if i < pivot:
                startnumbers.append(i)
            if i > pivot:
                endnumbers.append(i)
            elif i == pivot:
                middlenumbers.append(i)
    return quicksort(startnumbers) + middlenumbers + quicksort(endnumbers)

# 1.2
def findelement(somelist, element):
    """
    Function that finds wished element in the list
    :param somelist: list of elements
    :param element: element that needs to be found
    :return: index of found element or None
    """
    if len(somelist) >= 1:
        listindex = 0
        for i in somelist:
            if i == element:
                return listindex
            listindex += 1
        return None
    else:
        return None


def findfirstNmins(randlist, elemcount):
    """
        Function that fins out first N-min elements of list.
        :param randlist: randomized list
        :param elemcount: N-min elements to find
        :return: list: list of first N-min elements
        """
    if len(randlist) <= 1:
        return randlist
    else:
        firstNmins = []
        for i in range(len(randlist) - 1):
            if randlist[i] >= randlist[i + 1]:
                firstNmins.append(randlist[i + 1])
            if len(firstNmins) == elemcount:
                break
        return firstNmins

# 1.4
def findfirstNmaxes(randlist, elemcount):
    """
    Function that fins out first N-max elements of list.
    :param randlist: randomized list
    :param elemcount: N-max elements to find
    :return: list: list of first N-max elements
    """
    if len(randlist) <= 1:
        return randlist
    else:
        firstNmaxes = []
        for i in range(len(randlist) - 1):
            if randlist[i] >= randlist[i + 1]:
                firstNmaxes.append(randlist[i])
            if len(firstNmaxes) == elemcount:
                break
        return firstNmaxes


randlist = random.sample(range(100), 10)
mylist = [1, 5 ,10.2 ,5, 6 ,'word', 7 ,'7',102 , 24 ,4245, 5]
print(randlist)
print(findfirstNmaxes.__doc__)
print(findfirstNmaxes(randlist, 5))
print(randlist)
print(quicksort.__doc__)
print(quicksort(randlist))
#value = int(input("input searched value: "))
print(findelement.__doc__)
print(findelement(mylist, 'word'))
print(findfirstNmins.__doc__)
print(findfirstNmins(randlist,5))
