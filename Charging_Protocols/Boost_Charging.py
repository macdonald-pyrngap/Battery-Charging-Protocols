import pybamm
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

model=pybamm.lithium_ion.SPMe() 
param=pybamm.ParameterValues("Chen2020")

experiment=pybamm.Experiment([
    "Charge at 1 A until 4 V",
    "Charge at 0.5 A until 4.2 V",
    "Hold at 4.2 V until C/20",
])

sim=pybamm.Simulation(model, experiment=experiment)
solution=sim.solve()

time=solution["Time [s]"].entries
voltage=solution["Terminal voltage [V]"].entries
current=solution["Current [A]"].entries

plt.figure(figsize=(15,5))

# Voltage
plt.subplot(2,1,1)
plt.plot(time, voltage, 'r')
plt.xticks(np.arange(0, max(time), 500))
plt.xlabel("Time [s]")
plt.ylabel("Voltage [V]")
plt.title("Terminal voltage")

# Current
plt.subplot(2,1,2)
plt.plot(time, -current, 'r')
plt.xticks(np.arange(0, max(time), 500))
plt.xlabel("Time [s]")
plt.ylabel("Current [A]")
plt.title("Current")

plt.tight_layout()
plt.show()

