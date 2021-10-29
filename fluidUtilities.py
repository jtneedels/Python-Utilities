# Fluid Utility Functions
# Jacob Needels
# Created: 9.3.2021

import numpy as np

global gamma
global R
gamma = 1.4
R = 287

def computeStagTemp(Ma, T):

	Tt = T * (1 + (gamma - 1)/2 * Ma ** (2)) 

	return Tt

def computeStagPress(Ma, P):

	Pt = P * (1 + (gamma - 1)/2 * Ma ** (2)) ** (gamma / (gamma - 1))

	return Pt

def computeStagDens(Ma, rho):

	rhot = rho * (1 + (gamma - 1)/2 * Ma ** (2)) ** (1 / (gamma - 1))

	return rhot

def computeSutherlandViscosityAir(T):
	# constants
	C1 = 1.458E-6 # kg/ms/sqrt(K)
	S = 110.4 # K

	mu = C1 * T ** (3/2) / (T + S)

	return mu

def computeReynoldsX(rho, u, x, mu):
	
	Rex = rho * u * x / mu

	return Rex

def machToVel(Ma, T):
	
	u = Ma * np.sqrt(gamma * R * T)

	return u