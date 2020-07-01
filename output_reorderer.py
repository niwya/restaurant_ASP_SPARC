## Program to read output from SPARC file and reorganize it to make it more readable ## 
import subprocess, shlex

command='java -jar sparc.jar restaurant2.sparc -A'
args=shlex.split(command)

output=subprocess.check_output(args)
output=str(output)
output=output[3:-6]
output_list=output.split(' ')

final_output=[]
for i in output_list:
    if i[-1]==',' : i=i[:-1]
    final_output.append(i)  

# Sorting by keywords #
keywords=input('Keywords, separated by a comma:\n')
keywords=keywords.split(',')
dct={i:[] for i in keywords}
for i in dct:
    for j in range(len(final_output)):
        if i in final_output[j]: dct[i].append(final_output[j])

# Displaying it properly #
for i in dct:
    for j in dct[i]:
        print(j)