d ← ⊃⎕NGET 'input.txt' 1
d ← ⍎¨¨¨'-'(≠⊆⊢)¨¨','∘(≠⊆⊢)¨d

range ← {(⍳⍺)~⍳(⍵-1)}
rangeContain ← {(∧/⍺∊⍵)∨(∧/⍵∊⍺)}

+/rangeContain/⊃¨(range⍨)/¨↑d


rangeOverlap ← {1≤≢⍺∩⍵}

+/rangeOverlap/⊃¨(range⍨)/¨↑d