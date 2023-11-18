 parse←{
     thing←{(⊢⊂⍨1 0⍴⍨≢)1↓⍵/⍨⍵∊⎕A}¨⍵
     pos←(⊂∘⍋⌷⊢)∪⊃,/thing
     t←⍋{⊃pos⍳⍵}¨thing
     d←((⊂t)⌷⊢)⍎¨('\d+'⎕S'&')⍵
     i←⊃,/{1↓(⊃⍵)∘,¨⍵}¨{pos⍳⍵}¨thing
     d,pos,×(⍉+⊢)1@i⊢0⍴⍨2/≢pos
 }