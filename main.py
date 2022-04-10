from graphics import *
import math
import random
import sys
import time
import pygame
from pygame.locals import *
import numpy


def main():
    wybor = 0
    while wybor != 5:

        print("1. lab 1")
        print("2. lab 2")
        print("3. lab 3")
        print("4. lab 4")
        print("5. Zakonczenie programu")

        wybor = int(input("Wybierz projekt(1-4):\n"))

        if wybor == 1:
            win = GraphWin("Rysunek: Dom", 800, 800)
            win.setBackground(color_rgb(30, 144, 255))

            pttrawa = Point(800, 800)
            trawa = Rectangle(Point(0,500), pttrawa)
            trawa.setFill(color_rgb(86,225,70))
            trawa.draw(win)

            ptdom = Point(700,200)
            dom = Rectangle(Point(100, 700), ptdom)
            dom.setFill(color_rgb(0, 0, 0))
            dom.draw(win)

            ptdom2 = Point(695, 205)
            dom2 = Rectangle(Point(105, 695), ptdom2)
            dom2.setFill(color_rgb(80, 80, 80))
            dom2.draw(win)

            ptdach = Point(700,200)
            dach = Polygon(Point(400,50), ptdach, Point(100,200))
            dach.setFill(color_rgb(80,80,80))
            dach.setOutline('black')
            dach.setWidth(5)
            dach.draw(win)

            ptdrzwi = Point(350, 500)
            drzwi = Rectangle(Point(450, 700), ptdrzwi)
            drzwi.setFill(color_rgb(0, 0, 0))
            drzwi.draw(win)

            ptdrzwi2 = Point(355, 505)
            drzwi2 = Rectangle(Point(445, 695), ptdrzwi2)
            drzwi2.setFill(color_rgb(80, 30, 0))
            drzwi2.draw(win)

            ptklamka = Point(370,600)
            klamka = Line(Point(380, 600), ptklamka)
            klamka.setFill(color_rgb(0, 0, 0))
            klamka.setWidth(3)
            klamka.draw(win)

            ptslonce = Point(0,0)
            slonce = Circle(ptslonce, 130)
            slonce.setFill(color_rgb(255,204,51))
            slonce.draw(win)

            ptokno1 = Point(330, 300)
            okno1 = Rectangle(Point(130, 500), ptokno1)
            okno1.setWidth(5)
            okno1.draw(win)

            ptokno1fill = Point(328, 302)
            okno1fill = Rectangle(Point(132, 498), ptokno1fill)
            okno1fill.setFill(color_rgb(0,200,250))
            okno1fill.draw(win)

            ptokno2 = Point(670, 300)
            okno2 = Rectangle(Point(470, 500), ptokno2)
            okno2.setWidth(5)
            okno2.draw(win)

            ptokno2fill = Point(668, 302)
            okno2fill = Rectangle(Point(472, 498), ptokno2fill)
            okno2fill.setFill(color_rgb(0, 200, 250))
            okno2fill.draw(win)

            ptLine1okno1 = Point(230, 300)
            Line1okno1 = Line(Point(230, 500), ptLine1okno1)
            Line1okno1.setFill(color_rgb(0, 0, 0))
            Line1okno1.setWidth(4)
            Line1okno1.draw(win)

            ptLine1okno2 = Point(570, 300)
            Line1okno2 = Line(Point(570, 500), ptLine1okno2)
            Line1okno2.setFill(color_rgb(0, 0, 0))
            Line1okno2.setWidth(4)
            Line1okno2.draw(win)

            ptLine2okno1 = Point(330, 400)
            Line2okno1 = Line(Point(130, 400), ptLine2okno1)
            Line2okno1.setFill(color_rgb(0, 0, 0))
            Line2okno1.setWidth(4)
            Line2okno1.draw(win)

            ptLine2okno2 = Point(670, 400)
            Line2okno2 = Line(Point(470, 400), ptLine2okno2)
            Line2okno2.setFill(color_rgb(0, 0, 0))
            Line2okno2.setWidth(4)
            Line2okno2.draw(win)

            win.getMouse()
            win.close()

        if wybor == 2:

            pygame.init()
            pygame.font.init()
            pygame.display.set_caption('Cool game')

            fps = 60
            fpsClock = pygame.time.Clock()

            width, height = 801, 801
            screen = pygame.display.set_mode((width, height))

            tlo = pygame.image.load("tlo.png")
            target64px = pygame.image.load("target64px.png")

            kordy = [(150, 420), (150, 320), (250, 320), (250, 420), (490, 420), (490, 320), (590, 320), (590, 420)]

            def odleglosc(x1, y1, x2, y2):
                d = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
                if d <= 30:
                    return True
                else:
                    return False

            pojawianie_sie = "TAK"
            kordy_x_y = [-200, -200]
            teraz = 0
            zycia = 5
            score = 0
            myszka_czy_moze_byc_wcisnieta = True
            endscreen = ""
            koniec_gry = False
            running = True

            font = pygame.font.Font('freesansbold.ttf', 32)

            while running:

                mouse_pos = pygame.mouse.get_pos(0)
                mouse_x = mouse_pos[0]
                mouse_y = mouse_pos[1]
                myszka_czy_moze_byc_wcisnieta = True

                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()

                screen.blit(tlo, (0, 0))
                if not koniec_gry:
                    if pojawianie_sie == "TAK":
                        kordy_x_y = kordy[random.randrange(0, len(kordy))]
                        teraz = time.time()
                        pojawianie_sie = "NIE"

                    #aby zmienić "poziom trudności", należy zmienić 0.8 na inną liczbę podawaną w sekundach
                    if time.time() - teraz >= 0.8:
                        zycia -= 1
                        pojawianie_sie = "TAK"

                    if odleglosc(mouse_x, mouse_y, kordy_x_y[0] + 30, kordy_x_y[1] + 30) and pygame.mouse.get_pressed()[0]:
                        score += 1
                        pojawianie_sie = "TAK"
                        now = time.time()

                    if zycia == 0:
                        koniec_gry = True

                    infoklik = font.render("Szybko klikaj w tarcze!", True, (0, 0, 0), (80, 80, 80))
                    screen.blit(infoklik, (220, 155))

                    text = font.render("Score: " + str(score) + " Zycia: " + str(zycia), True, (0, 0, 0),
                                       (30, 144, 255))
                    textRect = text.get_rect()
                    textRect.center = (600, 50)
                    screen.blit(text, textRect)
                    screen.blit(target64px, (kordy_x_y[0], kordy_x_y[1]))

                if koniec_gry:
                    endscreen = font.render("Skończyły Ci się życia! Twój wynik: " + str(score), True, (0, 0, 0), (30, 144, 255))
                    screen.blit(endscreen, (150, 10))

                if pygame.key.get_pressed()[K_r]:
                    zycia = 5
                    score = 0
                    koniec_gry = False

                if pygame.key.get_pressed()[K_q]:
                    pygame.quit()

                inforeset = font.render("Aby zresetować grę wcisnij klawisz: R", True, (0, 0, 0), (86, 225, 70))
                screen.blit(inforeset, (100, 710))

                infoquit = font.render("Aby wyłączyć grę wcisnij klawisz: Q", True, (0, 0, 0), (86, 225, 70))
                screen.blit(infoquit, (110, 760))

                pygame.display.flip()
                fpsClock.tick(fps)
        if wybor == 3:

            win = GraphWin('Krzywe beziera - Piotr Piotrak', 500, 400)

            def newton(n, i):
                return math.factorial(n) / (math.factorial(i) * math.factorial(n - i))

            def krzywe_beziera(punkty_x, punkty_y, p_kontrolne):
                for t in numpy.arange(0.0, 1.0, 0.001):
                    punkt_x = 0
                    punkt_y = 0
                    for i in range(p_kontrolne + 1):
                        punkt_x = punkt_x + (newton(p_kontrolne, i) * ((1 - t) ** (p_kontrolne - i)) * (t ** i)) * \
                                  punkty_x[i]
                        punkt_y = punkt_y + (newton(p_kontrolne, i) * ((1 - t) ** (p_kontrolne - i)) * (t ** i)) * \
                                  punkty_y[i]
                    punkt = Point(punkt_x, punkt_y)
                    punkt.draw(win)

            punkty_x = [104, 112, 100, 88, 408, 106]
            punkty_y = [377, 64, 55, 46, 115, 202]
            punkty_x_2 = [304, 312, 300, 288, 608, 306]
            punkty_y_2 = [377, 64, 55, 46, 115, 202]

            krzywe_beziera(punkty_x, punkty_y, 5)
            krzywe_beziera(punkty_x_2, punkty_y_2, 5)

            win.getMouse()
            win.close()

        if wybor == 4:
            print(" ------------------ Niestety nie zrobiłem programu z lab 4 :( ------------------")

main()