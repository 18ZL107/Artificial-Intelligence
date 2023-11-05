# Overview
An introduction course to the basic principles and tools of artificial intelligence. Problem solving methods and knowledge representation techniques.

## Assignment1
### Introduction
There are two parts to this assignment.
- Propagators. You will implement two constraint propagators—a Forward Checking constraint propagator, and a Generalized Arc Consistency (GAC) constraint propagator—and two heuristics— Minimum-Remaining-Value (MRV) and Degree (DH).
- Models. You will implement three different CSP models: two grid-only Cagey models, and one full Cagey puzzle model (adding cage constraints to grid).
### What is supplied
- cspbase.py. Class definitions for the python objects Constraint, Variable, and BT.
- propagators.py. Starter code for the implementation of your two propagators. You will modify this file with the addition of two new procedures prop FC and prop GAC.
- heuristics.py. Starter code for the implementation of the variable ordering heuristics, MRV and DH.
### Modified file
- cagey csp.py. Starter code for the CSP models. You will modify three procedures in this file: binary ne grid, nary ad grid, and cagey csp model.
- tests.py. Sample test cases. Run the tests with “python3 tests.py”.
- csp sample run.py. Example CSP problems to demonstrate usage of the API.
### Team members
Irving Wu
