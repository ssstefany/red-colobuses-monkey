import random as rnd
import numpy as np
import math
from problem import Problem

class Monkey:
    def __init__(self):
        self.problem = Problem()
        self.weight = rnd.randint(4, 6)                 # aleatorio [4,6]
        self.body_power_PB = rnd.randint(-5,5)          # aleatorio [-5,5]
        self.combat_power_PA = rnd.random()             # aleatorio [0,1]  
        self.position = self.__init_factible_solution()

    # 0 -> 1 -> 3 -> 2 -> 0 ruta

    # vector de la ruta
    # [1,3,0,2]
    #  0 1 2 3

    def __init_factible_solution(self):
        position = [0] * self.problem.dimension
        next_index = 0

        route = list(range(self.problem.dimension))[1:]
        rnd.shuffle(route)
        route.append(0)

        for i in route:
            position[next_index] = i
            next_index = i

        return position

    def is_feasible(self):
        return self.problem.check(self.position)
    
    def is_better_than(self, other):
        return self.fitness() < other.fitness()
    
    def is_worse_than(self, other):
        return self.fitness() > other.fitness()

    def fitness(self):
        return self.problem.fit(self.position)
    
    # Operador de movimiento
    def move(self, leader_weight, best_position):


        # MOVIMIENTO MODIFICADO
        for j in range(self.problem.dimension):  
            self.body_power_PB =  self.combat_power_PA * self.body_power_PB * rnd.random() + (leader_weight - self.weight) * (best_position[j] - self.position[j]) * rnd.random()
            self.position[j] = self.position[j] + self.body_power_PB * rnd.random()
            self.combat_power_PA = self.combat_power_PA * rnd.random()
        
        # MOVIMIENTO ORIGINAL 
        # for j in range(self.problem.dimension):  
        #     self.body_power_PB =  (self.combat_power_PA * self.body_power_PB) + (leader_weight - self.weight) * (best_position[j] - self.position[j]) * rnd.random()
        #     self.position[j] = self.position[j] + self.body_power_PB 
        #     self.combat_power_PA = self.combat_power_PA * rnd.random()
        

        self.position = self.to_discretize(self.position)

    def to_discretize(self,vector):
        return (np.argsort(np.array(vector))).tolist()

    def __str__(self) -> str:
        return f"fit:{self.fitness()} x:{self.position}"

    def copy(self, a):
        self.position = a.position.copy()
        self.combat_power_PA = a.combat_power_PA
        self.body_power_PB = a.body_power_PB
        self.weight = a.weight

