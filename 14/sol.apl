m ← ⌊⌊/⊃,/⍎¨('->' ','⎕R ' , ' '.')¨file←⊃⎕NGET 'test.txt' 1

cords ← {⍵⊂⍨1 0⍴⍨≢⍵}¨⌽¨⍎¨('->' ','⎕R ' , ' ' ')¨file
d ← {(a b) ← ⍵ ⋄ (a+1),1+b-m}¨¨cords

wid ← 1+m-⍨⌈/2∘⊃¨⊃,/cords
hei ← 1+⌈/⊃¨⊃,/cords
off ← hei
o ← 1,1+500-m

to ← {,(1-⍨⍺⌊⍵)∘+¨⍳1+|⍵-⍺}
next ← {und ← (1 0) (1 ¯1)  (1 1) (0 0)⋄ ⍵+⊃und⌷⍨⊃⍸0=⍺[⍵∘+¨und]}
end ← {(⍺ next ⍵)≡⍵:⍵ ⋄ ⍺ ∇(⍺ next ⍵)}

i ← (⊃,/{⊃,/2to/⍵}¨d)
map ← 1@i⊢hei wid ⍴ 0

0∘{3 :: ⍺ ⋄ (⍺+1)∇(1@(⊂⍵ end o))⍵}map

⍝ Part two
o ← 1,off+1+500-m

i ← (⊃,(off+2∘⊃))¨(⊃,/{⊃,/2to/⍵}¨d)

map ← 1⍪⍨0⍪⍨1@i⊢hei (wid+2×off) ⍴ 0

'`#' vis map

0∘{o⌷⍵:⍺ ⋄ (⍺+1)∇(1@(⊂⍵ end o))⍵}map