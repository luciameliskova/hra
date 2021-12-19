import tkinter
import threading
import random
import time

# obrazky musia byt 80x80
####################################
def nacitaj_mapu():
    txt = open('textak.txt')
    sirka = int(txt.readline())
    vyska = int(txt.readline())
    mapa = []

    global kac_x
    global kac_y
    kac_found = False

    for i in range(0, vyska):
        riadok = txt.readline()
        mapa.append(list(riadok))

    txt.close()

    # prehladavame maticu mapy(riadky, stlpce) a hladame umiestnenie postavicky
    for y in range(0, vyska):
        if kac_found:
            break;

        for x in range(0, sirka):
            # ak na sucasnom policku sa ma nachadzat postavicka
            if mapa[y][x] == 'a':
                # tak to prepiseme na volne policko a ulozime si poziciu a zmenime
                # najdenie panacika na True, aby vybehli z vonkajsieho cyklu von
                mapa[y][x] = ' '
                kac_x = x
                kac_y = y
                kac_found = True

            if kac_found:
                break;

    return sirka, vyska, mapa, kac_x, kac_y
####################################
# funkcia na vytvorenie platna

def vytvor_platno(okno, sirka, vyska, mapa, cell_size, wall):
    platno = tkinter.Canvas(okno, \
                            width=sirka * cell_size, \
                            height=vyska * cell_size)
    platno.config(bg="#7E7574")
    platno.pack()

    for y in range(0, vyska):
        for x in range(0, sirka):
            if mapa[y][x] == '#':
                platno.create_image(x * cell_size + cell_size / 2, \
                                    y * cell_size + cell_size / 2, \
                                    image=wall)

    return platno
global platno

####################################
# funkcia na zobrazenie duchov tam, kde je v textovom subore urcite pismeno
global duch

def zobraz_duchov(okno, platno, sirka, vyska, mapa, cell_size, duch):
    duchovia = []
    for y in range(0, vyska):
        for x in range(0, sirka):
            if mapa[y][x] == 'c':
                obr = platno.create_image(x * cell_size + cell_size / 2, \
                                          y * cell_size + cell_size / 2, \
                                          image=duch)
                duchovia.append([x, y, obr])
    return duchovia
####################################
# funkcia na zobrazenie minci = rovnaky princip ako duchovia
global minca
global obr_m
global m

m = []

def zobraz_mince(okno, platno, sirka, vyska, mapa, cell_size, minca):
    mince = []
    for y in range(0, vyska):
        for x in range(0, sirka):
            if mapa[y][x] == 'm':
                obr_m = platno.create_image(x * cell_size + cell_size / 2, \
                                            y * cell_size + cell_size / 2, \
                                            image=minca)
                mince.append([x, y, obr_m])
                m.append(obr_m)
    return mince, obr_m

####################################
# pohyb panacika pomocou sipok a zbieranie minci
skore = 0

def panacikmove(event):
    global kac_x
    global kac_y
    global platno
    global kacka
    global cell_size
    global mapa
    global skore
    global mince
    global okno
    global obr_m

    target_x = kac_x
    target_y = kac_y

    if event.keysym == 'Up':
        target_y -= 1

    elif event.keysym == 'Down':
        target_y += 1

    elif event.keysym == 'Left':
        target_x -= 1

    elif event.keysym == 'Right':
        target_x += 1

    if mapa[target_y][target_x] != '#':
        # zapamatame nove suradnice
        kac_x = target_x
        kac_y = target_y
        # posunieme obrazok
        platno.coords(kacka, \
                      target_x * cell_size + cell_size / 2, \
                      target_y * cell_size + cell_size / 2)

    kacka_coords_tuple = (platno.coords(kacka))

    #vymazavanie minci ked na ne stupi panacik
    if mapa [target_y][target_x] == 'm':
        #tak budeme 'prechadzat' cez list minci m tolkokrat, kolko poloziek ma
        for i in range (len(m)):
            #ak sa prvy coord mince i v liste minci = aj tomu kackinmu
           if platno.coords(m[i])[0] == (kacka_coords_tuple[0]):
               #a zaroven aj druhy sa rovna s kackynim
                if platno.coords(m[i])[1] == (kacka_coords_tuple[1]):
                    #tak priratame skore
                    skore + 1
                    #popneme objekt prec z listu minci m
                    vymazana_minca = m.pop(i)
                    #vymyzame objekt z platna
                    platno.delete(vymazana_minca)
                    break;

####################################
# mapa - steny a prechody (1. index - vyska, 2. index sirka)
mapa = []

# pozicia panacika v scene
kac_x = 0
kac_y = 0

# rozmery mapy
siroka = 20
vysoka = 0

# rozmery policka v px
cell_size = 80

####################################

okno = tkinter.Tk()
okno.title("moja hra")

sirka, vyska, mapa, kac_x, kac_y = nacitaj_mapu()

wall = tkinter.PhotoImage(file="wall.gif")

global platno
platno = vytvor_platno(okno, sirka, vyska, mapa, cell_size, wall)

# nacitame data k obrazku a zobrazime ho na konk suradniciach
kacka_data = tkinter.PhotoImage(file='duck.gif')
kacka = platno.create_image(kac_x * cell_size + cell_size / 2, \
                            kac_y * cell_size + cell_size / 2, \
                            image=kacka_data)

duch = tkinter.PhotoImage(file='duc.gif')
duchovia = zobraz_duchov(okno, platno, sirka, vyska, mapa, cell_size, duch)

minca = tkinter.PhotoImage(file='coin.gif')
mince = zobraz_mince(okno, platno, sirka, vyska, mapa, cell_size, minca)

terminate = False

platno.bind_all('<KeyPress-Up>', panacikmove)
platno.bind_all('<KeyPress-Down>', panacikmove)
platno.bind_all('<KeyPress-Left>', panacikmove)
platno.bind_all('<KeyPress-Right>', panacikmove)
platno.bind_all('<KeyPress-Escape>', lambda key: okno.destroy())

#print(m)
okno.mainloop()
terminate = True

print("O")