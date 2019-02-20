#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 18:27:41 2019

@author: flo
"""

import random
import math
import collections

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
                    pairs += 1;
            if(i==(len(positions)-1)): break
            k -= 1
        
        return pairs
    
    def geneticAlgorithm(self):
        goal = self.nCr(self.numQueens, 2)
        fitPercents = []
        allScores = []
        
        
        #while(True)
        
        
        #calculate sum of all fitness scores
        for i in range(len(self.population)):
            allScores.append(self.fitnessFunction(self.population[i]))
        
        print('allScores: ',allScores)
        total = sum(allScores)
        
        #insert list of tuples of (fitness percentage and individual)
        for j in range(len(self.population)):
            fitScore = allScores[j]
            
            fitPercents.append((round((fitScore / total),2) , self.population[j]))
            print(fitPercents[j])
        
        #x, y = cross_over

        #new_population = getNextPopulation();
        
        #self.population = new_population
        
        
    
        print("out of loop")
            
    def nCr(self, n,r):
        f = math.factorial
        return int(f(n) / f(r) / f(n-r))
        
    
    #===================================================
    #detects horizontal/vertical/diagonal alignment
    #input(s): a position (x,y)
    #===================================================
    def collision(self, q1, q2):
        return (abs(q2[0]-q1[0]) == abs(q2[1]-q1[1])) or (q1[0] == q2[0]) or (q1[1] == q2[1])
    
#    def collision(self, x1, y1, x2, y2):
#        print("x1 = ",x1)
#        print("y1 = ",y1)
#        print("x2 = ",x2)
#        print("y2 = ",y2)
#        print("x2-x1 = ",abs(x2-x1))
#        print("y2-y1 = ",abs(y2-y1))
#        return (abs(x2-x1) == abs(y2-y1)) or (x1 == x2) or (y1 == y2)
    
if __name__ == '__main__':
    print("\n")
    q = solveQueens(4,4)
    
#    population = q.getpopulation
    
    
#    pos = []
#    for i in range(4):
#        pos.append(random.randint(0, 3))
#        print(pos[i])
    
    #get population
    
    pos = q.geneticAlgorithm();
        
    #q.show(pos)    
    
    #fitness = q.fitnessFunction(pos)
    #print(fitness)
#    q.placeQueens()


    