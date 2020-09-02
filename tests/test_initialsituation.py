import re

outputList = ["goal(1)", "goal(7)", "goal(18)", "hello(j)"]
initList = ["holds(something(c1), 12)", "holds(otherthing(c2), 1)", "holds(test,1)", "-holds(test, 1)"]

goalList = []
stepList = []
initTransmit = []

for i in range(len(outputList)):
    if "goal" in outputList[i]: goalList.append(outputList[i])
if len(goalList)>0:
    for i in range(len(goalList)):
        stepList.append(int(re.findall('\((.*?)\)', goalList[i])[0]))
    stepList.sort()
for i in range(len(initList)):
        temp = initList[i]
        matches = re.finditer(r"(?:[^\,](?!(\,)))+$", temp)
        for matchNum, match in enumerate(matches, start = 1):
            if int(temp[match.start():match.end()-1]) == stepList[0]:
                initTransmit.append(temp)
print(initTransmit)