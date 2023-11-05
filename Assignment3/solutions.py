# solutions.py
# ------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

'''Implement the methods from the classes in inference.py here'''

import util
from util import raiseNotDefined
import random
import busters
import inference

def normalize(self):
    """
    Normalize the distribution such that the total value of all keys sums
    to 1. The ratio of values for all keys will remain the same. In the case
    where the total value of the distribution is 0, do nothing.

    >>> dist = DiscreteDistribution()
    >>> dist['a'] = 1
    >>> dist['b'] = 2
    >>> dist['c'] = 2
    >>> dist['d'] = 0
    >>> dist.normalize()
    >>> list(sorted(dist.items()))
    [('a', 0.2), ('b', 0.4), ('c', 0.4), ('d', 0.0)]
    >>> dist['e'] = 4
    >>> list(sorted(dist.items()))
    [('a', 0.2), ('b', 0.4), ('c', 0.4), ('d', 0.0), ('e', 4)]
    >>> empty = DiscreteDistribution()
    >>> empty.normalize()
    >>> empty
    {}
    """
    "*** YOUR CODE HERE ***"
    # use the total method to find the sum of the values in the distribution
    total = self.total()

    # only normalize the values in the distribution if the total value of the distribution is not 0
    if total != 0:
        for key, value in self.items():
            self[key] = value / total
            
            

def sample(self):
    """
    Draw a random sample from the distribution and return the key, weighted
    by the values associated with each key.

    >>> dist = DiscreteDistribution()
    >>> dist['a'] = 1
    >>> dist['b'] = 2
    >>> dist['c'] = 2
    >>> dist['d'] = 0
    >>> N = 100000.0
    >>> samples = [dist.sample() for _ in range(int(N))]
    >>> round(samples.count('a') * 1.0/N, 1)  # proportion of 'a'
    0.2
    >>> round(samples.count('b') * 1.0/N, 1)
    0.4
    >>> round(samples.count('c') * 1.0/N, 1)
    0.4
    >>> round(samples.count('d') * 1.0/N, 1)
    0.0
    """
    "*** YOUR CODE HERE ***"
    total = self.total()
    random1 = random.random()
    
    # indicate the lower bound of the distribution
    limit = 0
    
    for key, value in self.items():
        # when the random number falls within the distribution, the corresponding key is returned
        if random1 < (limit + value / total):
            return key
        # update the lower bound for the next distribution
        limit += value / total
    



def getObservationProb(self, noisyDistance, pacmanPosition, ghostPosition, jailPosition):
    """
    Return the probability P(noisyDistance | pacmanPosition, ghostPosition).
    """
    "*** YOUR CODE HERE ***"
    # solve the situation when the ghost is in jail
    if ghostPosition == jailPosition:
        # noisyDistance==None
        if noisyDistance == None:
            return 1
        # noisyDistance is not None
        else:
            return 0
    # solve the situation when the ghost is not in jail
    else:
        # noisyDistance==None
        if noisyDistance == None:
            return 0
        # noisyDistance is not None
        else:
            manhattanD = util.manhattanDistance(ghostPosition, pacmanPosition)
            ObservationProb = busters.getObservationProbability(noisyDistance, manhattanD)
            return ObservationProb
        



def observeUpdate(self, observation, gameState):
    """
    Update beliefs based on the distance observation and Pacman's position.

    The observation is the noisy Manhattan distance to the ghost you are
    tracking.

    self.allPositions is a list of the possible ghost positions, including
    the jail position. You should only consider positions that are in
    self.allPositions.

    The update model is not entirely stationary: it may depend on Pacman's
    current position. However, this is not a problem, as Pacman's current
    position is known.
    """
    "*** YOUR CODE HERE ***"
  
    # obtain the Pacman's position and the jail position for later iteration
    pacmanPosition = gameState.getPacmanPosition()
    jailPosition = self.getJailPosition()
    
    # iterate the updates over the variables in self.allPositions
    for ghostPosition in self.allPositions:
        # the probability of an observation given Pacman’s position, a potential ghost position, and the jail position
        probability = self.getObservationProb(observation, pacmanPosition, ghostPosition, jailPosition)
        self.beliefs[ghostPosition] *= probability
    
    self.beliefs.normalize()


def elapseTime(self, gameState):
    """
    Predict beliefs in response to a time step passing from the current
    state.

    The transition model is not entirely stationary: it may depend on
    Pacman's current position. However, this is not a problem, as Pacman's
    current position is known.
    """
    "*** YOUR CODE HERE ***"
    # get the original beliefs first
    oldBelief = self.beliefs

    # establish a new DiscreteDistribution object to store the new beliefs
    newBelief = inference.DiscreteDistribution()
    
    # obtain the distribution over new positions for the ghost
    for oldPos in self.allPositions:
        newPosDist = self.getPositionDistribution(gameState, oldPos)
        # accumulate the probability of getting from oldPos to newPos into the new beliefs
        for newPos in self.allPositions:
            # the probability of getting from oldPos to newPos might be 0, don't include it
            if newPosDist[newPos] > 0:
                newBelief[newPos] += newPosDist[newPos] * oldBelief[oldPos]

    self.beliefs = newBelief
    self.beliefs.normalize()
    
    # raiseNotDefined()
