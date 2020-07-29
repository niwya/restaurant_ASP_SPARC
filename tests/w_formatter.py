## Observations/Goals formatter + file updater ## 
import re

# Path of file that is going to be modified
w_file='restaurant3.sparc'

# Getting an input
sample=[['obs', 'bill_wave(c1)', 'true', '2'], ['goal', '3', 'isonchair(c1,chair2t1)']]

# Initializing the goal and observation strings
goal='%b_goal\n'
obs='%b_obs\n'

# Formatting the data
def format_data(o,g,input_list):
    for list_go in input_list:
        if list_go[0]=='obs':
            # Observations are pretty straightforward, as the first item in list will be the 'observed' indicator, and the
            # following will be the fluent, then if has been seen as true or false then the step at which it occured.
            o+=list_go[0] + '(' + list_go[1] + ',' + list_go[2] +','+list_go[3] + ').\n'
        elif list_go[0]=='goal': 
            # Goals are less straightforward, as they can be constitued of multiple fluents. The first item in the list
            # is the goal indicator, then the step at which the goal is wanted to be archieved. Then comes the fluents
            # themselves.
            g+=list_go[0] + '(' + list_go[1] + '):- '
            for elem in list_go[2:-1]:
                g+='holds('+ elem + ',' + list_go[1] + '),'
            g+='holds(' + list_go[-1] + ',' + list_go[1] + ').\n'
        else: print("Unauthorized format")
    o+='%e_obs\n'
    g+='%e_goal\n'
    return o,g

o_lines,g_lines=format_data(obs,goal,sample)

# Writing said input into the desired file
goal_sep='%b_goal(\n.*?)*?\n%e_goal\n'
obs_sep='%b_obs(\n.*?)*?\n%e_obs\n'

with open(w_file, 'r+') as f:
    text=f.read()
    try:
        new=re.sub(goal_sep, g_lines, text, flags=re.MULTILINE)
        new2=re.sub(obs_sep, o_lines, new, flags=re.MULTILINE)
        f.seek(0)
        f.write(new2)
    except: 
        print("Editing file has failed")
