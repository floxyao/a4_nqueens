#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 18:27:41 2019

@author: flo
"""
import numpy as np
import random

#class Map:
#    def __init__(self, width, height):     
#        self.dirty = [[random.randint(0, 1) for i in range(width)] for j in range(height)] #nested loop
#        
#    def show(self):
#        print(np.matrix(self.dirty))

class solveQueens:
    def __init__(self, _numQueens, _numStates):
        self.numQueens = _numQueens
        self.numStates = _numStates
        self.board = []
        for i in range(self.numQueens):
            self.board.append([None] * self.numQueens)
            #print(i, self.board[i])
            #print(self.board[i])
            #self.board[i][j] = elt
        
    def show(self, positions):
        i = 0
        for array in self.board:
            elt = positions[i]
            i += 1
            array[elt] = elt
            print(array)
            
            
    def fitnessFunction(self, positions):
        qpos = [] #array of queen positions
        pairs = 0
        
        for i in range(len(positions)):
            x = i
            y = positions[i]
            qpos.append((x,y))
        print(qpos)
        
        k=len(positions)-1
        for i in range(len(qpos)):
            #print ("i",i)
            queen1 = (qpos[i][0],qpos[i][1])
            print(queen1)
            for j in range(k):
                j += i+1
                #print("j: ",j)
                queen2 = (qpos[j][0],qpos[j][1])
                print(queen2)
                if(self.collision(queen1,queen2)):
                    print("colliding pairs: ",queen1,queen2)
                else:
                    pairs += 1;
            if(i==(len(positions)-1)): break
            k -= 1
        
        return pairs
    
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
    q = solveQueens(4,0)
    
    pos = []
    for i in range(4):
        pos.append(random.randint(0, 3))
        print(pos[i])
    
    print("\n")
        
    q.show(pos)    
    fitness = q.fitnessFunction(pos)
    print(fitness)
#    q.placeQueens()

    