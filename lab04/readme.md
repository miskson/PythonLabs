# Лабораторна №03
## Кортежі та словники
## Варіант 10
### Завдання А
Реалізувати режим виведення всіх значень словника;
Було реалізовано за допомогою функції, яка приймає у якості аргументу список кортежів. Список кортежей був згенерований з випадковими значеннями salary та sex.
```
Joebob : salary - 251.46 , sex - female
King : salary - 331.19 , sex - male
Bill : salary - 493.39 , sex - female
Mann : salary - 286.07 , sex - male
Ripley : salary - 339.79 , sex - male
Weaver : salary - 443.13 , sex - male
Hicks : salary - 308.5 , sex - male
Nukem : salary - 471.91 , sex - female
Anderson : salary - 329.42 , sex - male
Smith : salary - 474.98 , sex - male
```
### Завдання Б
Реалізувати додавання (видалення) нового запису до (зі) словника;
Також було реалізовано за допомогою окремих функцій які додають та видаляють кортежі по їх полям.
```
Let's update the dictionary, input following values(or input 'q' to exit): 
Surname: Levshnia
Salary: 2000
1 - male / 2 - female: 1
/Base has been updated.
Anderson : salary - 329.42 , sex - male
Bill : salary - 493.39 , sex - female
Hicks : salary - 308.5 , sex - male
Joebob : salary - 251.46 , sex - female
King : salary - 331.19 , sex - male
Mann : salary - 286.07 , sex - male
Nukem : salary - 471.91 , sex - female
Ripley : salary - 339.79 , sex - male
Smith : salary - 474.98 , sex - male
Weaver : salary - 443.13 , sex - male
Levshnia : salary - 2000.0 , sex - male
```
### Завдання В
Розробити  режим перегляду вмісту словника за відсортованими ключами (перетворити об’єкт подання ключів в список);
Функція сортує список за полем surname в алфавітному порядку.
```
Sorted list:
Anderson : salary - 329.42 , sex - male
Bill : salary - 493.39 , sex - female
Hicks : salary - 308.5 , sex - male
Joebob : salary - 251.46 , sex - female
King : salary - 331.19 , sex - male
Mann : salary - 286.07 , sex - male
Nukem : salary - 471.91 , sex - female
Ripley : salary - 339.79 , sex - male
Smith : salary - 474.98 , sex - male
Weaver : salary - 443.13 , sex - male
```
### Завдання 10
Задано дані про n=10 співробітників фірми (прізвище, зарплата і стать). Скласти програму, яка визначає: а) прізвище особи, яка має найбільшу зарплату (вважати, що такий є лише один); б) прізвища чоловіка і жінки, які мають найменшу зарплату (вважати, що такі є і вони єдині в своїй групі співробітників)

 а) Прізвище особи визначаеться за допомогою використання функції `max()` яка приймає в якості аргументів список співробітників та зарплату співробітника у якості ключа і шукає серед них людину з максимальною зарплатою. 
```
Maximal salary person:
Levshnia : salary - 2000.0 , sex - male
```

б) У функції программа окремо створює два списки: жінок та чоловіків. У цих списках вона знаходить людей з мінімальною зарплатою за допомогою  функції `min()`,   приймає в якості аргументів список співробітників та зарплату співробітника у якості ключа, і шукає серед них людину з максимальною зарплатою.
```
Minimal salary staff:
Mann : salary - 286.07 , sex - male
Joebob : salary - 251.46 , sex - female
```
