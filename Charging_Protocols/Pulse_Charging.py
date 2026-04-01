import pybamm
import numpy as np 
import matplotlib.pyplot as plt

model=pybamm.lithium_ion.SPMe()

steps = ["Charge at 2 A for 30 seconds"]

pulse_time = 0.1
num_pulse = 18

for i in range(num_pulse):
    steps.append(f"Charge at 2 A for 0.5 seconds")
    steps.append(f"Rest for {pulse_time} seconds")
    
    pulse_time *= 1.3

steps.append(f"Hold at 3.9 V for 10 seconds")



experiment=pybamm.Experiment(steps)

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


