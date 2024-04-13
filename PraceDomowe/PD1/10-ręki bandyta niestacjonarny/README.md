# Wieloręki bandyta niestacjonarny

**Zadanie warte 10 pkt**

## Osoba zgłoszona (max 2 osoby, wybiorę jedną do zaprezentowania na zajęciach):

(1) Norbert Frydrysiak

(2) ...


## Problem wielorękiego bandyty
Na zajęciach rozważaliśmy zadanie wielorękiego bandyty:

Mamy wiele maszyn, z których każde ma pewną nieznaną funkcję nagrody. "Granie" polega na wyborze maszyny, od której nagrodę otrzymamy. Celem jest granie tak, aby zdobyć sumarycznie jak największą nagrodę.

## Eksploracja kontra eksploatacja

Aby zdobyć dużą nagrodę, agent chciałby grać często na maszynie, która do tej pory się sprawdzała. Powinien jednak czasem grać na tych mniej obiecujących, bo być może okażą się one lepsze.

## Niestacjonarny

Dodatkowym utrudnieniem często występującym w praktycznych zastosowaniach jest niestacjonarność. Rozkład nagrody może zależeć od tego, jak długo trwa gra.

## Zadanie
Zadanie 2.5 ze strony 33 "Reinforcement Learning: An Introduction" Sutton, Barto. Czyli:

Zwizualizuj problemy, jakie napotykają metody estymujące średnią dla niestacjonarnych bandytów. Narysuj wykres, gdzie na osi OX będzie liczba losowań, a na osi OY % wyboru optymalnej akcji. Użyj $\alpha = 0.1$, $\varepsilon = 0.1$, 100 000 losowań.

Zacznij od 10 bandytów $\mathcal{N}(0, 1)$. Po każdym losowaniu do rozkładu każdego z bandytów dodaj liczbę wylosowaną (niezależnie dla każdego z bandytów) z rozkładu $\mathcal{N}(0, 0.01)$ i kumuluj je.

(Nie mam pewności, czy opisałem to w sposób zrozumiały. W razie wątpliwości proszę pytać.)





