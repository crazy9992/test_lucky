while True:
    # Импортируем библиотеку
    import random

    # Пишем код
    print("Hi, let's test your luck."
          " ")
    print("")

    list = ("You are lucky!", "Unlucky", "Unlucky", "Unlucky", "Unlucky", "Unlucky", "Unlucky", "Unlucky", "Unlucky",
            "Unlucky", "Unlucky", "Unlucky", "Unlucky", "Unlucky", "Unlucky", "Unlucky", "Unlucky", "Unlucky",
            "Unlucky", "Unlucky", "Unlucky", "Unlucky", "Unlucky", "Unlucky", "Unlucky", "Unlucky", "Unlucky",
            "Unlucky", "Unlucky", "Unlucky", "Unlucky", "Unlucky", "Unlucky", "Unlucky", "Unlucky", "Unlucky",
            "Unlucky", "Unlucky", "Unlucky", "Unlucky", "Unlucky", "Unlucky", "Unlucky", "Unlucky"
            " ")


    # Программа выбирает ответ
    print(random.choice(list))
    
    # Повтор
    input("Repeat the test, press Enter")
    print("")
