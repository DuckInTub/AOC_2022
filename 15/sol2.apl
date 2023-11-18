⍝ Solution 2021 15

noR←{x1 y1 x2 y2←⍵ ⋄ d←(y1-y2)+⍥|x1-x2 ⋄ d<dl←|⍺-y1:0 ⋄ x1(-,+)d-dl}
cords←{⍎¨⍵⊆⍨⍵∊⎕D}¨⊃⎕NGET 'input.txt' 1
(⌈/-⌊/)⊃,/0~⍨10∘noR¨cords


lines←{x1 y1 x2 y2←⍵ ⋄ d←(y1-y2)+⍥|x1-x2 ⋄ (y1-x1),⍥((-,+)∘d)y1+x1}
pos neg←2(↑,⍥⊂⍥,↓)⍉↑lines¨cords

⍝ p←∪0~⍨,∘.{2=|⍺-⍵:1+⍺⌊⍵ ⋄ 0}⍨pos
⍝ n←∪0~⍨,∘.{2=|⍺-⍵:1+⍺⌊⍵ ⋄ 0}⍨neg
y x←⊃pos∘.{0.5×⍺(+,-⍨)⍵}⍥{∪0~⍨,∘.{2=|⍺-⍵:1+⍺⌊⍵ ⋄ 0}⍨⍵}neg

⎕PP←32
y+4000000×x

