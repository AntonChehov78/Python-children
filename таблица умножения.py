exitnumber = "Нет"
while exitnumber != "qw":
    table=int(input("Ввести множитель"))
    for x in range(0,100):
        print (x, "x", table, "=", x*table)
    exitnumber = input ("Нажать Enter для продолжения или написать qw для выхода")
