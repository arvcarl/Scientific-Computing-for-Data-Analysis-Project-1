# Scientific Computing for Data Analysis - Project 1
Code for project 1 in Scientific Computing for Data Analysis: "Pollutant dispersion: deterministic and stochastic models"  

## Overview
The aim of the project is to write a Python program to simulate Brownian motion of particles in two dimensions using stochastic models and methods. From a deterministic partial differential equation of motion, a numerical stochastic method is used to simulate individual particles. 


## Tasks
The main task in this project is to use the Euler-Maruyama method to simulate stochastic particles. This is used for plotting particle clouds and for estimation of pollutant concentrations via use of Monte Carlo methods, and is done both with all particles released at once and with constant source of particles.   

## Running the simulations
No extra files besides `project.py` and Python libraries `NumPy` and `Matplotlib`are needed to run the simulations. More information about simulations parameters and prepared function calls are in the bottom of the program.  

The program has four main functions used for different simulations and plots:
- `Euler_Maruyama`    - Simulates N particles and returns an array of their positions over time
- `particle_cloud`    - Generates four scatter plots of particle positions at chosen times
- `concentration`     - Generates estimation of concentration of particles using Monte Carlo simulation
- `source_simulation` - Simulates a constant particle source and generates scatter plots and concentration estimation


See setup for setup  
  
Uppsala  
April 2026