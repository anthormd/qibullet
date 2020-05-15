#!/usr/bin/env python
# coding: utf-8

import pybullet
import pybullet_data
from qibullet import PepperVirtual
from qibullet import SimulationManager

def main():
    simulation_manager = SimulationManager()
    client = simulation_manager.launchSimulation(gui=True)
    pepper = simulation_manager.spawnPepper(client, spawn_ground_plane=True)
    texte = "Salut les amis"
    pepper.speak(texte)
    
    
    
if __name__ == "__main__":
    main()
