⍝ Better solution to day 9 2022

⍝ Gives new tail position
⍝ based on old tail position ⍺
⍝ and new head position ⍵
tail_i←{
    t h←⍺,⍵
    diff←h-t
    b_move←1J1<⍥|diff
    b_move:t+1 0J1+.××9 11○diff
    t
}

⍝ Modified version of the \ operator
⍝ that scans from the left instead of right.
⍝ Run the following for an overview:
⍝   {⍺ 'f' ⍵} scanL ⍳5
scanL←{c f←⊃⍵ ⋄ f,⍺⍺{⊢c∘←c ⍺⍺ ⍵}¨1↓⍵}

⍝ tests←m/⍥,⍨1J1<⍥|m←(0j1∘×∘.+⊢)¯2 ¯1 0 1 2

⍝ Calculate the sequential positions of the head
⍝ Note the use of imaginary numbers:
⍝   0J1*⍳4
⍝ This part of the code will give us the 
⍝ complex numbers of the cardinal directions.
headPos←+\(⍎¨2↓¨p)/0J1*'ULDR'⍳⊃¨p←⊃⎕NGET 'test.txt' 1

⍝ Part 1
≢∪ tail_i scanL 0,headPos
⍝ Part 2
≢∪(tail_i scanL)⍣9⊢ headPos,⍨9/0

