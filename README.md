# Overview
An introduction course to the basic principles and tools of artificial intelligence. Problem solving methods and knowledge representation techniques.

## Assignment 1
### Introduction
There are two parts to this assignment.
- Propagators. You will implement two constraint propagators—a Forward Checking constraint propagator, and a Generalized Arc Consistency (GAC) constraint propagator—and two heuristics— Minimum-Remaining-Value (MRV) and Degree (DH).
- Models. You will implement three different CSP models: two grid-only Cagey models, and one full Cagey puzzle model (adding cage constraints to grid).
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
### Team members
Irving Wu, Baorong Wei
