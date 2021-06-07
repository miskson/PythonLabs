# Лабораторна №05
## Множини та обробка рядків
## Варіант 10
### Завдання 1
Задано речення, в якому є декілька пар однакових слова. Скласти програму, 
яка визначає їх і виводить на екран.

Программа отримує строку і переверіяє її у функціях на те чи є вона строкою та не чи не містить вона заперечених знаків. Якщо строка проходить перевірку - вона буде розбита на список та відсортована за допомогою `sort()`, у вже відсортованому списку однакові слова будуть стояти поряд, це значить, що ми переберемо список у циклі та виведемо тільки слова які будуть зустрічатися 2 рази поспіль.
```
input string: this is a simple string. Nothing special, nothing special at all
Pairs of words that are similar it the string:  ['special', 'special']
```
### Завдання 2
A) Задано текст (не менше 10 речень) з латинських літер. Скласти програму, 
яка визначає і видаляє з цього тексту три слова, які містять найбільшу кількість 
різних приголосних букв.

Спочатку текст буде перевіренно за допомогою шаблонного виразу на те чи складається він з латинських літер, якщо він пройшов перевірку то программа йде по кожному слову у тексті та підраховує кількість приголосних у ньому, на основі кількості приколосних программа формує словник у якому є інформація про слово(`theword`), кількість приголосних у ньому(`consonants`) та його позицію(`posindex`). Потім, цей словник буде відсортовано за зростанням по ключу `consonants` та виведено у кносль. Далі, программа видалить слова у яких найбільша кількість приголосних букв за допомогою ключа `posindex` і виведе результат. 
```
INPUT YOUR TEXT:
Sed ut perspiciatis, unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam eaque ipsa, quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt, explicabo. Nemo enim ipsam voluptatem, quia voluptas sit, aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos, qui ratione voluptatem sequi nesciunt, neque porro quisquam est, qui dolorem ipsum, quia dolor
Sed ut perspiciatis, unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam eaque ipsa, quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt, explicabo. Nemo enim ipsam voluptatem, quia voluptas sit, aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos, qui ratione voluptatem sequi nesciunt, neque porro quisquam est, qui dolorem ipsum, quia dolor
neededwords:  [Word(theword='consequuntur', consonants=7, posindex=98), Word(theword='voluptatem', consonants=6, posindex=19), Word(theword='perspiciatis', consonants=7, posindex=4)]
the text after words being deleted:
Sed ut , unde omnis iste natus error sit  accusantium doloremque laudantium, totam rem aperiam eaque ipsa, quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt, explicabo. Nemo enim ipsam voluptatem, quia voluptas sit, aspernatur aut odit aut fugit, sed quia  magni dolores eos, qui ratione voluptatem sequi nesciunt, neque porro quisquam est, qui dolorem ipsum, quia dolor
```

Б) б) Задано текст з латинських літер. Скласти програму, яка визначає і виводить 
на екран: а) всі літери, які входять в текст не менше двох разів; б) всі літери, 
які входять в текст один раз.

Програма створює декілька списків та кортеж з інформацією про букву та кількість її потраплянь у строку, на основі данних з кортежу программа сортує інформацію по спискам та виводить їх склад у кінці виконання програми.
```
INPUT NEW TEXT: Sed ut perspiciatis, unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam eaque ipsa
[Letter(lettername='v', quantity=1), Letter(lettername='m', quantity=8), Letter(lettername='p', quantity=5), Letter(lettername='l', quantity=3), Letter(lettername='a', quantity=12), Letter(lettername='d', quantity=4), Letter(lettername='q', quantity=2), Letter(lettername='r', quantity=7), Letter(lettername='e', quantity=12), Letter(lettername='o', quantity=6), Letter(lettername='s', quantity=9), Letter(lettername='n', quantity=5), Letter(lettername='i', quantity=10), Letter(lettername='c', quantity=3), Letter(lettername='t', quantity=11), Letter(lettername='u', quantity=10)]
Letters that occure only once in the text:  ['v']
Letters that occure two or more times in the text:  ['m', 'p', 'l', 'a', 'd', 'q', 'r', 'e', 'o', 's', 'n', 'i', 'c', 't', 'u']
```
