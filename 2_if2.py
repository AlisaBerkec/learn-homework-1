"""


Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки+
* Проверить, является ли то, что передано функции, строками.+ 
  Если нет - вернуть 0+
* Если строки одинаковые, вернуть 1+
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""
first  = "test 222"
second = "test222"

def main (first, second):
    if type (first) is not str or type (second) is not str:
        return "0"
    elif len(first) == len(second):
        return '1'
    elif len(first) >= len(second) and second != 'learn':
        return '2'
    elif len(first)!= len(second) and second == 'learn':
        return '3'


if __name__ == '__main__':
  
   main (first, second) 

   print(main (first, second))



