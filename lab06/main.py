import random


# 1.1
def quicksort(somelist):
    """
    quick sort of list
    :param somelist: list with numeric values
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


# 1.3
def findfirtsmin(somelist, count):
    """
    Function that finds first n-minimum items in list
    :param somelist: list
    :param count: how much elements you want to find
    :return: list of elements
    """
    if len(somelist) <= 1:
        return somelist
    else:
        sortedlist = quicksort(somelist)
        firstmins = []
        for i in range(count):
            firstmins.append(sortedlist[i])
        return firstmins


# 1.4
def findfirstmax(somelist, count):
    """
    Function that finds first n-maximum items in list
    :param somelist: list
    :param count: how much elements you want to find
    :return: list of elements
    """
    if len(somelist) <= 1:
        return somelist
    else:
        sortedlist = quicksort(somelist)
        sortedlist.reverse()
        firstmaxes = []
        for i in range(count):
            firstmaxes.append(sortedlist[i])
        return firstmaxes


# 1.5
def findaverage(somelist):
    """
    Finds average in the list of numbers.
    :param somelist: list of float or int
    :return: average number (float)
    """
    listlen = len(somelist)
    number = 0
    for i in somelist:
        number = number + i

    return number / listlen


randlist = random.sample(range(100), 9)
mylist = [1, 5, 10.2, 5, 6, 'word', 7, '7', 102,  24, 4245, 5]
print(randlist)
print(quicksort.__doc__)
print("list after being quicksorted: ", quicksort(randlist))
print(findelement.__doc__)
print("index of found element: ", findelement(mylist, 'word'))
print(findfirtsmin.__doc__)
print("first minimum values: ", findfirtsmin(randlist, 4))
print(findfirstmax.__doc__)
print("first maximum values: ", findfirstmax(randlist, 3))
print(findaverage.__doc__)
print("list average: ", findaverage(randlist))
