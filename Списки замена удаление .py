spisok = ["vasj", "petj", "bob", "john"]
spisok [0] = ["terminator"]
for item in spisok:
    print(item)
print("-----------------------------------------------")
spisok = ["vasj", "petj", "bob", "john"]
del spisok [0]
for item in spisok:
    print(item)
print("-----------------------------------------------")
spisok = ["vasj", "petj", "bob", "john"]
spisok.append  ("moon")
for item in spisok:
    print(item)

print("-----------------------------------------------")
spisok1 = ["vasj", "petj", "bob", "john"]
spisok2 = ["vasj1", "petj1", "bob1", "john1"]
spisok = spisok1 + spisok2
for item in spisok:
    print(item)
