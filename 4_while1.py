"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def ask_user (answer_user):   
  while True:                                            
    if answer_user  == 'Хорошо':          
        print("Отлично.Я рад")
        break
    else:                                  
        answer_user = input ('Привет.Как дела? \n')  


if __name__ == "__main__":   
 answer_user = input("Привет.Как дела? \n")
 ask_user(answer_user)  