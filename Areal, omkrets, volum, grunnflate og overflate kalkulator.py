import math
from re import L

type = ""


def start():
    hva_man_kan_regne = ["areal","omkrets","volum","grunnflate","overflate"]
    print("Denne kalkulatoren kan regne areal, omkrets, volum, grunnflate og overflate.")
    what_type = input("Hva vil du regne? Hvis du ikke vil regne noe trykk på enter.\n")
    global type
    if what_type in hva_man_kan_regne:
        type = what_type
    elif what_type == "":
        type = what_type
    else:
        print("Oppgi et gyldig svar!")
        start()
    

def areal():
    print("Denne kalkulatoren kan regne arealet av kvadrat, rektangel, trekant, parallellogram, rombe og sirkel.")
    hva = input("Hva vil du regne arealet av?\n")
    if hva == "kvadrat":
        l = float(input("Oppgi lengden: "))
        print("Denne kalkulatoren aksepterer bar disse måleenhetene mm, cm, dm, m og km.")
        m = input("Oppgi måleenhet: ")
        gyldig = ["mm", "cm", "dm", "m", "km"]
        if m in gyldig:
            print("Arealet til kvadraten er = ", l*l, m + "^2")
            noe_annet = input("Hvis du vil regne noe annet en areal tast 'ja' ellers tast hva som helst.\n")
            if noe_annet == "ja":
                start()
        else:
            print("Oppgi et gyldig måleenhet")
    elif hva == "rektangel":
        l = float(input("Oppgi lengden: "))
        h = float(input("Oppgi høyden: "))
        m = input("Oppgi måleenhet\n")
        gyldig = ["mm", "cm", "dm", "m", "km"]
        if m in gyldig:
            print("Arealet til rektangelen er = ", l*h, m + "^2")
            noe_annet = input("Hvis du vil regne noe annet en areal tast 'ja' ellers trykk på enter.\n")
            if noe_annet == "ja":
                start()
        else:
            print("Oppgi et gyldig måleenhet")
    elif hva == "trekant":
        g = float(input("Oppgi grunnflaten: "))
        h = float(input("Oppgi høyden: "))
        m = input("Oppgi måleenhet\n")
        gyldig = ["mm", "cm", "dm", "m", "km"]
        if m in gyldig:
            print("Arealet til trekanten er = ", (g*h)/2, m + "^2")
            noe_annet = input("Hvis du vil regne noe annet en areal tast 'ja' ellers trykk på enter.\n")
            if noe_annet == "ja":
                start()
        else:
            print("Oppgi et gyldig måleenhet")
    elif hva == "parallellogram":
        g = float(input("Oppgi grunnflaten: "))
        h = float(input("Oppgi høyden: "))
        m = input("Oppgi måleenhet\n")
        gyldig = ["mm", "cm", "dm", "m", "km"]
        if m in gyldig:
            print("Arealet til parallellogramet er = ", g*h, m + "^2")
            noe_annet = input("Hvis du vil regne noe annet en areal tast 'ja' ellers trykk på enter.\n")
            if noe_annet == "ja":
                start()
        else:
            print("Oppgi et gyldig måleenhet")
    elif hva == "rombe":
        g = float(input("Oppgi grunnflaten: "))
        h = float(input("Oppgi høyden: "))
        m = input("Oppgi måleenhet\n")
        gyldig = ["mm", "cm", "dm", "m", "km"]
        if m in gyldig:
            print("Arealet til romben er = ", g*h, m + "^2")
            noe_annet = input("Hvis du vil regne noe annet en areal tast 'ja' ellers trykk på enter.\n")
            if noe_annet == "ja":
                start()
        else:
            print("Oppgi et gyldig måleenhet")
    elif hva == "sirkel":
        r = float(input("Oppgi radiusen: "))
        m = input("Oppgi måleenhet\n")
        gyldig = ["mm", "cm", "dm", "m", "km"]
        if m in gyldig:
            print("Arealet til sirkelen er = ", math.pi*r*r, m + "^2")
            noe_annet = input("Hvis du vil regne noe annet en areal tast 'ja' ellers trykk på enter.\n")
            if noe_annet == "ja":
                start()
        else:
            print("Oppgi et gyldig måleenhet")
    else:
        print("Oppgi en gyldig figur!")
        areal()


