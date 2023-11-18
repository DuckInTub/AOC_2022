d ← ↑⍎¨¨⊃⎕NGET 'input.txt' 1

HL ← (¯1↓1↓⊢)(⊢≤¯1⌽⌈\)			⍝ Takes a row, gives back a one for each tree that is hidden from the left
HR ← (¯1↓1↓⊢)⌽∘(⊢≤¯1⌽⌈\)∘⌽		⍝ Same idea but hidden from the right
HLR ← ↑((0,⍨0,HL∧HR)¨↓)			⍝ Same idea, but both left and right, and this one takes a matrix

+/,~(⍉HLR ⍉d) ∧ HLR d			⍝ Finally, check if hidden for each row and column (the ⍉) and then and those togheter
								⍝ The number of zeros is the answer

⍝ Part two
view_r ← {t ← ⍺⊃,⍵ ⋄ b←1∊t≤⍺↓⍵ ⋄ b:⊃⍸t≤⍺↓⍵ ⋄ ≢⍺↓⍵}
view_l ← {i ← 1+⍺-⍨≢⍵ ⋄ t ← i⊃,⍵ ⋄ b←1∊t≤i↓⍵ ⋄ b:⊃⍸t≤i↓⍵ ⋄ ≢i↓⍵}∘⌽
scene_m ← {↑⍵∘{⍵∘(view_l×view_r)¨↓⍺}¨⍳≢⍵}
⌈/⌈/⍉((⍉scene_m∘⍉)×scene_m) d
