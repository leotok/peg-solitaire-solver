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
