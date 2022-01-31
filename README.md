# A basic restaurant domain 
*This Git repository is meant to depict a simple restaurant domain for a reasoning agent to reason on. The rules in place are quite straigthforward - and based on real-world restaurants, with a few simplifications along the way.*
## Files to consider
The readed should only take into account the **restaurant_basic_v3.sparc** file aswell as the associated action language file **AL_v3.txt**. Other files are either test files or outdated files that were inconsistent. Those files are meant to work within [this context](https://github.com/ArthurFDLR/Robotics_Vision_Simulator). The goal of the whole project is to link observations made in a simulated world with a knowledge base that is meant to reason on. The reasoning agent using the knowledge base coded there in **Answer Set Programming (ASP - SPARC)** (see [here](https://github.com/iensen/sparc)) should thus be able to be "commanded" by simple hand signs (*e.g a raise of the hand means a customer wants his bill*). The ultimate aim is to render the reasoning agent completely autonomous in a restaurant where he is not the sole employee and has to manage unpredictable behavior.
## Current capabilities
The current state of the domain integrates 4 actions that a capable reasoning agent (referred to as "agent") can perform in a really simple restaurant context (2 tables - one with a capacity of 2 and the other of 4, 2 customers, a ghost waiter and the reasoning agent). The number of tables can be increased to 3 max. in the current configuration (adding more tables would require the user to change the node layout of the restaurant in the ASP file). The number of customers can be changed to any integer. Same goes for the number of waiters (as they do nothing in this configuration, and are not even declared as occupying a node in the restaurant). There can only be one reasoning agent. 
Aforementioned actions are:
- Picking up a (group of) customer(s) Cu : pick(agent, Cu)
- Seating a (group of) customer(s) at table T : seat(agent, Cu, T)
- Bringing the bill to table T : give_bill(agent, T)
- Moving around in the restaurant : go_to(agent, N)
Certain actions (in italic) are triggered by **observations made in a world simulated on PyBullet**. The list of actions triggered by observations may grow bigger.
*More details on how groups of customers are managed in the AL_v3.txt file, and in the comments in the restaurant_basic_v3.sparc file*
## Inputs/Outputs of the restaurant domain restaurant_basic.v3 file 
*Note that the file does not take any input in the sense commonly used - I use "input" to refer to the goals/observations that can be updated using [this communication script](https://github.com/ArthurFDLR/Commonsense-Reasoning-Bot/blob/master/commonsense_reasoning_bot/ASP/CommunicationASP.py). The outputs of the SPARC script (i.e the answer sets) cannot be used as is either. For testing, I used the [output_reorderer2.py](https://github.com/niwya/restaurant_ASP_SPARC/blob/master/output_reorderer2.py) file to properly chose what is to be displayed from the answer sets. In practise, the answer sets will be formatted using the communication script mentioned above.*
The currently supported observations are:
- Observing that a (group of) customer(s) Cu has entered the restaurant : has_entered(Cu). This leads the reasoning agent to go pick up the customer(s) at the entrance of the restaurant, and bring them to a table that accomodate their needs. If there is no such table, the simulation crashes (no handling of exceptions as of now). This behaviour should be changed to either set the state of the (group of) customer(s) as "pending_table" or as "has_left". More informations on states (called fluents) in the restaurant_basic_v3.sparc file.
- Observing that a (group of) customer(s) seated at table T wants the bill : bill_wave(T). This leads to the reasoning agent bringing the bill to table T, and the knowledge base automatically assumes that all clients at table T have paid the bill once it has been brought. This behaviour will be subject to change.

Note: groups need to be manually declared by the user.


