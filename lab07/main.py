import random
import time
import datetime

REGISTERED = []


def register_decorator(func):
    def inner(*arguments):
        currentfunc = func(*arguments)
        i = 0
        for i in range(len(REGISTERED)):
            if func.__name__ == REGISTERED[i]:
                return currentfunc
            i = i + 1
        REGISTERED.append(func.__name__)
        return currentfunc

    return inner


def time_decoretor(func):
    def inner(n):
        """
            Decorator which counts time of function execution
            :param n: function to count execution time of
            :return: inner function
        """
        starttime = time.monotonic()
        func(n)
        endtime = time.monotonic()
        print("calculation time: ", datetime.timedelta(seconds=endtime - starttime))

    return inner


def chance_decorator(func):
    def inner(n):
        """
            Decorator to demonstrate multiple chances of function execution
            :param n: function to operate on
            :return: inner function
        """
        marker = False
        tries = 0
        for i in range(len(n)):
            tries = tries + 1
            marker = func(n)
            if marker is True:
                break

        print("Function finished after ", tries, " tries.")

    return inner


@register_decorator
def bubblesorted(somelist):
    """
    Simple bubble sort
    :param somelist: list to sort
    :return: sorted list
    """
    time.sleep(0.5)
    for i in range(len(somelist) - 1):
        for j in range(len(somelist) - i - 1):
            if somelist[j] > somelist[j + 1]:
                sortedlist = somelist[j]
                somelist[j] = somelist[j + 1]
                somelist[j + 1] = sortedlist
    return print(somelist)


@chance_decorator
@register_decorator
def randomsevendivision(somelist):
    """
    This is show-off function for demonstrating decorators capabilities.
    If random value of list could be divided by 7 without remainder
    :param somelist: list to operate on
    :return: boolean value
    """
    marker = False
    num = random.choice(somelist)
    print(num)
    if num % 7 == 0:
        marker = True
    else:
        marker = False

    return marker


@time_decoretor
@register_decorator
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

    return print(number / listlen)


randlist = random.sample(range(100), 20)

bubblesorted = time_decoretor(bubblesorted)
bubblesorted(randlist)
print(bubblesorted.__doc__)

randomsevendivision(randlist)
print(randomsevendivision.__doc__)

findaverage(randlist)

print(f"registered functions are: {REGISTERED}")