def omkrets():
    print("Denne kalkulatoren kan regne omkretsen av kvadrat, rektangel, trekant, parallellogram, rombe og sirkel.")
    hva = input("Hva vil du regne omkretsen av?\n")
    if hva == "kvadrat":
        l = float(input("Oppgi lengden: "))
        print("Denne kalkulatoren aksepterer bar disse måleenhetene mm, cm, dm, m og km.")
        m = input("Oppgi måleenhet\n")
        gyldig = ["mm", "cm", "dm", "m", "km"]
        if m in gyldig:
            print("Omkretsen til kvadraten er = ", l*l, m)
            noe_annet = input("Hvis du vil regne noe annet en omkrets tast 'ja' ellers trykk på enter.\n")
            if noe_annet == "ja":
                start()
        else:
            print("Oppgi et gyldig måleenhet")
    elif hva == "rektangel":
        l = float(input("Oppgi lengden: "))
        h = float(input("Oppgi høyden: "))
        m = input("Oppgi måleenhet\n")
        gyldig = ["mm", "cm", "dm", "m", "km"]
        if m in gyldig:
            print("Omkretsen til rektangelen er = ", l*2 + h*2, m)
            noe_annet = input("Hvis du vil regne noe annet en omkrets tast 'ja' ellers trykk på enter.\n")
            if noe_annet == "ja":
                start()
        else:
            print("Oppgi et gyldig måleenhet")
    elif hva == "trekant":
        a = float(input("Oppgi lengden til side a: "))
        b = float(input("Oppgi lengden til side b: "))
        c = float(input("Oppgi lengden til side c: "))
        m = input("Oppgi måleenhet\n")
        gyldig = ["mm", "cm", "dm", "m", "km"]
        if m in gyldig:
            print("Omkretsen til trekanten er = ", a+b+c, m)
            noe_annet = input("Hvis du vil regne noe annet en omkrets tast 'ja' ellers trykk på enter.\n")
            if noe_annet == "ja":
                start()
        else:
            print("Oppgi et gyldig måleenhet")
    elif hva == "parallellogram":
        l = float(input("Oppgi lengden: "))
        h = float(input("Oppgi høyden: "))
        m = input("Oppgi måleenhet\n")
        gyldig = ["mm", "cm", "dm", "m", "km"]
        if m in gyldig:
            print("Omkretsen til parallellogram er = ", l*2 + h*2, m)
            noe_annet = input("Hvis du vil regne noe annet en omkrets tast 'ja' ellers trykk på enter.\n")
            if noe_annet == "ja":
                start()
        else:
            print("Oppgi et gyldig måleenhet")
    elif hva == "rombe":
        l = float(input("Oppgi lengden: "))
        print("Denne kalkulatoren aksepterer bar disse måleenhetene mm, cm, dm, m og km.")
        m = input("Oppgi måleenhet\n")
        gyldig = ["mm", "cm", "dm", "m", "km"]
        if m in gyldig:
            print("Omkretsen til romben er = ", l*l, m)
            noe_annet = input("Hvis du vil regne noe annet en omkrets tast 'ja' ellers trykk på enter.\n")
            if noe_annet == "ja":
                start()
        else:
            print("Oppgi et gyldig måleenhet")
    elif hva == "sirkel":
        r = float(input("Oppgi radiusen: "))
        print("Denne kalkulatoren aksepterer bar disse måleenhetene mm, cm, dm, m og km.")
        m = input("Oppgi måleenhet\n")
        gyldig = ["mm", "cm", "dm", "m", "km"]
        if m in gyldig:
            print("Omkretsen til sirkelen er = ", 2*math.pi*r, m)
            noe_annet = input("Hvis du vil regne noe annet en omkrets tast 'ja' ellers trykk på enter.\n")
            if noe_annet == "ja":
                start()
        else:
            print("Oppgi et gyldig måleenhet")
    else:
        print("Oppgi en gyldig figur!")
        omkrets()


