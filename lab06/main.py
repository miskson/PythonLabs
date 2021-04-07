import random


# 1.1
def quicksort(somelist):
    """
    Function to quick sort the list
    parameters:
        somelist(list): list with numeric values
    returns:
        (list) sorted list
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
    parameters:
        somelist(list): list of elements
        element: element that needs to be found
    returns:
        (int) index of found element or None
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
    parameters:
        somelist(list): list to operate on
        count(int): how much elements you want to find
    returns:
        (list) list of elements
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
    parameters:
        somelist(list): list to operate on
        count(int): how much elements you want to find
    returns:
        (list) list of elements
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
    parameters:
        somelist(list): list to operate on
    returns:
        average(float): average number
    """
    listlen = len(somelist)
    number = 0
    for i in somelist:
        number = number + i

    return number / listlen


# 1.6
def cleanedlist(somelist):
    """
    Function returns sorted list without any similar elements
    parameters:
        somelist(list): list to clean from similar items
    returns:
        newcleanedlist(list): cleaned list
    """
    if len(somelist) <= 1:
        return somelist
    newcleanedlist = []
    sortedlist = quicksort(somelist)
    for i in range(len(sortedlist) - 1):
        if sortedlist[i] != sortedlist[i + 1]:
            newcleanedlist.append(sortedlist[i])
    newcleanedlist.append(sortedlist[len(sortedlist) - 1])
    return newcleanedlist


def yearlyincome(amount, percentage=5, years=1):
    """
    Function that determines the amount of profit when depositing a given amount of money in the bank
    under the established percentage of annual for years
    parameters:
        amount(float): amount of money to deposit
        years(int): amount of years
        percentage(float): percentage of annual
    returns:
        amount(float): amount of profit after years
    """
    for i in range(years):
        amount = amount + ((amount * percentage) / 100)
    return float("{0:.2f}".format(amount))


randlist = random.sample(range(100), 20)
mylist = [1, 5, 10.2, 5, 6, 'word', 7, '7', 102,  24, 4245, 5]
toclean = [0, 2, 3, 3, 1, 3, 1, 2, 67, 3, 4, 77, 7, 1, 8, 5, 6, 6, 7, 7, 5, 31, 77, 77, 77, 77, 77, 0]

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
print(cleanedlist.__doc__)
print("cleanedlist :", cleanedlist(toclean))
print(yearlyincome.__doc__)
print("my sum: ", yearlyincome(300))
