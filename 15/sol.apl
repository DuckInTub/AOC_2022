d ← ⌽¨¨(⊢⊂⍨1 0⍴⍨≢)¨d←⍎¨('-' '[^0-9]'⎕R  ' ¯' ' ')⊃⎕NGET 'test.txt' 1
b ← 2∘⊃¨d

dis ← {1++/|⍺-⍵}
cantRowRange ← {(s b) ← ⍵ ⋄ d ← ¯1+s dis b ⋄ off ← |⊃s-⍺ ⋄ l ← 0⌈1+2×d-off ⋄ (mn mx) ← t,(¯1+l∘+)t←off+d-⍨2⊃s ⋄ mn<mx: mn,mx ⋄ 0}

(+/10=⊃¨∪b)-⍨(1+⌈/-⌊/)⊃,/0~⍨10∘cantRowRange¨d