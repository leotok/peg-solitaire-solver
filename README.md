# Peg Solitaire Solver
> "Resta-1" game in Portuguese

## Representation
```
- ' ': invalid field
- 'o': field with a peg
- '_': empty field

tabuleiro = [
    [' ',' ','o','o','o',' ',' '],
    [' ',' ','o','o','o',' ',' '],
    ['o','o','o','o','o','o','o'],
    ['o','o','o','_','o','o','o'],
    ['o','o','o','o','o','o','o'],
    [' ',' ','o','o','o',' ',' '],
    [' ',' ','o','o','o',' ',' '],
]
```

## Results

- Backtracking with old movements/table constraints and symetric states prunning
    - Solves the game in 867588 turns (4min40s)

```
Turno 867587 | Nivel 31
    _ _ _
    _ _ _
_ _ _ _ _ _ _
_ _ _ _ _ _ _
_ _ _ o _ _ _
    _ o _
    _ _ _
_______________
Turno 867588 | Nivel 32
    _ _ _
    _ _ _
_ _ _ _ _ _ _
_ _ _ o _ _ _
_ _ _ _ _ _ _
    _ _ _
    _ _ _
_______________
Jogadas:
2 4 baixo
5 4 cima
4 2 direita
4 4 cima
1 4 baixo
2 3 baixo
5 3 cima
5 1 direita
3 1 baixo
5 6 esquerda
5 4 esquerda
5 1 direita
6 3 cima
4 3 cima
1 3 baixo
7 5 cima
3 6 baixo
3 4 direita
3 2 direita
1 5 baixo
4 5 cima
3 7 esquerda
3 4 direita
5 7 cima
3 7 esquerda
2 5 baixo
4 5 baixo
7 3 direita
7 5 cima
5 6 esquerda
6 4 cima
Parabens você ganhou o jogo!
```