

letters ← (⊢,⎕C)⎕A

split ← {(⍵↑⍨⊢)¨(⊢,-)(0.5×≢)⍵}
+/letters⍳,↑↑∩/¨∪¨¨split¨d

Group3 ← {(⊂1,1+3×⍳(1-⍨3÷⍨≢⍵))⌷3,/⍵}
+/letters⍳,↑↑∩/¨∪¨¨Group3 d


⍝Better solution (Code_Report)

letters ← (⊢,⎕C)⎕A

+/letters⍳(⊃(.5×≢)(↑∩↓)⊢)¨d

+/letters⍳⊃¨↑∩/¨((1 0 0⍴⍨≢)⊂⊢)d