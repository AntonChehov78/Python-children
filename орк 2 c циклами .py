import random
exitChoise = "Нет"
while exitChoise != "Exit":
    print ("Вы в замке")
    print ("нужно открыть одну их четырех дверей")
    pleerChoise = input ("введи 1 или 2 или 3 или 4")
    if pleerChoise == '1':
        print ("Сокровища ваши")
        print ("Победа")
    elif pleerChoise == "2":
        print ("Орк ударил вас")
        print ("Проигрыш")
    elif pleerChoise == "3":
        print ("Спящий дракон")
        print ("можно:")
        print ("1 украсть золото")
        print ("2 убежать")

        dragonChoise = input ("1/2")
        if dragonChoise == "1":
            print ("Проснулся и съел Вас")
            print ("Проигрыш")
        elif dragonChoise == "2":
            print ("вы убежали")
            print ("Победа")
        else:
            print ("что с драконом")
            print ("Еще раз")
            
    elif pleerChoise == "4":
        print ("Внутри кот")
        print ("Говорит: 'Отгадай число от 1 до 10'")
        number = int(input ("твой выбор"))
        if number == random.randint (1,10):
             print ("Молодец, Угадал")
             print ("Свободен")
             print ("ПОбеда")
        else:
             print ("ХаХаХа. НЕ угадал")
             print ("Съеден")
             print ("Проигрыш")
             
    else:
        print ("не введено условие")
    exitChoise = input ("Нажать Enter для продолжения или написать Exit для выхода")

        
