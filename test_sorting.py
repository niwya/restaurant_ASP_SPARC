import re

test_list=['occurs(isinroom(c1,mainroom),541)', 'holds(isinroom(c1,mainroom),61)', 'holds(isinroom(c1,mainroom),7)', 'holds(isattable(chair2t1,table1),4)']
test_list2=['c1,12)', 'c75,13)', 'c73,1)', 'c3,4)']

# does work but does take into account both the step nb and the intg in the customer/chairs etc defs
def sort_nicely( l ):
    """ Sort the given list in the way that humans expect.
    """
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    l.sort( key=alphanum_key )



def sort_nicely2( l ):
    def func(x):
        return x.split(',')[-1].split(')')[0]
    for i in range(len(l)-1):
        if func(l[i]) > func(l[i+1]):
            temp = l[i]
            l[i]=l[i+1]
            l[i+1]=temp


test_list.sort(key = lambda x:int(x.split(',')[-1].split(')')[0]))

print(test_list)
