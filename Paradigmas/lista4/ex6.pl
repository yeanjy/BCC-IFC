pai(joao, maria).
pai(joao, pedro).
pai(joao, marcos).
pai(joao, joana).
pai(pedro, ricardo).
pai(pedro, bruno).
pai(bruno, victor).
sexo(joao, masculino).
sexo(maria, feminino).
sexo(pedro, masculino).
sexo(marcos, masculino).
sexo(joana, feminino).
sexo(ricardo, masculino).
sexo(bruno, masculino).
sexo(victor, masculino).

irmao(X, Y) :- 
  pai(Z, X),
  pai(Z, Y),
  sexo(X, masculino),
  X \= Y.

irma(X, Y) :- 
  pai(Z, X),
  pai(Z, Y),
  sexo(X, feminino),
  X \= Y.

neto(X, Y) :- 
  pai(Z, X),
  pai(Y, Z),
  sexo(X, masculino).

neta(X, Y) :- 
  pai(Z, X),
  pai(Y, Z),
  sexo(X, feminino).

bisneto(X, Y) :-
  neto(Z, Y),
  pai(Z, X),
  sexo(X, masculino).
