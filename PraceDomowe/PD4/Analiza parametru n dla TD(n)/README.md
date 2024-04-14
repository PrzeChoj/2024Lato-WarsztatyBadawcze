# Analiza parametru n dla TD(n)

**Zadanie za 15 pkt**

**UWAGA**
Do zadania możne się zgłosić dowolnie dużo studentów. Każdy jednak musi wybrać sobie inną grę.

**UWAGA**
Jedną grę można rozwiązywać samodzielnie (za 100% pkt) albo w parze (obie osoby dostają po 50% pkt każda).

**UWAGA**
Przy wyborze jakiejś bardziej skomplikowanej gry można argumentować zwiększenie punktacji do 15 pkt. Z taką propozycją zapraszam na prv.

## Osoba zgłoszona (w nawiasie jaką grę będzie rozwiązywać):

a) ... - Windy Gridworld

b) ...

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

TN(n), zwany również n-step TD, wykorzystuje więcej niż jedną nagrodę w przód. Jest więc czymś pośrednim między TD, a MC. Schemat TD(n) znajduje się w książce Barto na stronie 144.

## Zadanie

Zreprodukuj obrazek 7.2 z książki Barto ze strony 145. Czyli dla "gry" Random Walk (opisanej w książce Barto na stronie 125) na 19 stanach chcemy estymować wartość stanu dla polityki całkiem losowej. Porównaj algorytmy TD(n) dla $n \in \{1, 2, 4, 8, 16, 32\}$ oraz $\alpha \in \{0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9\}$. Policz błąd dla estymacji (względem poprawnej, teoretycznej wartości stanu) po 10 epizodach gry. Błąd, o którym mowa w poprzednim zdaniu, policz wiele razy i uśrednij (nie wiem, na ile pozwoli moc obliczeniowa; jeśli będzie 10, to będę zadowolony).


