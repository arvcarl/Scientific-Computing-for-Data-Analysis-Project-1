# Scientific Computing for Data Analysis - Project 1
Code for project 1 in Scientific Computing for Data Analysis: "Pollutant dispersion: deterministic and stochastic models"  

## Overview
The aim of the project is to write a Python program to simulate Brownian motion of particles using stochastic models. From a deterministic partial differential equation of motion, a numerical stochastic method is used to simulate individual particles. 


## Tasks
The main task in this project is to use the Euler-Maruyama method to simulate stochastic particles. This is used for plotting particle clouds and for estimation of pollutant concentrations via use of Monte Carlo methods, and is done both with all particles released at once and with constant source of particles. 

## Running the simulations
No extra files besides `project.py` are needed to run the simulations. The program has four main functions
- `Euler_Maruyama`    - Simulates N particles 
- `particle_cloud`    - Generates four scatter plots of particle positions
- `concentration`     - Generates estimation of concentration of particles using Monte Carlo simulation
- `source_simulation` - Simulates a constant particle source and generates scatter plots and concentration estimation


See setup for setup
