#import re
#s="(hello) {man} ily"
#l = re.findall(k, s)
#print(l)

import subprocess, shlex, re
curly_brack='\{(.*?)\}'
command='java -jar sparc.jar restaurant2.sparc -A -n '
command+=str(input('How many answer sets?\n'))

## Running the command line                                   ##
args=shlex.split(command)
## Retrieving the output                                       ##
output=subprocess.check_output(args)
output=str(output)
## Splitting the output according to the different answer sets ##
## Each sub-list corresponds to one answer set                 ##
output_list=re.findall(curly_brack,output)
output_list2=[0]*len(output_list)
output_list3=[[]]*len(output_list)

for i in range(len(output_list)):
    output_list2[i]=output_list[i].split(' ')

for i in range(len(output_list2)):
    for j in output_list2[i]:
        if j[-1]==',' : j=j[:-1]
        output_list3[i].append(j) 
print(output_list3)

## Sorting by keywords                                        ##
keywords=input('Keywords, separated by a comma:\n')
keywords=keywords.split(',')
print("#############################")
for i in range(len(output_list3)):
    ind=i+1
    print("Answer set number %d" % ind + ":")
    print("#############################\n")
    for k in keywords:
        print("Keyword "  + k +":")
        for j in range(len(output_list3[i])):
            if k in output_list3[i][j]: print(output_list3[i][j])
        print('\n')
    print("#############################")