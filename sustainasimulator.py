#HooHacks 2021 Submission
#Title: Sustainasimulator
#Authors: Victor Lin, Adam Surrey, Anna Cummins, Daniel Campbell
import random

bPopulaton = input("Population: ")
youthMortality = input("Percentage of death among youth: ")
agriculture = input("The amount of agriculture: ")
virusRate = input("Rate at which the virus spreads: ")
fertxy = input("Mininum age of fertility: ")
fertyy = input("Maximum age of fertility: ")
food = input("Amount of food: ")
popArray = []

class Human:
    def _init_(self, age):
        self.gender = random.randint(0,1) 
        self.age = age
        self.pregnant = 0

def getFood(food,agriculture):
    farmers = 0
    for human in popArray:
        if human.age > 15:
            farmers += 1
    food += farmers * agriculture
        
    if food < len(popArray):
       	del popArray[0:int(len(popArray)-food)] 
       	food = 0
    else:
        food -= len(popArray)
                
        def reproduction(fertxy, fertyy, youthMortality):
            for human in popArray:
                if human.gender == 1:
                    if human.age > fertxy:
                        if human.age < fertyy:
                            if random.randint(0, 6) == 1:
                                if random.randint(0, 100) > youthMortality:
                                    popArray.append(Human(0))
                           
        def startSim():
            for x in range(bPopulation):
                popArray.append(Human(random.randint(17,50)))
                
        def year(food, agriculture, fertxy, fertyy, youthMortality, virusRate):
                getFood(food, agriculture)
                for human in popArray:
                    if human.age > 75:
                        popArray.remove(human)
                else:
                    human.age += 1
                    reproduction(fertxy, fertyy, youthMortality)
                    if random.randint(0,100) < virusRate:
                        del popArray[0:int(random.uniform(0.05,0.2)*len(popArray))]
                    print(len(popArray))
                    youthMortality *= 0.9
                    return youthMortality
           
        startSim()
        while len(popArray) < 100000000 and len(popArray) > 1:
            youthMortality = year(food, agriculture, fertxy, fertyy, youthMortality, virusRate)
                    
     