def grunnflate():
    print("Denne kalkulatoren kan regne grunnflaten av sylinder, kjegle, pyramide, kube og rett firkantet prisme.")
    hva = input("Hva vil du regne grunnflaten av?\n")
    if hva == "sylinder":
        r = float(input("Oppgi radiusen: "))
        print("Denne kalkulatoren aksepterer bar disse måleenhetene mm, cm, dm, m og km.")
        m = input("Oppgi måleenhet\n")
        gyldig = ["mm", "cm", "dm", "m", "km"]
        if m in gyldig:
            print("Grunnflaten til sylinderen er = ", math.pi * r ** 2, m + "^2")
            noe_annet = input("Hvis du vil regne noe annet en grunnflate tast 'ja' ellers trykk på enter.\n")
            if noe_annet == "ja":
                start()
        else:
            print("Oppgi et gyldig måleenhet")
    elif hva == "kjegle":
        r = float(input("Oppgi radiusen: "))
        print("Denne kalkulatoren aksepterer bar disse måleenhetene mm, cm, dm, m og km.")
        m = input("Oppgi måleenhet\n")
        gyldig = ["mm", "cm", "dm", "m", "km"]
        if m in gyldig:
            print("Grunnflaten til kjeglen er = ", math.pi * r ** 2, m + "^2")
            noe_annet = input("Hvis du vil regne noe annet en grunnflate tast 'ja' ellers trykk på enter.\n")
            if noe_annet == "ja":
                start()
        else:
            print("Oppgi et gyldig måleenhet")
    elif hva == "pyramide":
        l = float(input("Oppgi lengden: "))
        b = float(input("Oppgi bredden: "))
        print("Denne kalkulatoren aksepterer bar disse måleenhetene mm, cm, dm, m og km.")
        m = input("Oppgi måleenhet\n")
        gyldig = ["mm", "cm", "dm", "m", "km"]
        if m in gyldig:
            print("Grunnflaten til pyramiden er = ", (l*b)/2, m + "^2")
            noe_annet = input("Hvis du vil regne noe annet en grunnflate tast 'ja' ellers trykk på enter.\n")
            if noe_annet == "ja":
                start()
        else:
            print("Oppgi et gyldig måleenhet")
    elif hva == "kube":
        l = float(input("Oppgi lengden: "))
        b = float(input("Oppgi bredden: "))
        print("Denne kalkulatoren aksepterer bar disse måleenhetene mm, cm, dm, m og km.")
        m = input("Oppgi måleenhet\n")
        gyldig = ["mm", "cm", "dm", "m", "km"]
        if m in gyldig:
            print("Grunnflaten til kuben er = ", l*b, m + "^2")
            noe_annet = input("Hvis du vil regne noe annet en grunnflate tast 'ja' ellers trykk på enter.\n")
            if noe_annet == "ja":
                start()
        else:
            print("Oppgi et gyldig måleenhet")
    elif hva == "rett firkantet prisme":
        l = float(input("Oppgi lengden: "))
        b = float(input("Oppgi bredden: "))
        print("Denne kalkulatoren aksepterer bar disse måleenhetene mm, cm, dm, m og km.")
        m = input("Oppgi måleenhet\n")
        gyldig = ["mm", "cm", "dm", "m", "km"]
        if m in gyldig:
            print("Grunnflaten til rett firkantet prisme er = ", l*b, m + "^2")
            noe_annet = input("Hvis du vil regne noe annet en grunnflate tast 'ja' ellers trykk på enter.\n")
            if noe_annet == "ja":
                start()
        else:
            print("Oppgi et gyldig måleenhet")
    else:
        print("Oppgi en gyldig figur!")
        grunnflate()


