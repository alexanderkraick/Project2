import DefensePaths as DefensePaths
import SpaceJamclasses as SpaceJamclasses
from direct.showbase.ShowBase import ShowBase
from panda3d.core import *

class SpaceJam(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.SetScene()
        fullCycle = 60
        for j in range(fullCycle):
            SpaceJamclasses.Drone.droneCount += 1
            nickname = "Drone" + str(SpaceJamclasses.Drone.droneCount)
            self.DrawCloudDefense(self.planet1, nickname)
        
    def DrawCloudDefense(self, centralObject, droneName):
        unitVec = DefensePaths.Cloud()
        unitVec.normalize()
        position = unitVec * 5000 + centralObject.modelNode.getPos()
        SpaceJamclasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", position, 5)
        
    def DrawBaseballSeams(self, centralObject, droneName, step, numSeams, radius = 1):
        unitVec = DefensePaths.BaseballSeams(step, numSeams, B = 0.4)
        unitVec.normalize()
        position = unitVec* radius * 250 + centralObject.modelNode.getPos()
        SpaceJamclasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", position, 5)
        
        self.Universe = SpaceJamclasses.Universe(self.loader, "./Assets/Universe/Universe.x", self.render, 'Universe', "./Assets/Universe/Universe.jpg", (0, 0, 0), 10000)
        self.Planet1 = SpaceJamclasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet1', "./Assets/Planets/Earth.jpg", (-6000, -3000, -800), 250)
        self.Planet2 = SpaceJamclasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet2', "./Assets/Planets/Jupiter.jpg", (0, 6000, 0), 300)
        self.Planet3 = SpaceJamclasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet3', "./Assets/Planets/Mars.jpg", (500, -5000, 200), 500)
        self.Planet4 = SpaceJamclasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet4', "./Assets/Planets/Moon.jpg", (300, 6000, 500), 150)
        self.Planet5 = SpaceJamclasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet5', "./Assets/Planets/Pluto.jpg", (700, -2000, 100), 500)
        self.Planet6 = SpaceJamclasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, 'Planet6', "./Assets/Planets/Venus.jpg", (0, -900, -1400), 700)
        self.SpaceStation1 = SpaceJamclasses.SpaceStation(self.loader, "./Assets/Space_Station/spaceStation.x", self.render, 'Space Station', "./Assets/Space_Station/SpaceStation1_Dif2.png", (1500, 1000, -100), 40)
        self.Hero = SpaceJamclasses.Spaceship(self.loader, "./Assets/Spaceship/theBorg.x", self.render, 'Hero', "./Assets/Spaceship/theBorg.jpg", (1000, 1200, -50), 50)
    
app = SpaceJam()
app.run()