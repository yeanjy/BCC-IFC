aluno(yean).
aluno(jota).
aluno(kadu).
aluno(estevao).
frequencia(yean, 92).
frequencia(jota, 100).
frequencia(kadu, 75).
frequencia(estevao, 74).
nota(yean, 9).
nota(jota, 2).
nota(kadu, 7).
nota(estevao, 8).

passou2(X) :-
  aluno(X),
  nota(X, Y),
  Y >= 7,
  frequencia(X, Z),
  Z >= 75.

passou(X) :-
  aluno(X),
  nota(X, Y),
  Y >= 7.
