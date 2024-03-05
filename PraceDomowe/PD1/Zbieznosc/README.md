# Zbieżność

Zwizualizuj zbieżność.

**Zadanie warte 5 pkt**

## Osoba zgłoszona (max 2 osoby, wybiorę jedną do zaprezentowania na zajęciach):

(1) ...

(2) Paweł Świderski

## Twierdzenie o zbieżności
Na zajęciach podane było twierdzenie (Strona 33, "Reinforcement Learning: An Introduction" Sutton, Barto):

$Q_1 \in \mathbb{R}$, $R_i$ - ciąg niezależnych zmiennych losowych o tej samej wartości oczekiwanej.

$Q_{n+1} = Q_n + \alpha_n\cdot (R_n - Q_n)$

Wtedy:

$Q_n$ zbiega z prawdopodobieństwem 1 do $\mathbb{E}[R_1]$ iff:

(1) ${\sum_{n=1}}^\infty \alpha_n = \infty$

(2) ${\sum_{n=1}}^\infty \alpha_n^2 < \infty$

## Zadanie
Zwizualizuj powyższą zbieżność dla następujących ciągów:

(a) $\alpha_n = \frac{1}{n}$

(b) $\alpha_n = \frac{1}{nlog(n)}$

(c) $\alpha_n = \frac{1}{n^{2/3}}$

Zwizualizuj brak zbieżności dla następujących ciągów:

(d) $\alpha_n = \frac{1}{n^2}$, gdzie (1) jest zbieżny

(e) $\alpha_n = \frac{1}{\sqrt{n}}$, gdzie (2) jest rozbieżny

(f) $\alpha_n = 0.05$, gdzie (2) jest rozbieżny

(g) $\alpha_n = 0.2$, gdzie (2) jest rozbieżny

(h) Jeszcze jeden ciąg wybrany przez siebie.

Jako zmienne losowe $R_i$ weź iid. z rozkładu standardowego normalnego. Jako $Q_1$ wybierz:

(I) $Q_1 = 0$

(II) $Q_1 = 10$

