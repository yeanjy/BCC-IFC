aluno(yean).
aluno(jota).
aluno(kadu).
aluno(estevao).
nota(yean, 9).
nota(jota, 2).
nota(kadu, 7).
nota(estevao, 8).

passou(X) :-
  aluno(X),
  nota(X, Y),
  Y >= 7.
