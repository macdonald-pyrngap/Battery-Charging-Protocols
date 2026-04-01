import pybamm
import numpy as np 
import matplotlib.pyplot as plt 

model = pybamm.lithium_ion.SPMe()
param = pybamm.ParameterValues("Chen2020")

experiment = pybamm.Experiment([
    "Discharge at 5 A for 60 minutes",
    "Charge at 5 A until 4.2 V",
    "Hold at 4.2 V until 0.05 A",
])

sim = pybamm.Simulation(model, 
        parameter_values=param,
         experiment=experiment)
solution = sim.solve()

time = solution["Time [s]"].entries
voltage = solution["Terminal voltage [V]"].entries
current = solution["Current [A]"].entries

plt.figure(figsize=(12,5))

plt.subplot(2,1,1)
plt.plot(time, voltage, 'r')
plt.xlabel("Time [s]")
plt.ylabel("Voltage [V]")
plt.title("Terminal Voltage")

plt.subplot(2,1,2)
plt.plot(time, -current, 'r')
plt.xlabel("Time [s]")
plt.ylabel("Current [A]")
plt.title("Current")

plt.tight_layout()
plt.show()

