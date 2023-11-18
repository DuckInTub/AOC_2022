d ← ⍎¨¨((''∘≢¨)⊆⊢)⊃⎕NGET 'input.txt' 1

⌈/+/¨d ⍝ Part One

+/3↑(⊂∘⍒⌷⊢)+/¨d ⍝ Part Two