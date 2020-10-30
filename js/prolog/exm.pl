ok.
input(A, B) :- read(A), read(B); ok.
printA(A, S) :- A >= S, write(A), nl; ok.
cicle(A, B, S, F) :- C is (A + B), printA(A, S), B =< F, cicle(B, C, S, F); ok.
start :- input(A, B), cicle(1, 1, A, B); ok.