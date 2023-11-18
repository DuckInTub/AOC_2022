⍝ Solution 2022 18
dim←⌈⌿↑cords←(1+⍎)¨⊃⎕NGET 'input.txt' 1
UDLRFB←(-,⊢)⊂⍤⊢⌺3⊢0 1 0
≢sides←d~⍨,d∘.+UDLRFB

psble←d~⍨,⍳dim
out←{psble∩⍵,,⍵∘.+UDLRFB}⍣≡⊢⊂3⍴1
in←psble~out
≢in~⍨sides
