"""

Домашнее задание №1

Исключения: приведение типов

* Перепишите функцию discounted(price, discount, max_discount=20)
  из урока про функции так, чтобы она перехватывала исключения,
  когда переданы некорректные аргументы.
* Первые два нужно приводить к вещественному числу при помощи float(),
  а третий - к целому при помощи int() и перехватывать исключения
  ValueError и TypeError, если приведение типов не сработало.
    
"""

def discounted(price, discount, max_discount=20):
    """
    Замените pass на ваш код
    """
    if type (price) is not float or type (discount) is not float:
        return 'TypeError'
    if type (max_discount) is not int:
        return 'TypeError'
    else:
      price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(int(max_discount))
    if max_discount >= 20:
        raise ValueError('Больше заданной скидки')
    if discount >= max_discount:
        return price
    else:
        return price - (price * discount / 20) 

        
    
if __name__ == "__main__":
    print(discounted(100, 2))
    print(discounted(100, "3"))
    print(discounted("100", "4.5"))
    print(discounted("five", 5))
    print(discounted("сто", "десять"))
    print(discounted(100.0, 5, "10"))