def overflate():
    print("Denne kalkulatoren kan regne overflaten av kule, sylinder, kjegle, pyramide, kube og rett firkantet prisme.")
    hva = input("Hva vil du regne overflaten av?\n")
    if hva == "kule":
        r = float(input("Oppgi radiusen: "))
        print("Denne kalkulatoren aksepterer bar disse måleenhetene mm, cm, dm, m og km.")
        m = input("Oppgi måleenhet\n")
        gyldig = ["mm", "cm", "dm", "m", "km"]
        if m in gyldig:
            print("Overflaten til kulen er = ", 4 * math.pi * r ** 2, m + "^2")
            noe_annet = input("Hvis du vil regne noe annet en overflate tast 'ja' ellers trykk på enter.\n")
            if noe_annet == "ja":
                start()
        else:
            print("Oppgi et gyldig måleenhet")
    elif hva == "sylinder":
        r = float(input("Oppgi radiusen: "))
        h = float(input("Oppgi høyden: "))
        print("Denne kalkulatoren aksepterer bar disse måleenhetene mm, cm, dm, m og km.")
        m = input("Oppgi måleenhet\n")
        gyldig = ["mm", "cm", "dm", "m", "km"]
        if m in gyldig:
            print("Overflaten til sylinderen er = ", 2 * math.pi * r ** 2 + 2* math.pi * r * h, m + "^2")
            noe_annet = input("Hvis du vil regne noe annet en overflate tast 'ja' ellers trykk på enter.\n")
            if noe_annet == "ja":
                start()
        else:
            print("Oppgi et gyldig måleenhet")
    elif hva == "kjegle":
        r = float(input("Oppgi raiusen av grunnflaten: "))
        s = float(input("Oppgi lengden av siden til sirklsektoren: "))
        print("Denne kalkulatoren aksepterer bar disse måleenhetene mm, cm, dm, m og km.")
        m = input("Oppgi måleenhet\n")
        gyldig = ["mm", "cm", "dm", "m", "km"]
        if m in gyldig:
            print("Overflaten til kjeglen er = ", math.pi * r * r + math.pi * r * s , m + "^2")
            noe_annet = input("Hvis du vil regne noe annet en overflate tast 'ja' ellers trykk på enter.\n")
            if noe_annet == "ja":
                start()
        else:
            print("Oppgi et gyldig måleenhet")
    elif hva == "pyramide":
        l = float(input("Oppgi lengden: "))
        b = float(input("Oppgi bredden: "))
        g = float(input("Oppgi grunnflaten: "))
        h = float(input("Oppgi høyden"))
        print("Denne kalkulatoren aksepterer bar disse måleenhetene mm, cm, dm, m og km.")
        m = input("Oppgi måleenhet\n")
        gyldig = ["mm", "cm", "dm", "m", "km"]
        if m in gyldig:
            print("Overflaten til pyramiden er = ", l * b + 4 * ((g*h)/2), m + "^2")
            noe_annet = input("Hvis du vil regne noe annet en overflate tast 'ja' ellers trykk på enter.\n")
            if noe_annet == "ja":
                start()
        else:
            print("Oppgi et gyldig måleenhet")
    elif hva == "kube":
        l = float(input("Oppgi lengden: "))
        print("Denne kalkulatoren aksepterer bar disse måleenhetene mm, cm, dm, m og km.")
        m = input("Oppgi måleenhet\n")
        gyldig = ["mm", "cm", "dm", "m", "km"]
        if m in gyldig:
            print("Overflaten til kuben er = ", 6 * l ** 2, m + "^2")
            noe_annet = input("Hvis du vil regne noe annet en overflate tast 'ja' ellers trykk på enter.\n")
            if noe_annet == "ja":
                start()
        else:
            print("Oppgi en gyldig måleenhet")
    elif hva == "rett firkantet prisme":
        l = float(input("Oppgi lengden: "))
        b = float(input("Oppgi bredden: "))
        h = float(input("Oppgi høyden"))
        print("Denne kalkulatoren aksepterer bar disse måleenhetene mm, cm, dm, m og km.")
        m = input("Oppgi måleenhet\n")
        gyldig = ["mm", "cm", "dm", "m", "km"]
        if m in gyldig:
            print("Overflaten til rett firkantet prismen er = ", l * b + l * b + l*h + l*h + b*h + b*h, m + "^2")
            noe_annet = input("Hvis du vil regne noe annet en overflate tast 'ja' ellers trykk på enter.\n")
            if noe_annet == "ja":
                start()
        else:
            print("Oppgi et gyldig måleenhet!")
    else:
        print("Oppgi en gyldig figur!")
        overflate()


