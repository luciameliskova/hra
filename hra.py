import tkinter
import threading
import random
import time 


####################################

def nacitaj_mapu():
    txt = open('textak.txt')
    sirka = int(txt.readline())
    vyska = int(txt.readline())
    mapa = [] 

    #ulozime, ci sme inicializovali pacmana - moze mat hodnotu True alebo False.
    #Aká bude na začiatku

    kac_found = False
    duc_found = False

    kac_x = 0
    kac_y = 0
    duc_x = 0
    duc_y = 0

    #obrazok musi byt 80x80

    for i in range(0, vyska):
        riadok = txt.readline()
        mapa.append(riadok)

    txt.close

    #return sirka, vyska, mapa


#prehladavame maticu mapy(riadky, stlpce) a hladame umiestnenie postavicky
# a potvorky a v scene


    for y in range (0, vyska):
        #ak sme ich oboch nasli, tak vybehni z cyklu
        if kac_found and duc_found:
            break;

        for x in range(0, sirka):
            #ak na sucasnom policku sa ma nachadzat postavicka
            if mapa [y][x] == 'a':
                #tak to prepiseme na volne policko a ulozime si poziciu a zmenime
                #najdenie panacika na True, aby vybehli z vonkajsieho cyklu von
                mapa [y][x] = ' '
                kac_x = x
                kac_y = y
                kac_found = True
                #vkladame do sceny potvorku, zloducha
            elif mapa [y][x] == 'b':
                mapa[y][x] = ' '
                duc_x = x
                duc_y = y
                duc_found = True

            if kac_found and duc_found:
                break;

        #tieto hodnoty nam vrati z funkcie
        return sirka, vyska, mapa, kac_x, kac_y, duc_x, duc_y

####################################
def vytvor_platno(okno, sirka, vyska, mapa, cell_size, wall):
    platno = tkinter.Canvas(okno, \
                            width=sirka * cell_size, \
                            height=vyska * cell_size)
    platno.config(bg="cyan")
    platno.pack()

    for y in range(0, vyska):
        for x in range(0, sirka):
            if mapa[y][x] == '#':
                # co je [y] [x]???
                platno.create_image(x * cell_size + sirka / 2, \
 
                                    y * cell_size + vyska / 2, \
 
                                    image=wall)
    ##vrati sa nam nakreslene platno
    return platno


####################################

#pohyb panacika pomocou sipok

def move(event):

    global kac_x
    global kac_y
    global platno
    global kacka
    global cell_size
    global mapa
    global skore
    global gulicky
    global okno

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
    #zapamatame nove suradnice
        kac_x = target_x
        kac_y = target_y
        #posunieme obrazok
        platno.coords(kacka, \
                      target_x *cell_size+cell_size /2, \
                      target_y *cell_size+cell_size /2)


    global duc_x
    global duc_y

####################################
    
# mapa - steny a prechody (1. index - vyska, 2. index sirka)
mapa = []

#pozicia panacika v scene
kac_x = 0
kac_y = 0

duc_x = 0
duc_y = 0

# rozmery mapy
siroka = 20
vysoka = 0

# rozmery policla v px
cell_size = 80

####################################

okno = tkinter.Tk()
okno.title("moja hra") 

# nacitaj zo suboru mapu a vratane hodnoty uloz do premennych
# vsteky nazvy premennych sedia s lokalnymi premennymi, ale nie su to
# totozne premenne

sirka, vyska, mapa, kac_x, kac_y, duc_x, duc_y = nacitaj_mapu()

# obrazok si musime odlozit v premennej, ktora prezije platno a preto
# je globalna

wall = tkinter.PhotoImage(file="wall.gif")

platno = vytvor_platno(okno, sirka, vyska, mapa, cell_size, wall)

#nacitame data k obrazku a zobrazime ho na konk suradniciach
kacka_data = tkinter.PhotoImage(file = 'duck.gif')
kacka = platno.create_image (kac_x * cell_size + cell_size/2, \
                             kac_y * cell_size + cell_size/2, \
                             image = kacka_data)

duc_data = tkinter.PhotoImage (file = 'duc.gif')
duc = platno.create_image (duc_x * cell_size + cell_size/2, \
                           duc_y * cell_size + cell_size/2, \
                           image = duc_data)

duc_smer = 3
terminate = False

platno.bind_all ('<KeyPress-Up>', move)
platno.bind_all ('<KeyPress-Down>', move)
platno.bind_all ('<KeyPress-Left>', move)
platno.bind_all ('<KeyPress-Right>', move)
platno.bind_all ('<KeyPress-Escape>', lambda key: okno.destroy())



# volame funkciu vytvor_platno tak, ze ju priradime do premennej
# v zatvorke musia byt nazvy vsetkych premennych, ktore potrebujeme
# na inicializaciu

# platno = vytvor_platno(okno, sirka, vyska, mapa, cell_size, wall)

okno.mainloop()
terminate = True

print("O")
