for radek in range(0, 6):
    for sloupec in range(0, 6):
        if radek == 0 or radek == 6-1 or sloupec == 0 or sloupec == 6-1:
            print("X", end=" ")
        else:
            print(" ", end=" ")
    print("")
