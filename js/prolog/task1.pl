ok.
input(A, B) :- read(A), read(B); ok.
fibb(A, B, C, D) :- E is (A + B), A => C, write(A), A =< D, fibb(B, E, C, D); ok.
start :- input(A, B), fibb(1, 1, A, B); ok.