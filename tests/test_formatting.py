import time
## Testing how to format the observations/goals to update the SPARC file ## 
sample=[['observed', 'bill_wave(c1)', 'true', '2'], ['goal', '3', 'isonchair(c1,chair2t1)']]
print(sample)
goals='%b_goal\n'
observations='%b_obs\n'

def format_data(o,g):
    start_time=time.time()
    for list_go in sample:
        if list_go[0]=='observed':
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
    print("--- %s seconds ---" % (time.time()-start_time))
    return o,g

observations,goals=format_data(observations,goals)
print(observations)
print(goals)