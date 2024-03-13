# Rozwiąż małą grę

Znajdź rozwiązanie małej gry.

**UWAGA**
Zadanie można rozwiązywać samodzielnie (za 100% pkt) albo w parze (obie osoby dostają po 50% pkt każda).

## Osoba zgłoszona:

(a) Hubert Kowalski

(b) Paweł Świderski 

(c) Norbert Frydrysiak

(d) Adam Kaniasty

(e) ...

(f) ...

## Równanie Bellmana

Na zajęciach wyprowadzone zostało równanie Bellmana:

$$\forall_{s\in S} v_{\pi}(s) = \sum_{a\in A} \pi (a|s) \cdot \sum_{s'\in S, r\in R} p(s',r|s,a)\cdot (r+\gamma\cdot v_{\pi}(s'))$$

gdzie $\pi (a|s)$ oraz $p(s',r|s,a)$ są znane.

Jest to układ $|S|$ równań liniowych z $|S|$ niewiadomymi, który ma jednoznaczne rozwiązanie, gdy $\gamma\in [0,1)$.

Jedną z numerycznych metod rozwiązywania tego układu jest zaczęcie z jakiegokolwiek wektora dla $v_{\pi}^{(0)}(s)$, wstawienie go do prawej strony równań i w ten sposób otrzymanie nowego wektora $v_{\pi}^{(1)}(s)$. Iterowanie tej metody zbiegnie do prawdziwego $v_{\pi}(s)$.

Po zbiegnięciu można wybrać alternatywną politykę $\pi'$ taką, że jest ona zachłanna względem $v_{\pi}(s)$. Będzie ona na pewno lepsza, czyli $\pi' \ge \pi$. Jeśli będzie $\pi' = \pi$, to znaczy, że algorytm się zakończył i mamy $\pi = \pi^*$, czyli znaleźliśmy optymalną politykę dla danego środowiska.

Powyższy algorytm nazywa się **Programowanie Dynamiczne**.

## Zadanie
Rozwiąż grę algorytmem Programowania Dynamicznego

(a, 5 pkt) Modyfikacja przykładu 4.1 z książki ze strony 76. Plansza jest 7x7. Gracz może się po niej poruszać w 4 kierunkach. Gdy będzie próbował wejść w ścianę, to jego pozycja się nie zmienia. Za każdym ruchem dostaje "nagrodę" -1. Koniec gry następuje, gdy wejdzie do prawego dolnego albo lewego górnego rogu. Idąc w prawo, gracz przechodzi dwa pola zamiast jednego (jeżeli jest o jedno pole od ściany, to jedynie idzie o jedno pole).

Narysuj rozwiązanie. W Pythonie można printować strzałki. Chcę zobaczyć planszę i jaki jest optymalny krok.

(b, 10 pkt) Plansza 5 na 5. W jednym miejscu znajduje się gracz. Gracz może się przesuwać góra, dół lewo, prawo. W jednym z miejsc znajduje się moneta, której zebranie daje +10 pkt. W jednej ze ścian jest wyjście, które daje +10 pkt.

Sprawdź wynik dla dużego $\gamma = 0.999$ oraz małego $\gamma = 0.001$.

Narysuj rozwiązanie. W Pythonie można printować strzałki. Chcę zobaczyć planszę i jaki jest optymalny krok z monetą, a jaki bez monety. Jeśli gracz znajdzie się w kratce z monetą, moneta znika - nie można więc być w tej samej kratce co istniejąca moneta.

(c, 10 pkt) Mamy $s \in \{1, 2, \ldots , 98, 99\}$ PLN. Jeśli będziemy mieli $100$, to agent dostaje +10. W każdym innym przypadku agent dostaje 0. Gra kończy się gdy mamy $0$, albo $100$ PLN. Agent może w jednym kroku postawić na szali dowolną liczbę złotych, ale nie mniej niż 1 i nie więcej niż posiada. Szansa wygranej jest $p$, która jest parametrem. Zbadaj $p=0.4$ (strona 84 w książce) oraz $p=0.9$.

Jaka jest optymalna strategia grania? Zwizualizuj, rysując wykres słupkowy, gdzie na osi OX jest liczba posiadanych pieniędzy, a na osi OY wartość, którą agent powinien postawić. Czy wynik zależy od $\gamma$? Jeśli tak / nie, to dlaczego? Zinterpretuj.

(d, 10 pkt) Przykład 3.5 z książki ze strony 60. Zreprodukuj prawą część obrazka 3.2 (obliczając te liczby równaniem Bellmana). Później za pomocą Programowania Dynamicznego znajdź strategię optymalną, czyli obrazek 3.5 z przykładu 3.8 ze strony 65.

(e, 5 pkt) Na planszy 7 x 7 wymyśl labirynt. Rozwiąż go przy pomocy równania Bellmana.

(f, 10 pkt) Na planszy N x N wylosuj dla każdej kratki niezależnie, czy będzie ona ścianą z p-stwem 5%. Wylosuj jedną kratkę, która będzie końcem gry. Za wykonanie ruchu agent dostaje -1 pkt (więc jego celem jest jak najszybciej dostać się do kratki końca gry).

Rozwiąż to zadanie przy pomocy równania Bellmana.

Zwiększaj wartość N. Narysuj wykres, w którym na osi OX będzie N, a na osi OY czas, jaki był potrzebny do znalezienia rozwiązania (średnia z 3 różnych labiryntów wielkości N).



