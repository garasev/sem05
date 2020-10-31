ok.
input(A, B, C) :- read(A), read(B), read(C); ok.
check(T, C) :- M is (T mod C), M is 0, write(T), nl; ok.
cicle(A, B, C) :-  T is (B - 1), T >= A, check(T, C), cicle(A, T, C); ok.
start :- input(A, B, C), cicle(A, B, C); ok.