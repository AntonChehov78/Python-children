aliens = 2
password = 'ALIENS'
print ("Внимание пришельцы")
print ("Спасите землю")
print ("Подберите пароль")
print ()
print ('----------------------------------------------------------')
print ('             WELCOME                                      ')
print ('__________________________________________________________')
print ()
guess = input ('Введите пароль').upper()
while guess != password:
    print ()
    print ("Некорректный пароль")
    print ()
    aliens = aliens ** 2
    print ("Там", aliens, "пришельцев на земле. еще раз")
    if aliens > 7500000000:
        break
    print ()
    print ('Подсказка. Кто на нас нападает?')
    print ()
    guess = input ('Быстрее введите пароль').upper()
if aliens>7500000000:
    print ('Земля уничтожена')
else:
     print ('Мы спасены')
