⍝d ← (⊃,(⍎∘⊃⌽))¨' '(≠⊆⊢)¨⊃⎕NGET 'test.txt' 1

d ← ⊃⎕NGET 'test.txt'1
parseMove←{d t←' '(≠⊆⊢)⍵ ⋄ (⍎t)×⊃((⊢,-)(⌽,⍥⊂⊢)1 0)⌷⍨'URDL'⍳d}

move←{⍺+⊃(0 1)(0 ¯1)(¯1 0)(1 0)⌷⍨'UDLR'⍳⍵}

 tail←{
     ⍝ Gives new tail position
     ⍝ based on old tail position ⍺
     ⍝ and new head position ⍵
     move←×⍵-⍺
     need_move←1<⌈/|⍵-⍺
     need_move:move+⍺
     ⍺

 }

 positions←solveA data
 t←0 0
 h←0 0
 been←⊂0 0
 :For mve :In data
     (dir steps)←mve
     :For step :In ⍳steps
         h←h move dir
         t←t tail h
         been←(⊂t),been
     :EndFor
 :EndFor
 positions←been

 ≢∪solveA d

 positions←solveB data
 t←9/⊂0 0
 h←0 0
 been←⊂0 0
 :For mve :In data
     (dir steps)←mve
     :For step :In ⍳steps
         h←h move dir
         t[1]←⊂(⊃t[1])tail h
         :For i :In 1↓⍳≢t
             t[i]←⊂(⊃t[i])tail⊃t[i-1]
         :EndFor
         been←been,t[9]
     :EndFor
 :EndFor
 positions←been

 ≢∪solveB d
