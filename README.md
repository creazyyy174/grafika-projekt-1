# grafika-projekt-1
Aby cały projekt działał poprawnie, potrzebne jest posiadanie 2 plików .png które są potrzebne do gry z lab nr 2.
Zrobiłem proste menu, aby łatwo było można przemieszczać się pomiędzy projektami z lab 1-4, niestety podczas wyłączania projektu nr 2, cały kod się zatrzymuje i trzeba go włączyć ponownie, poza tym wszystko działa poprawnie.
W projekcie z lab nr 1, wykonałem prosty, ale ładny domek za pomocą biblioteki "graphics.py".
Projekt z lab nr 2 jest to gra. Jako tło tej gry użyłem stworzony wcześniej domek z lab nr 1, ale tło ustawiłem za pomocą wczytania pliku .png, aby nie podwajać kodu z lab nr 1. Do tego użyłem pliku "target64px.png" który jest tarczą w grze. W tym projekcie głównie używałem biblioteki pygame. Gra polega na tym, aby klikać w pojawiające się tarcze w oknach domku. Domyślny czas na kliknięcie w tarcze wynosi 0.8s, ale można to zmienić w kodzie w linijce 173. W przypadku gdy nie zdążymy w tym czasie kliknąć w tarcze tracimy 1 życie, których na start jest 5. Dodałem również przycisk resetujący grę (R) oraz przycisk wyjścia z gry (Q)
Do stworzenia krzywych Beziera z lab nr 3 użyłem bibliotek numpy, math oraz graphics.
