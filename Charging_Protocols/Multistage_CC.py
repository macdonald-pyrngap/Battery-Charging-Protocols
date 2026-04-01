import pybamm
import numpy as np
import matplotlib.pyplot as plt

model=pybamm.lithium_ion.SPMe()

experiment=pybamm.Experiment([
    "Charge at 5 A until 4.2 V",
    "Charge at 4.5 A until 4.2 V",
    "Charge at 4 A until 4.2 V",
    "Charge at 3.5 A until 4.2 V",
    "Charge at 3 A until 4.2 V",
])

sim=pybamm.Simulation(model, experiment=experiment)
solution=sim.solve()

time=solution["Time [s]"].entries
voltage=solution["Terminal voltage [V]"].entries
current=solution["Current [A]"].entries

plt.figure(figsize=(12,5))

plt.subplot(2,1,1)
plt.plot(time, voltage, 'r')
plt.xticks(np.arange(0, max(time), 10))
plt.xlabel("Time [s]")
plt.ylabel("Voltage [V]")
plt.title("Terminal voltage")

plt.subplot(2,1,2)
plt.plot(time, -current, 'r')
plt.xticks(np.arange(0, max(time), 10))
plt.xlabel("Time [s]")
plt.ylabel("Current [A]")
plt.title("Current")

plt.tight_layout()
plt.show()

