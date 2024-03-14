# Porównaj wersje MC

**Zadanie za 10 pkt**

**UWAGA**
Do zadania możne się zgłosić dowolnie dużo studentów. Każdy jednak musi wybrać sobie inną grę.

**UWAGA**
Jedną grę można rozwiązywać samodzielnie (za 100% pkt) albo w parze (obie osoby dostają po 50% pkt każda).

**UWAGA**
Przy wyborze jakiejś bardziej skomplikowanej gry można argumentować zwiększenie puntacji do 15 pkt. Z taką propozycją zapraszam na prv.

## Osoba zgłoszona (w nawiasie jaką grę będzie rozwiązywać):

a) ...

b) ...

c) ...

...

## Monte Carlo

Na zajęciach omawiane były algorytmy Monte Carlo rozwiązywania gier. Jest ona użyteczna nawet w sytuacji, w której nie znamy p(s',r|s,a). Wymagana jest jedynie możliwość jej symulacji.

Schemat tego algorytmu opisany jest w książce Barto na stronie 92. Musi być do niego dołożony element eksploracji. Można tę eksplorację dołożyć w dwóch miejscach:
* Eksploracyjny początek; algorytm na stronie 99 - Monte Carlo ES (Exploring Starts)
* Eksploracyjna polityka; algorytm na stronie 101 - On-policy first-visit MC control

## Zadanie
Dla wybranej przez siebie gry na siatce (np. jednej z możliwych do wyboru z PD2) zaimplementuj obie wersje algorytmu MC. Porównaj ich działanie. Czy zbiegały tak samo czybko? Jak dużą nagrodę miały algorytmy w czasie uczenia?


