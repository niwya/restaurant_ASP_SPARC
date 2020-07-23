import time
## Testing how to format the observations/goals to update the SPARC file ## 
sample=[['observed', 'bill_wave(c1)', 'true', '2'], ['goal', '3', 'isonchair(c1,chair2t1)'],]
print(sample)
goals='%b_goal\n'
observations='%b_obs\n'

def format_data(o,g):
    start_time=time.time()
    for list in sample:
        if list[0]=='observed':
            # Observations are pretty straightforward, as the first item in list will be the 'observed' indicator, and the
            # following will be the fluent, then if has been seen as true or false then the step at which it occured.
            o+=list[0]+'('+list[1]+','+list[2]+','+list[3]+').\n'
        elif list[0]=='goal': print('You have a new goal')
            # Goals are less straightforward, as they can be constitued of multiple fluents. The first item in the list
            # is the goal indicator, then the step at which the goal is wanted to be archieved. Then comes the fluents
            # themselves.
        else: print("Unauthorized format")
    o+='%e_obs\n'
    g+='%e_goal\n'
    print("--- %s seconds ---" % (time.time()-start_time))
    return o,g

observations,goals=format_data(observations,goals)
print(observations)
print(goals)