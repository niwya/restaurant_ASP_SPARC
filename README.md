# A basic restaurant domain 
*This Git repository is meant to depict a simple restaurant domain for a reasoning agent to reason on. The rules in place are quite straigthforward - and based on real-world restaurants, with a few simplifications along the way.*
## Files to consider
The readed should only take into account the **restaurant_basic_v2.sparc** file aswell as the associated action language file **AL_v2.txt**. Other files are either test files or outdated files that were inconsistent. Those files are meant to work within [this context](https://github.com/ArthurFDLR/Robotics_Vision_Simulator). The goal of the whole project is to link observations made in a simulated world with a knowledge base that is meant to reason on. The reasoning agent using the knowledge base coded there in **Answer Set Programming (ASP) - SPARC)** (see [here](https://github.com/iensen/sparc)) should thus be able to be "commanded" by simple hand signs (*e.g a raise of the hand means a customer wants his bill*). The ultimate aim is to render the reasoning agent completely autonomous in a restaurant where he is not the sole employee and has to manage unpredictable behavior.
## Current capabilities
The current state of the domain integrates 4 actions in a really simple restaurant context (2 tables with a 2-person capacity each, 2 customers, a ghost waiter and a reasoning agent). Said actions are:
- Picking up (a group of) customer(s)
- Seating (a group of) customer(s)
- *Bringing the bill to a table*
- Moving around in the restaurant
Certain actions (in italic) are triggered by **observations made in a world simulated on PyBullet**. The list of actions triggered by observations may grow bigger.

