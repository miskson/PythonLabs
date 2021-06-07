# Лабораторна №06
## Функції
## Варіант 10
### Завдання 1
Розробіть функції для здійснення наступних операцій зі списками: 
1. Швидке сортування; 
2. Пошук елементу за значенням; 
3. Пошук перших 𝑛 мінімальних елементів; 
4. Пошук перших 𝑛 максимальних елементів; 
5. Пошук середнього арифметичного; 
6. Повернення списку, що сформований з початкового списку, але не містить 
повторів (залишається лише перший з однакових елементів).

Усі алгоритми були реалізовани згідно з вседоступними даними про алгоритми з інтернету і обернено у функції які приймають певні обов'язкові аргументи. Кожна функція приймає список, та робить над ним певні маніпуляції.

### Завдання 2
10. Визначити об’єм прибутку при вкладі заданої суми грошей х у банк
під встановлений процент річних y за n років

Значення знаходимо у циклі де на кожній ітерації до заданої суми додаємо вирахувана сума проценту річних

Усі функції було описано Doc string-ом. Doc string - являє собою короткий опис функції та аргументів які вона приймає.
```
[31, 66, 85, 69, 19, 76, 49, 34, 83, 81, 52, 28, 3, 98, 55, 7, 30, 42, 37, 24]

    Function to quick sort the list
    parameters:
        somelist(list): list with numeric values
    returns:
        (list) sorted list
    
list after being quicksorted:  [3, 7, 19, 24, 28, 30, 31, 34, 37, 42, 49, 52, 55, 66, 69, 76, 81, 83, 85, 98]

    Function that finds wished element in the list
    parameters:
        somelist(list): list of elements
        element: element that needs to be found
    returns:
        (int) index of found element or None
    
index of found element:  5

    Function that finds first n-minimum items in list
    parameters:
        somelist(list): list to operate on
        count(int): how much elements you want to find
    returns:
        (list) list of elements
    
first minimum values:  [3, 7, 19, 24]

    Function that finds first n-maximum items in list
    parameters:
        somelist(list): list to operate on
        count(int): how much elements you want to find
    returns:
        (list) list of elements
    
first maximum values:  [98, 85, 83]

    Finds average in the list of numbers.
    parameters:
        somelist(list): list to operate on
    returns:
        average(float): average number
    
list average:  48.45

    Function returns sorted list without any similar elements
    parameters:
        somelist(list): list to clean from similar items
    returns:
        newcleanedlist(list): cleaned list
    
cleanedlist : [0, 1, 2, 3, 4, 5, 6, 7, 8, 31, 67, 77]

    Function that determines the amount of profit when depositing a given amount of money in the bank
    under the established percentage of annual for years
    parameters:
        amount(float): amount of money to deposit
        years(int): amount of years
        percentage(float): percentage of annual
    returns:
        amount(float): amount of profit after years
    
my sum:  315.0

Process finished with exit code 0

```
