import tkinter
import threading
import random
import time

#treba si dat wall.gif a textak.txt do jedneho foldru spolu s tymto

####################################

def nacitaj_mapu():
    txt = open("hra/textak.txt")
    sirka = int(txt.readline())
    vyska = int(txt.readline())
    mapa = []

    for i in range(0, vyska):
        riadok = txt.readline()
        mapa.append(riadok)

    txt.close

    return sirka, vyska, mapa

####################################

def vytvor_platno (okno, sirka, vyska, mapa, cell_size, wall):
    platno = tkinter.Canvas(okno, \
                                               width = sirka * cell_size, \
                                               height = vyska * cell_size)
    platno.config (bg="cyan")
    platno.pack()

    for y in range (0, vyska):
        for x in range (0, sirka):
            if mapa[y][x] == '#':
                # co je [y] [x]???
                platno.create_image(x * cell_size + sirka /2, \
                                    
                                    y * cell_size + vyska /2, \
                                    
                                    image = wall)
    ##vrati sa nam nakreslene platno
    return platno

####################################

# mapa - steny a prechody (1. index - vyska, 2. index sirka)
mapa = []

#rozmery mapy
siroka = 20
vysoka = 0

#rozmery policla v px
cell_size = 80

####################################

okno = tkinter.Tk()
okno.title ("moja hra")

#nacitaj zo suboru mapu a vratane hodnoty uloz do premennych
#vsteky nazvy premennych sedia s lokalnymi premennymi, ale nie su to
#totozne premenne

sirka, vyska, mapa = nacitaj_mapu()

#obrazok si musime odlozit v premennej, ktora prezije platno a preto
#je globalna

wall = tkinter.PhotoImage (file = "hra/wall.gif" )

#volame funkciu vytvor_platno tak, ze ju priradime do premennej
#v zatvorke musia byt nazvy vsetkych premennych, ktore potrebujeme
#na inicializaciu

platno = vytvor_platno(okno, sirka, vyska, mapa, cell_size, wall)

okno.mainloop()
terminate = True

print("O")

