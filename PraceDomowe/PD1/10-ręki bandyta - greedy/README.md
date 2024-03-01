# Wieloręki bandyta

**Zadanie warte 5 pkt**

## Osoba zgłoszona:

(a) ...

(b) ...

(c) ...

(d) Michał Matejczuk

(e) Aleks Kapich

(f) Jakub Lange

(g) Norbert Frydrysiak 

## Problem wielorękiego bandyty
Na zajęciach rozważaliśmy zadanie wielorękiego bandyty:

Mamy wiele maszyn, z których każde ma pewną nieznaną funkcję nagrody. "Granie" polega na wyborze maszyny, od której nagrodę otrzymamy. Celem jest granie tak, aby zdobyć sumarycznie jak największą nagrodę.

## Eksploracja kontra eksploatacja

Aby zdobyć dużą nagrodę, agent chciałby grać często na maszynie, która do tej pory się sprawdzała. Powinien jednak czasem grać na tych mniej obiecujących, bo być może okażą się one lepsze.

## Zadanie
Zreprodukuj obrazek 2.3 ze strony 34 "Reinforcement Learning: An Introduction" Sutton, Barto. Czyli:

Estymuj wartość średnią bandyty przy pomocy wzoru $Q_{n+1} = Q_n + \alpha_n\cdot (R_n - Q_n)$, gdzie $\alpha = 0.1$.

Porównaj 2 podejścia:

1. eps-greedy gdzie $\varepsilon = 0.1$, $Q_1 = 0$
2. greedy gdzie $Q_1 = 5$

Narysuj wykres 2D, gdzie na osi OX będzie liczba gier, a na osi OY % wyborów najlepszego bandyty.

### Wersja a
Mamy 10 bandytów:

1. $\mathcal{N}(1, 1)$
1. $\mathcal{N}(0, 1)$
1. $\mathcal{N}(0, 1)$
1. $\mathcal{N}(0, 1)$
1. $\mathcal{N}(0, 1)$
1. $\mathcal{N}(0, 1)$
1. $\mathcal{N}(0, 1)$
1. $\mathcal{N}(0, 1)$
1. $\mathcal{N}(0, 1)$
1. $\mathcal{N}(0, 1)$

### Wersja b
Mamy 10 bandytów:

1. $\mathcal{N}(0.1, 1)$
1. $\mathcal{N}(0, 1)$
1. $\mathcal{N}(0, 1)$
1. $\mathcal{N}(0, 1)$
1. $\mathcal{N}(0, 1)$
1. $\mathcal{N}(0, 1)$
1. $\mathcal{N}(0, 1)$
1. $\mathcal{N}(0, 1)$
1. $\mathcal{N}(0, 1)$
1. $\mathcal{N}(0, 1)$

### Wersja c
Mamy 10 bandytów:

1. $\mathcal{N}(0, 10)$
1. $\mathcal{N}(0, 10)$
1. $\mathcal{N}(0, 10)$
1. $\mathcal{N}(0, 10)$
1. $\mathcal{N}(0, 10)$
1. $\mathcal{N}(1, 0.1)$
1. $\mathcal{N}(1, 0.1)$
1. $\mathcal{N}(1, 0.1)$
1. $\mathcal{N}(1, 0.1)$
1. $\mathcal{N}(1.1, 0.1)$


### Wersja d
Mamy 10 bandytów:

1. Moduł z rozkładu Cauchy'ego minus 50, zwróć uwagę, że to ma nieskończoną wartość oczekiwaną
1. $\mathcal{N}(0, 1)$
1. $\mathcal{N}(0, 1)$
1. $\mathcal{N}(0, 1)$
1. $\mathcal{N}(0, 1)$
1. $\mathcal{N}(0, 1)$
1. $\mathcal{N}(0, 1)$
1. $\mathcal{N}(0, 1)$
1. $\mathcal{N}(0, 1)$
1. $\mathcal{N}(0, 1)$


### Wersja e
Mamy 10 bandytów:

1. $U(0.1,1)$
1. $U(0,1)$
1. $U(0,1)$
1. $U(0,1)$
1. $U(0,1)$
1. $U(0,1)$
1. $U(0,1)$
1. $U(0,1)$
1. $U(0,1)$
1. $U(0,1)$


### Wersja f
Mamy 10 bandytów:

1. $Exp(2)$
1. $Exp(1)$
1. $Exp(1)$
1. $Exp(1)$
1. $Exp(1)$
1. $Exp(1)$
1. $Exp(1)$
1. $Exp(1)$
1. $Exp(1)$
1. $Exp(1)$


### Wersja g
Mamy 10 bandytów:

1. $Bernoulli(0.6)$, czyli 1 z p-stwem 0.6, 0 z p-stwem 0.4
1. $Bernoulli(0.5)$
1. $Bernoulli(0.5)$
1. $Bernoulli(0.5)$
1. $Bernoulli(0.5)$
1. $Bernoulli(0.5)$
1. $Bernoulli(0.5)$
1. $Bernoulli(0.5)$
1. $Bernoulli(0.5)$
1. $Bernoulli(0.5)$







