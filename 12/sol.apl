n←27⌊2⌈('S',⎕C ⎕A)⍳p←↑⊃⎕NGET 'test.txt' 1

e←⊃⍸'E'=p
s←'S'=p

UDLR ←3 3 ⍴ 0 1 0 1 1 1 0 1 0

f ← ({⌈/⌈/UDLR×⍵}⌺3 3)

solveA ← 0∘{e⌷⍵:⍺ ⋄ (⍺+1)∇ n≤1+f n×⍵}

solveA s

solveA 'Sa' ∊⍨ p