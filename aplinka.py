vienas = "1"
du = "2"
trys = "3"
keturi = "4"
penki = "5"
sesi = "6"
septyni = "7"
astuoni = "8"
devyni = "9"


def pasisveikinimas():
    print("Sveiki atvykę į žaidimą," + "\n" + "'Kryžiukai nuliukai'")


def zaidimo_lenta():
    print("\n      " + vienas + "|" + du + "|" + trys + "\n      " + keturi + "|" + penki + "|" + sesi + "\n      " + septyni + "|" + astuoni + "|" + devyni + "\n")


def x_laimejimas():
    if (((vienas == "X") and (du == "X") and (trys == "X")) or
     ((vienas == "X") and (keturi == "X") and (septyni == "X")) or
     ((vienas == "X") and (penki == "X") and (devyni == "X")) or
     ((du == "X") and (penki == "X") and (astuoni == "X")) or
     ((keturi == "X") and (penki == "X") and (sesi == "X")) or
     ((trys == "X") and (penki == "X") and (septyni == "X")) or
     ((trys == "X") and (sesi == "X") and (devyni == "X")) or
     ((septyni == "X") and (astuoni == "X") and (devyni == "X"))):
        return True


def o_laimejimas():
    if (((vienas == "0") and (du == "0") and (trys == "0")) or
     ((vienas == "0") and (keturi == "0") and (septyni == "0")) or
     ((vienas == "0") and (penki == "0") and (devyni == "0")) or
     ((du == "0") and (penki == "0") and (astuoni == "0")) or
     ((keturi == "0") and (penki == "0") and (sesi == "0")) or
     ((trys == "0") and (penki == "0") and (septyni == "0")) or
     ((trys == "0") and (sesi == "0") and (devyni == "0")) or
     ((septyni == "0") and (astuoni == "0") and (devyni == "0"))):
        return True


def lygiosios():
    if ((vienas, du, trys == "X" and keturi, penki, sesi == "0") or
     (vienas, du, trys == "0" and keturi, penki, sesi == "X") or
     (keturi, penki, sesi == "X" and septyni, astuoni,devyni == "0") or
     (keturi, penki, sesi == "0" and septyni, astuoni, devyni == "X") or
     (vienas, du, trys == "X" and septyni, astuoni, devyni == "0") or
     (vienas, du, trys == "0" and septyni, astuoni, devyni == "X") or
     (vienas, keturi, septyni == "X" and du, penki, astuoni == "X") or
     (vienas, keturi, septyni == "0" and du, penki, astuoni == "X") or
     (du, penki, astuoni == "X" and trys, sesi, devyni == "0") or
     (du, penki, astuoni == "0" and trys, sesi, devyni == "X") or
     (vienas, keturi, septyni == "X" and trys, sesi, devyni == "0") or
     (vienas, keturi, septyni == "X" and trys, sesi, devyni == "0")):
        return True