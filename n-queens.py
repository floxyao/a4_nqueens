#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 18:27:41 2019

@author: flo
"""

import random
import math
from random import randint
from random import randrange
import numpy


class solveQueens:
    def __init__(self, _numQueens, _numStates):
        self.numQueens = _numQueens
        self.numStates = _numStates
        
        self.board = []
        #init queens with position
        for i in range(self.numQueens):
            self.board.append([None] * self.numQueens)
            #print(i, self.board[i])
            #print(self.board[i])
            #self.board[i][j] = elt
            
        self.population = [[]]
        for i in range(self.numStates):
            for j in range(self.numQueens):
                self.population[i].append(random.randint(0, self.numQueens))
            if i != self.numStates-1:
                self.population.append([])
        print(self.population)

        

#        for array in self.population:
#            print(array, end=' ')
    #===================================================
    #prints board
    # *CURRENTLY NOT IN THE RIGHT FORMAT*
    #===================================================
    def show(self, positions):
        i = 0
        for array in self.board:
            elt = positions[i]
            i += 1
            array[elt] = elt
            print(array)
            
    #===================================================
    #returns fitness of an individual
    #inputs: array of integers (position of each queen)
    #===================================================
    def fitnessFunction(self, positions):
        qpos = [] #array of queen positions
        pairs = 0
        
        #insert all positions in (x,y) form in an array "qpos" 
        for i in range(len(positions)):
            x = i
            y = positions[i]
            qpos.append((x,y))
        #print('qpos: ',qpos)
        
        #compare each pair with each other for collisions
        k=len(positions)-1
        for i in range(len(qpos)):
            #print ("i",i)
            queen1 = (qpos[i][0] , qpos[i][1])
            #print(queen1)
            for j in range(k):
                j += i+1
                #print("j: ",j)
                queen2 = (qpos[j][0] , qpos[j][1])
                #print(queen2)
                if(self.collision(queen1,queen2) == False):
                    pairs += 1
            if(i==(len(positions)-1)): break
            k -= 1
        
        return pairs
        
    def geneticAlgorithm(self):
        goal = self.nCr(self.numQueens, 2)
        fitPercents = []
        allScores = []
        indexes = []
        #while(True)
        #calculate sum of all fitness scores
        for i in range(len(self.population)):
            allScores.append(self.fitnessFunction(self.population[i]))
       
        print('allScores: ',allScores)
        total = sum(allScores)
       
        #insert list of tuples of (fitness percentage and individual)
        for j in range(len(self.population)):
            fitScore = allScores[j] 
            fitPercents.append(((fitScore / total) , self.population[j]))
            indexes.append(i)
            
        # call selection()
        choice = self.selection(fitPercents, indexes)

        # crossover the pairs from top to bottom, if states are odd then just copy last parent to child
        for i in range(0, len(self.population)-1, 2):
            self.crossover(self.population[choice[i]], self.population[choice[i + 1]])  # even num of parents
            if range(len(self.population) % 2 == 1): # odd num of parents
                self.population[len(self.population)-1] = self.population[len(self.population)-1]
        print("children after crossover: ", self.population)

        # probability to run mutation is 1%
        mutation_probability = 1/100.
        for i in range(len(self.population)-1):
            if random.random() < mutation_probability:
                self.mutation(self.population[i])
        print("children after mutations: ", self.population)
            
    # ======================================================
    # selects states based on probability
    # returns a state
    # input(s): list of tuple(fitScore, state)
    # ======================================================
    def selection(self, fitPercents, indexes):
        choice = []
        percents = [x[0] for x in fitPercents]
        #print(percents)
        # selection of pairs based on probability, has duplicate pairs
        choice = numpy.random.choice(indexes, len(self.population), replace=True, p=percents)
        #print("choice list of indexes based on prob: ", choice)
        return choice
        
    # ======================================================
    # crossover's two integer arrays
    # returns both arrays after crossovers
    # input(s): 2 arrays of integers
    # ======================================================
    def crossover(self, positions, positions2):
        crosspoint = random.choice(positions)
        positions2[crosspoint:], positions[crosspoint:] = positions[crosspoint:], positions2[crosspoint:]
        print("---crossover--- ")
        print("\t1st array: ", positions)
        print("\t2nd array: ", positions2)
        print("--------------- ")
        return positions, positions2

    # ======================================================
    # randomly chooses an index in the array and changes
    # its value with any number from 1-N
    # returns the new array
    # input(s): 2 arrays of integers
    # ======================================================
    def mutation(self, positions):
        print("---mutation---")
        print("\tarray:\t\t\t", positions)
        rand_index = randrange(len(positions))
        element = randint(0, self.numQueens) # may choose the same value to replace
        positions[rand_index] = element
        print("\tmutated array:  ", positions)
        print("--------------- ")
        return positions
            
    # ======================================================
    # calculates the combination formula
    # ======================================================
    def nCr(self, n,r):
        f = math.factorial
        return int(f(n) / f(r) / f(n-r))
        
    #===================================================
    #detects horizontal/vertical/diagonal alignment
    #input(s): a position (x,y)
    #===================================================
    def collision(self, q1, q2):
        return (abs(q2[0]-q1[0]) == abs(q2[1]-q1[1])) or (q1[0] == q2[0]) or (q1[1] == q2[1])

    
if __name__ == '__main__':
    print("\n")
    q = solveQueens(4,4)
    
    pos = q.geneticAlgorithm();
        
    #q.show(pos)    


    