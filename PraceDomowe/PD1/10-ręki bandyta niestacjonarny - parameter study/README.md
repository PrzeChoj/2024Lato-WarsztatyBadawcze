# Wieloręki bandyta

**Zadanie warte 10 pkt**

## Osoba zgłoszona:

(a) Krzysztof Sawicki

(b) Natalia Safiejko

(c) Wojciech Grabias

## Problem wielorękiego bandyty
Na zajęciach rozważaliśmy zadanie wielorękiego bandyty:

Mamy wiele maszyn, z których każde ma pewną nieznaną funkcję nagrody. "Granie" polega na wyborze maszyny, od której nagrodę otrzymamy. Celem jest granie tak, aby zdobyć sumarycznie jak największą nagrodę.

## Eksploracja kontra eksploatacja

Aby zdobyć dużą nagrodę, agent chciałby grać często na maszynie, która do tej pory się sprawdzała. Powinien jednak czasem grać na tych mniej obiecujących, bo być może okażą się one lepsze.

## Niestacjonarny

Dodatkowym utrudnieniem często występującym w praktycznych zastosowaniach jest niestacjonarność. Rozkład nagrody może zależeć od tego, jak długo trwa gra.

## Zadanie
Zadanie 2.11 ze strony 44 "Reinforcement Learning: An Introduction" Sutton, Barto. Czyli:

Narysuj wykres 2D, gdzie na osi OX będzie wartość parametru, a na osi OY średnia nagroda z gier od 10 000 do 20 000.

Zacznij od 10 bandytów $\mathcal{N}(0, 1)$. Po każdym losowaniu do rozkładu każdego z bandytów dodaj liczbę wylosowaną (niezależnie dla każdego z bandytów) z rozkładu $\mathcal{N}(0, 0.01)$ i kumuluj je.

(Nie mam pewności, czy opisałem to w sposób zrozumiały. W razie wątpliwości proszę pytać.)


### Wersja a

UCB, gdzie parametrem jest $c$.


### Wersja b

eps-greedy, gdzie parametrem jest $\varepsilon$.

### Wersja c

Optymistyczny greedy, gdzie parametrem jest $Q_0$. Wybierz $\alpha = 0.1$.



