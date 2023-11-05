# Overview
An introduction course to the basic principles and tools of artificial intelligence. Problem solving methods and knowledge representation techniques.

## Assignment 1
### Introduction
There are two parts to this assignment.
- Propagators. You will implement two constraint propagators—a Forward Checking constraint propagator, and a Generalized Arc Consistency (GAC) constraint propagator—and two heuristics— Minimum-Remaining-Value (MRV) and Degree (DH).
- Models. You will implement three different CSP models: two grid-only Cagey models, and one full Cagey puzzle model (adding cage constraints to grid).
### File Supplied by Prof. Christian Muise
- cspbase.py. Class definitions for the python objects Constraint, Variable, and BT.
- propagators.py. Starter code for the implementation of your two propagators. You will modify this file with the addition of two new procedures prop FC and prop GAC.
- heuristics.py. Starter code for the implementation of the variable ordering heuristics, MRV and DH. You will modify this file with the addition of the new procedures ord mrv and ord dh.
- cagey csp.py. Starter code for the CSP models. You will modify three procedures in this file: binary ne grid, nary ad grid, and cagey csp model.
- tests.py. Sample test cases. Run the tests with “python3 tests.py”.
- csp sample run.py. Example CSP problems to demonstrate usage of the API.
### Team members
Irving Wu

## Assignment 2
### Introduction
This assignment is intended to gauge your understanding of planning and the PDDL modeling system. Your goal will be to implement a domain in PDDL as well as several problems that fall in that domain. You will be given a zip folder, pddl_template.zip, containing a template file for the domain as well as template files for the problems you are expected to implement.
### Domain Description – The Treasure Hunter
A treasure hunter just walked into a dungeon with a priceless treasure waiting to be found! Looking around, they gather the following easily apparent facts about the dungeon:
- The dungeon contains rooms that are connected to corridors allowing the hero to move around.
- The hero moves through the corridors but is only ever at a single room.
- Some of the corridors are risky.
- There are locked corridors with coloured locks.
- Each room can be empty or have any number of keys in it.
- The hero can hold a single key.
- There are two-use keys and one-use keys that are limited in use, and multi-use keys can be used infinitely many times.
- One of the rooms is the goal with (containing treasure!).

The hero is lucky to have so much information about this dungeon! But they are not that lucky. The corridors can collapse, the keys are scattered, and it’s not so easy to figure out a path through the dungeon. Nonetheless, there’s treasure at the end!! The hero can perform any of the following actions:
- The hero can move to an adjacent room (connected to a common corridor as the current room) as long as the corridor is not locked and is not collapsed. The corridors with a red lock are risky and will collapse once passed (i.e., can only be passed once).
- When holding the correctly coloured key, the hero can unlock a corridor it is adjacent to (i.e., to open a blue lock, the hero must be holding the blue key).
  - 1-use keys can only be used once.
  - 2-use keys can only be used twice.
  - Multi-use keys can be used any number of times.
  - “Used up” keys do not disappear, but rather remain with the hero.
- The hero can pickup a key in their current room and they aren’t already holding a key.
- The hero can drop a key they are holding, and it will then be in the current room.
Important: please read and reread the above until you understand it completely. Failing to understand the domain will significantly hamper your ability to succeed on this assignment!
### Team members
Irving Wu, Baorong Wei

## Assignment 3
### Introduction
Pacman spends his life running from ghosts, but things were not always so. Legend has it that many years ago, Pacman’s great grandfather, Grandpac, learned to hunt ghosts for sport. However, he was blinded by his power and could only track ghosts by their banging and clanging. In this project, you will design Pacman agents that use sensors to locate and eat invisible ghosts. You’ll advance from locating single, stationary ghosts to hunting packs of multiple moving ghosts with ruthless efficiency.
### File Provided by Prof. Christian Muise
- inference.py: Code for tracking ghosts over time using their sounds. You may refer to this file to assist your implementations in solutions.py.
- busters.py: The main entry to Ghostbusters (replacing Pacman.py).
- bustersGhostAgents.py: New ghost agents for Ghostbusters.
- distanceCalculator.py: Computes maze distances.
- game.py: Inner workings and helper classes for Pacman.
- ghostAgents.py: Agents to control ghosts.
- graphicsDisplay.py: Graphics for Pacman.
- graphicsUtils.py: Support for Pacman graphics.
- keyboardAgents.py:Keyboard interfaces to control Pacman.
- layout.py: Code for reading layout files and storing their contents.
- util.py: Utility functions.
### File Modified by Team Members
- bustersAgents.py: Agents for playing the Ghostbusters variant of Pacman.
- solutions.py: Code to implement the functionalities of inference.py which track ghosts over time using their sounds.
### Team members
Irving Wu, Baorong Wei
