⍝ Solution 2022 25
to_snafu←{
     mod←0 1 2 ¯2 ¯1
     out←⍬
     to_fold←⌽⍵,5*⍳⌈5⍟⍵
     f←{d←mod⌷⍨1+5|¯2+⍺|⍵+2 ⋄ out∘←out,d ⋄ (⌊5÷⍨⍵-d)}
     ⌽out⊣f/to_fold
 }

s←'=-012'
parse←{¯3+s⍳⍵}
to_snafu←{¯2+5⊥⍣¯1⊢⍵+5⊥2/⍨⌈5⍟⍵}
n←+/(5⊥parse)¨⊃⎕NGET 'test.txt' 1
s[3+to_snafu n]
