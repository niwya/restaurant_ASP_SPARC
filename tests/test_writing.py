## SPARC FILE UPDATER ##
# This script allows to insert a new goal or a new observation into the
# restaurant SPARC file.

## Importations ##
import re

## Keys for start and end of allowed writing zones ##
g_start='%b_goal'
g_end='%b_goal'

o_start='%b_obs'
o_end='%e_obs'

## Path of file to write into ##
path='test_writing.sparc'

## Samples of lines to insert ##
g1='goal(I):- holds(isonchair(c1,chair2t2),I)).'
o1='observed(bill_wave(c2),3).'

## 1. Clear the previous goals/obseravtions ##
## 2. Write the ones that have been passed ##
