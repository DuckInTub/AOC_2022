⍝ Solution 2022 25
to_snafu←{
     mod←0 1 2 ¯2 ¯1
     out←⍬
     to_fold←⌽⍵,5*⍳⌈5⍟⍵
     f←{d←mod⌷⍨1+5|¯2+⍺|⍵+2 ⋄ out∘←out,d ⋄ (⌊5÷⍨⍵-d)}
     ⌽out⊣f/to_fold
 }

<<<<<<< Updated upstream
=======
add_snafu←{
     s←'=-012'
     mx_len←⍺⌈⍥≢⍵
     a w←mx_len∘{'0'@(' '∘=)(-⍺)↑⍵}¨⍺ ⍵
     m←a,[0.5]⍥{¯3+s⍳⍵} w
     c←0
     ⍝ (s)um, (c)arry, (d)igit
     f←{s←⍺+⍵+c ⋄ d←¯2+5|s+2 ⋄ d⊣c∘←⌊5÷⍨s-d}
     ret←⌽f⌿⌽m
     c≠0:s[3+c,ret]
     s[3+ret]
 }


>>>>>>> Stashed changes
s←'=-012'
parse←{¯3+s⍳⍵}
to_snafu←{¯2+5⊥⍣¯1⊢⍵+5⊥2/⍨⌈5⍟⍵}
n←+/(5⊥parse)¨⊃⎕NGET 'test.txt' 1
s[3+to_snafu n]
