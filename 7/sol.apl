⍝ Solution 9 2022
d←' '∘(≠⊆⊢)¨⊃⎕NGET 'test.txt' 1

depth←+\0 ¯1 1[' .'⍳{⊃⊃⌽⍵}¨insts←↓↑d]

sz←{6 2::0 ⋄ ⍎⊃⍵}¨insts

+/dirs/⍨1E5≥dirs←⊃,/sz∘{+/¨⍵⊆⍺}¨↓(∪∘.≤⊢)depth

used←7E7-⊃dirs
⌊/dirs/⍨3E7<used+dirs
