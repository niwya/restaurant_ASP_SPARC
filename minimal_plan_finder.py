import subprocess, fileinput, re
filepath = "restaurant_basic_test.sparc"
command = "java -jar sparc.jar restaurant_basic_test.sparc -A -n 1"
curly_brack=r"\{(.*?)\}"

# This script is meant to find the minimal plan provided a supposedly non
# inconsistent program in ASP-SPARC 

def edit_n(file, n:int):
    '''Same function as writeStepLimit in CommunicationASP.py '''
    for line in fileinput.FileInput(filepath,inplace=1):
        if "#const nstep =" in line:
            line=line.replace(line, "#const nstep = {}.\n".format(n))
        print(line,end='')

def find_minplan(file):
    # First we update the initial n to zero
    n = 0
    edit_n(filepath, n)
    # Then we can start iterating until we get an answer set 
    output = str(subprocess.check_output(command))
    output_list = re.findall(curly_brack, output)
    while  output_list == []:
        n += 1
        output = str(subprocess.check_output(command))
        output_list = re.findall(curly_brack, output)
        edit_n(filepath, n)

find_minplan(filepath)