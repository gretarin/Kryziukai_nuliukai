import aplinka
from aplinka import zaidimo_lenta, pasisveikinimas

zaidimas = "Vyksta"

pasisveikinimas()

while zaidimas == "Vyksta":
    if (aplinka.vienas == "1" or aplinka.du == "2" or aplinka.trys == "3" or
            aplinka.keturi == "4" or aplinka.penki == "5" or aplinka.sesi == "6" or
            aplinka.septyni == "7" or aplinka.astuoni == "8" or aplinka.devyni == "9"):

        if aplinka.x_laimejimas():
            zaidimas = "Baigėsi"
            zaidimo_lenta()
            print("Laimėjo pirmasis žaidėjas")

        elif aplinka.o_laimejimas():
            zaidimas = "Baigėsi"
            zaidimo_lenta()
            print("Laimėjo antrasis žaidėjas")

        else:
            zaidimo_lenta()
            skaicius = int(input("Pirmasis žaidėjas \nPasirinkikte skaičių \n"))
            if skaicius == 1:
                aplinka.vienas = "X"
            elif skaicius == 2:
                aplinka.du = "X"
            elif skaicius == 3:
                aplinka.trys = "X"
            elif skaicius == 4:
                aplinka.keturi = "X"
            elif skaicius == 5:
                aplinka.penki = "X"
            elif skaicius == 6:
                aplinka.sesi = "X"
            elif skaicius == 7:
                aplinka.septyni = "X"
            elif skaicius == 8:
                aplinka.astuoni = "X"
            elif skaicius == 9:
                aplinka.devyni = "X"
            else:
                print("Pasirinkote neteisingą skaičių")
                continue
            if (aplinka.vienas == "1" or aplinka.du == "2" or aplinka.trys == "3" or
                    aplinka.keturi == "4" or aplinka.penki == "5" or aplinka.sesi == "6" or
                    aplinka.septyni == "7" or aplinka.astuoni == "8" or aplinka.devyni == "9"):
                zaidimo_lenta()
                skaicius = int(input("Antrasis žaidėjas \nPasirinkikte skaičių \n"))
                if skaicius == 1:
                    aplinka.vienas = "0"
                elif skaicius == 2:
                    aplinka.du = "0"
                elif skaicius == 3:
                    aplinka.trys = "0"
                elif skaicius == 4:
                    aplinka.keturi = "0"
                elif skaicius == 5:
                    aplinka.penki = "0"
                elif skaicius == 6:
                    aplinka.sesi = "0"
                elif skaicius == 7:
                    aplinka.septyni = "0"
                elif skaicius == 8:
                    aplinka.astuoni = "0"
                elif skaicius == 9:
                    aplinka.devyni = "0"
                else:
                    print("Pasirinkote neteisingą skaičių")
                    continue
    else:
        zaidimas = "Baigėsi"
        zaidimo_lenta()
        print("Žaidimas baigėsi")
        if aplinka.x_laimejimas():
            print("Laimėjo pirmasis žaidėjas")
        elif aplinka.o_laimejimas():
            print("Laimėjo antrasis žaidėjas")
