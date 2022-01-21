# A basic restaurant domain 
*This Git repository is meant to depict a simple restaurant domain for a reasoning agent to reason on. The rules in place are quite straigthforward - and based on real-world restaurants, with a few simplifications along the way.*
## Files to consider
The readed should only take into account the **restaurant_basic_v2.sparc** file aswell as the associated action language file **AL_v2.txt**. Other files are either test files or outdated files that were inconsistent. Those files are meant to work within [this context](https://github.com/ArthurFDLR/Robotics_Vision_Simulator). The goal of the whole project is to link observations made in a simulated world with a knowledge base that is meant to reason on. The reasoning agent using the knowledge base coded there in **Answer Set Programming (ASP - SPARC)** (see [here](https://github.com/iensen/sparc)) should thus be able to be "commanded" by simple hand signs (*e.g a raise of the hand means a customer wants his bill*). The ultimate aim is to render the reasoning agent completely autonomous in a restaurant where he is not the sole employee and has to manage unpredictable behavior.
## Current capabilities
The current state of the domain integrates 4 actions that a capable reasoning agent (referred to as "agent") can perform in a really simple restaurant context (2 tables with a 2-person capacity each, 2 customers, a ghost waiter and a reasoning agent). Said actions are:
- Picking up a (group of) customer(s) Cu : pick(agent, Cu)
- Seating a (group of) customer(s) at table T : seat(agent, Cu, T)
- *Bringing the bill to table T* : give_bill(agent, T)
- Moving around in the restaurant : go_to(agent, N)
Certain actions (in italic) are triggered by **observations made in a world simulated on PyBullet**. The list of actions triggered by observations may grow bigger.
*More details on how groups of customers are managed in the AL_v2.txt file, and in the comments in the restaurant_basic_v2.sparc file*
## Inputs/Outputs of the restaurant domain restaurant_basic.v2 file 
*Note that the file does not take any input in the sense commonly used - I use "input" to refer to the goals/observations that can be updated using [this communication script](https://github.com/ArthurFDLR/Commonsense-Reasoning-Bot/blob/master/commonsense_reasoning_bot/ASP/CommunicationASP.py). The outputs of the SPARC script (i.e the answer sets) cannot be used as is either. For testing, I used the [output_reorderer2.py](https://github.com/niwya/restaurant_ASP_SPARC/blob/master/output_reorderer2.py) file to properly chose what is to be displayed from the answer sets. In practise, the answer sets will be formatted using the communication script mentioned above.*
The currently supported observations are:
- Observing that a customer Cu has entered the restaurant : has_entered(Cu)
- Observing that a (group of) customer(s) seated at table T wants the bill : bill_wave(T)


