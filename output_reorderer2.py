1#import re
#s="(hello) {man} ily"
#l = re.findall(k, s)
#print(l)

import subprocess, shlex, re
curly_brack='\{(.*?)\}'
#command= 'java -jar sparc.jar restaurant_basic.sparc'
command= 'java -jar sparc.jar restaurant_test2.sparc'
#command='java -jar sparc.jar test_newseat.sparc'
n=int(input('How many answer sets?\n'))
command+=' -A -n ' + str(n)


## Running the command line                                    ##
args=shlex.split(command)
## Retrieving the output                                       ##
output=subprocess.check_output(args)
output=str(output)
## Splitting the output according to the different answer sets ##
## Each sub-list corresponds to one answer set                 ##
output_list=re.findall(curly_brack,output)
output_list2=[0]*n
output_list3=[[]]*n
exceptional_values=[[]]*n
normal_values=[[]]*n

for i in range(len(output_list)):
    output_list2[i]=output_list[i].split(' ')

try:
    for i in range(len(output_list2)):
        for j in output_list2[i]:
            if j[-1]==',' : j=j[:-1]
            output_list3[i].append(j) 

## Sorting chronologically                                     ##
    for i in range(n):
        for j in range(len(output_list3[i])):
            if ("occurs" in output_list3[i][j] or "holds" in output_list3[i][j] or "observed" in output_list3[i][j]): normal_values[i].append(output_list3[i][j])
            else: exceptional_values[i].append(output_list3[i][j])
    for i in range(n):
        for j in range(len(normal_values[i])):
            normal_values[i].sort(key = lambda x:int(x.split(',')[-1].split(')')[0]))


## Printing by keywords                                        ##
    keywords=input('Keywords, separated by a comma:\n')
    keywords=keywords.split(',')
    print("#############################")
    for i in range(n):
        ind=i+1
        print("Answer set number %d" % ind + ":")
        print("#############################\n")
        for k in keywords:
            if k!='':
                print("Keyword "  + k +":")
            else: print("No keyword given.") 
            for j in range(len(normal_values[i])):
                if k in normal_values[i][j]: print(normal_values[i][j])
            for j in range(len(exceptional_values[i])):
                if k in exceptional_values[i][j]: print(exceptional_values[i][j])
            print('\n')
        print("#############################")

except: print("The program is inconsistent.")