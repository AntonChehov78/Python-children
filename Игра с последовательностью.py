woman = ["сценарист", "королева", "пират", "стритизерша"]
man = ["водитель", "стриптезер", "электрик", "дедушка"]
place = ["магазин", "клуб", "спортзал", "метро", "машина"]
sheWore = ["сумка", "мяч", "шляпа", "трусы"]
heWore = ["розовый чемодан", "ключи", "костюм акулы", "парик"]
womanSays = ["кто ты", "сколько 2+2", "почему", "зачем"]
manSays = ["тсссссссс", "донт вори", "сколько время", "бинго"]
consequence = ["пиво с чипсами", "миру мир", "я красивый", "печеньки?"]
worldSaid = ["нонсенс", "сыыыыр", " плавлюсь"]
import random
while True:
    print(random.choice(woman), "встретились", random.choice(man), random.choice(place))
    print("она была одета", random.choice(sheWore))
    print("он был одета", random.choice(heWore))
    print("она сказала", random.choice(womanSays))
    print("он сказал", random.choice(manSays))
    print("последствие", random.choice(consequence))
    print("мир сказал", random.choice(worldSaid))
    print()
    input("нажмите enter для повторной игры")
    print()     