def volum():
    print("Denne kalkulatoren kan regne volum av kule, sylinder, kjegle, pyramide, kube og rett firkantet prisme.")
    hva = input("Hva vil du regne volum av?\n")
    if hva == "kule":
        o = float(input("Oppgi overflaten: "))
        print("Denne kalkulatoren aksepterer bar disse måleenhetene mm, cm, dm, m og km.")
        m = input("Oppgi måleenhet\n")
        gyldig = ["mm", "cm", "dm", "m", "km"]
        if m in gyldig:
            print("Volumet til kulen er = ", 1/3 * o * math.pi, m + "^3")
            noe_annet = input("Hvis du vil regne noe annet en volum tast 'ja' ellers trykk på enter.\n")
            if noe_annet == "ja":
                start()
        else:
            print("Oppgi et gyldig målenhet!")
    elif hva == "sylinder":
        g = float(input("Oppgi grunflaten: "))
        h = float(input("Oppgi høyden: "))
        print("Denne kalkulatoren aksepterer bar disse måleenhetene mm, cm, dm, m og km.")
        m = input("Oppgi måleenhet\n")
        gyldig = ["mm", "cm", "dm", "m", "km"]
        if m in gyldig:
            print("Volumet til sylinderen er = ", g * h, m + "^3")
            noe_annet = input("Hvis du vil regne noe annet en volum tast 'ja' ellers trykk på enter.\n")
            if noe_annet == "ja":
                start()
        else:
            print("Oppgi et gyldig målenhet!")
    elif hva == "kjegle":
        g = float(input("Oppgi grunflaten: "))
        h = float(input("Oppgi høyden: "))
        print("Denne kalkulatoren aksepterer bar disse måleenhetene mm, cm, dm, m og km.")
        m = input("Oppgi måleenhet\n")
        gyldig = ["mm", "cm", "dm", "m", "km"]
        if m in gyldig:
            print("Volumet til kjegle er = ", (g * h)/3, m + "^3")
            noe_annet = input("Hvis du vil regne noe annet en volum tast 'ja' ellers trykk på enter.\n")
            if noe_annet == "ja":
                start()
        else:
            print("Oppgi et gyldig målenhet!")
    elif hva == "pyramide":
        g = float(input("Oppgi grunflaten: "))
        h = float(input("Oppgi høyden: "))
        print("Denne kalkulatoren aksepterer bar disse måleenhetene mm, cm, dm, m og km.")
        m = input("Oppgi måleenhet\n")
        gyldig = ["mm", "cm", "dm", "m", "km"]
        if m in gyldig:
            print("Volumet til pyramiden er = ", (g * h)/3, m + "^3")
            noe_annet = input("Hvis du vil regne noe annet en volum tast 'ja' ellers trykk på enter.\n")
            if noe_annet == "ja":
                start()
        else:
            print("Oppgi et gyldig målenhet!")
    elif hva == "kube":
        l = float(input("Oppgi lenden: "))
        print("Denne kalkulatoren aksepterer bar disse måleenhetene mm, cm, dm, m og km.")
        m = input("Oppgi måleenhet\n")
        gyldig = ["mm", "cm", "dm", "m", "km"]
        if m in gyldig:
            print("Volumet til pyramiden er = ", l*3, m + "^3")
            noe_annet = input("Hvis du vil regne noe annet en volum tast 'ja' ellers trykk på enter.\n")
            if noe_annet == "ja":
                start()
        else:
            print("Oppgi et gyldig målenhet!")
    elif hva == "rett firkantet prisme":
        l = float(input("Oppgi lenden: "))
        h = float(input("Oppgi høyden: "))
        b = float(input("Oppgi bredden: "))
        print("Denne kalkulatoren aksepterer bar disse måleenhetene mm, cm, dm, m og km.")
        m = input("Oppgi måleenhet\n")
        gyldig = ["mm", "cm", "dm", "m", "km"]
        if m in gyldig:
            print("Volumet til rett firkantet prismen er = ", l * b * h, m + "^3")
            noe_annet = input("Hvis du vil regne noe annet en volum tast 'ja' ellers trykk på enter.\n")
            if noe_annet == "ja":
                start()
        else:
            print("Oppgi et gyldig målenhet!")
    else:
        print("Oppgi en gyldig figur!")
        volum()


start()

while True:
    if type == "":
        break
    elif type == "areal":
        areal()
    elif type == "omkrets":
        omkrets()
    elif type == "grunnflate":
        grunnflate()
    elif type == "overflate":
        overflate()
    elif type == "volum":
        volum()