## SPARC FILE UPDATER ##
# This script allows to insert a new goal or a new observation into the
# restaurant SPARC file.

## Importations ##
import re

## Path of file to write into ##
file='test_writing.sparc'

## Samples of lines to insert, don t forget the \n ##'
g1='goal(I):- holds(isonchair(c1,chair2t2),I)).\n'
o1='observed(bill_wave(c2),3).\n'

g_lines= '%goal_b\n'+ g1 + '%goal_e\n'
o_lines= '%obs_b\n' + o1 + '%obs_e\n'

goal='%goal_b(\n.*?)*?\n%goal_e\n'
obs='%obs_b(\n.*?)*?\n%obs_e\n'


## 1. Clear the previous goals/obseravtions ##
## Might be a non-optimal way to do so, but it works ##
## Does not reset anything if does not work (previous state) ##
with open(file, 'r+') as f:
    text=f.read()
    newf=open('test_writing.sparc', 'w')
    try:
        new=re.sub(goal, g_lines, text, flags=re.MULTILINE)
        new2=re.sub(obs, o_lines, new, flags=re.MULTILINE)
        newf.write(new2)
        newf.close()
    except: 
        print("Editing file has failed")
        newf.write(text)
        newf.close()
