with open("maps.txt", "r") as text:
    for line in text:
        saboloo = (f"\"{str(line).strip()}\"" + " {}" )
        print(saboloo)