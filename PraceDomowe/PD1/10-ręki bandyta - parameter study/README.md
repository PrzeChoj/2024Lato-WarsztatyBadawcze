# Wieloręki bandyta

**Zadanie warte 5 pkt**

## Osoba zgłoszona:

(a) Krzysztof Sawicki

(b) Krzysztof Sawicki

(c) ...

## Problem wielorękiego bandyty
Na zajęciach rozważaliśmy zadanie wielorękiego bandyty:

Mamy wiele maszyn, z których każde ma pewną nieznaną funkcję nagrody. "Granie" polega na wyborze maszyny, od której nagrodę otrzymamy. Celem jest granie tak, aby zdobyć sumarycznie jak największą nagrodę.

## Eksploracja kontra eksploatacja

Aby zdobyć dużą nagrodę, agent chciałby grać często na maszynie, która do tej pory się sprawdzała. Powinien jednak czasem grać na tych mniej obiecujących, bo być może okażą się one lepsze.

## Zadanie
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


Zreprodukuj obrazek 2.6 ze strony 42 "Reinforcement Learning: An Introduction" Sutton, Barto. Czyli:

Narysuj wykres 2D, gdzie na osi OX będzie wartość parametru, a na osi OY średnia nagroda po 1000 grach.

### Wersja a

UCB, gdzie parametrem jest $c$.


### Wersja b

eps-greedy, gdzie parametrem jest $\varepsilon$.

### Wersja c

Optymistyczny greedy, gdzie parametrem jest $Q_0$. Wybierz $\alpha = 0.1$.



