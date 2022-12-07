"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
from itertools import product

    
stock =[
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]

summ =0
for mobile in stock:
    phone_name = mobile['product']
    summ_prod =sum(mobile['items_sold'])
    summ_prod_sred =sum(mobile['items_sold'])/(len(mobile['items_sold']))
    summ =summ + sum(mobile['items_sold'])
    summ_sred = summ/len(stock)
    print(f'суммарное количество продаж {phone_name}: {summ_prod}')
    print(f'среднее количество продаж {phone_name}: {summ_prod_sred}')
    print(f'суммарное количество продаж телефонов: {summ}')
    print(f'среднее количество продаж телефонов: {summ_sred}')
    
  


if __name__ == "__main__":
    main()
