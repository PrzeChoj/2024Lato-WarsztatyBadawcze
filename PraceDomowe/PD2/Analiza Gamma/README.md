# Analiza Gamma

**Zadanie za 10 pkt - należy rozwiązać obie części**

**UWAGA**
Zadanie można rozwiązywać samodzielnie (za 100% pkt) albo w parze (obie osoby dostają po 50% pkt każda).

## Osoba zgłoszona:

Aleks Kapich

## Równanie Bellmana

Na zajęciach wyprowadzone zostało równanie Bellmana:

$$\forall_{s\in S} v_{\pi}(s) = \sum_{a\in A} \pi (a|s) \cdot \sum_{s'\in S, r\in R} p(s',r|s,a)\cdot (r+\gamma\cdot v_{\pi}(s'))$$

gdzie $\pi (a|s)$ oraz $p(s',r|s,a)$ są znane.

Jest to układ $|S|$ równań liniowych z $|S|$ niewiadomymi, który ma jednoznaczne rozwiązanie, gdy $\gamma\in [0,1)$.

Jedną z numerycznych metod rozwiązywania tego układu jest zaczęcie z jakiegokolwiek wektora dla $v_{\pi}^{(0)}(s)$, wstawienie go do prawej strony równań i w ten sposób otrzymanie nowego wektora $v_{\pi}^{(1)}(s)$. Iterowanie tej metody zbiegnie do prawdziwego $v_{\pi}(s)$.

Po zbiegnięciu można wybrać alternatywną politykę $\pi'$ taką, że jest ona zachłanna względem $v_{\pi}(s)$. Będzie ona na pewno lepsza, czyli $\pi' \ge \pi$. Jeśli będzie $\pi' = \pi$, to znaczy, że algorytm się zakończył i mamy $\pi = \pi^*$, czyli znaleźliśmy optymalną politykę dla danego środowiska.

Powyższy algorytm nazywa się **Programowanie Dynamiczne**.

## Zadanie
### Część (a)

Niech dana będzie gra na planszy 1D na liczbach $\{0, 1, 2, 3, 4\}$. Gracz może grać w prawo, albo STOP. Jeśli gracz zagra w prawo, jego stan zwiększa się o 1 (poza stanem $5$, gdy stan się nie zmienia) i nie dostaje żadnej nagrody, czyli $r = 0$. Jeśli gracz zagra STOP, gra się kończy, a on dostaje nagrodę: +1, jeśli był w stanie 0, +5 jeśli był w stanie 4, +0 jeśli był w pozostałych stanach.

Dla małych wartości paramteru $\gamma$ optymalna polityka będzie w stanie $0$ wołać STOP. Dla dużych wartości będzie szła w prawo i dopiero zawoła STOP w stanie $4$.

Zbadaj empirycznie dla jakich wartości parametru $\gamma$ następuje ta zmiana optymalnego zachowania.

### Część (b)

Gra jest na planszy 1D na liczbach $\{0, 1, \ldots, 99, 100\}$. Gracz może grać w prawo, albo STOP. Jeśli gracz zagra w prawo, jego stan zwiększa się o 1 (poza stanem $100$, gdy stan się nie zmienia) i nie dostaje żadnej nagrody, czyli $r = 0$. Jeśli gracz zagra STOP, gra się kończy, a on dostaje nagrodę RÓWNĄ WARTOŚCI STANU W KTÓRYM SIĘ ZNAJDUJE.

Zbadaj jak zachowuje się optymalne rozwiązanie gracza w tym środowisku w zależności od parametru $\gamma$. Narysuj wykres w którym na osi OX będzie wartość parametru $\gamma$, a na osi OY liczba punktów (niezdyskontowana) które zdobędzie gracz nauczony optymalnie dla danej $\gamma$.




