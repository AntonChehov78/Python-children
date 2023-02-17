import random
exitnumber = "Нет"
while exitnumber != "Exit":
    number = random.randint(1,20)
    guess = int(input("ввести число от 1 до 20"))
    while guess != number:
        if guess<number:
            print("меньше загаданного")
        else:
            print("больше загаданного")
        guess = int(input("ввести число еще раз"))
    print("Поздравляю число угадано")
    exitnumber = input ("Нажать Enter для продолжения или написать Exit для выхода")
