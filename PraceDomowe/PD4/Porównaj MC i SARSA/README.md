# Porównaj MC i TD

**Zadanie za 10 pkt**

**UWAGA**
Do zadania możne się zgłosić dowolnie dużo studentów. Każdy jednak musi wybrać sobie inną grę.

**UWAGA**
Jedną grę można rozwiązywać samodzielnie (za 100% pkt) albo w parze (obie osoby dostają po 50% pkt każda).

**UWAGA**
Przy wyborze jakiejś bardziej skomplikowanej gry można argumentować zwiększenie punktacji do 15 pkt. Z taką propozycją zapraszam na prv.

## Osoba zgłoszona (w nawiasie jaką grę będzie rozwiązywać):

a) ... - Windy Gridworld

b) Anna Ostrowska (PD2 - rozwiąż małą grę a)

c) ...

...

## Monte Carlo

Na zajęciach omawiane były algorytmy Monte Carlo rozwiązywania gier. Jest ona użyteczna nawet w sytuacji, w której nie znamy p(s',r|s,a). Wymagana jest jedynie możliwość jej symulacji.

Schemat tego algorytmu opisany jest w książce Barto na stronie 92. Musi być do niego dołożony element eksploracji. Można tę eksplorację dołożyć w dwóch miejscach:
* Eksploracyjny początek; algorytm na stronie 99 - Monte Carlo ES (Exploring Starts)
* Eksploracyjna polityka; algorytm na stronie 101 - On-policy first-visit MC control

## Temporal Difference

Omawiany na zajęciach podstawowy algorytm TD, znany w literaturze szerzej jako TD(lambda = 0) albo TD(n = 1), różni się od MC tym, że update następuje nie tylko na koniec epizodu, ale po każdym ruchu. Wykorzystywana jest idea bootstrap w taki sposób, że przy estymacji nowej wartości V(s) wykorzystywane są estymacje pozostałych V(s').

Schemat TD(lambda = 0) jest przedstawiony w książce Barto na stronie 120.

## SARSA

SARSA jest drobną modyfikacją TD umożliwiającą uczenie się wykonywania akcji.

Schemat algorytmu SARSA jest przedstawiony w książce Barto na stronie 130.

## Zadanie
Dla wybranej przez siebie gry na siatce (np. jednej z możliwych do wyboru z PD2 albo "Windy Gridworld", który jest przedstawiony w książce Barto na stronie 130) zaimplementuj którąś wersje algorytmu MC oraz algorytm TD. Porównaj ich działanie. Czy zbiegały tak samo szybko? Jak dużą nagrodę miały algorytmy w czasie uczenia?


