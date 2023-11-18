⍝ Example data
d ← 'ZN' 'MCD' 'P'
inst ← (1 2 1)(3 1 3)(2 2 1)(1 1 2)

⍝ My data
            [C]         [N] [R]    
[J] [T]     [H]         [P] [L]    
[F] [S] [T] [B]         [M] [D]    
[C] [L] [J] [Z] [S]     [L] [B]    
[N] [Q] [G] [J] [J]     [F] [F] [R]
[D] [V] [B] [L] [B] [Q] [D] [M] [T]
[B] [Z] [Z] [T] [V] [S] [V] [S] [D]
[W] [P] [P] [D] [G] [P] [B] [P] [V]
 1   2   3   4   5   6   7   8   9 


d ← 'WBDNCFJ' 'PZVQLST' 'PZBGJT' 'DTLJZBHC' 'GVBJS' 'PSQ' 'BVDFLMPN' 'PSMFBDLR' 'VDTR'
inst ← ¯501↑⊃⎕NGET 'input.txt' 1
inst ← ⍎¨¨((⎕D∘(∊⍨))⊆⊢)¨inst


⍝ Part 1
⍝ DFN for calculating the stacks after one instruction

 change←{
     (a b c) ← ⍵
     moving←⌽(-a)↑(b⊃⍺)
     to←⊂(c⊃⍺),moving
     from←⊂(-a)↓(b⊃⍺)
     (from@b)(to@c)⍺
 }

⍝ Reductions in APL start from the right:
⍝ It takes the operator and places it between the last two elements
⍝ It then replaces the last two elements with the result and continues.
⍝ Hence this magical reduction
(⊃⌽)¨↑change⍨/⌽(⊂d),inst

⍝ Part two

⍝ Same problem but we can pick up multiple crates
⍝ Hence removed the ⌽ glyph on the moving line
⍝ Otherwise the solution is the same
 change_2←{
     (a b c) ← ⍵
     moving←(-a)↑(b⊃⍺)
     to←⊂(c⊃⍺),moving
     from←⊂(-a)↓(b⊃⍺)
     (from@b)(to@c)⍺
 }

(⊃⌽)¨↑change_2⍨/⌽(⊂d),inst