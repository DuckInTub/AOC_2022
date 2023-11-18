p ← {(s o d n1 n2) ← ⍵ ⋄ (⊂⍎18↓s),(⊂19↓o),((⍎21↓d),(1+⍎29↓n1),(1+⍎30↓n2))}¨1↓¨p⊆⍨(0≠≢)¨p←⊃⎕NGET 'test.txt' 1
⎕pp←30

exec ← {op ← '+×'⌷⍨'+*'⍳⍵[5] ⋄ 'old'≡6↓⍵:⍎'⍺',op'⍺' ⋄ ⍎'⍺',op,6↓⍵}
struct ← ⊂(79 98)('old * 19')(23 2 3)

 ans←solveA d
 ret←(≢d)⍴0
 :For _ :In ⍳20
     :For index :In ⍳≢d
         part←⊃d[index]
         (i op div nt nf)←part
         ret[index]←ret[index]+≢i
         i←⌊3÷⍨i exec op
         b←0=div|i
         t←b/i
         f←(~b)/i
         (⊃d[index])[1]←⊂⍬
         (⊃d[nt])[1]←⊂t,⍨⊃(⊃d[nt])[1]
         (⊃d[nf])[1]←⊂f,⍨⊃(⊃d[nf])[1]
     :EndFor
 :EndFor
 ans←×/2↑(⊂∘⍒⌷⊢)ret

 ans←solveB d
 ret←(≢d)⍴0
 divs←×/3∘⊃¨d
 :For _ :In ⍳10000
     :For index :In ⍳≢d
         part←⊃d[index]
         (i op div nt nf)←part
         ret[index]←ret[index]+≢i
         i←divs|i exec op
         b←0=div|i
         t←b/i
         f←(~b)/i
         (⊃d[index])[1]←⊂⍬
         (⊃d[nt])[1]←⊂t,⍨⊃(⊃d[nt])[1]
         (⊃d[nf])[1]←⊂f,⍨⊃(⊃d[nf])[1]
     :EndFor
 :EndFor
 ans←×/2↑(⊂∘⍒⌷⊢)ret

solveA p
solveB p